# AUDYT RYZYK — NDA HELIX SOFT / BALTIC CAPITAL (benchmark, tryb express)

> **WERDYKT: 🟨 ŻÓŁTY** — Do negocjacji: umowa deklaruje wzajemność, której nie zawiera, a poufność wygasa razem z negocjacjami; poprawki przed podpisem konieczne, brak nieważności z mocy prawa.

Audyt neutralny — wady flagowane niezależnie od tego, którą stronę krzywdzą (przy każdej fladze wskazano poszkodowanego). Tryb express: bez STOPów, bez pamięci MCP. Brak MCP `legal-cite` → wszystkie cytaty przepisów `[NIEZWERYFIKOWANE]`.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | brak (NDA bez wynagrodzenia) | — | `[BRAK DANYCH]` |
| Cap odpowiedzialności | brak klauzuli capu | — | ekspozycja na zasadach ogólnych, bez limitu |
| Kara umowna — Strona Otrzymująca | 200.000 zł „za każde naruszenie" (§ 3 ust. 1) | brak sufitu liczby naruszeń: 200.000 zł × n | **ekspozycja otwarta** (np. 5 naruszeń = 1.000.000 zł) |
| Kara umowna — Strona Ujawniająca | 0 zł (§ 3 ust. 2) | — | 0 zł |
| Asymetria kar (Otrzymująca vs Ujawniająca) | — | 200.000 zł × n vs 0 zł | **asymetria całkowita (∞)** |
| Okres poufności | „przez okres prowadzenia Negocjacji" (§ 4) | koniec negocjacji = koniec ochrony | **0 dni ochrony po zakończeniu** |
| Daty graniczne | brak daty zawarcia, brak terminu zwrotu materiałów | — | `[BRAK DANYCH]` |

Wniosek z rachunku: jedna strona niesie nieograniczoną liczbowo ekspozycję karną, druga zero — a jednocześnie realna ochrona informacji kończy się w dniu zerwania negocjacji. Umowa jest słaba dla obu stron naraz, tylko w różnych miejscach.

### Bramka ius cogens (R10)

Przebiegnięto katalog `normy-bezwzglednie.md`: kara umowna z § 3 zabezpiecza zobowiązanie niepieniężne (poufność) — art. 483 § 1 KC `[NIEZWERYFIKOWANE]` nie jest naruszony. Brak klauzul wyłączających winę umyślną, brak manipulacji przedawnieniem. Trigger mikroprzedsiębiorcy (art. 385⁵ KC `[NIEZWERYFIKOWANE]`): nieaktywny — obie strony to spółki kapitałowe. **Brak trafień** — werdykt nie jest wymuszony na 🟥.

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

#### 1. Pozorna wzajemność — kary tylko na jedną stronę — § 1 ust. 1 vs § 3 ust. 2 *(krzywdzi: BALTIC CAPITAL)*
**Opis:** § 1 ust. 1 deklaruje, że „Strony wzajemnie zobowiązują się do zachowania w poufności", ale role są przypisane sztywno (HELIX = zawsze Ujawniająca, BALTIC = zawsze Otrzymująca), a § 3 ust. 2 stanowi wprost: „Strona Ujawniająca nie ponosi kar umownych na podstawie niniejszej Umowy". W negocjacjach inwestycyjnych informacje ujawnia zwykle także inwestor (warunki oferty, strategia). Antywzorzec „fałszywa symetria".
**Skutek:** BALTIC płaci 200.000 zł za naruszenie, HELIX za lustrzane naruszenie — nic; informacje BALTIC w ogóle nie są objęte definicją Informacji Poufnych.
**Rekomendacja (preferowana):** prawdziwie wzajemna konstrukcja — każda strona jest Ujawniającą wobec własnych informacji, kary symetryczne.
**Fallback (minimum akceptowalne):** utrzymanie ról jednostronnych, ale objęcie ochroną (bez kary) także informacji przekazanych przez BALTIC + sufit łączny kar.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 2. Kara 200.000 zł „za każde naruszenie" bez sufitu i bez definicji naruszenia — § 3 ust. 1 *(krzywdzi: BALTIC CAPITAL)*
**Opis:** brak sufitu łącznego i brak rozstrzygnięcia, czy np. jeden e-mail do trzech osób to jedno czy trzy naruszenia. Ekspozycja otwarta (zob. rachunek). Kara oderwana od jakiejkolwiek wartości odniesienia (umowa nie ma wartości).
**Skutek:** roszczenia w skali wielokrotności realnej szkody; dla HELIX ryzyko odwrotne — zarzut rażącego wygórowania i miarkowanie (art. 484 § 2 KC `[NIEZWERYFIKOWANE]`), czyli kara mniej pewna, niż wygląda.
**Rekomendacja:** sufit łączny (np. 400.000 zł), definicja „przypadku naruszenia", zastrzeżenie odszkodowania uzupełniającego dla Ujawniającej.
**Fallback:** sam sufit łączny.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Poufność wygasa z końcem Negocjacji — § 4 ust. 1 *(krzywdzi: HELIX SOFT)*
**Opis:** „Umowa obowiązuje przez okres prowadzenia Negocjacji." Brak okresu ochrony po zakończeniu umowy — a właśnie po zerwanych negocjacjach ryzyko wykorzystania informacji jest największe. Dodatkowo „okres prowadzenia Negocjacji" jest niepoliczalny (kto i jak stwierdza ich koniec?).
**Skutek:** dzień po zerwaniu rozmów BALTIC może — na gruncie tej umowy — swobodnie korzystać z know-how HELIX (pozostaje tylko ochrona ustawowa tajemnicy przedsiębiorstwa, art. 11 uznk `[NIEZWERYFIKOWANE]`).
**Rekomendacja:** okres poufności 3–5 lat po zakończeniu Negocjacji; dla tajemnicy przedsiębiorstwa — bezterminowo.
**Fallback:** minimum 2 lata po zakończeniu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` — model warstwowy okresów

#### 4. Definicja Informacji Poufnych bez wyłączeń — § 1 ust. 2 *(krzywdzi: BALTIC CAPITAL)*
**Opis:** „wszelkie informacje przekazane przez Stronę Ujawniającą w związku z Negocjacjami" — zakres maksymalny („wszelkie"), brak standardowych wyłączeń: informacje publicznie dostępne, znane wcześniej, opracowane niezależnie, ujawniane na żądanie organu.
**Skutek:** BALTIC ryzykuje karę 200.000 zł nawet za posłużenie się informacją powszechnie dostępną, o ile HELIX też ją „przekazał".
**Rekomendacja:** katalog czterech standardowych wyłączeń + wyjątek ujawnienia z mocy prawa z obowiązkiem notyfikacji.
**Fallback:** minimum wyłączenie informacji publicznie dostępnych i ujawnienia wymaganego prawem.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. Definicje-widma: „Negocjacje" i „Materiały Robocze" — § 1, § 2 ust. 4 *(obie strony)*
Pojęcia pisane wielką literą bez definicji (Złota Reguła 1). „Materiały Robocze podlegają zwrotowi na żądanie" — nie wiadomo, co to za materiały, bez terminu zwrotu i bez obowiązku zniszczenia kopii. **Rekomendacja:** § Definicje + procedura zwrotu/zniszczenia z terminem (np. 7 dni) i potwierdzeniem.

#### 2. Zobowiązania rozmyte: „dołoży starań" i „niezwłocznie" — § 2 ust. 2–3 *(krzywdzi: HELIX SOFT)*
Zabezpieczenie informacji jako staranne działanie bez standardu (jakiego poziomu zabezpieczeń wolno oczekiwać?) oraz notyfikacja naruszenia „niezwłocznie" bez liczby dni — oba antywzorce. **Rekomendacja:** standard ochrony „co najmniej jak dla własnych informacji tego rodzaju, nie mniej niż rozsądne środki" + notyfikacja w 24/48 h.

#### 3. Braki formalne: data, miejsce zawarcia, reprezentacja, KRS/NIP — komparycja *(obie strony)*
Brak daty i miejsca zawarcia, brak osób podpisujących i umocowania (Złota Reguła 8). Bez daty nie da się nawet ustalić początku „okresu prowadzenia Negocjacji". **Rekomendacja:** uzupełnić komparycję o pełne dane rejestrowe i reprezentację.

#### 4. Brak regulacji danych osobowych w due diligence *(obie strony)*
Negocjacje inwestycyjne zwykle obejmują dane osobowe (pracownicy, klienci). Umowa milczy o podstawie wymiany i rolach RODO. **Rekomendacja:** klauzula kwalifikująca role (odrębni administratorzy) i minimalizacja danych na etapie DD.

### 🟢 RYZYKA NISKIE

#### 1. Sąd siedziby Strony Ujawniającej — § 5 ust. 2 *(krzywdzi: BALTIC CAPITAL)*
Gdynia vs Sopot — praktycznie ten sam okręg, waga znikoma; niespójne tylko z deklarowaną wzajemnością. Sugestia: sąd siedziby pozwanego.

### ✓ Obszary bez zastrzeżeń (bramka kompletności R9 — 9 obszarów)

- **Odpowiedzialność i kary** — ryzyka 🟠 nr 1–2 (powyżej)
- **Prawa autorskie** — n/d (NDA nie przenosi IP; brak też ukrytych klauzul licencyjnych — sprawdzono)
- **Definicje i logika** — ryzyka 🟠 nr 4, 🟡 nr 1
- **Reprezentacja** — ryzyko 🟡 nr 3
- **Wypowiedzenie i exit** — ryzyko 🟠 nr 3 (okres obowiązywania) + 🟡 nr 1 (zwrot materiałów)
- **RODO** — ryzyko 🟡 nr 4
- **Tytuł prawny i przekwalifikowanie** — ✓ sprawdzone, brak zastrzeżeń (NDA bez świadczenia pracy/usług)
- **Poufność** — ryzyka 🟠 nr 3–4
- **Spory** — ✓ sprawdzone poza uwagą 🟢 nr 1: prawo polskie, sąd powszechny — bez zastrzeżeń

---

## OCENA BEZPIECZEŃSTWA: 56/100

Brak wad nieusuwalnych (ius cogens czysty), ale konstrukcja rozjeżdża się z deklaracją: „wzajemne" NDA chroni wyłącznie jedną stronę karą bez sufitu, a jednocześnie nie chroni nikogo po zakończeniu negocjacji. Cztery ryzyka wysokie, cztery średnie — wszystkie naprawialne standardowymi klauzulami.

**Werdykt:** DO NEGOCJACJI

### Klauzule z bazy KTZR do uzupełnienia

🟠 RYZYKO 1, 3, 4 → `references/baza-klauzul/09-poufnosc.md` (wzajemność, warstwowe okresy, wyłączenia)
🟠 RYZYKO 2 → `references/baza-klauzul/10-kary-umowne.md` (sufit łączny, definicja przypadku naruszenia)

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
