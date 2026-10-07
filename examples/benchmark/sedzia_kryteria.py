"""Sędzia per kryterium — metoda v3. Jedno kryterium = jedno zapytanie.

Wzorzec oceniania z Harvey LAB: werdykt zero-jedynkowy, bez częściowego
zaliczenia, kryteria oceniane osobno, żeby nie wpływały na siebie. Model
spoza dostawcy audytującego (Gemini przez Vertex), temperatura 0.
"""
import json, pathlib, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

B = pathlib.Path("/mnt/c/Users/Adam/Desktop/AI/Claude skill/Na gita/commercial-legal-pl/examples/benchmark")
UMOWA = "04-matematyczna-tm"
AUDYTY = {
    "fable-skill":    B / f"wyniki/v0.8/fable-skill/{UMOWA}.md",
    "sonnet-skill-p1": B / f"wyniki/v0.8/sonnet-skill/p1/{UMOWA}.md",
    "sonnet-skill-p2": B / f"wyniki/v0.8/sonnet-skill/p2/{UMOWA}.md",
    "sonnet-skill-p3": B / f"wyniki/v0.8/sonnet-skill/p3/{UMOWA}.md",
}
TOK = subprocess.run(["/home/adam/google-cloud-sdk/bin/gcloud", "auth", "print-access-token"],
                     capture_output=True, text=True, check=True).stdout.strip()
URL = ("https://aiplatform.googleapis.com/v1/projects/ktzr-asystent/locations/global/"
       "publishers/google/models/gemini-2.5-pro:generateContent")

tekst_umowy = (B / "umowy" / f"{UMOWA}.md").read_text(encoding="utf-8")
sur = (B / "manifesty/kryteria" / f"{UMOWA}.yaml").read_text(encoding="utf-8")
bloki = re.findall(r"- id: (K04-\d+)\n\s+wada: (\S+)\n\s+typ: (\S+)\n\s+title: (.+?)\n\s+match_criteria: >\n((?:\s{6}.+\n)+)", sur)
KRYT = [{"id": a, "wada": b, "typ": c, "title": d.strip(),
         "match": re.sub(r"\s+", " ", e).strip()} for a, b, c, d, e in bloki]
print(f"kryteriów wczytanych: {len(KRYT)}", file=sys.stderr)


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
    for _ in range(3):
        r = subprocess.run(["curl", "-sS", "-X", "POST", "-H", f"Authorization: Bearer {TOK}",
                            "-H", "Content-Type: application/json", "-d", json.dumps(ciało), URL],
                           capture_output=True, text=True, timeout=300)
        try:
            d = json.loads(r.stdout)
            txt = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"])
            w = json.loads(txt)
            return {**k, "konfiguracja": audyt_nazwa,
                    "werdykt": w["werdykt"], "uzasadnienie": w.get("uzasadnienie", "")}
        except Exception:
            continue
    return {**k, "konfiguracja": audyt_nazwa, "werdykt": "BŁĄD", "uzasadnienie": ""}


zadania = [(n, p.read_text(encoding="utf-8"), k) for n, p in AUDYTY.items() for k in KRYT]
with ThreadPoolExecutor(max_workers=8) as ex:
    wyniki = list(ex.map(lambda z: ocen(*z), zadania))

out = B / "wyniki/v0.8/oceny/kryteria-04.json"
out.write_text(json.dumps(wyniki, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"\n{'konfiguracja':18s} {'zaliczone':>10s} {'odsetek':>8s}  all-pass")
for n in AUDYTY:
    w = [x for x in wyniki if x["konfiguracja"] == n]
    ok = sum(1 for x in w if x["werdykt"] == "zaliczone")
    print(f"{n:18s} {ok:>7d}/{len(w):<3d} {ok/len(w):>7.0%}  {'1,0' if ok == len(w) else '0,0'}")
print(f"\nbłędów zapytań: {sum(1 for x in wyniki if x['werdykt']=='BŁĄD')}")
print("\nniezaliczone per kryterium:")
for k in KRYT:
    nz = [x["konfiguracja"] for x in wyniki if x["id"] == k["id"] and x["werdykt"] == "niezaliczone"]
    if nz:
        print(f"  {k['id']} ({k['wada']}/{k['typ']}) {k['title'][:52]:52s} -> {', '.join(nz)}")
