## AUDYT RYZYK — UMOWA WDROŻENIOWA

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie — umowa zawiera wady prawne i krytyczne ryzyka biznesowe, które czynią ją skrajnie niekorzystną i niebezpieczną, głównie dla Zamawiającego.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
| :--- | :--- | :--- | :--- |
| Wartość umowy | 480 000 zł netto | — | 480 000 zł |
| Cap nominalny | [BRAK DANYCH] | Odpowiedzialność Wykonawcy ograniczona do winy umyślnej, bez limitu kwotowego. | Brak realnego limitu, ale skrajnie zawężony zakres odpowiedzialności. |
| Kary umowne (max) | Zamawiający: 50 000 zł/dzień. Wykonawca: 0 zł. | 50 000 zł × 30 dni (przykładowo) | **1 500 000 zł** (dla Zamawiającego) |
| Efektywna ekspozycja | — | **Wykonawca:** Odpowiedzialność tylko za własne działania umyślne. **Zamawiający:** Potencjalnie nieograniczona (kara umowna bez sufitu). | **Ekspozycja Zamawiającego >312% wartości umowy po 30 dniach opóźnienia.** |
| Asymetria (Z vs W) | — | Odpowiedzialność, kary, wypowiedzenie – jednostronnie na korzyść Wykonawcy. | Skrajna asymetria. |
| Daty graniczne | Terminy: „niezwłocznie”, „na bieżąco”. Płatność: 60 dni. | Brak konkretnych dat. | Terminy niewiążące, ryzyko sporów. |

**Wniosek z rachunku:** Umowa tworzy iluzję współpracy, przerzucając niemal całe ryzyko i koszty na Zamawiającego. Ekspozycja finansowa Zamawiającego jest nieograniczona, podczas gdy Wykonawca jest niemal całkowicie zwolniony z odpowiedzialności.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Nieważna kara umowna za opóźnienie w płatności — § 5 ust. 2
**Opis:** Umowa przewiduje karę umowną w wysokości 50 000 zł za każdy dzień opóźnienia w zapłacie wynagrodzenia. Zastrzeganie kar umownych na wypadek niewykonania lub nienależytego wykonania zobowiązania pieniężnego jest nieważne z mocy prawa.
**Skutek:** Postanowienie jest nieważne zgodnie z art. 483 § 1 KC [NIEZWERYFIKOWANE]. Wykonawcy za opóźnienie w płatności przysługują jedynie odsetki ustawowe za opóźnienie w transakcjach handlowych. Mimo nieważności, tak sformułowana klauzula świadczy o skrajnie agresywnym i nieprofesjonalnym podejściu Wykonawcy.
**Rekomendacja (preferowana):** Usunąć całe postanowienie.
**Fallback (minimum akceptowalne):** Brak. Postanowienie jest bezwzględnie nieważne.

#### 2. Skrajnie asymetryczne prawo do wypowiedzenia umowy — § 7
**Opis:** Zamawiający jest pozbawiony prawa do wypowiedzenia umowy, podczas gdy Wykonawca może ją rozwiązać „w każdym czasie i bez podania przyczyny”.
**Skutek:** Zamawiający jest „uwięziony” w kontrakcie bez możliwości wyjścia, nawet jeśli Wykonawca nie realizuje prac. Wykonawca może porzucić projekt w dowolnym momencie bez żadnych konsekwencji, narażając Zamawiającego na ogromne straty. Klauzula może być uznana za sprzeczną z naturą stosunku zobowiązaniowego i zasadami współżycia społecznego (art. 353¹ KC [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** Wprowadzić symetryczne prawo do wypowiedzenia dla obu stron z zachowaniem okresu wypowiedzenia (np. 30 dni) oraz z ważnych powodów (np. rażące naruszenie umowy).
**Fallback (minimum akceptowalne):** Przyznać Zamawiającemu prawo do wypowiedzenia umowy za okresem wypowiedzenia, np. 1-miesięcznym, na koniec miesiąca kalendarzowego.

#### 3. Nieskuteczne przeniesienie praw autorskich — § 4 ust. 1
**Opis:** Klauzula o przeniesieniu praw autorskich ma charakter blankietowy („wszelkie prawa autorskie (...) bez ograniczeń”). Zgodnie z art. 41 ust. 2 Prawa autorskiego [NIEZWERYFIKOWANE], umowa musi wyraźnie wymieniać pola eksploatacji, na których utwór ma być wykorzystywany.
**Skutek:** Brak wymienienia pól eksploatacji powoduje, że przeniesienie praw jest nieskuteczne. Zamawiający zapłaci pełne wynagrodzenie, ale nie nabędzie praw do oprogramowania, za które płaci.
**Rekomendacja (preferowana):** Zastąpić klauzulę precyzyjnym postanowieniem wymieniającym wszystkie istotne pola eksploatacji (np. zwielokrotnianie, wprowadzanie do pamięci komputera, modyfikacje, dystrybucja etc.).
**Fallback (minimum akceptowalne):** Wprowadzić co najmniej podstawowe pola eksploatacji niezbędne do korzystania z systemu zgodnie z jego przeznaczeniem.

#### 4. Wybór prawa i sądu obcego — § 8 ust. 1
**Opis:** Umowa między dwiema polskimi spółkami podlega prawu stanu Delaware (USA), a spory rozstrzygać ma sąd w Wilmington. Jest to zapis absurdalny i skrajnie niekorzystny.
**Skutek:** Drastycznie podnosi koszty i próg dochodzenia jakichkolwiek roszczeń. Prowadzenie sporu w USA wymaga zatrudnienia amerykańskich prawników i generuje ogromne koszty, co w praktyce uniemożliwia Zamawiającemu egzekwowanie swoich praw.
**Rekomendacja (preferowana):** Zmienić zapis na prawo polskie i sąd właściwy miejscowo dla siedziby Zamawiającego.
**Fallback (minimum akceptowalne):** Prawo polskie i sąd właściwy według przepisów Kodeksu postępowania cywilnego lub sąd polubowny w Polsce.

#### 5. Przetwarzanie danych do trenowania AI — § 8 ust. 2
**Opis:** Klauzula przyznaje Wykonawcy prawo do wykorzystania danych Zamawiającego do trenowania modeli AI, i to „niezależnie od pozostałych postanowień Umowy”.
**Skutek:** Jest to gigantyczne ryzyko biznesowe i prawne. Jeśli dane obejmują tajemnice przedsiębiorstwa, know-how lub dane osobowe, ich wykorzystanie w ten sposób stanowi rażące naruszenie poufności i przepisów RODO (brak podstawy prawnej, naruszenie zasady ograniczenia celu). Klauzula unieważnia jakiekolwiek gwarancje poufności.
**Rekomendacja (preferowana):** Usunąć całe postanowienie.
**Fallback (minimum akceptowalne):** Brak. Klauzula jest niedopuszczalna.

#### 6. Iluzoryczna odpowiedzialność Wykonawcy — § 5 ust. 1
**Opis:** Wykonawca ogranicza swoją odpowiedzialność wyłącznie do szkód wyrządzonych umyślnie, wyłączając winę umyślną podwykonawców.
**Skutek:** Wyłączenie odpowiedzialności za winę umyślną jest nieważne (art. 473 § 2 KC [NIEZWERYFIKOWANE]). Jednakże, ograniczenie odpowiedzialności do samej winy umyślnej (z wyłączeniem rażącego niedbalstwa) jest w obrocie B2B dopuszczalne, ale w tym przypadku skrajnie niekorzystne dla Zamawiającego. Oznacza to, że za wszelkie błędy, opóźnienia i wady systemu, które nie wynikają z celowego działania Wykonawcy, nie poniesie on żadnej odpowiedzialności.
**Rekomendacja (preferowana):** Wprowadzenie pełnej odpowiedzialności Wykonawcy za niewykonanie lub nienależyte wykonanie umowy, z limitem odpowiedzialności (cap) np. do 100% wartości umowy.
**Fallback (minimum akceptowalne):** Rozszerzenie odpowiedzialności co najmniej o rażące niedbalstwo i wprowadzenie limitu odpowiedzialności na akceptowalnym poziomie (np. 50-100% wartości umowy).

### 🟠 RYZYKA WYSOKIE

#### 1. Zobowiązanie starannego działania zamiast rezultatu — § 1 ust. 1
**Opis:** Wykonawca „dołoży starań w celu wdrożenia”, a nie „zobowiązuje się wdrożyć”. Jest to zobowiązanie starannego działania, a nie rezultatu.
**Skutek:** Zamawiający płaci za próbę wdrożenia, a nie za działający system. Wykonawca może argumentować, że dochował należytej staranności, nawet jeśli wdrożenie się nie powiodło, i żądać pełnego wynagrodzenia.
**Rekomendacja (preferowana):** Zmienić sformułowanie na: „Wykonawca zobowiązuje się do wdrożenia Systemu (...)”.
**Fallback (minimum akceptowalne):** Pozostawienie starannego działania, ale powiązanie płatności z odbiorem konkretnych, działających funkcjonalności (kamieni milowych).

#### 2. Brak gwarancji dostępu do kodu źródłowego — § 4 ust. 2
**Opis:** Umowa stanowi, że Wykonawca „może, ale nie jest zobowiązany” przekazać kod źródłowy.
**Skutek:** Brak dostępu do kodu źródłowego powoduje całkowite uzależnienie (vendor lock-in) Zamawiającego od Wykonawcy w zakresie dalszego rozwoju, utrzymania i napraw systemu.
**Rekomendacja (preferowana):** Wprowadzić obowiązek przekazania kodu źródłowego po zapłacie wynagrodzenia lub ustanowić depozyt kodu źródłowego (escrow).
**Fallback (minimum akceptowalne):** Zapewnienie prawa do otrzymania kodu źródłowego w określonych sytuacjach (np. upadłość Wykonawcy, zaprzestanie wsparcia dla produktu).

#### 3. Iluzoryczne wsparcie powdrożeniowe — § 5 ust. 3
**Opis:** Zakres wsparcia jest ustalany „według wyłącznego uznania” Wykonawcy.
**Skutek:** Zamawiający nie ma żadnej gwarancji otrzymania jakiegokolwiek wsparcia po wdrożeniu. Jest to puste zobowiązanie.
**Rekomendacja (preferowana):** Usunąć zapis i zawrzeć odrębną umowę SLA (Service Level Agreement) lub w tej umowie określić konkretne parametry wsparcia (czas reakcji, dostępność, zakres usług).
**Fallback (minimum akceptowalne):** Określić minimalny, gwarantowany zakres wsparcia (np. X godzin w miesiącu na usuwanie krytycznych błędów).

#### 4. Szczątkowa klauzula poufności — § 6
**Opis:** Klauzula poufności jest ogólnikowa, nie definiuje informacji poufnych, nie określa czasu trwania obowiązku po zakończeniu umowy ani nie przewiduje sankcji za naruszenie. Jest dodatkowo unieważniona przez § 8 ust. 2.
**Skutek:** Brak realnej ochrony informacji poufnych Zamawiającego.
**Rekomendacja (preferowana):** Wprowadzić rozbudowaną klauzulę poufności z definicją, wyłączeniami, okresem obowiązywania (np. 5 lat po wygaśnięciu umowy) i karą umowną za naruszenie.
**Fallback (minimum akceptowalne):** Zdefiniować Informacje Poufne i określić co najmniej 3-letni okres ochrony po zakończeniu umowy.

### 🟡 RYZYKA ŚREDNIE

#### 1. Niewiążące i nieprecyzyjne terminy — § 2
**Opis:** Użycie sformułowań „niezwłocznie” i „na bieżąco” bez zdefiniowania ich w dniach roboczych.
**Skutek:** Brak konkretnych, egzekwowalnych terminów realizacji prac i zgłaszania uwag. Rodzi to wysokie ryzyko sporów interpretacyjnych.
**Rekomendacja (preferowana):** Zastąpić te sformułowania harmonogramem wdrożenia (w załączniku) z konkretnymi datami lub liczbą dni na wykonanie poszczególnych etapów i reakcję stron.
**Fallback (minimum akceptowalne):** Zdefiniować „niezwłocznie” jako np. „w terminie 3 dni roboczych”.

### ✓ Obszary bez zastrzeżeń

*   **Tytuł prawny i przekwalifikowanie:** n/d (nie dotyczy tego typu umowy).
*   Wszystkie pozostałe analizowane obszary (Odpowiedzialność i kary, Prawa autorskie, Definicje i logika, Reprezentacja, Wypowiedzenie i exit, RODO, Poufność, Spory) zawierają zidentyfikowane ryzyka.

---

## OCENA BEZPIECZEŃSTWA: 5/100

**Uzasadnienie:** Umowa jest jednostronna do granic absurdu. Zawiera postanowienia nieważne z mocy prawa, klauzule stwarzające krytyczne ryzyka finansowe i operacyjne dla Zamawiającego, a jednocześnie niemal całkowicie zwalniające Wykonawcę z odpowiedzialności. Dokument nie zabezpiecza podstawowych interesów Zamawiającego, takich jak nabycie praw do dzieła czy możliwość wyegzekwowania wykonania umowy.

**Werdykt:** **NIE PODPISYWAĆ**