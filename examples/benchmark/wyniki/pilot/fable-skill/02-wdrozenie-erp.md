# AUDYT RYZYK — Umowa wdrożeniowa ERP NOVA RETAIL / CODEX WORKS (benchmark, tryb express)

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie: umowa zawiera klauzule nieważne z mocy prawa (wina umyślna, kara za zobowiązanie pieniężne), nie przenosi skutecznie praw autorskich i jest systemowo jednostronna.

Audyt neutralny — wady flagowane niezależnie od tego, którą stronę krzywdzą. Tryb express: bez STOPów, bez pamięci MCP. Brak MCP `legal-cite` → wszystkie cytaty przepisów `[NIEZWERYFIKOWANE]`.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto ryczałt (§ 3 ust. 1) | — | 480.000 zł |
| Cap odpowiedzialności Wykonawcy | brak capu — zamiast tego wyłączenie: odpowiada „wyłącznie za szkody wyrządzone umyślnie" (§ 5 ust. 1) | — | ekspozycja Wykonawcy ≈ 0 (poza umyślnością własną) |
| Kara na Zamawiającego | 50.000 zł / dzień opóźnienia w płatności (§ 5 ust. 2), bez sufitu | 50.000 zł × 30 dni | **1.500.000 zł = 312% wartości umowy** (miesiąc opóźnienia); bez sufitu — ekspozycja otwarta |
| Kary na Wykonawcę | „Wykonawca nie ponosi kar" (§ 5 ust. 2) | — | 0 zł |
| Asymetria kar (Zamawiający vs Wykonawca) | — | 50.000 zł/dzień bez sufitu vs 0 zł | **asymetria całkowita (∞)** — i to na korzyść strony, która ma świadczyć |
| Termin płatności | 60 dni od doręczenia faktury (§ 3 ust. 2) | granica ustawy o zatorach | na limicie; sztywno niedopuszczalny, jeśli NOVA RETAIL = MŚP a CODEX = duży przedsiębiorca `[BRAK DANYCH]` o statusie stron |
| Termin wykonania | „niezwłocznie po podpisaniu" (§ 2 ust. 1) | niepoliczalne | `[BRAK DANYCH]` — brak jakiejkolwiek daty granicznej wdrożenia |
| Wypowiedzenie | Zamawiający: 0 możliwości; Wykonawca: w każdym czasie | — | asymetria całkowita; Zamawiający zamknięty w umowie bez terminu końcowego |

Wniosek z rachunku: Zamawiający płaci 480.000 zł za zobowiązanie starannego działania bez terminu, z ekspozycją karną 312% wartości umowy za miesiąc opóźnienia płatności, przy odpowiedzialności Wykonawcy bliskiej zeru. To nie jest umowa wzajemna w sensie ekonomicznym.

### Bramka ius cogens (R10) — TRAFIENIA

Skan katalogu `normy-bezwzglednie.md` dał **trzy trafienia** (szczegóły w 🔴 nr 1–3) — każde z nich to nieważność z mocy prawa, nie ryzyko negocjacyjne. Werdykt-triage wymuszony na 🟥. Trigger mikroprzedsiębiorcy (art. 385⁵ KC `[NIEZWERYFIKOWANE]`): nieaktywny — obie strony to sp. z o.o. Zastosowano także test efektu kumulatywnego — wynik w 🔴 nr 5.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Wyłączenie odpowiedzialności za winę umyślną podwykonawców — § 5 ust. 1 *(krzywdzi: NOVA RETAIL; klauzula częściowo nieważna)*
**Opis:** Wykonawca odpowiada „wyłącznie za szkody wyrządzone umyślnie, z wyłączeniem winy umyślnej podwykonawców". Nie można ważnie wyłączyć odpowiedzialności za szkodę wyrządzoną wierzycielowi umyślnie (art. 473 § 2 KC `[NIEZWERYFIKOWANE]`); za osoby, którymi dłużnik się posługuje, odpowiada jak za własne działanie (art. 474 KC `[NIEZWERYFIKOWANE]`) — wyłączenie umyślności podwykonawców to próba obejścia tej granicy. Dodatkowo redukcja całej odpowiedzialności do wyłącznie winy umyślnej oznacza zero odpowiedzialności za rażące niedbalstwo i zwykłe niewykonanie — na granicy właściwości stosunku (art. 353¹, art. 58 § 2 KC `[NIEZWERYFIKOWANE]`), bo wydrąża zobowiązanie z sankcji.
**Skutek:** fragment o podwykonawcach — nieważny (art. 58 § 3 KC `[NIEZWERYFIKOWANE]`); reszta daje Zamawiającemu iluzję kontraktu: szkoda z niedbalstwa przy wdrożeniu ERP (utrata danych, przestój sklepu) — bez rekompensaty umownej.
**Rekomendacja (preferowana):** odpowiedzialność na zasadach ogólnych z capem 100% wynagrodzenia; wyłączenie utraconych korzyści.
**Fallback (minimum akceptowalne):** cap 12-miesięczny / 50% wynagrodzenia, ale odpowiedzialność za rażące niedbalstwo zachowana.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Kara umowna za opóźnienie w płatności (zobowiązanie pieniężne) — § 5 ust. 2 *(krzywdzi: NOVA RETAIL; klauzula nieważna)*
**Opis:** „Zamawiający zapłaci karę umowną 50.000 zł za każdy dzień opóźnienia w płatności" — kara umowna za zobowiązanie pieniężne jest niedopuszczalna (art. 483 § 1 KC `[NIEZWERYFIKOWANE]`); za opóźnienie w zapłacie należą się odsetki, nie kara. Niezależnie od nieważności: rachunek — 30 dni = 1.500.000 zł = 312% wartości umowy, bez sufitu.
**Skutek:** klauzula nieważna, ale do czasu przesądzenia sporu działa jak straszak negocjacyjny i windykacyjny.
**Rekomendacja:** wykreślić; odsetki ustawowe za opóźnienie w transakcjach handlowych.
**Fallback:** brak — kary za zobowiązanie pieniężne nie da się „naprawić" sufitem.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Przeniesienie praw autorskich „bez ograniczeń" — brak pól eksploatacji — § 4 ust. 1 *(krzywdzi: NOVA RETAIL)*
**Opis:** „Wykonawca przenosi na Zamawiającego wszelkie prawa autorskie do stworzonego oprogramowania bez ograniczeń" — ogólna formuła zamiast wyraźnego wskazania pól eksploatacji (art. 41 ust. 2 PrAut `[NIEZWERYFIKOWANE]`). Antywzorzec „wszelkie… bez ograniczeń": nie zastępuje identyfikacji pól.
**Skutek:** brak skutku rozporządzającego w zakładanym zakresie — Zamawiający po zapłacie 480.000 zł może nie nabyć praw, które sądzi, że kupił. Wzmacnia to § 4 ust. 2: kod źródłowy „może, ale nie jest zobowiązany" przekazać — ERP bez kodu i bez pewnych praw.
**Rekomendacja:** katalog pól eksploatacji (utrwalanie, zwielokrotnianie, wprowadzanie do pamięci, modyfikacje/opracowania z prawem zezwalania, itd.), obowiązkowe wydanie kodu źródłowego i dokumentacji jako warunek odbioru.
**Fallback:** licencja wyłączna, nieograniczona czasowo, z depozytem kodu (escrow).
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Prawo do trenowania AI na danych Zamawiającego „niezależnie od pozostałych postanowień" — § 8 ust. 2 *(krzywdzi: NOVA RETAIL)*
**Opis:** „Niezależnie od pozostałych postanowień Umowy, Wykonawca zachowuje prawo do wykorzystania danych Zamawiającego do trenowania modeli AI." Podwójny antywzorzec: klauzula nadpisująca (ubezskutecznia m.in. poufność z § 6) + otwarty cel przetwarzania. Dane systemu ERP retailera to dane osobowe klientów i pracowników — przetwarzanie we własnym celu Wykonawcy wykracza poza powierzenie; umowa nie zawiera żadnego instrumentu z art. 28 ust. 3 RODO `[NIEZWERYFIKOWANE]`.
**Skutek:** naruszenie RODO po stronie Zamawiającego jako administratora (kara administracyjna — art. 83 RODO `[NIEZWERYFIKOWANE]`), wyciek tajemnicy przedsiębiorstwa do modeli Wykonawcy.
**Rekomendacja:** wykreślić; zawrzeć umowę powierzenia (art. 28 RODO) z zakazem przetwarzania w celach własnych Wykonawcy.
**Fallback:** brak dla obecnego brzmienia; ewentualnie trenowanie wyłącznie na danych zanonimizowanych, za odrębną, wyraźną zgodą.
**Klauzula z bazy:** `references/baza-klauzul/14-rodo.md` + `references/checklist-dpa-art28.md`

#### 5. Efekt kumulatywny: systemowa jednostronność — § 1 + § 2 + § 5 + § 7 *(krzywdzi: NOVA RETAIL)*
**Opis:** test pięciopunktowy, krok 5: nawet klauzule z osobna obronialne składają się tu na niedopuszczalną całość — zobowiązanie tylko starannego działania („dołoży starań", § 1 ust. 1) + brak terminu („niezwłocznie po podpisaniu", § 2 ust. 1) + zerowa odpowiedzialność (§ 5) + wsparcie „według wyłącznego uznania" (§ 5 ust. 3) + zakaz wypowiedzenia przez Zamawiającego przy wypowiedzeniu Wykonawcy „w każdym czasie i bez podania przyczyny" (§ 7). Zamawiający nie ma żadnego środka egzekucji ani wyjścia; Wykonawca — pełną swobodę. Rażąca asymetria bez uzasadnienia gospodarczego (art. 353¹ + art. 58 § 2 KC `[NIEZWERYFIKOWANE]`).
**Skutek:** ryzyko nieważności konstrukcji w zakresie sprzecznym z zasadami współżycia; biznesowo — zapłata bez gwarancji świadczenia.
**Rekomendacja:** zobowiązanie rezultatu z harmonogramem i karami za zwłokę Wykonawcy, symetryczne wypowiedzenie z okresem, wsparcie z SLA.
**Fallback:** kamienie milowe z prawem odstąpienia Zamawiającego po przekroczeniu terminu o X dni.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Prawo stanu Delaware i sąd w Wilmington — § 8 ust. 1 *(krzywdzi: NOVA RETAIL)*
**Opis:** umowa między dwiema polskimi spółkami, wykonywana w Polsce, poddana „prawu stanu Delaware (USA)" z sądem w Wilmington — bez żadnego uzasadnienia. Koszt dochodzenia roszczeń za oceanem czyni ochronę prawną iluzoryczną; ocena skuteczności klauzul (w tym nieważności z 🔴) wymagałaby opinii z prawa obcego.
**Rekomendacja:** prawo polskie, sąd siedziby pozwanego lub Zamawiającego. **Fallback:** prawo polskie + arbitraż w Polsce (np. SA KIG).

#### 2. „Dołoży starań" + „niezwłocznie" + „na bieżąco" — § 1 ust. 1, § 2 *(krzywdzi: NOVA RETAIL)*
**Opis:** wdrożenie ERP zdegradowane do starannego działania bez terminu; obowiązek Zamawiającego zgłaszania uwag „na bieżąco" — niepoliczalny, a może posłużyć do zarzutu braku współdziałania. Brak harmonogramu, kamieni milowych, procedury odbioru.
**Rekomendacja:** zobowiązanie rezultatu, harmonogram etapów z datami, procedura odbioru z terminami zgłaszania uwag. **Fallback:** minimum data końcowa wdrożenia + odbiór końcowy.

#### 3. Kod źródłowy: „może, ale nie jest zobowiązany" — § 4 ust. 2 *(krzywdzi: NOVA RETAIL)*
**Opis:** pozorne zobowiązanie (antywzorzec) — uprawnienie udające świadczenie. Bez kodu Zamawiający jest trwale uzależniony od Wykonawcy (vendor lock-in), którego wsparcie i tak jest „według wyłącznego uznania".
**Rekomendacja:** wydanie kodu i dokumentacji jako element odbioru. **Fallback:** depozyt kodu z warunkami wydania.

### 🟡 RYZYKA ŚREDNIE

#### 1. Termin płatności 60 dni — § 3 ust. 2 *(krzywdzi: CODEX WORKS lub NOVA RETAIL — zależnie od statusu)*
Na limicie ustawy o przeciwdziałaniu nadmiernym opóźnieniom (art. 7 `[NIEZWERYFIKOWANE]`); jeśli dłużnik jest dużym przedsiębiorcą a wierzyciel MŚP — 60 dni to sztywny maks. `[BRAK DANYCH]` o statusie stron. Zweryfikować i rozważyć 30 dni.

#### 2. Poufność szczątkowa — § 6 *(obie strony)*
Jedno zdanie: brak definicji, okresu po zakończeniu umowy, wyłączeń i sankcji — a § 8 ust. 2 i tak ją nadpisuje. Uzupełnić o pełną klauzulę (`references/baza-klauzul/09-poufnosc.md`).

#### 3. Braki formalne komparycji *(obie strony)*
Brak daty i miejsca zawarcia, siedzib, KRS/NIP, reprezentacji (Złota Reguła 8). Brak potwierdzenia istnienia Załącznika nr 1, od którego zależy zakres wdrożenia (ryzyko osieroconego załącznika).

### 🟢 RYZYKA NISKIE

#### 1. Terminologia „Wdrożenie" — § 1 ust. 2
Pojęcie pisane wielką literą bez definicji; zakres wynika tylko z Załącznika nr 1. Dodać do definicji.

### ✓ Obszary bez zastrzeżeń (bramka kompletności R9 — 9 obszarów)

- **Odpowiedzialność i kary** — 🔴 nr 1, 2, 5
- **Prawa autorskie** — 🔴 nr 3, 🟠 nr 3
- **Definicje i logika** — 🟡 nr 3, 🟢 nr 1
- **Reprezentacja** — 🟡 nr 3
- **Wypowiedzenie i exit** — 🔴 nr 5 (asymetria § 7; brak procedury exit i zwrotu danych)
- **RODO** — 🔴 nr 4
- **Tytuł prawny i przekwalifikowanie** — ✓ sprawdzone, brak zastrzeżeń (umowa B2B wdrożeniowa między spółkami; brak ryzyka KP/ZUS)
- **Poufność** — 🟡 nr 2
- **Spory** — 🟠 nr 1

---

## OCENA BEZPIECZEŃSTWA: 12/100

Trzy trafienia ius cogens (wina umyślna podwykonawców, kara za zobowiązanie pieniężne, pola eksploatacji), klauzula trenowania AI nadpisująca resztę umowy, obce prawo i sąd oraz systemowa jednostronność potwierdzona testem kumulatywnym. Dla Zamawiającego umowa nie daje ani świadczenia pewnego, ani praw, ani wyjścia; dla Wykonawcy część jego „przewag" jest po prostu nieważna, więc też nie dostaje tego, co sądzi.

**Werdykt:** NIE PODPISYWAĆ

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 → `references/baza-klauzul/11-odpowiedzialnosc.md` — wariant z capem i zachowaną odpowiedzialnością za rażące niedbalstwo
🔴 RYZYKO 2 → `references/baza-klauzul/10-kary-umowne.md` — kary za zwłokę Wykonawcy (niepieniężne), odsetki za płatności
🔴 RYZYKO 3 → `references/baza-klauzul/08-prawa-autorskie-ip.md` — katalog pól + wydanie kodu
🔴 RYZYKO 4 → umowa powierzenia wg `references/checklist-dpa-art28.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
