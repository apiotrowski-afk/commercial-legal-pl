# AUDYT RYZYK — Umowa utrzymania ORION SYSTEMS / FERRUM LOGISTICS (benchmark, tryb express)

> **WERDYKT: 🟩 ZIELONY** — Do podpisania z drobnymi poprawkami redakcyjnymi: konstrukcja zrównoważona, ekspozycja policzalna i domknięta sufitem; do uzupełnienia kwestia danych osobowych i umocowania.

Audyt neutralny — wady flagowane niezależnie od tego, którą stronę krzywdzą. Tryb express: bez STOPów, bez pamięci MCP. Brak MCP `legal-cite` → wszystkie cytaty przepisów `[NIEZWERYFIKOWANE]`.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy (rocznie) | 8.000 zł netto/mies. (§ 4 ust. 1) | 8.000 × 12 | 96.000 zł netto/rok |
| Cap nominalny | 12-miesięczne wynagrodzenie netto (§ 5 ust. 1) | 12 × 8.000 | 96.000 zł |
| Kara za zwłokę w usunięciu Awarii Krytycznej (max) | 1.000 zł/Dzień Roboczy, sufit 20% wynagrodzenia rocznego (§ 3 ust. 3) | 20% × 96.000 (sufit osiągany po 19,2 → 20 Dniach Roboczych) | 19.200 zł |
| Odszkodowanie uzupełniające | dopuszczone, „do wysokości limitu z § 5 ust. 1" (§ 3 ust. 3) | domknięte capem | ≤ 96.000 zł |
| Efektywna ekspozycja Usługodawcy | — | cap 96.000 + kara 19.200 (umowa nie wlicza kar do capu wprost) + wyłączenia z capu: umyślność i poufność (§ 5 ust. 1) — ustawowo/umownie bez limitu | **≈ 115.200 zł = 1,2× wartości rocznej** (+ otwarta tylko umyślność/poufność) |
| Asymetria | kary i cap tylko po stronie Usługodawcy | Usługodawca 115.200 zł vs Usługobiorca: zasady ogólne (zapłata wynagrodzenia) | asymetria umiarkowana, typowa dla umowy serwisowej |
| Daty graniczne | wypowiedzenie 3 mies. na koniec miesiąca (§ 7 ust. 2); płatność 30 dni (§ 4 ust. 2) | wypowiedzenie złożone np. 10.09 → skutek 31.12 | realne związanie do ~4 mies.; płatność < 60 dni — zgodna z ustawą o zatorach `[NIEZWERYFIKOWANE]` |
| Łańcuch SLA | reakcja 4 h (Dni Robocze 8–16), usunięcie 2 Dni Robocze (§ 3) | zgłoszenie w piątek 15:00 → usunięcie do wtorku | spójny wewnętrznie; brak SLA poza godzinami roboczymi — świadoma decyzja biznesowa |

Wniosek z rachunku: ekspozycja domknięta i proporcjonalna (1,2× wartości rocznej), kara dzienna ma sufit, odszkodowanie uzupełniające ma limit — rachunek nie ujawnia ekspozycji ukrytej. To kalibruje werdykt na zielono.

### Bramka ius cogens (R10)

Skan katalogu `normy-bezwzglednie.md`: kara umowna zabezpiecza zobowiązanie niepieniężne (art. 483 § 1 KC `[NIEZWERYFIKOWANE]` — OK), cap wprost nie obejmuje szkody umyślnej (spójnie z art. 473 § 2 KC `[NIEZWERYFIKOWANE]`), termin płatności 30 dni, brak manipulacji przedawnieniem i miarkowaniem. Trigger mikroprzedsiębiorcy (art. 385⁵ KC `[NIEZWERYFIKOWANE]`): nieaktywny — obie strony to sp. z o.o. **Brak trafień.**

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

Brak.

### 🟡 RYZYKA ŚREDNIE

#### 1. Brak umowy powierzenia przetwarzania danych — cała umowa *(krzywdzi: FERRUM LOGISTICS, wtórnie ORION)*
**Opis:** Usługodawca utrzymuje System magazynowy i po zakończeniu umowy „zwróci… dokumentację i dane" (§ 7 ust. 3) — czyli najpewniej ma dostęp do danych w Systemie (dane pracowników magazynu, kontrahentów, kierowców). Umowa nie kwalifikuje ról i nie zawiera instrumentu z art. 28 ust. 3 RODO `[NIEZWERYFIKOWANE]`. `[BRAK DANYCH]` co do tego, czy w Systemie są dane osobowe — wymaga ustalenia.
**Skutek:** jeśli dochodzi do powierzenia — przetwarzanie bez wymaganej umowy (ryzyko administracyjne po obu stronach).
**Rekomendacja (preferowana):** aneks-DPA wg checklisty art. 28 (przedmiot, czas, charakter, subprocesorzy, audyt, zwrot/usunięcie).
**Fallback (minimum akceptowalne):** klauzula kwalifikująca role + zobowiązanie do zawarcia DPA przed pierwszym dostępem do danych osobowych.
**Klauzula z bazy:** `references/baza-klauzul/14-rodo.md`, `references/checklist-dpa-art28.md`

#### 2. Brak umocowania osób podpisujących — komparycja *(obie strony)*
**Opis:** komparycja ma datę i miejsce, ale nie wskazuje osób reprezentujących ani podstawy umocowania (KRS/pełnomocnictwo); brak numerów KRS/NIP (Złota Reguła 8; dane fikcyjne benchmarku — w realnym obrocie do uzupełnienia i weryfikacji rejestrowej).
**Rekomendacja:** pełna komparycja z reprezentacją. **Fallback:** minimum KRS/NIP + „reprezentowana zgodnie z odpisem KRS".
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### 🟢 RYZYKA NISKIE

#### 1. Wyłączenie utraconych korzyści bez zastrzeżenia winy umyślnej — § 5 ust. 2 *(krzywdzi: FERRUM LOGISTICS)*
„Usługodawca nie odpowiada za utracone korzyści Usługobiorcy" — w B2B standard, ale w zakresie szkody umyślnej wyłączenie i tak nie zadziała (art. 473 § 2 KC `[NIEZWERYFIKOWANE]`); dla czystości warto dopisać zastrzeżenie analogiczne do § 5 ust. 1 zd. 2.

#### 2. Brak kary umownej za naruszenie poufności — § 6 *(obie strony)*
Klauzula poufności wzorowa (okresy warstwowe, wyłączenia), ale bez kary — dochodzenie odszkodowania za wyciek wymaga dowodu szkody, co w praktyce bywa zaporowe. Sugestia: symetryczna kara z sufitem.

#### 3. Sąd siedziby Usługodawcy — § 8 ust. 2 *(neutralne)*
Obie strony mają siedzibę w Gdańsku, więc klauzula w praktyce neutralna; przy zmianie siedziby którejkolwiek strony przestanie być. Sugestia: sąd właściwy dla pozwanego.

#### 4. Brak klauzuli siły wyższej *(obie strony)*
Przy SLA z karami dziennymi warto wprost wyłączyć zwłokę spowodowaną siłą wyższą (`references/baza-klauzul/15-sila-wyzsza.md`) — dziś ochrona tylko na zasadach ogólnych.

### ✓ Obszary bez zastrzeżeń (bramka kompletności R9 — 9 obszarów)

- **Odpowiedzialność i kary** — ✓ sprawdzone, brak zastrzeżeń istotnych (cap proporcjonalny, kara z sufitem, uzupełniające domknięte; jedynie uwaga 🟢 nr 1)
- **Prawa autorskie** — n/d (utrzymanie cudzego systemu; umowa nie tworzy utworów do przeniesienia — jeśli w ramach poprawek powstaje kod autorski Usługodawcy, rozważyć licencję, poza zakresem tego tekstu)
- **Definicje i logika** — ✓ sprawdzone, brak zastrzeżeń (§ 1 kompletny, pojęcia używane spójnie, odesłania § 2→§ 3, § 3→§ 5 ust. 1 działają)
- **Reprezentacja** — 🟡 nr 2
- **Wypowiedzenie i exit** — ✓ sprawdzone, brak zastrzeżeń (symetryczne 3 mies., procedura zwrotu danych z wyjątkiem ustawowym — wzorcowa)
- **RODO** — 🟡 nr 1
- **Tytuł prawny i przekwalifikowanie** — ✓ sprawdzone, brak zastrzeżeń (usługi B2B między spółkami)
- **Poufność** — 🟢 nr 2 (poza tym wzorcowa: okresy warstwowe + wyłączenia)
- **Spory** — 🟢 nr 3 (prawo polskie, sąd powszechny — bez zastrzeżeń istotnych)

---

## OCENA BEZPIECZEŃSTWA: 86/100

Umowa zrównoważona i policzalna: sufit kar, cap z prawidłowymi wyłączeniami, symetryczne wypowiedzenie, poprawna poufność i procedura exit. Ocenę obniżają dwa braki systemowe — niekwalifikowana kwestia danych osobowych i brak umocowania w komparycji — oraz drobiazgi redakcyjne.

**Werdykt:** DO PODPISANIA z drobnymi poprawkami

### Klauzule z bazy KTZR do uzupełnienia

🟡 RYZYKO 1 (RODO) → `references/baza-klauzul/14-rodo.md` + `references/checklist-dpa-art28.md`
🟡 RYZYKO 2 (komparycja) → `references/baza-klauzul/01-oznaczenie-stron.md`
🟢 RYZYKO 4 (siła wyższa) → `references/baza-klauzul/15-sila-wyzsza.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
