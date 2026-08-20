## AUDYT RYZYK — NDA wzajemne (Helix Soft / Baltic Capital)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; kara umowna bez sufitu liczby naruszeń i brak okresu poufności po zakończeniu negocjacji to dwa dealbreakery wymagające renegocjacji przed podpisem.

*Audyt neutralny — wady oznaczone niezależnie od tego, którą stronę faktycznie krzywdzą; przy każdej wskazano stronę dotkniętą.*

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | brak — NDA bez wynagrodzenia | — | [BRAK DANYCH] |
| Cap odpowiedzialności | brak w umowie | — | brak jakiegokolwiek limitu |
| Kara umowna (§ 3 ust. 1) | 200.000 zł „za każde naruszenie" | 200.000 zł × N (brak sufitu liczby naruszeń) | ekspozycja **otwarta**, teoretycznie nieograniczona przy powtarzających się naruszeniach |
| Efektywna ekspozycja | — | kara bez sufitu + brak capu odpowiedzialności | **nieograniczona** dla Strony Otrzymującej |
| Asymetria (Otrzymująca vs Ujawniająca) | kara: 200.000 zł / 0 zł (§ 3 ust. 2 wprost zwalnia Ujawniającą) | stosunek kar A/B = ∞ | 100% ryzyka kar po stronie Strony Otrzymującej |
| Daty graniczne | koniec obowiązywania = „okres prowadzenia Negocjacji" (§ 4 ust. 1) | brak definicji zdarzenia końcowego, brak daty | **brak** okresu poufności po zakończeniu współpracy — obowiązek wygasa razem z Negocjacjami |

**Wniosek z rachunku:** kara bez sufitu liczby naruszeń + brak jakiegokolwiek okresu przetrwania poufności po zakończeniu negocjacji razem tworzą sytuację, w której ochrona informacji Strony Ujawniającej kończy się w niejasnym momencie, a ryzyko finansowe Strony Otrzymującej nie ma górnej granicy — to kalibruje werdykt do 🟥, mimo że nominalnie umowa wygląda na prostą, standardową NDA.

### Bramka ius cogens (R10)

Żadna klauzula nie próbuje wprost obejść normy bezwzględnie obowiązującej (brak wyłączenia winy umyślnej, kara nie dotyczy zobowiązania pieniężnego, brak przeniesienia praw autorskich osobistych). Trigger mikroprzedsiębiorcy (art. 3855 KC) — nie dotyczy: obie strony to spółki kapitałowe (sp. z o.o., S.A.). Test kumulatywny: patrz „Ryzyka wysokie" niżej — kombinacja braku sufitu kar + braku okresu poufności po zakończeniu + jednostronności sankcji to efekt kumulatywny wart odnotowania, choć żadna z klauzul osobno nie jest nieważna z mocy prawa.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna bez sufitu liczby naruszeń — § 3 ust. 1
**Opis:** „Strona Otrzymująca zapłaci Stronie Ujawniającej karę umowną w wysokości 200.000 zł za każde naruszenie" — brak maksymalnej liczby naruszeń i brak łącznego sufitu kwotowego. Dotyczy Strony Otrzymującej (Baltic Capital).
**Skutek:** przy kilku odrębnych zdarzeniach naruszenia (np. kilka niezależnych ujawnień) ekspozycja rośnie liniowo bez ograniczenia — praktycznie nieograniczona odpowiedzialność finansowa.
**Rekomendacja (preferowana):** wprowadzić łączny sufit kar (np. „nie więcej niż X zł łącznie w okresie obowiązywania Umowy").
**Fallback (minimum akceptowalne):** doprecyzować, że wielokrotne naruszenia tego samego zdarzenia/przecieku traktowane są jako jedno naruszenie, z jednym pułapem kary.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Brak okresu poufności po zakończeniu negocjacji — § 4 ust. 1
**Opis:** Umowa „obowiązuje przez okres prowadzenia Negocjacji" — bez oznaczonej daty końcowej i bez klauzuli przetrwania (survival) obowiązku poufności po zakończeniu lub zerwaniu Negocjacji. Dotyczy interesu Strony Ujawniającej (Helix Soft) — po zakończeniu rozmów Informacje Poufne przestają być chronione.
**Skutek:** po formalnym/nieformalnym zakończeniu negocjacji obowiązek poufności może zostać uznany za wygasły, mimo że informacje wciąż mają wartość.
**Rekomendacja (preferowana):** dodać okres przetrwania poufności min. 3–5 lat od zakończenia Negocjacji (lub bezterminowo dla informacji stanowiących tajemnicę przedsiębiorstwa).
**Fallback (minimum akceptowalne):** minimum 12–24 miesiące od zakończenia Negocjacji.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 2. Asymetria sankcji — § 3 ust. 1–2
**Opis:** „Strona Ujawniająca nie ponosi kar umownych na podstawie niniejszej Umowy" — deklarowana wzajemność obowiązku poufności (§ 1 ust. 1: „Strony wzajemnie zobowiązują się") nie idzie w parze z wzajemnością sankcji. Dotyczy Strony Otrzymującej, która ponosi 100% ryzyka finansowego.
**Skutek:** przy typowej NDA przedinwestycyjnej obie strony zwykle wymieniają się informacjami — jeśli tak jest i tu, jednostronna sankcja jest nieuzasadniona gospodarczo.
**Rekomendacja (preferowana):** kara umowna wzajemna, symetryczna dla obu Stron.
**Fallback (minimum akceptowalne):** jeśli faktycznie tylko Strona Ujawniająca przekazuje informacje poufne — utrzymać asymetrię, ale wyraźnie to uzasadnić w preambule.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Brak wyłączeń z zakresu Informacji Poufnych — § 1 ust. 2
**Opis:** Definicja „Informacje Poufne oznaczają wszelkie informacje przekazane przez Stronę Ujawniającą w związku z Negocjacjami" — brak standardowych wyłączeń (informacje publicznie dostępne, uzyskane zgodnie z prawem od osób trzecich, opracowane niezależnie, wymagane do ujawnienia przez prawo). Dotyczy Strony Otrzymującej.
**Skutek:** teoretycznie Strona Otrzymująca odpowiada za „ujawnienie" nawet informacji już publicznie znanych.
**Rekomendacja (preferowana):** dodać standardowy katalog wyłączeń.
**Fallback (minimum akceptowalne):** minimum wyłączenie dla informacji już publicznie dostępnych.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. „Dołoży starań" przy obowiązku zabezpieczenia — § 2 ust. 2
**Opis:** „Strona Otrzymująca dołoży starań, aby zabezpieczyć Informacje Poufne przed dostępem osób trzecich" — obowiązek starannego działania zamiast konkretnego standardu bezpieczeństwa. Dotyczy Strony Ujawniającej (słabsza ochrona jej informacji).
**Skutek:** trudniej dochodzić naruszenia, gdy Strona Otrzymująca może bronić się „dołożeniem starań".
**Rekomendacja (preferowana):** określić konkretny standard („co najmniej takie środki bezpieczeństwa, jakie stosuje wobec własnych informacji poufnych, nie niższe niż standard rynkowy").
**Fallback (minimum akceptowalne):** pozostawić „dołoży starań", ale dodać przykładowy niewyczerpujący katalog środków.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 2. „Niezwłocznie" bez liczby dni — § 2 ust. 3
**Opis:** „Strona Otrzymująca niezwłocznie poinformuje Stronę Ujawniającą o każdym przypadku ujawnienia" — termin nieoznaczony liczbowo.
**Skutek:** spór o to, czy powiadomienie było „niezwłoczne".
**Rekomendacja (preferowana):** zastąpić „niezwłocznie" konkretnym terminem, np. „w terminie 48 godzin".
**Fallback (minimum akceptowalne):** „niezwłocznie, nie później niż w terminie 3 Dni Roboczych".
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 3. Zwrot ograniczony do „Materiałów Roboczych" — § 2 ust. 4
**Opis:** „Materiały Robocze podlegają zwrotowi na żądanie" — pojęcie „Materiały Robocze" użyte z wielkiej litery, ale **nie zdefiniowane** w umowie (antywzorzec: definicja-widmo). Obowiązek zwrotu nie obejmuje wprost wszystkich Informacji Poufnych (np. przekazanych ustnie, w prezentacjach, e-mailach).
**Skutek:** niejasny zakres obowiązku zwrotu/usunięcia po zakończeniu Negocjacji.
**Rekomendacja (preferowana):** zdefiniować „Materiały Robocze" lub zastąpić szerszym obowiązkiem zwrotu/usunięcia wszystkich nośników Informacji Poufnych, wraz z pisemnym potwierdzeniem.
**Fallback (minimum akceptowalne):** doprecyzować definicję choćby w jednym zdaniu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 4. Sąd wyłącznie siedziby Strony Ujawniającej — § 5 ust. 2
**Opis:** „sądem właściwym jest sąd siedziby Strony Ujawniającej" — jednostronny wybór forum na korzyść Helix Soft, bez uzasadnienia.
**Skutek:** dla Strony Otrzymującej (Baltic Capital) potencjalnie mniej dogodne prowadzenie sporu.
**Rekomendacja (preferowana):** właściwość ogólna wg siedziby pozwanego albo sąd neutralny.
**Fallback (minimum akceptowalne):** pozostawić, jeśli obie siedziby są blisko siebie (Gdynia/Sopot) — ryzyko praktycznie niewielkie.
**Klauzula z bazy:** `references/baza-klauzul/13-postanowienia-koncowe.md`

### 🟢 RYZYKA NISKIE

#### 1. Brak wskazania umocowania osób podpisujących
**Opis:** Umowa nie wskazuje sposobu reprezentacji (KRS) ani pełnomocnictw — w treści dostępnej do audytu brak tej sekcji (dane fikcyjne w nagłówku).
**Skutek:** przy realnym podpisie — ryzyko braku umocowania podpisującego.
**Rekomendacja (preferowana):** uzupełnić dane rejestrowe i sposób reprezentacji obu spółek.
**Fallback (minimum akceptowalne):** —
**Klauzula z bazy:** `references/baza-klauzul/01-strony-reprezentacja.md`

### ✓ Obszary bez zastrzeżeń

- **Prawa autorskie / IP** — n/d (NDA przedinwestycyjne, brak przedmiotu twórczego)
- **RODO** — n/d w treści (brak wskazania przetwarzania danych osobowych; jeśli w toku Negocjacji wymieniane będą dane osobowe pracowników/zarządu, warto dodać klauzulę RODO — nieuwzględnione jako osobne ryzyko z braku wskazania w tekście)
- **Tytuł prawny / przekwalifikowanie** — n/d (nie dotyczy umowy o świadczenie usług/zatrudnienie)

---

## OCENA BEZPIECZEŃSTWA: 52/100

Jedno ryzyko 🔴 (kara bez sufitu liczby naruszeń → nieograniczona ekspozycja) automatycznie ustawia werdykt na 🟥. Do tego trzy ryzyka 🟠 (brak okresu poufności po zakończeniu, jednostronność sankcji, brak wyłączeń z definicji) i cztery 🟡/🟢 — dokument wymaga uzupełnień redakcyjnych typowych dla NDA; zakres poprawek jest wąski (sufit kary, okres poufności po zakończeniu, wyłączenia z definicji), ale dopóki nie są wprowadzone, kara bez górnej granicy jest dealbreakerem.

**Werdykt:** NIE PODPISYWAĆ w obecnej formie — wymaga negocjacji punktu krytycznego (sufit kary) i uzupełnień 🟠 przed podpisem.

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (kara bez sufitu)
→ Zastosuj: `references/baza-klauzul/10-kary-umowne.md` — wariant z łącznym sufitem kar

🟠 RYZYKO 1 (brak survival poufności)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` — model warstwowy okresów poufności

🟠 RYZYKO 3 (brak wyłączeń definicji)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` — standardowy katalog wyłączeń

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
