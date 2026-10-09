"""Sędzia per kryterium — metoda v3. Jedno kryterium = jedno zapytanie.

Wzorzec oceniania z Harvey LAB: werdykt zero-jedynkowy, bez częściowego
zaliczenia, kryteria oceniane osobno, żeby nie wpływały na siebie. Model
spoza dostawcy audytującego (Gemini przez Vertex), temperatura 0.

Użycie:
    python3 sedzia_kryteria.py 02-wdrozenie-erp
    python3 sedzia_kryteria.py 02-wdrozenie-erp --out /tmp/proba.json
    python3 sedzia_kryteria.py 02-wdrozenie-erp --dopytaj   # tylko pary z BŁĄD

Błąd zapytania to nie werdykt: liczony osobno, nigdy jako niezaliczenie.
"""
import argparse, json, pathlib, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

B = pathlib.Path(__file__).resolve().parent
URL = ("https://aiplatform.googleapis.com/v1/projects/ktzr-asystent/locations/global/"
       "publishers/google/models/gemini-2.5-pro:generateContent")
GCLOUD = "/home/adam/google-cloud-sdk/bin/gcloud"
PROB = 3

arg = argparse.ArgumentParser()
arg.add_argument("umowa", help="np. 04-matematyczna-tm")
arg.add_argument("--out", help="plik wynikowy (domyślnie wyniki/v0.8/oceny/kryteria-NN.json)")
arg.add_argument("--dopytaj", action="store_true", help="ponów tylko pary z werdyktem BŁĄD")
a = arg.parse_args()

UMOWA = a.umowa
NR = UMOWA[:2]
OUT = pathlib.Path(a.out) if a.out else B / f"wyniki/v0.8/oceny/kryteria-{NR}.json"
AUDYTY = {
    "fable-skill":     B / f"wyniki/v0.8/fable-skill/{UMOWA}.md",
    "sonnet-skill-p1": B / f"wyniki/v0.8/sonnet-skill/p1/{UMOWA}.md",
    "sonnet-skill-p2": B / f"wyniki/v0.8/sonnet-skill/p2/{UMOWA}.md",
    "sonnet-skill-p3": B / f"wyniki/v0.8/sonnet-skill/p3/{UMOWA}.md",
}

tekst_umowy = (B / "umowy" / f"{UMOWA}.md").read_text(encoding="utf-8")
sur = (B / "manifesty/kryteria" / f"{UMOWA}.yaml").read_text(encoding="utf-8")
# Wzorzec składany konkatenacją, nie f-stringiem: w f-stringu {6} znika jako pole podstawienia.
WZORZEC = (r"- id: (K" + NR + r"-\d+)\n\s+wada: (\S+)\n\s+typ: (\S+)\n\s+title: (.+?)\n"
           r"\s+match_criteria: >\n((?:\s{6}.+\n)+)")
bloki = re.findall(WZORZEC, sur)
KRYT = [{"id": i, "wada": w, "typ": t, "title": ti.strip(),
         "match": re.sub(r"\s+", " ", m).strip()} for i, w, t, ti, m in bloki]
zadeklarowanych = len(re.findall(r"^\s*- id: K" + NR + r"-\d+", sur, re.M))
print(f"kryteriów wczytanych: {len(KRYT)} z {zadeklarowanych} zadeklarowanych", file=sys.stderr)
# Bez kryteriów albo z niepełną rubryką nie wolno niczego zapisać — inaczej nadpiszemy wynik pustką.
if not KRYT or len(KRYT) != zadeklarowanych:
    sys.exit("STOP: rubryka wczytana niepełnie, nic nie zapisuję")
brak = [n for n, p in AUDYTY.items() if not p.exists()]
if brak:
    sys.exit(f"STOP: brak audytów {brak}")

TOK = subprocess.run([GCLOUD, "auth", "print-access-token"],
                     capture_output=True, text=True, check=True).stdout.strip()


def ocen(audyt_nazwa, audyt, k):
    prompt = (
        "Oceniasz pracę prawniczego systemu AI wobec jednego kryterium jakości.\n"
        "Odpowiadasz wyłącznie na podstawie treści audytu i tekstu umowy. "
        "Werdykt jest zero-jedynkowy — nie ma zaliczenia częściowego.\n\n"
        f"=== TEKST UMOWY (źródło) ===\n{tekst_umowy}\n\n"
        f"=== AUDYT DO OCENY ===\n{audyt}\n\n"
        f"=== KRYTERIUM ===\nTytuł: {k['title']}\nTreść: {k['match']}\n\n"
        "Odpowiedz wyłącznie JSON-em w postaci:\n"
        '{"uzasadnienie": "krótko, z odwołaniem do konkretnego miejsca w audycie", '
        '"werdykt": "zaliczone" lub "niezaliczone"}')
    ciało = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
             "generationConfig": {"temperature": 0, "maxOutputTokens": 2000,
                                  "responseMimeType": "application/json"}}
    for proba in range(PROB):
        try:
            r = subprocess.run(["curl", "-sS", "-X", "POST", "-H", f"Authorization: Bearer {TOK}",
                                "-H", "Content-Type: application/json", "-d", json.dumps(ciało), URL],
                               capture_output=True, text=True, timeout=300)
            d = json.loads(r.stdout)
            txt = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"])
            w = json.loads(txt)
            if w["werdykt"] in ("zaliczone", "niezaliczone"):
                return {**k, "konfiguracja": audyt_nazwa,
                        "werdykt": w["werdykt"], "uzasadnienie": w.get("uzasadnienie", "")}
        except Exception:
            pass
        time.sleep(5 * (proba + 1))
    return {**k, "konfiguracja": audyt_nazwa, "werdykt": "BŁĄD", "uzasadnienie": ""}


tresci = {n: p.read_text(encoding="utf-8") for n, p in AUDYTY.items()}
if a.dopytaj:
    wyniki = json.loads(OUT.read_text(encoding="utf-8"))
    kryt = {k["id"]: k for k in KRYT}
    do_powtorki = [x for x in wyniki if x["werdykt"] == "BŁĄD"]
    print(f"do powtórki: {len(do_powtorki)}", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=3) as ex:
        nowe = list(ex.map(lambda x: ocen(x["konfiguracja"], tresci[x["konfiguracja"]], kryt[x["id"]]),
                           do_powtorki))
    idx = {(x["konfiguracja"], x["id"]): x for x in nowe}
    wyniki = [idx.get((x["konfiguracja"], x["id"]), x) for x in wyniki]
else:
    zadania = [(n, tresci[n], k) for n in AUDYTY for k in KRYT]
    with ThreadPoolExecutor(max_workers=8) as ex:
        wyniki = list(ex.map(lambda z: ocen(*z), zadania))

OUT.write_text(json.dumps(wyniki, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"zapisane: {OUT}", file=sys.stderr)

print(f"\n{'konfiguracja':18s} {'zaliczone':>10s} {'niezal.':>8s} {'błąd':>5s}  all-pass")
for n in AUDYTY:
    w = [x for x in wyniki if x["konfiguracja"] == n]
    ok = sum(1 for x in w if x["werdykt"] == "zaliczone")
    nz = sum(1 for x in w if x["werdykt"] == "niezaliczone")
    bl = sum(1 for x in w if x["werdykt"] == "BŁĄD")
    # Przy błędach zapytań all-pass jest nieustalony, a nie 0,0.
    ap = "n/d" if bl else ("1,0" if nz == 0 else "0,0")
    print(f"{n:18s} {ok:>7d}/{len(w):<3d} {nz:>7d} {bl:>5d}  {ap}")
bledy = sum(1 for x in wyniki if x["werdykt"] == "BŁĄD")
print(f"\nbłędów zapytań: {bledy}" + ("  -> uruchom ponownie z --dopytaj" if bledy else ""))
print("\nniezaliczone per kryterium:")
for k in KRYT:
    nz = [x["konfiguracja"] for x in wyniki if x["id"] == k["id"] and x["werdykt"] == "niezaliczone"]
    if nz:
        print(f"  {k['id']} ({k['wada']}/{k['typ']}) {k['title'][:52]:52s} -> {', '.join(nz)}")
