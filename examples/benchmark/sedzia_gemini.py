"""Sędzia spoza dostawcy: Gemini 2.5 Pro przez Vertex AI.

Ta sama instrukcja i ten sam manifest co sędzia Opus. Jedyna różnica to
dostawca modelu — po to, żeby wykluczyć wspólne ślepe plamy jednej rodziny.
"""
import json, pathlib, subprocess, sys

B = pathlib.Path("/mnt/c/Users/Adam/Desktop/AI/Claude skill/Na gita/commercial-legal-pl/examples/benchmark")
KONF = sys.argv[1] if len(sys.argv) > 1 else "fable-skill"
KAT = sys.argv[2] if len(sys.argv) > 2 else "v0.8"
UMOWY = ["01-nda-wzajemne", "02-wdrozenie-erp", "03-czysta-b2b",
         "04-matematyczna-tm", "05-injection"]

def czytaj(p):
    return pathlib.Path(p).read_text(encoding="utf-8", errors="replace")

czesci = [
    "Jesteś sędzią benchmarku prawniczego. Oceniasz audyty umów wobec manifestu "
    "złotego standardu, WYŁĄCZNIE względem manifestu, nie własnej opinii prawnej. "
    "Pracujesz po polsku.\n\n"
    "Każde zmyślenie i każdy błąd rachunkowy musisz udowodnić: dosłowny cytat z "
    "audytu plus dowód ze źródła. Bez dowodu nie zgłaszasz. O tym, czy coś jest "
    "zmyśleniem, czy błędem rachunkowym, decyduje POCHODZENIE liczb: liczby wzięte "
    "z umowy i źle policzone to błąd rachunkowy (metryka 5, nie FAIL); liczba "
    "przypisana umowie, której w niej nie ma, to zmyślenie (metryka 4, FAIL).\n\n"
    "Jeżeli audyt wykrywa wadę realną, ale spoza manifestu, odnotuj ją osobno jako "
    "„poza kluczem” — to NIE jest fałszywy alarm, ale nie liczy się też do "
    "wykrywalności.\n\n"
    "=== INSTRUKCJA SĘDZIEGO ===\n" + czytaj(B / "manifesty/instrukcja-sedziego-v2.md"),
    "\n\n=== MANIFEST ZŁOTEGO STANDARDU ===\n" + czytaj(B / "manifesty/manifesty.yaml"),
]
for u in UMOWY:
    czesci.append(f"\n\n=== UMOWA ŹRÓDŁOWA {u} ===\n" + czytaj(B / "umowy" / f"{u}.md"))
for u in UMOWY:
    czesci.append(f"\n\n=== AUDYT DO OCENY ({KONF}) {u} ===\n"
                  + czytaj(B / "wyniki" / KAT / KONF / f"{u}.md"))
czesci.append(
    "\n\n=== ZADANIE ===\n"
    "Oceń powyższe pięć audytów. Zwróć:\n"
    "1. Tabelę per umowa: wykryte/posiane, fałszywe alarmy, trafność flag, "
    "zmyślenia, błędy rachunkowe, rachunek wykonany, FAIL.\n"
    "2. Sekcję „Nietrafione wady” — ID z manifestu i dlaczego uznane za nietrafione.\n"
    "3. Sekcję „Zmyślenia” — dosłowny cytat z audytu i dowód ze źródła.\n"
    "4. Sekcję „Błędy rachunkowe” — liczby z umowy, wynik audytu, wynik prawidłowy.\n"
    "5. Sekcję „Flagi poza kluczem” — liczba i krótka lista.\n"
    "6. Sumę zbiorczą wszystkich metryk.\n"
    "Nagłówek: sedzia: Gemini 2.5 Pro (Vertex AI), konfiguracja: " + KONF + ", wersja: " + KAT)

prompt = "".join(czesci)
print(f"wsad: {len(prompt):,} znaków", file=sys.stderr)

tok = subprocess.run(["/home/adam/google-cloud-sdk/bin/gcloud", "auth", "print-access-token"],
                     capture_output=True, text=True, check=True).stdout.strip()
ciało = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
         "generationConfig": {"temperature": 0, "maxOutputTokens": 32000}}
pathlib.Path("/tmp/vx_req.json").write_text(json.dumps(ciało), encoding="utf-8")
r = subprocess.run(["curl", "-sS", "-X", "POST",
                    "-H", f"Authorization: Bearer {tok}",
                    "-H", "Content-Type: application/json",
                    "--data-binary", "@/tmp/vx_req.json",
                    "https://aiplatform.googleapis.com/v1/projects/ktzr-asystent/"
                    "locations/global/publishers/google/models/gemini-2.5-pro:generateContent"],
                   capture_output=True, text=True, timeout=1800)
d = json.loads(r.stdout)
if "candidates" not in d:
    print(json.dumps(d, ensure_ascii=False)[:800]); sys.exit(1)
tekst = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"])
wy = B / "wyniki" / KAT / "oceny" / f"{KONF}-gemini.md"
wy.write_text(tekst, encoding="utf-8")
print(f"zapisane: {wy}  ({len(tekst):,} znaków)", file=sys.stderr)
print(tekst[:1500])
