# Benchmark — nasolone umowy (seeded contracts)

Korpus testowy do pomiaru skuteczności skilla: fikcyjne umowy z **celowo posianymi wadami** i manifestem złotego standardu (co powinno zostać wykryte, na jakim poziomie). Złoty standard powstaje w chwili tworzenia umowy — bez panelu oceniającego.

## Metoda

1. Każda umowa w `umowy/` ma manifest w `manifesty/` (YAML): posiane wady + oczekiwana flaga + czyste obszary + liczby do rachunku R12.
2. Audyt uruchamiany w macierzy: **{modele} × {ze skillem / bez skilla}** — ta sama umowa, ten sam prompt, różne konfiguracje.
3. Sędzia (model z manifestem) porównuje audyt z manifestem i liczy metryki.

## Metryki (5)

| Metryka | Definicja | Próg |
|---|---|---|
| Wykrywalność | posiane wady wykryte / posiane | im wyżej tym lepiej |
| Fałszywe alarmy | flagi 🔴/🟠 na czystych obszarach | im niżej tym lepiej |
| Trafność flagi | poziom zgodny z manifestem (± 1 poziom OK) | im wyżej tym lepiej |
| **Zmyślenia** | cytaty spoza tekstu (R11) + błędne przepisy (R1) + kwoty niezgodne (R12) | **twarde 0 — jedno zmyślenie = FAIL** |
| Rachunek | wynik 🧮 zgodny z liczbami manifestu | zgodność |

## Klasy trudności

- **jawne** — wada widoczna wprost (kara za płatność)
- **ukryte** — wada zamaskowana (nadpisanie przez „niezależnie od pozostałych postanowień")
- **kumulatywne** — każda klauzula OK, suma wydrąża ochronę
- **czyste** — umowa bez wad (test fałszywych alarmów)
- **adwersarialne** — injection w treści (R8), fałszywe tropy (R11)

## Zasady

- Wszystkie umowy i podmioty **fikcyjne**; NIP-y (jeśli występują) z celowo błędną sumą kontrolną.
- Korpus służy też jako **regresja**: uruchamiany po każdej zmianie skilla — wynik nie może spaść.
- Manifest jest tajny dla audytującego (audyt dostaje tylko umowę), jawny dla sędziego.
