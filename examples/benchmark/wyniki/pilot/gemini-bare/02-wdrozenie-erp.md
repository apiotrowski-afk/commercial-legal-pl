# RAPORT Z AUDYTU UMOWY WDROŻENIOWEJ

**Data sporządzenia:** 24.05.2024 r.
**Przedmiot audytu:** Umowa Wdrożeniowa pomiędzy NOVA RETAIL sp. z o.o. („Zamawiający”) a CODEX WORKS sp. z o.o. („Wykonawca”).
**Cel audytu:** Neutralna analiza ryzyk prawnych i biznesowych wynikających z Umowy w świetle polskiego prawa, wraz z rekomendacjami.

---

### **I. OGÓLNA OCENA I WERDYKT**

Analizowana Umowa jest **krytycznie wadliwa i skrajnie niekorzystna dla Zamawiającego**. Zawiera liczne postanowienia, które są nieprecyzyjne, niezgodne z dobrymi praktykami rynkowymi, a w niektórych przypadkach potencjalnie nieważne lub bezskuteczne na gruncie polskiego prawa. Struktura Umowy w sposób rażący faworyzuje Wykonawcę, praktycznie zwalniając go z odpowiedzialności za realizację projektu, jednocześnie nakładając na Zamawiającego surowe i nieproporcjonalne obowiązki.

**Werdykt:** Umowa w obecnym kształcie **nie nadaje się do podpisania**. Stwarza ona dla Zamawiającego ryzyko utraty całości wynagrodzenia bez otrzymania funkcjonalnego produktu, a także ryzyko utraty kontroli nad kluczowymi danymi biznesowymi. Rekomenduje się **całkowite odrzucenie projektu Umowy i przygotowanie nowego dokumentu od podstaw** w oparciu o standardy rynkowe dla umów wdrożeniowych IT.

---

### **II. SZCZEGÓŁOWA ANALIZA RYZYK**

#### **§ 1. Przedmiot Umowy**

*   **Zidentyfikowane Ryzyko:**
    1.  **Zobowiązanie starannego działania zamiast rezultatu:** Sformułowanie „dołoży starań” oznacza, że Wykonawca jest zobowiązany jedynie do podjęcia próby wdrożenia, a nie do osiągnięcia konkretnego, działającego rezultatu. Zamawiający płaci za pracę, a nie za efekt w postaci wdrożonego i działającego systemu ERP.
    2.  **Brak zdefiniowanego zakresu:** Umowa odwołuje się do Załącznika nr 1, który nie został przedstawiony. Bez szczegółowej specyfikacji funkcjonalnej i technicznej, harmonogramu oraz kryteriów odbioru, przedmiot umowy jest nieokreślony. Prowadzi to do ogromnego ryzyka sporów interpretacyjnych.
    3.  **Ogólnikowy obowiązek współpracy:** Zapis o „wzajemnej współpracy” jest zbyt ogólny, aby można go było egzekwować. Nie precyzuje, jakie konkretne działania (np. dostarczenie danych, udostępnienie środowiska, dedykowanie personelu) i w jakich terminach są wymagane od każdej ze Stron.

*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** Głównie **Zamawiający**.
*   **Rekomendacja:**
    1.  Zmienić sformułowanie na zobowiązanie rezultatu, np. „Wykonawca zobowiązuje się do zaprojektowania, stworzenia i wdrożenia Systemu ERP (...) zgodnie ze specyfikacją określoną w Załączniku nr 1”.
    2.  Sporządzić szczegółowy Załącznik nr 1 (Opis Przedmiotu Umowy), zawierający co najmniej: specyfikację funkcjonalną i techniczną systemu, wymagania dotyczące infrastruktury, harmonogram prac z podziałem na etapy (kamienie milowe) oraz procedurę i kryteria testów akceptacyjnych (odbiorczych).
    3.  Doprecyzować obowiązki Stron w zakresie współpracy (np. wskazanie koordynatorów projektu, terminy na dostarczanie materiałów i informacji zwrotnych).

#### **§ 2. Terminy**

*   **Zidentyfikowane Ryzyko:** Sformułowania „niezwłocznie” oraz „na bieżąco” są nieprecyzyjne i w praktyce niemożliwe do wyegzekwowania. Brak konkretnego harmonogramu uniemożliwia Zamawiającemu monitorowanie postępów i dochodzenie roszczeń z tytułu opóźnień.
*   **Poziom Ryzyka:** **WYSOKI**
*   **Strona Obciążona Ryzykiem:** Głównie **Zamawiający**.
*   **Rekomendacja:** Wprowadzić szczegółowy harmonogram wdrożenia (w Załączniku nr 1 lub osobnym), określający terminy realizacji poszczególnych etapów i termin końcowy. Zdefiniować procedurę odbioru każdego etapu oraz czas na zgłaszanie uwag przez Zamawiającego (np. 5 dni roboczych).

#### **§ 3. Wynagrodzenie**

*   **Zidentyfikowane Ryzyko:**
    1.  **Płatność z góry bez powiązania z postępem prac:** Umowa przewiduje jedną płatność za całość, niezależnie od tego, czy wdrożenie zakończyło się sukcesem. Zamawiający ryzykuje zapłatę 100% wynagrodzenia za niedziałający lub niekompletny system.
    2.  **Długi termin płatności (60 dni):** Jest to niekorzystne dla Wykonawcy, jednak w kontekście pozostałych zapisów stanowi niewielkie ryzyko w porównaniu z ryzykami Zamawiającego.

*   **Poziom Ryzyka:** **WYSOKI** (dla Zamawiającego), **ŚREDNI** (dla Wykonawcy z powodu terminu płatności).
*   **Rekomendacja:** Podzielić wynagrodzenie na transze płatne po pomyślnym odbiorze poszczególnych, zdefiniowanych w harmonogramie etapów prac (np. 20% po analizie, 50% po wdrożeniu, 30% po pozytywnym zakończeniu testów akceptacyjnych).

#### **§ 4. Prawa autorskie**

*   **Zidentyfikowane Ryzyko:**
    1.  **Nieskuteczne przeniesienie praw:** Zgodnie z art. 41 ust. 2 polskiej ustawy o prawie autorskim, umowa o przeniesienie autorskich praw majątkowych musi wyraźnie wymieniać **pola eksploatacji**. Ogólne sformułowanie „wszelkie prawa autorskie” jest niewystarczające i może zostać uznane za bezskuteczne.
    2.  **Brak dostępu do kodu źródłowego:** Fakultatywne przekazanie kodu źródłowego jest **krytycznym zagrożeniem dla Zamawiającego**. Bez kodu źródłowego nie jest on w stanie samodzielnie (lub z pomocą innej firmy) rozwijać, modyfikować ani naprawiać systemu. Prowadzi to do całkowitego uzależnienia od Wykonawcy (tzw. *vendor lock-in*).

*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** **Zamawiający**.
*   **Rekomendacja:**
    1.  Wymienić w umowie konkretne pola eksploatacji, na których następuje przeniesienie praw, np. „w zakresie utrwalania i zwielokrotniania oprogramowania – wytwarzanie określoną techniką egzemplarzy utworu (...), w zakresie obrotu oryginałem albo egzemplarzami (...), w zakresie rozpowszechniania utworu w sposób inny niż określony powyżej (...)” oraz prawo do modyfikacji i tworzenia opracowań (utworów zależnych).
    2.  Wprowadzić **bezwzględny obowiązek przekazania kompletnego i skompilowanego kodu źródłowego** wraz z dokumentacją techniczną po zapłacie ostatniej transzy wynagrodzenia. Można rozważyć depozyt kodu źródłowego u niezależnego podmiotu (escrow).

#### **§ 5. Odpowiedzialność**

*   **Zidentyfikowane Ryzyko:**
    1.  **Niedopuszczalne ograniczenie odpowiedzialności Wykonawcy:** Ograniczenie odpowiedzialności Wykonawcy wyłącznie do szkód wyrządzonych umyślnie jest skrajnie niekorzystne dla Zamawiającego. Co więcej, zgodnie z art. 473 § 2 Kodeksu cywilnego, nieważne jest zastrzeżenie umowne, które z góry wyłącza odpowiedzialność za szkodę wyrządzoną z winy umyślnej. Zapis wyłączający winę umyślną podwykonawców jest próbą obejścia tego przepisu i prawdopodobnie byłby bezskuteczny przed sądem.
    2.  **Rażąco niewspółmierne kary umowne:** Kara umowna w wysokości 50 000 zł za każdy dzień opóźnienia w płatności jest astronomiczna i z pewnością zostałaby uznana przez sąd za „rażąco wygórowaną” i podlegałaby miarkowaniu. Jednoczesny brak jakichkolwiek kar dla Wykonawcy za opóźnienia w realizacji projektu stanowi o rażącej nierównowadze stron.
    3.  **Brak gwarancji i wsparcia:** Pozostawienie zakresu wsparcia powdrożeniowego „wyłącznemu uznaniu” Wykonawcy jest równoznaczne z brakiem jakiegokolwiek zobowiązania w tym zakresie.

*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** **Zamawiający**.
*   **Rekomendacja:**
    1.  Określić odpowiedzialność Wykonawcy co najmniej za winę umyślną i rażące niedbalstwo. Wprowadzić limit odpowiedzialności (np. do 100-150% wartości umowy), ale z wyłączeniem szkód wyrządzonych umyślnie.
    2.  Wprowadzić symetryczne i proporcjonalne kary umowne dla Wykonawcy za opóźnienia w realizacji kamieni milowych. Zracjonalizować karę dla Zamawiającego do standardowego poziomu (np. odsetki ustawowe za opóźnienie w transakcjach handlowych).
    3.  Zdefiniować w osobnym paragrafie lub załączniku warunki gwarancji (rękojmia za wady jest ustawowa) oraz płatnego wsparcia powdrożeniowego (umowa serwisowa SLA), określając czas reakcji, czas naprawy błędów krytycznych itp.

#### **§ 6. Poufność**

*   **Zidentyfikowane Ryzyko:** Klauzula jest zbyt ogólna. Nie definiuje, co stanowi Informację Poufną, nie określa okresu obowiązywania poufności po zakończeniu umowy ani nie precyzuje dozwolonych wyjątków od obowiązku zachowania poufności.
*   **Poziom Ryzyka:** **ŚREDNI**
*   **Strona Obciążona Ryzykiem:** **Obie Strony**.
*   **Rekomendacja:** Rozbudować klauzulę, definiując „Informacje Poufne”, określając czas trwania obowiązku poufności (np. 5 lat od rozwiązania umowy) oraz standardowe wyłączenia (informacje publicznie znane, wymagane przez prawo lub sąd).

#### **§ 7. Rozwiązanie Umowy**

*   **Zidentyfikowane Ryzyko:** Postanowienia są skrajnie jednostronne. Zamawiający jest pozbawiony prawa do wypowiedzenia umowy (nawet w przypadku całkowitego braku postępów prac), podczas gdy Wykonawca może porzucić projekt w dowolnym momencie bez żadnych konsekwencji.
*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** **Zamawiający**.
*   **Rekomendacja:** Usunąć obecne zapisy. Wprowadzić standardowe postanowienia, pozwalające obu stronom na wypowiedzenie umowy ze skutkiem natychmiastowym w przypadku istotnego naruszenia jej postanowień przez drugą stronę (po uprzednim bezskutecznym wezwaniu do zaprzestania naruszeń). Można również rozważyć prawo Zamawiającego do odstąpienia od umowy za zapłatą określonej części wynagrodzenia.

#### **§ 8. Postanowienia końcowe**

*   **Zidentyfikowane Ryzyko:**
    1.  **Niewłaściwy wybór prawa i sądu:** Wybór prawa stanu Delaware i sądu w Wilmington dla umowy zawieranej między dwiema polskimi spółkami, realizowanej w Polsce, jest absurdalny, niepraktyczny i generuje olbrzymie koszty i niepewność prawną. Polskie sądy mogłyby i tak uznać swoją jurysdykcję na podstawie przepisów KPC.
    2.  **Niedopuszczalne wykorzystanie danych do trenowania AI:** Zapis ten stanowi **ogromne zagrożenie dla bezpieczeństwa danych i tajemnicy przedsiębiorstwa Zamawiającego**. Jest to de facto zgoda na przekazanie potencjalnie wszystkich danych firmy (finansowych, handlowych, o klientach) do nieokreślonych celów. Jeśli dane te zawierają dane osobowe, zapis ten rażąco narusza RODO.

*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** **Zamawiający**.
*   **Rekomendacja:**
    1.  Zmienić zapis na: „Prawem właściwym dla niniejszej Umowy jest prawo polskie. Wszelkie spory wynikające z Umowy rozstrzygane będą przez sąd powszechny właściwy dla siedziby Zamawiającego”.
    2.  **BEZWZGLĘDNIE USUNĄĆ** klauzulę dotyczącą trenowania modeli AI. Jakiekolwiek przetwarzanie danych osobowych przez Wykonawcę musi być uregulowane w odrębnej, zgodnej z RODO umowie powierzenia przetwarzania danych osobowych.