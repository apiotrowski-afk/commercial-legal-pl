konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 1 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, bez MCP legal-cite: każdy przepis [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa wdrożeniowa ERP (NOVA RETAIL sp. z o.o. / CODEX WORKS sp. z o.o.)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie. Cztery klauzule trafiają w normy bezwzględnie obowiązujące lub w dane Zamawiającego, a zobowiązanie Wykonawcy jest wydrążone (starania, bez terminu, bez zakresu). Całość chroni wyłącznie Wykonawcę.

Perspektywa: audyt neutralny. Przy każdej fladze wskazano stronę dotkniętą. Zdecydowana większość wad obciąża Zamawiającego (NOVA RETAIL); wady obciążające Wykonawcę są nieliczne i oznaczone.

### 🧮 Rachunek ekspozycji

Liczby wyciągnięte z umowy: wynagrodzenie 480.000 zł netto (§ 3 ust. 1); płatność 60 dni od doręczenia faktury (§ 3 ust. 2); kara 50.000 zł/dzień opóźnienia w płatności, tylko dla Zamawiającego (§ 5 ust. 2); kar Wykonawcy brak; cap odpowiedzialności brak; termin wdrożenia „niezwłocznie" (§ 2 ust. 1).

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto | — | 480.000 zł netto (VAT [BRAK DANYCH — stawka nie podana w umowie]) |
| Kara dzienna Zamawiającego | 50.000 zł/dzień | 50.000 / 480.000 | 10,4% wartości umowy za każdy dzień; 100% wartości po 9,6 dnia |
| Kara po 30 dniach | brak sufitu | 50.000 × 30 | 1.500.000 zł = 3,13× wartości umowy |
| Kara po 60 dniach | brak sufitu | 50.000 × 60 | 3.000.000 zł = 6,25× wartości umowy |
| Kara po 365 dniach | brak sufitu | 50.000 × 365 | 18.250.000 zł = 38× wartości umowy |
| Kary Wykonawcy | „Wykonawca nie ponosi kar" | — | 0 zł, także za opóźnienie lub niewykonanie |
| Cap odpowiedzialności Wykonawcy | brak capu, ale odpowiedzialność tylko za winę umyślną | szkody z winy nieumyślnej: 0 zł | Efektywna ekspozycja Wykonawcy z tytułu wadliwego wdrożenia (szkoda nieumyślna): 0 zł; Zamawiający nie odzyska nawet części 480.000 zł |
| Efektywna ekspozycja Zamawiającego | kara bez sufitu + zapłata 480.000 zł niezależnie od rezultatu | 480.000 + kary bez górnej granicy | min. 480.000 zł; po 30 dniach zwłoki 1.980.000 zł = 4,1× wartości umowy |
| Asymetria kar | 50.000 zł/dzień vs 0 zł | 50.000 / 0 | nieskończona; brak kary po stronie Wykonawcy przy nieoznaczonym terminie |
| Termin płatności | 60 dni od doręczenia faktury | — | równo na granicy ustawowej B2B (ustawa o zatorach, art. 7 ust. 2) [NIEZWERYFIKOWANE]; dopuszczalny tylko przy braku rażącej nieuczciwości |
| Moment przeniesienia praw | „z chwilą zapłaty" | doręczenie faktury + do 60 dni | Zamawiający może do 60 dni korzystać z oprogramowania bez praw autorskich, jeśli płaci w ostatnim dniu; wcześniej: kiedy wystawić fakturę — umowa milczy |
| Termin wdrożenia | „niezwłocznie po podpisaniu" | brak liczby | [BRAK DANYCH] — nie da się policzyć; brak daty granicznej, więc brak opóźnienia w sensie umowy |
| Wypowiedzenie Zamawiającego | zakaz przed zakończeniem Wdrożenia | termin Wdrożenia nieoznaczony | okres związania: [BRAK DANYCH] — w praktyce bezterminowy |
| Wypowiedzenie Wykonawcy | w każdym czasie, bez przyczyny | okres wypowiedzenia 0 dni | wyjście natychmiastowe, bez rozliczenia, przy ryczałcie 480.000 zł; zasady zwrotu zapłaty: brak |

Wniosek: karą 50.000 zł/dzień Zamawiający wyczerpuje wartość umowy po niecałych 10 dniach zwłoki, a Wykonawca nie ponosi żadnej odpowiedzialności finansowej za brak rezultatu. Ekspozycja jest jednostronna i otwarta po stronie Zamawiającego, co samo przesądza o werdykcie CZERWONY.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Odpowiedzialność tylko za winę umyślną, wyłączenie winy umyślnej podwykonawców — § 5 ust. 1
**Strona dotknięta:** Zamawiający.
**Opis:** Wykonawca odpowiada „wyłącznie za szkody wyrządzone umyślnie". Odpowiedzialność za niedbalstwo, wadliwe wdrożenie i niewykonanie jest wyłączona. Dodatkowo klauzula wyłącza odpowiedzialność za winę umyślną podwykonawców. Wyłączenie lub ograniczenie odpowiedzialności za winę umyślną dłużnika jest nieważne (art. 473 § 2 KC) [NIEZWERYFIKOWANE]. Co do podwykonawców: odpowiedzialność za osoby, którymi dłużnik się posługuje (art. 474 KC) [NIEZWERYFIKOWANE] podlega odrębnej ocenie, ale wyłączenie umyślności osób trzecich zestawione z zakresem „tylko umyślnie" czyni całą regulację pustą.
**Skutek:** Przy ERP za 480.000 zł Zamawiający nie dochodzi odszkodowania za awarię, utratę danych, przestój sprzedaży ani za wadliwy system. W praktyce odpowiedzialność istnieje tylko na papierze, bo umyślność trzeba udowodnić. Rachunek: ekspozycja Wykonawcy z winy nieumyślnej = 0 zł.
**Rekomendacja (preferowana):** Usunąć „wyłącznie" i wyłączenie podwykonawców; odpowiedzialność na zasadach ogólnych, za podwykonawców jak za własne działania (art. 474 KC) [NIEZWERYFIKOWANE]; cap np. 100% wynagrodzenia, bez capu dla winy umyślnej, poufności, IP i danych.
**Fallback (minimum akceptowalne):** Cap 100% wynagrodzenia dla winy nieumyślnej, bez wyłączeń przedmiotowych, z wyraźnym wyjęciem winy umyślnej i rażącego niedbalstwa spod capu.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Kara umowna za opóźnienie w płatności, jednostronna, bez sufitu — § 5 ust. 2
**Strona dotknięta:** Zamawiający (Wykonawca jest uprzywilejowany).
**Opis:** Kara 50.000 zł za każdy dzień opóźnienia w płatności. Płatność wynagrodzenia jest zobowiązaniem pieniężnym; kara umowna nie może zabezpieczać zobowiązań pieniężnych (art. 483 § 1 KC) [NIEZWERYFIKOWANE]. Postanowienie jest nieważne; należą się odsetki (art. 481 KC) [NIEZWERYFIKOWANE], nie kara. Poza tym stawka dzienna to 10,4% wartości umowy, bez sufitu. Pozorna wzajemność: „Wykonawca nie ponosi kar".
**Skutek:** Po 30 dniach 1.500.000 zł (3,13× wartości), po 60 dniach 3.000.000 zł (6,25×). Nawet gdyby klauzula zadziałała, byłaby narażona na miarkowanie (art. 484 § 2 KC) [NIEZWERYFIKOWANE], ale ryzyko sporu i egzekucji pozostaje.
**Rekomendacja (preferowana):** Skreślić; w zamian odsetki ustawowe za opóźnienie w transakcjach handlowych, a kary umowne wprowadzić po stronie Wykonawcy za zwłokę w wykonaniu (z sufitem np. 10–20% wynagrodzenia).
**Fallback (minimum akceptowalne):** Odsetki za opóźnienie plus symetryczna kara za zwłokę Wykonawcy, obie z tym samym sufitem procentowym.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Prawo do trenowania modeli AI na danych Zamawiającego — § 8 ust. 2
**Strona dotknięta:** Zamawiający.
**Opis:** „Niezależnie od pozostałych postanowień Umowy" Wykonawca może wykorzystywać dane Zamawiającego do trenowania modeli AI. Klauzula nadpisuje poufność (§ 6), nie ma celu, zakresu, okresu ani zabezpieczeń. ERP przetwarza dane handlowe, kontrahentów i prawdopodobnie dane osobowe pracowników i klientów detalicznych. Brak umowy powierzenia i brak podstawy do przetwarzania we własnym celu Wykonawcy (art. 28 ust. 3 RODO i art. 6 RODO) [NIEZWERYFIKOWANE]; trenowanie na danych klienta czyni Wykonawcę administratorem, a Zamawiającego narażonym na naruszenie obowiązków administratora. Dla informacji będących tajemnicą przedsiębiorstwa to także ryzyko ujawnienia.
**Skutek:** Utrata kontroli nad danymi, kara administracyjna po stronie Zamawiającego (art. 83 RODO) [NIEZWERYFIKOWANE], roszczenia osób, których dane dotyczą, nieodwracalne „zaszycie" danych w modelu. Skutek jest nieograniczony czasowo i kwotowo.
**Rekomendacja (preferowana):** Skreślić. Dodać umowę powierzenia zgodną z art. 28 RODO [NIEZWERYFIKOWANE] i zakaz używania danych do celów własnych Wykonawcy, w tym do trenowania modeli.
**Fallback (minimum akceptowalne):** Wyłącznie dane zanonimizowane i zagregowane, za uprzednią pisemną zgodą Zamawiającego dla każdego przypadku, z wyłączeniem danych osobowych i tajemnic przedsiębiorstwa.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria RODO/powierzenie, poufność); `references/checklist-dpa-art28.md`

#### 4. Przeniesienie praw autorskich bez pól eksploatacji, warunkowo i bez kodu — § 4 ust. 1
**Strona dotknięta:** Zamawiający.
**Opis:** „Wszelkie prawa autorskie … bez ograniczeń", bez wyliczenia pól eksploatacji. Umowa o przeniesienie majątkowych praw autorskich obejmuje tylko pola wyraźnie wymienione (art. 41 ust. 2 PrAut) [NIEZWERYFIKOWANE]; ogólna formuła zamiast identyfikacji pól jest wadliwa, a pola nieznane w chwili zawarcia nie są objęte (art. 41 ust. 4 PrAut) [NIEZWERYFIKOWANE]. Klauzula obejmuje tylko „stworzone oprogramowanie", nie obejmuje dokumentacji, konfiguracji, skryptów ani zależnych opracowań. Przejście praw „z chwilą zapłaty" jest niejasne: zapłaty czego i kiedy. Brak wskazania zakresu terytorialnego, czasowego, prawa do modyfikacji i zezwolenia na prawa zależne.
**Skutek:** Zamawiający płaci 480.000 zł, a skuteczność nabycia praw jest wątpliwa; bez praw do modyfikacji nie rozwinie systemu bez zgody Wykonawcy. Do 60 dni od faktury (rachunek wyżej) nie ma żadnych praw.
**Rekomendacja (preferowana):** Wyliczyć pola eksploatacji (art. 74 ust. 4 PrAut — pola dla programów komputerowych) [NIEZWERYFIKOWANE], objąć dokumentację i utwory zależne, upoważnić do wykonywania zależnych praw autorskich, uregulować moment przejścia (odbiór bez zastrzeżeń) i zobowiązanie do niewykonywania praw osobistych (nie ich przeniesienie, art. 16 PrAut) [NIEZWERYFIKOWANE].
**Fallback (minimum akceptowalne):** Licencja wyłączna, nieograniczona w czasie, z prawem sublicencji i modyfikacji, w formie pisemnej (art. 67 ust. 5 PrAut) [NIEZWERYFIKOWANE], plus escrow kodu.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 5. Brak rezultatu i terminu: „dołoży starań", „niezwłocznie" — § 1 ust. 1, § 2 ust. 1
**Strona dotknięta:** Zamawiający (przy braku terminu także Wykonawca, który nie ma jasnych kryteriów wykonania).
**Opis:** Wykonawca zobowiązuje się tylko do „dołożenia starań" w celu wdrożenia, a nie do wdrożenia. Przy wynagrodzeniu ryczałtowym oznacza to zapłatę za staranne działanie, nie za działający system. Termin „niezwłocznie" nie ma liczby dni, więc nie istnieje data, od której Wykonawca jest w zwłoce. Załącznik nr 1 wskazany w § 1 ust. 1 nie jest dołączony ani w treści umowy nie ma zakresu (zob. 🟠). Esencjalne elementy zobowiązania (przedmiot świadczenia, termin) są nieoznaczone.
**Skutek:** Roszczenia o niewykonanie nie dają się zbudować: rezultatu nie ma, terminu nie ma, kar nie ma (§ 5 ust. 2). W połączeniu z § 5 ust. 1 i § 7 ust. 1 Zamawiający jest związany, płaci i nie ma środków ochrony (efekt kumulatywny § 1 + § 2 + § 5 + § 7).
**Rekomendacja (preferowana):** „Wykonawca zobowiązuje się wdrożyć … do dnia [data] zgodnie z Załącznikiem nr 1"; harmonogram z kamieniami milowymi, kryteria odbioru, procedura odbioru.
**Fallback (minimum akceptowalne):** Termin końcowy liczbowy i opis rezultatu w Załączniku nr 1, choćby bez kamieni milowych.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Asymetria wypowiedzenia — § 7 ust. 1–2
**Strona dotknięta:** Zamawiający.
**Opis:** Zamawiający nie może wypowiedzieć umowy do zakończenia Wdrożenia (termin nieoznaczony), a Wykonawca może w każdym czasie i bez przyczyny. Klauzula „w każdym czasie i bez podania przyczyny" bez okresu i bez rozliczenia. Zamawiający jest zablokowany, Wykonawca może porzucić projekt w środku wdrożenia (ryzyko szkody poprzez nieukończony ERP; art. 746 KC jako punkt odniesienia dla wypowiedzenia umowy o świadczenie usług) [NIEZWERYFIKOWANE]. Brak procedury exit: zwrot danych, kodu, dokumentacji, rozliczenie wynagrodzenia za wykonaną część.
**Skutek:** Zamawiający traci środek wyjścia, Wykonawca zachowuje pełną elastyczność; rozliczenie ryczałtu przy wcześniejszym wypowiedzeniu: brak regulacji.
**Rekomendacja (preferowana):** Wypowiedzenie symetryczne, okres np. 30 dni, rozwiązanie z ważnych przyczyn bez okresu, rozliczenie proporcjonalne do odebranych etapów, obowiązek przekazania prac w toku.
**Fallback:** Zamawiający może wypowiedzieć z ważnych przyczyn (opóźnienie powyżej 30 dni, brak rezultatu); Wykonawca tylko z przyczyn leżących po stronie Zamawiającego, za 30-dniowym okresem.
**Klauzula z bazy:** `references/baza-klauzul/` (wypowiedzenie i exit)

#### 2. Prawo obce i sąd zagraniczny — § 8 ust. 1
**Strona dotknięta:** Zamawiający (a faktycznie obie strony, to spółki polskie).
**Opis:** Prawo stanu Delaware i sąd w Wilmington dla umowy między dwiema polskimi spółkami, o wdrożeniu w infrastrukturze Zamawiającego w Polsce. Brak uzasadnienia gospodarczego; polskie normy bezwzględne (m.in. art. 473 § 2 KC, art. 483 KC [NIEZWERYFIKOWANE]) nadal mogą znaleźć zastosowanie jako przepisy wymuszające, co rodzi niepewność, który reżim obowiązuje. Brak zapisu o języku postępowania, kosztach.
**Skutek:** Koszty dochodzenia roszczeń w USA, ocena ważności klauzul według obcego prawa, praktyczny zakaz dochodzenia roszczeń o mniejszej wartości.
**Rekomendacja (preferowana):** Prawo polskie, sąd właściwy dla siedziby pozwanego lub wskazanego miasta w Polsce.
**Fallback:** Prawo polskie i arbitraż w Polsce z jasno określonym trybem i językiem.
**Klauzula z bazy:** `references/baza-klauzul/` (prawo właściwe i spory)

#### 3. Kod źródłowy tylko „może, ale nie jest zobowiązany" — § 4 ust. 2
**Strona dotknięta:** Zamawiający.
**Opis:** Przekazanie kodu źródłowego jest dla Wykonawcy uprawnieniem, nie obowiązkiem (pozorne zobowiązanie). Przeniesienie praw bez kodu jest pozbawione treści praktycznej: Zamawiający nie może utrzymać ani rozwijać systemu.
**Skutek:** Uzależnienie od Wykonawcy (vendor lock-in), przy jednoczesnym wygaśnięciu wsparcia na jego uznaniu (zob. pozycja 4).
**Rekomendacja (preferowana):** Obowiązek przekazania kodu źródłowego i dokumentacji wraz z odbiorem, w formacie umożliwiającym kompilację.
**Fallback:** Escrow kodu z wydaniem przy upadłości lub wypowiedzeniu przez Wykonawcę.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Wsparcie powdrożeniowe „według wyłącznego uznania", brak gwarancji, SLA i rękojmi — § 5 ust. 3
**Strona dotknięta:** Zamawiający.
**Opis:** Zakres wsparcia ustala Wykonawca jednostronnie, bez kryteriów, czasów reakcji i poziomu usługi. Umowa nie reguluje gwarancji ani rękojmi za wady (czas, zakres, tryb zgłoszeń). Przy systemie ERP wsparcie jest krytyczne dla ciągłości działania.
**Skutek:** Zamawiający nie ma żadnego egzekwowalnego świadczenia po wdrożeniu; ryzyko, że wsparcie wyniesie zero.
**Rekomendacja (preferowana):** Załącznik SLA: czasy reakcji i naprawy, godziny, ceny, okres gwarancji (np. 12–24 mies.).
**Fallback:** Gwarancja usunięcia wad przez okres 12 mies. i wsparcie na stawkach z cennika załączonego do umowy.
**Klauzula z bazy:** `references/baza-klauzul/` (gwarancja/rękojmia, SLA)

#### 5. Brak zakresu (Załącznik nr 1 nieobecny), kamieni milowych i odbioru; płatność całości ryczałtu — § 1 ust. 1, § 3
**Strona dotknięta:** obie strony (Zamawiający: płaci bez wykazania rezultatu; Wykonawca: brak kryteriów, po których wynagrodzenie jest wymagalne).
**Opis:** Umowa powołuje Załącznik nr 1, którego nie ma w dokumencie (osierocone odesłanie). Ryczałt 480.000 zł bez harmonogramu płatności, bez odbioru, bez kryteriów akceptacji. Nie wiadomo, kiedy powstaje prawo do faktury. Płatność 60 dni od doręczenia faktury znajduje się dokładnie na granicy ustawowej dla B2B (art. 7 ust. 2 ustawy o zatorach) [NIEZWERYFIKOWANE]; sama w sobie jest dopuszczalna, ale dla Wykonawcy oznacza długie finansowanie projektu z własnych środków.
**Skutek:** Spór o zakres („co jest w cenie") i o moment płatności; zmiany zakresu bez trybu change request.
**Rekomendacja (preferowana):** Dołączyć Załącznik nr 1 z zakresem funkcjonalnym, harmonogram z płatnościami za etapy, protokół odbioru, tryb zmian.
**Fallback:** Co najmniej płatność dwuetapowa (zaliczka + płatność po odbiorze) i definicja odbioru.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 6. Brak gwarancji czystości IP, licencji na komponenty zewnętrzne i klauzuli anty-copyleft — § 4
**Strona dotknięta:** Zamawiający.
**Opis:** Wdrożenie ERP zwykle obejmuje oprogramowanie osób trzecich i open source. Umowa przenosi prawa tylko do „stworzonego oprogramowania", bez licencji na komponenty zewnętrzne, bez oświadczenia o prawach do utworów, bez zakazu użycia GPL/AGPL i bez zwolnienia z roszczeń osób trzecich.
**Skutek:** Ryzyko roszczeń właścicieli komponentów, obowiązek ujawnienia kodu przy copyleft; w połączeniu z § 5 ust. 1 Zamawiający nie ma regresu wobec Wykonawcy.
**Rekomendacja (preferowana):** Oświadczenie o prawach, wykaz komponentów zewnętrznych i licencji, zakaz copyleft, zwolnienie z roszczeń.
**Fallback:** Wykaz komponentów w załączniku i obowiązek usunięcia lub zastąpienia komponentu naruszającego prawa.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. Poufność bez okresu, wyłączeń i sankcji — § 6
**Strona dotknięta:** obie strony; faktycznie Zamawiający (jego dane). Klauzula jest ogólnikowa i nadpisana przez § 8 ust. 2. Brak definicji informacji poufnych, okresu po zakończeniu umowy, wyłączeń, zwrotu/zniszczenia.
**Rekomendacja:** Definicja, okres (np. 5 lat po zakończeniu), wyłączenia, zwrot danych; fallback: okres 3 lata.

#### 2. Dane stron, reprezentacja, data i miejsce zawarcia — nagłówek
**Strona dotknięta:** obie strony. Brak KRS, NIP, adresów, sposobu reprezentacji, daty i miejsca zawarcia (dane oznaczone jako fikcyjne).
**Rekomendacja:** Uzupełnić; fallback: oświadczenia o umocowaniu i odpis KRS w załączniku.

#### 3. Obowiązki Zamawiającego nieokreślone — § 1 ust. 2, § 2 ust. 2
**Strona dotknięta:** Wykonawca (i pośrednio obie strony). „Współpraca" i „uwagi na bieżąco" bez trybu, terminu, osób kontaktowych. Wykonawca może powołać się na niewspółdziałanie bez kryteriów, a Zamawiający nie wie, czego od niego oczekuje.
**Rekomendacja:** Katalog obowiązków Zamawiającego (dostęp, dane, osoba kontaktowa) z terminami; fallback: termin na zgłoszenie uwag (np. 5 dni roboczych).

#### 4. Kwalifikacja typu umowy i definicje — cała umowa
**Strona dotknięta:** obie strony. Nie wiadomo, czy to umowa o dzieło, o świadczenie usług, czy nienazwana; pojęcia „Wdrożenie" i „Umowa" pisane wielką literą bez definicji. Konsekwencje: rękojmia, odbiór, możliwość wypowiedzenia (np. art. 644 KC przy dziele) [NIEZWERYFIKOWANE].
**Rekomendacja:** Słowniczek i wyraźna kwalifikacja; fallback: zdefiniować Wdrożenie przez odesłanie do Załącznika nr 1.

### 🟢 RYZYKA NISKIE

#### 1. Pozorna wzajemność — § 1 ust. 2
**Strona dotknięta:** Zamawiający. „Strony wzajemnie zobowiązują się do współpracy" przy asymetrii pozostałych klauzul to obowiązek pusty, a zarazem źródło argumentu o braku współpracy Zamawiającego. Doprecyzować lub skreślić.

#### 2. Redakcja kwot i terminów — § 3
**Strona dotknięta:** obie strony. Kwota zapisana cyfrą bez słownie; termin „od doręczenia faktury" bez określenia sposobu doręczenia; brak waluty VAT. Uzupełnić.

### ✓ Obszary bez zastrzeżeń

Każdy z dziewięciu obszarów z Kroku 1 jest zamknięty flagą (odpowiedzialność i kary: 🔴1, 🔴2; prawa autorskie: 🔴4, 🟠3, 🟠6; definicje i logika: 🔴5, 🟠5, 🟡4; reprezentacja: 🟡2; wypowiedzenie i exit: 🟠1; RODO: 🔴3; tytuł prawny i przekwalifikowanie: 🟡4, w zakresie kwalifikacji dzieło/usługi, body leasing — n/d; poufność: 🟡1; spory: 🟠2). Obszarów czystych brak.

Trigger mikroprzedsiębiorcy (art. 385⁵ KC): n/d — obie strony to spółki z o.o. Bramka ius cogens (R10): trafienia w art. 473 § 2 KC (§ 5 ust. 1), art. 483 § 1 KC (§ 5 ust. 2), art. 41 ust. 2 PrAut (§ 4 ust. 1), art. 28 RODO (§ 8 ust. 2) [wszystkie NIEZWERYFIKOWANE]. Efekt kumulatywny: § 1 ust. 1 + § 2 + § 5 + § 7 + § 4 ust. 2 łącznie pozbawiają Zamawiającego realnego środka ochrony.

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (odpowiedzialność) → `references/baza-klauzul/11-odpowiedzialnosc.md` — wariant z capem i wyjęciem winy umyślnej
🔴 RYZYKO 2 (kary) → `references/baza-klauzul/10-kary-umowne.md` — kara symetryczna z sufitem
🔴 RYZYKO 3 (AI/dane) → `references/checklist-dpa-art28.md` oraz kategoria poufność/powierzenie
🔴 RYZYKO 4 (prawa autorskie) → `references/baza-klauzul/08-prawa-autorskie-ip.md`
🔴 RYZYKO 5 (rezultat, termin) → `references/baza-klauzul/07-terminy-kamienie-milowe.md`

---

## OCENA BEZPIECZEŃSTWA: 5/100

Pięć ryzyk krytycznych (w tym cztery trafienia w normy bezwzględne lub dane), sześć wysokich, cztery średnie i dwa niskie. Umowa jest jednostronnie korzystna dla Wykonawcy: zero odpowiedzialności, zero kar, wyjście w każdym czasie i prawo do danych klienta, a po stronie Zamawiającego kara 50.000 zł/dzień bez sufitu i związanie bez terminu.

**Werdykt:** NIE PODPISYWAĆ

Liczba flag: 17 (🔴 5 · 🟠 6 · 🟡 4 · 🟢 2).

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
