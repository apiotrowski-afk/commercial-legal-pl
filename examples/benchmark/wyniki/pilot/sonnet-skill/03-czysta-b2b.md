## AUDYT RYZYK — Umowa o świadczenie usług utrzymania (Orion Systems / Ferrum Logistics)

> **WERDYKT: 🟨 ŻÓŁTY** — do negocjacji jednego istotnego braku (klauzula powierzenia danych, art. 28 RODO), bez dealbreakerów; poza tym umowa skonstruowana solidnie i zrównoważenie.

*Audyt neutralny — wady oznaczone niezależnie od tego, którą stronę faktycznie krzywdzą; przy każdej wskazano stronę dotkniętą.*

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 8.000 zł netto/mies. (§ 4 ust. 1), czas nieokreślony | roczna: 8.000 × 12 = 96.000 zł | 96.000 zł/rok (przy założeniu trwania pełnego roku) |
| Cap odpowiedzialności (§ 5 ust. 1) | 12-miesięczne wynagrodzenie netto | 8.000 × 12 | 96.000 zł, z wyłączeniem winy umyślnej i naruszenia § 6 (poufność) — wyłączenia zgodne z ius cogens, nie iluzoryczne |
| Kara za zwłokę w usunięciu Awarii Krytycznej (§ 3 ust. 3) | 1.000 zł/dzień, sufit 20% wynagrodzenia rocznego netto | 20% × 96.000 = 19.200 zł; do sufitu: 19.200 / 1.000 ≈ 19 dni | maksymalna kara: **19.200 zł** (sufit jawnie określony — kara nie jest otwarta) |
| Efektywna ekspozycja Usługodawcy | — | cap 96.000 zł (kary wliczają się w ten cap poza wyłączeniami z § 5 ust. 1) + odszkodowanie uzupełniające do wysokości limitu (§ 3 ust. 3 zd. 2) | efektywna ekspozycja **= cap nominalny**, bez ukrytego mnożnika — rzadki, pozytywny wynik rachunku |
| Asymetria (Usługodawca vs Usługobiorca) | kara tylko po stronie Usługodawcy (SLA); brak analogicznej kary dla Usługobiorcy za opóźnienie w płatności | typowe dla umów utrzymaniowych — Usługobiorca chroniony odsetkami ustawowymi (art. 481 KC [NIEZWERYFIKOWANE]) | asymetria obecna, ale w granicach rynkowej praktyki dla tego typu umowy |
| Daty graniczne | wypowiedzenie: 3 miesiące, koniec miesiąca kalendarzowego (§ 7 ust. 2); płatność: 30 dni od faktury (§ 4 ust. 2) | 30 dni < 60 dni (granica ustawy o zatorach płatniczych) | terminy w normie, brak przekroczeń |

**Wniosek z rachunku:** to jedna z niewielu umów w tym zestawie, w której cap nie jest iluzoryczny — kara SLA ma jawny sufit wliczony w logikę odpowiedzialności, a odszkodowanie uzupełniające jest wyraźnie ograniczone do wysokości limitu z § 5 ust. 1, a nie „ponad" niego. Rachunek nie generuje podstaw do podniesienia flag ponad poziom wynikający z analizy jakościowej.

### Bramka ius cogens (R10)

Brak prób obejścia norm bezwzględnie obowiązujących: kara umowna dotyczy zobowiązania niepieniężnego (usunięcie Awarii Krytycznej — świadczenie rezultatu, zgodnie z § 2 ust. 2), nie zobowiązania pieniężnego — art. 483 § 1 KC [NIEZWERYFIKOWANE] nie jest naruszony. Wyłączenia z capu (wina umyślna, naruszenie poufności) są zgodne z art. 473 § 2 KC [NIEZWERYFIKOWANE], nie wykraczają poza jego minimum. Brak wyłączenia miarkowania kary, brak skracania terminów przedawnienia, brak klauzuli majątkowych praw autorskich do zweryfikowania (n/d przy tym typie usługi). Termin płatności (30 dni) mieści się w granicach ustawy o przeciwdziałaniu nadmiernym opóźnieniom (art. 7 ust. 2 [NIEZWERYFIKOWANE]).

Trigger mikroprzedsiębiorcy (art. 3855 KC [NIEZWERYFIKOWANE]) — nie dotyczy, obie strony to spółki z o.o.

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

#### 1. Brak umowy powierzenia przetwarzania danych (art. 28 RODO) — brak w tekście
**Opis:** Usługodawca uzyskuje dostęp do „Systemu" — oprogramowania magazynowego Usługobiorcy (§ 1 ust. 1) — w celu usuwania awarii, instalacji poprawek i konsultacji. System magazynowy typowo przetwarza dane osobowe (dane kontrahentów, pracowników wykonujących przyjęcia/wydania, dane w dokumentach WZ/PZ). Umowa **nie zawiera żadnej klauzuli RODO** — brak wskazania podstawy przetwarzania, brak umowy powierzenia, brak listy podwykonawców (subprocesorów) mających dostęp do Systemu, brak procedury zgłaszania naruszeń ochrony danych. Dotyczy obu stron — Usługobiorcy (Ferrum Logistics) jako administratora danych oraz Usługodawcy (Orion Systems) jako potencjalnego procesora bez podstawy prawnej działania.
**Skutek:** jeśli relacja faktycznie ma charakter administrator–procesor (co jest prawdopodobne przy dostępie serwisowym do systemu magazynowego), brak instrumentu z art. 28 RODO [NIEZWERYFIKOWANE] naraża obie strony na ryzyko sankcji administracyjnej (RODO art. 83 ust. 4 lit. a [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** dodać odrębną umowę powierzenia przetwarzania danych (DPA) zgodną z art. 28 RODO — zakres, cel, kategorie danych, środki bezpieczeństwa, subprocesorzy, procedura zgłaszania naruszeń, audyt.
**Fallback (minimum akceptowalne):** minimalna klauzula RODO w treści Umowy (jeśli skala przetwarzania jest niewielka), z odesłaniem do pełnego DPA jako Załącznika.
**Klauzula z bazy:** `references/checklist-dpa-art28.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. Sąd wyłącznie siedziby Usługodawcy — § 8 ust. 2
**Opis:** „Sądem właściwym jest sąd powszechny właściwy dla siedziby Usługodawcy" — jednostronny wybór forum na korzyść Orion Systems. Dotyczy Usługobiorcy (Ferrum Logistics).
**Skutek:** przy sporze Usługobiorca musi prowadzić postępowanie w siedzibie kontrahenta — praktyka rynkowo częsta, ale wciąż asymetryczna.
**Rekomendacja (preferowana):** właściwość ogólna (siedziba pozwanego) albo sąd neutralny.
**Fallback (minimum akceptowalne):** pozostawić — obie strony mają siedzibę w Gdańsku, praktyczna uciążliwość minimalna.
**Klauzula z bazy:** `references/baza-klauzul/13-postanowienia-koncowe.md`

### 🟢 RYZYKA NISKIE

#### 1. Brak klauzuli praw autorskich do ewentualnych nowych utworów przy poprawkach
**Opis:** § 2 ust. 1 przewiduje „instalację poprawek" — jeśli w ramach utrzymania powstają nowe fragmenty kodu stanowiące utwór, Umowa nie reguluje ich statusu prawnoautorskiego.
**Skutek:** przy większej skali modyfikacji (nie tylko instalacja gotowych poprawek, ale też programowanie na zlecenie) mogłoby powstać niejasne prawo do nowego kodu.
**Rekomendacja (preferowana):** dodać klauzulę „drobne poprawki i konfiguracja nie stanowią odrębnego utworu; jeśli powstanie utwór w rozumieniu PrAut, prawa przechodzą na Usługobiorcę z chwilą zapłaty, z wymienieniem pól eksploatacji".
**Fallback (minimum akceptowalne):** pozostawić bez zmian, jeśli zakres usług faktycznie ogranicza się do instalacji gotowych poprawek producenta.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 2. Brak jawnego wskazania sposobu reprezentacji stron (KRS)
**Opis:** preambuła wskazuje siedziby stron, ale nie wskazuje wprost KRS ani sposobu reprezentacji osób podpisujących (adnotacja „dane fikcyjne" sugeruje uproszczenie testowe).
**Skutek:** przy realnym podpisie — ryzyko braku umocowania.
**Rekomendacja (preferowana):** uzupełnić dane rejestrowe i sposób reprezentacji.
**Fallback (minimum akceptowalne):** —
**Klauzula z bazy:** `references/baza-klauzul/01-strony-reprezentacja.md`

### ✓ Obszary bez zastrzeżeń

- **Odpowiedzialność i kary** — cap jasny i nieiluzoryczny (§ 5 ust. 1), kara SLA z jawnym sufitem 20% (§ 3 ust. 3), wyłączenia z capu zgodne z ius cogens
- **Definicje i logika** — słowniczek kompletny (System, Usługi, Dzień Roboczy, Awaria Krytyczna), spójnie używany w całym tekście, rozróżnienie rezultat/staranne działanie (§ 2 ust. 2) precyzyjne
- **Wypowiedzenie i exit** — symetryczne prawo wypowiedzenia dla obu stron (§ 7 ust. 2), procedura zwrotu danych z jasno opisanym wyjątkiem prawnym (§ 7 ust. 3)
- **Poufność** — okres 3 lata po zakończeniu + bezterminowo dla tajemnicy przedsiębiorstwa, z pełnym katalogiem wyłączeń (§ 6)
- **Tytuł prawny / przekwalifikowanie** — n/d (usługi utrzymania między dwiema spółkami, nie body leasing ani dzieło z osobą fizyczną)
- **Prawa autorskie / IP** — brak istotnych zastrzeżeń poza drobną uwagą 🟢 wyżej

---

## OCENA BEZPIECZEŃSTWA: 80/100

Jedno ryzyko 🟠 (brak instrumentu RODO art. 28 mimo dostępu serwisowego do systemu magazynowego zawierającego prawdopodobnie dane osobowe) i dwa drobne ryzyka 🟡/🟢. Poza tym umowa jest technicznie i redakcyjnie solidna: definicje kompletne, rozróżnienie rezultatu i starannego działania precyzyjne, cap nieiluzoryczny, wypowiedzenie symetryczne, poufność z pełnym katalogiem wyłączeń.

**Werdykt:** DO NEGOCJACJI — uzupełnić klauzulę RODO/art. 28 przed podpisem; pozostałe punkty są drobne i nie blokują podpisania.

### Klauzule z bazy KTZR do uzupełnienia

🟠 RYZYKO 1 (brak umowy powierzenia RODO)
→ Zastosuj: `references/checklist-dpa-art28.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
