## AUDYT RYZYK — UMOWA O ŚWIADCZENIE USŁUG UTRZYMANIA

> **WERDYKT: 🟨 ŻÓŁTY** — Do negocjacji — wskazane poprawki przed podpisem, w szczególności uzupełnienie umowy o klauzule dotyczące przetwarzania danych osobowych (RODO).

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
| :--- | :--- | :--- | :--- |
| Wartość umowy (roczna) | 8 000 zł netto / m-c | 12 × 8 000 zł | **96 000 zł netto** |
| Cap nominalny | 12-miesięczne wynagrodzenie netto | 12 × 8 000 zł | **96 000 zł** |
| Kary umowne (max) | 20% wynagrodzenia rocznego netto | 0,20 × 96 000 zł | **19 200 zł** |
| Efektywna ekspozycja | — | Cap + wyłączenia z capu | **96 000 zł** + odpowiedzialność za naruszenie poufności (bez limitu) + szkoda umyślna (bez limitu z mocy prawa) |
| Asymetria (Usługodawca vs Usługobiorca) | — | Sąd właściwy dla Usługodawcy; wyłączenie utraconych korzyści na korzyść Usługodawcy. | Umiarkowana asymetria na korzyść Usługodawcy. |
| Daty graniczne | Wypowiedzenie: 3 m-ce; Płatność: 30 dni | — | Standardowe, brak podwyższonego ryzyka. |

**Wniosek z rachunku:** Umowa jest dobrze zbalansowana pod kątem finansowym. Nominalny limit odpowiedzialności (cap) jest standardem rynkowym (100% wartości rocznej). Kluczowym ryzykiem finansowym dla Usługodawcy jest wyłączenie naruszeń poufności spod limitu odpowiedzialności, co tworzy potencjalnie nieograniczoną ekspozycję w tym zakresie.

### 🟠 RYZYKA WYSOKIE

#### 1. Brak umowy powierzenia przetwarzania danych (RODO) — [Luka w umowie]
**Opis:** Umowa dotyczy utrzymania "oprogramowania magazynowego", które z wysokim prawdopodobieństwem przetwarza dane osobowe (np. dane pracowników, kontrahentów). Umowa nie zawiera jednak klauzul powierzenia przetwarzania danych osobowych, wymaganych przez art. 28 RODO [NIEZWERYFIKOWANE]. Usługodawca, uzyskując dostęp do Systemu, staje się podmiotem przetwarzającym (procesorem) na zlecenie Usługobiorcy (administratora).
**Skutek:** Naruszenie przepisów RODO, które naraża **obie Strony** na wysokie kary administracyjne (do 10 mln EUR lub 2% rocznego obrotu). Umowa w obecnym kształcie nie legalizuje operacji przetwarzania danych przez Usługodawcę.
**Rekomendacja (preferowana):** Strony powinny zawrzeć odrębną Umowę Powierzenia Przetwarzania Danych Osobowych jako załącznik do niniejszej umowy.
**Fallback (minimum akceptowalne):** Dodać do umowy nowy paragraf, który będzie zawierał wszystkie obligatoryjne elementy z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE].

### 🟡 RYZYKA ŚREDNIE

#### 1. Asymetryczna klauzula jurysdykcyjna — § 8 ust. 2
**Opis:** Klauzula `[CYTAT NIEZWERYFIKOWANY]` "Sądem właściwym jest sąd powszechny właściwy dla siedziby Usługodawcy" jest jednostronna. W przypadku sporu zmusza Usługobiorcę do prowadzenia sprawy w sądzie właściwym dla drugiej strony, co może generować dodatkowe koszty i utrudnienia logistyczne.
**Skutek:** Ryzyko po stronie **Usługobiorcy**. Zwiększone koszty i złożoność ewentualnego procesu sądowego.
**Rekomendacja (preferowana):** Zmiana na klauzulę symetryczną: "sąd właściwy dla siedziby pozwanego" lub "sąd właściwy dla siedziby Usługobiorcy".
**Fallback (minimum akceptowalne):** Pozostawienie zapisu w obecnym kształcie – jest to częsty element negocjacji i standardowa pozycja wyjściowa dostawców usług.

#### 2. Wyłączenie odpowiedzialności za utracone korzyści — § 5 ust. 2
**Opis:** Zapis `[CYTAT NIEZWERYFIKOWANY]` "Usługodawca nie odpowiada za utracone korzyści Usługobiorcy" jest standardową klauzulą chroniącą dostawcę, ale stanowi istotne ryzyko dla klienta. Awaria Krytyczna Systemu magazynowego może prowadzić do wstrzymania operacji, a w konsekwencji do utraty zysków, których Usługobiorca nie będzie mógł dochodzić.
**Skutek:** Ryzyko po stronie **Usługobiorcy**. Brak możliwości uzyskania pełnej rekompensaty za szkody biznesowe wynikające z niewykonania lub nienależytego wykonania umowy.
**Rekomendacja (preferowana):** Usunięcie klauzuli.
**Fallback (minimum akceptowalne):** Ograniczenie wyłączenia tylko do przypadków winy nieumyślnej lub powiązanie odpowiedzialności za utracone korzyści z naruszeniem kluczowych parametrów SLA (np. czasu usunięcia Awarii Krytycznej).

#### 3. Brak pełnych danych i weryfikacji reprezentacji Stron — [Komparycja]
**Opis:** W komparycji umowy brakuje kluczowych danych rejestrowych Stron (NIP, REGON, KRS) oraz informacji o osobach upoważnionych do ich reprezentacji.
**Skutek:** Ryzyko dla **obu Stron**. Podpisanie umowy przez osoby nieupoważnione może prowadzić do jej nieważności. Brak danych utrudnia identyfikację kontrahenta.
**Rekomendacja (preferowana):** Uzupełnienie pełnych danych Stron zgodnie z aktualnym odpisem z KRS i wskazanie sposobu reprezentacji oraz osób podpisujących umowę.
**Fallback (minimum akceptowalne):** Brak – uzupełnienie danych jest obligatoryjne dla bezpieczeństwa prawnego transakcji.

### ✓ Obszary bez zastrzeżeń

*   **Definicje i logika:** Definicje są precyzyjne i spójnie stosowane.
*   **Prawa autorskie:** n/d (umowa nie dotyczy przenoszenia praw autorskich).
*   **Tytuł prawny i przekwalifikowanie:** Brak ryzyka przekwalifikowania na umowę o pracę.
*   **Poufność:** Klauzule są prawidłowo skonstruowane, z określeniem czasu trwania i standardowymi wyłączeniami.
*   **Wypowiedzenie i exit:** Symetryczny okres wypowiedzenia i procedura zwrotu danych są prawidłowe.

---

## OCENA BEZPIECZEŃSTWA: 80/100

**Uzasadnienie:** Umowa jest profesjonalnie przygotowana i dobrze zbalansowana w kluczowych obszarach (odpowiedzialność, kary umowne, SLA). Ocena została obniżona głównie z powodu całkowitego pominięcia kwestii RODO, co stanowi wysokie ryzyko regulacyjne dla obu stron. Pozostałe zidentyfikowane ryzyka mają charakter średni i są typowymi punktami negocjacyjnymi w umowach B2B.

**Werdykt:** DO NEGOCJACJI

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*