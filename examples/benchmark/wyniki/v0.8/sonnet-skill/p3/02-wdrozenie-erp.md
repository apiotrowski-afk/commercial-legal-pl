konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 3 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express; audyt neutralny; bez MCP legal-cite — każde powołanie przepisu jest [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa wdrożeniowa ERP (Nova Retail sp. z o.o. / Codex Works sp. z o.o.)

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie. Cztery klauzule są dotknięte wadą ius cogens lub równoważną, a pozostałe ryzyka (zakres, termin, exit, kod źródłowy) czynią umowę praktycznie niewykonalną dla Zamawiającego.

Oznaczenia: „Strona dotknięta" = strona, którą wada krzywdzi lub naraża. Umowa jest wyraźnie jednostronnie korzystna dla Wykonawcy. Kilka wad uderza jednak także w Wykonawcę (zakres bez definicji, forum, brak umowy powierzenia).

### 🧮 Rachunek ekspozycji

Liczby z tekstu umowy: wynagrodzenie 480.000 zł netto (§ 3 ust. 1) · termin płatności 60 dni od doręczenia faktury (§ 3 ust. 2) · kara 50.000 zł za każdy dzień opóźnienia w płatności (§ 5 ust. 2) · kary Wykonawcy: 0 zł (§ 5 ust. 2) · cap: brak · sufit kary: brak · termin wykonania: „niezwłocznie" (§ 2 ust. 1) · okres wypowiedzenia: brak · okres poufności: brak.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto | brutto przy 23% VAT (założenie, umowa nie podaje stawki): 480.000 × 1,23 | 480.000 zł netto / 590.400 zł brutto |
| Kara dzienna Zamawiającego | 50.000 zł / dzień | 50.000 / 480.000 | 10,4% wartości netto za każdy dzień |
| Kumulacja kary — sufit | brak | 10 dni: 500.000 zł · 30 dni: 1.500.000 zł · 100 dni: 5.000.000 zł | 10 dni = 104% wartości; 30 dni = 312,5%; 100 dni = 1.041,7% (ekspozycja otwarta, bez górnej granicy) |
| Ekspozycja Zamawiającego | wynagrodzenie + kary | 480.000 + 50.000 × n dni | przy 30 dniach zwłoki: 1.980.000 zł = 4,1× wartości umowy (o ile kara byłaby skuteczna, zob. ryzyko 2) |
| Cap Wykonawcy | brak; odpowiedzialność tylko za winę umyślną | odpowiedzialność za niewykonanie, zwłokę i niedbalstwo = 0 zł | ekspozycja Wykonawcy za wszystko poza winą umyślną = 0 zł (zob. ryzyko 1) |
| Kary Wykonawcy za zwłokę we Wdrożeniu | „Wykonawca nie ponosi kar" | 0 × n dni | 0 zł niezależnie od opóźnienia |
| Asymetria kar | A (Zamawiający): 50.000 zł/dzień, bez sufitu · B (Wykonawca): 0 zł | 50.000 / 0 | stosunek nieskończony; pozorna wzajemność w § 1 ust. 2 |
| Asymetria wypowiedzenia | Zamawiający: niedopuszczalne do zakończenia Wdrożenia · Wykonawca: w każdym czasie, bez przyczyny | okres wypowiedzenia Wykonawcy: 0 dni; Zamawiającego: do dnia zakończenia Wdrożenia, a ten dzień jest nieoznaczony (§ 2 ust. 1) | Zamawiający związany bezterminowo, Wykonawca może wyjść z dnia na dzień |
| Termin płatności | 60 dni od doręczenia faktury | doręczenie faktury w dniu D → termin do D+60; kara od D+61 | 60 dni = górna granica B2B [NIEZWERYFIKOWANE: art. 7 ust. 2 ustawy o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych]; brak przekroczenia, ale bez marginesu |
| Moment przejścia praw | „z chwilą zapłaty" | zapłata całości (brak etapów) | Zamawiający płaci 480.000 zł, zanim cokolwiek nabędzie; przy zwłoce 1 dzień — kara 50.000 zł, a prawa nie przeszły |
| Wartość wdrożenia przy wypowiedzeniu przez Wykonawcę | brak regulacji rozliczenia ryczałtu | — | [BRAK DANYCH] — umowa nie mówi, ile z 480.000 zł przysługuje za część prac |
| Termin zakończenia Wdrożenia | „niezwłocznie" | — | [BRAK DANYCH] — nie da się policzyć daty granicznej ani kamieni milowych |

**Wniosek z rachunku:** ekspozycja Zamawiającego jest otwarta (kara 10,4% wartości dziennie, bez sufitu), a Wykonawcy wynosi 0 zł poza winą umyślną. Przy liczbach z umowy każda zwłoka płatnicza dłuższa niż 10 dni przekracza wartość całej umowy. Rachunek potwierdza werdykt czerwony i nie pozwala ocenić umowy łagodniej niż etykiety klauzul sugerują.

### Bramka ius cogens (R10) — trafienia
Trafione: art. 473 § 2 KC (§ 5 ust. 1), art. 483 § 1 KC (§ 5 ust. 2), art. 41 ust. 2 PrAut (§ 4 ust. 1), art. 28 ust. 3 RODO (§ 8 ust. 2) — wszystkie [NIEZWERYFIKOWANE]. Trigger mikroprzedsiębiorcy (art. 385⁵ KC) [NIEZWERYFIKOWANE]: nieaktywny, obie strony to spółki z o.o.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Odpowiedzialność tylko za winę umyślną, bez winy umyślnej podwykonawców — § 5 ust. 1
**Strona dotknięta:** Zamawiający.
**Opis:** Wykonawca odpowiada „wyłącznie za szkody wyrządzone umyślnie, z wyłączeniem winy umyślnej podwykonawców". Zakres odpowiedzialności za niewykonanie i nienależyte wykonanie (art. 471 KC [NIEZWERYFIKOWANE]) sprowadza się do zera, bo umyślność w kontrakcie wdrożeniowym zdarza się w praktyce rzadko i trudno ją udowodnić. Druga część wyłącza nawet umyślne działania podwykonawców, a to ingeruje w art. 474 KC i w granice swobody umów (art. 353¹, art. 58 KC) [NIEZWERYFIKOWANE]. Fraza „wyłącznie" przy odpowiedzialności to jednocześnie antywzorzec jednostronnego wyłączenia.
**Skutek:** Zamawiający płaci 480.000 zł i nie ma roszczenia za wadliwe, opóźnione lub niezrealizowane wdrożenie ERP (utracone korzyści, koszty zastępczego wykonawcy, przestój sprzedaży).
**Rekomendacja (preferowana):** odpowiedzialność za winę umyślną i rażące niedbalstwo bez limitu, za pozostałe naruszenia do capu np. 100% wynagrodzenia; odpowiedzialność za podwykonawców jak za własne działania (art. 474 KC).
**Fallback (minimum):** cap 50% wynagrodzenia z wyłączeniem winy umyślnej, rażącego niedbalstwa, naruszenia poufności i praw osób trzecich do IP; odpowiedzialność za podwykonawców zachowana.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Jednostronna kara 50.000 zł dziennie za opóźnienie w płatności — § 5 ust. 2
**Strona dotknięta:** Zamawiający (kara bez sufitu); pośrednio także Wykonawca, bo klauzula jest najpewniej nieskuteczna.
**Opis:** Kara umowna za opóźnienie w zapłacie to kara za zobowiązanie pieniężne, której art. 483 § 1 KC nie dopuszcza [NIEZWERYFIKOWANE]. Za opóźnienie w pieniądzu należą się odsetki (art. 481 KC [NIEZWERYFIKOWANE]), a nie kara. Bez względu na nieważność klauzula pokazuje intencję stron: 50.000 zł = 10,4% wartości umowy dziennie, brak sufitu, brak symetrii („Wykonawca nie ponosi kar"). Do miarkowania służy art. 484 § 2 KC [NIEZWERYFIKOWANE]; sąd ocenia to w każdej sprawie osobno.
**Skutek:** jeśli klauzulę uznano by za skuteczną, 10 dni zwłoki = 500.000 zł (104% wartości), 30 dni = 1.500.000 zł. Nawet jej nieskuteczność wymaga procesu, żeby ją stwierdzić.
**Rekomendacja:** skreślić; zastąpić odsetkami ustawowymi za opóźnienie w transakcjach handlowych; kary za zwłokę w wykonaniu dla Wykonawcy, z sufitem (np. 10–20% wynagrodzenia).
**Fallback:** gdy Wykonawca nalega na „sankcję płatniczą" — wyłącznie odsetki, bez kary; wzajemna kara za zwłokę we Wdrożeniu o sufitowanej wysokości.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Przeniesienie praw autorskich „bez ograniczeń", bez pól eksploatacji — § 4 ust. 1
**Strona dotknięta:** Zamawiający (nie nabywa skutecznie praw); pośrednio Wykonawca (niepewność zakresu nabycia i ewentualny spór o zwrot).
**Opis:** „wszelkie prawa autorskie … bez ograniczeń" nie wymienia pól eksploatacji, więc art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE] nie uznaje skutku rozporządzającego w zakładanym zakresie. Nie ma też wymogu formy pisemnej dla przeniesienia (art. 53 PrAut [NIEZWERYFIKOWANE]); umowa jest co prawda pisemna, ale umowa nie rozstrzyga o dokumentowaniu przejścia. Przeniesienie następuje „z chwilą zapłaty" całości, więc przed zapłatą Zamawiający wdraża system bez żadnego tytułu poza niewyłączną domniemaną zgodą. Brak także regulacji praw osobistych (art. 16 PrAut [NIEZWERYFIKOWANE]), praw zależnych, komponentów otwartoźródłowych i oprogramowania Wykonawcy istniejącego przed umową (background IP) — „stworzone oprogramowanie" nie jest zdefiniowane.
**Skutek:** Zamawiający zapłaci 480.000 zł i może nie mieć skutecznego tytułu do dalszej modyfikacji systemu ERP ani do przeniesienia go na inny podmiot.
**Rekomendacja:** wyliczenie pól eksploatacji (art. 74 ust. 4 PrAut [NIEZWERYFIKOWANE]); przejście praw z chwilą odbioru, nie zapłaty całości; definicja utworów; licencja na background IP; klauzula anty-copyleft; gwarancja czystości IP.
**Fallback:** licencja wyłączna, nieograniczona w czasie, na wymienionych polach, z prawem sublicencji dla podmiotów grupy, plus przekazanie kodu.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Prawo do trenowania modeli AI na danych Zamawiającego „niezależnie od pozostałych postanowień" — § 8 ust. 2
**Strona dotknięta:** Zamawiający (dane, tajemnica przedsiębiorstwa, klienci); pośrednio Wykonawca (ekspozycja RODO).
**Opis:** Klauzula „niezależnie od pozostałych postanowień" przebija § 6 (poufność), więc poufność staje się iluzoryczna. Dane w systemie ERP detalisty obejmują dane klientów, pracowników i kontrahentów (dane osobowe [BRAK DANYCH o zakresie]). Wykorzystanie ich przez Wykonawcę do własnego celu (trenowanie modeli) przekształca go z procesora w administratora i wymaga odrębnej podstawy z art. 6 RODO oraz odpowiedniej zgodności z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]; umowa jej nie daje, a Zamawiający jako administrator nie może takiej zgody udzielić bez podstawy wobec osób, których dane dotyczą.
**Skutek:** wyciek wiedzy handlowej do modeli dostępnych dla konkurentów; ryzyko kar administracyjnych (art. 83 RODO [NIEZWERYFIKOWANE], do 10 mln EUR albo 2% obrotu w przypadku art. 83 ust. 4 — kwota z pamięci, nie z tekstu umowy) i roszczeń osób, których dane dotyczą.
**Rekomendacja:** skreślić; wprowadzić zakaz wykorzystania danych Zamawiającego do trenowania modeli AI, zakaz wtórnego użycia i obowiązek usunięcia danych po zakończeniu umowy; umowa powierzenia (ryzyko 🟠 7).
**Fallback:** wykorzystanie wyłącznie danych zanonimizowanych w sposób nieodwracalny, po pisemnej zgodzie i z odpowiednim wynagrodzeniem.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`, `references/baza-klauzul/14-rodo.md`

### 🟠 RYZYKA WYSOKIE

#### 5. Zobowiązanie rozmyte i brak terminu wykonania — § 1 ust. 1, § 2 ust. 1–2
**Strona dotknięta:** Zamawiający (nie ma obowiązku rezultatu ani terminu); pośrednio Wykonawca (brak kryterium odbioru, na którym mógłby oprzeć żądanie zapłaty).
**Opis:** „dołoży starań" zamienia wdrożenie (zobowiązanie rezultatu, znamiona umowy o dzieło, art. 627 KC [NIEZWERYFIKOWANE]) w zobowiązanie starannego działania. „Niezwłocznie po podpisaniu Umowy" nie ma liczby dni, więc nie da się policzyć daty zwłoki ani kary. „na bieżąco" w § 2 ust. 2 nie jest harmonogramem. Brak procedury odbioru, kryteriów akceptacji i testów. Brak także definicji „Wdrożenia" i „Umowy".
**Skutek:** nie da się wykazać opóźnienia ani niewykonania; płatność 480.000 zł nie jest powiązana z żadnym zdarzeniem.
**Rekomendacja:** „zobowiązuje się do wykonania"; harmonogram z datami, kamienie milowe, kryteria odbioru, kary za zwłokę z sufitem.
**Fallback:** termin końcowy w dniach (np. 120 dni od podpisania) i odbiór w 14 dni, brak reakcji = odbiór dopiero po wezwaniu.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 6. Brak zakresu — Załącznik nr 1 wskazany, lecz nieistniejący — § 1 ust. 1
**Strona dotknięta:** obie (Zamawiający nie wie, co kupuje; Wykonawca ryzykuje spór o zakres ryczałtu).
**Opis:** Umowa odsyła do „Załącznika nr 1", którego nie ma w treści (R11: nie przypisuję mu żadnej treści). Ryczałt 480.000 zł bez zakresu = brak przedmiotu świadczenia, co zagraża essentialia negotii umowy [NIEZWERYFIKOWANE: art. 627 KC]. Brak mechanizmu zmian zakresu (change request) i wycen prac dodatkowych.
**Skutek:** spór o to, czy integracje, migracja danych, szkolenia i testy mieszczą się w cenie.
**Rekomendacja:** dołączyć załącznik z zakresem funkcjonalnym, migracją, integracjami, szkoleniami; procedura zmian.
**Fallback:** zakres ogólny w umowie z opisem w odrębnym dokumencie zatwierdzanym przed podpisem.

#### 7. Brak umowy powierzenia danych osobowych — brak regulacji (obszar RODO)
**Strona dotknięta:** obie (Zamawiający jako administrator, Wykonawca jako procesor).
**Opis:** Wdrożenie ERP w infrastrukturze Zamawiającego oznacza dostęp Wykonawcy do danych (testy, migracja, wsparcie). Umowa nie zawiera postanowień z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]: przedmiot, czas, rodzaj danych, subprocesorzy, audyt, zwrot lub usunięcie. Jedyna wzmianka o danych to § 8 ust. 2 (trenowanie AI).
**Skutek:** naruszenie RODO po obu stronach; ekspozycja administracyjna [BRAK DANYCH o kwocie w umowie].
**Rekomendacja:** załącznik DPA wg `references/checklist-dpa-art28.md`.
**Fallback:** krótkie powierzenie z procedurą naruszeń i listą subprocesorów.

#### 8. Wypowiedzenie: Zamawiający związany, Wykonawca wychodzi w każdym czasie — § 7
**Strona dotknięta:** Zamawiający.
**Opis:** § 7 ust. 1 zabrania Zamawiającemu wypowiedzenia przed zakończeniem Wdrożenia, a data zakończenia nie jest określona (zob. 5). § 7 ust. 2 pozwala Wykonawcy odejść „w każdym czasie i bez podania przyczyny" (okres wypowiedzenia 0 dni). Brak procedury exit: zwrot materiałów i danych, przekazanie prac w toku (WIP), rozliczenie ryczałtu za wykonaną część. „w każdym czasie" w umowie o dzieło lub zlecenia bywa oceniane przez pryzmat art. 746 KC i art. 644 KC [NIEZWERYFIKOWANE].
**Skutek:** Wykonawca może porzucić projekt w połowie, a Zamawiający nie wyjdzie, nawet gdy Wykonawca nie pracuje; rozliczenie [BRAK DANYCH].
**Rekomendacja:** wzajemne wypowiedzenie z ważnej przyczyny (w tym zwłoka > 30 dni) i okres wypowiedzenia (np. 30 dni) dla obu stron; rozliczenie za wykonane prace; plan wyjścia i przekazania dokumentacji.
**Fallback:** wypowiedzenie przez Zamawiającego z przyczyn (zwłoka, utrata kluczowych osób) i odstąpienie po bezskutecznym wezwaniu.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md`

#### 9. Kod źródłowy „może, ale nie jest zobowiązany" — § 4 ust. 2
**Strona dotknięta:** Zamawiający.
**Opis:** Antywzorzec „może, ale nie jest zobowiązany": pozorne zobowiązanie. Bez kodu źródłowego nabyte prawa (nawet gdyby były skuteczne) nie dają możliwości utrzymania i rozwoju ERP, a uzależniają od Wykonawcy, który z kolei może wypowiedzieć umowę w każdym czasie (§ 7 ust. 2) i ustalać wsparcie według wyłącznego uznania (§ 5 ust. 3). Brak escrow, dokumentacji technicznej, praw dostępu do repozytorium.
**Skutek:** pełna zależność od jednego dostawcy.
**Rekomendacja:** obowiązek przekazania kodu i dokumentacji w ramach odbioru; escrow jako fallback.
**Fallback:** kodu nie przekazuje się w toku, ale escrow z wydaniem przy upadłości lub zaprzestaniu wsparcia.

#### 10. Wsparcie powdrożeniowe „według wyłącznego uznania" Wykonawcy — § 5 ust. 3
**Strona dotknięta:** Zamawiający.
**Opis:** Zakres wsparcia ustala jedna strona, bez kryteriów, SLA, czasu reakcji, ceny i okresu. Brak rękojmi i gwarancji (nie ma żadnej klauzuli o wadach); ustawowa rękojmia (art. 556 i n. KC [NIEZWERYFIKOWANE]) mogłaby działać, ale bez terminów i bez ograniczeń. Brak maintenance wg art. 750 KC [NIEZWERYFIKOWANE].
**Skutek:** po odbiorze Zamawiający nie ma gwarancji naprawy błędów; ERP jest systemem krytycznym.
**Rekomendacja:** SLA z poziomami priorytetów, czasami reakcji, okres gwarancji (np. 12 mies.), cena wsparcia.
**Fallback:** gwarancja 6 mies. oraz opcja wykupu wsparcia za stawkę określoną w umowie.

#### 11. Prawo obce i sąd zagraniczny przy braku elementu zagranicznego — § 8 ust. 1
**Strona dotknięta:** obie, w praktyce Zamawiający (koszt dochodzenia roszczeń w USA).
**Opis:** Prawo stanu Delaware i sąd w Wilmington w umowie dwóch spółek z o.o. (dane fikcyjne; z treści wynika polski kontekst: „zł", spółki z o.o., wdrożenie w infrastrukturze Zamawiającego). Wybór prawa obcego bez elementu zagranicznego może być nieskuteczny (art. 3 rozporządzenia Rzym I [NIEZWERYFIKOWANE]) i nie wyłącza norm bezwzględnych prawa polskiego (zob. ryzyka 1–4). Klauzula jurysdykcyjna zwiększa koszty dochodzenia 480.000 zł. Sprzeczność z § 4 ust. 1 (prawo autorskie: polskie pojęcia).
**Skutek:** spór o właściwość, koszty tłumaczeń i pełnomocnika w USA przekraczające wartość roszczenia.
**Rekomendacja:** prawo polskie, sąd właściwy dla siedziby pozwanego lub konkretny sąd polski; ewentualnie arbitraż z oznaczonym sądem.
**Fallback:** sąd polski wskazany z nazwy, prawo polskie dla IP i danych niezależnie od reszty.

#### 12. Brak gwarancji czystości IP, anty-copyleft i rękojmi — brak regulacji (obszar prawa autorskie)
**Strona dotknięta:** Zamawiający.
**Opis:** Umowa nie zawiera oświadczeń Wykonawcy o prawach do utworów, zakazu użycia komponentów GPL/AGPL bez zgody, zwolnienia z roszczeń osób trzecich (indemnity), ani procedury po zarzucie naruszenia. Brak też regulacji udziału komponentów otwartoźródłowych.
**Skutek:** Zamawiający odpowiada wobec osób trzecich za system, którego pochodzenia nie zna.
**Rekomendacja:** gwarancja IP, zakaz copyleft, zwolnienie z roszczeń osób trzecich (do capu z wyłączeniem IP).
**Fallback:** oświadczenie o czystości IP według wiedzy Wykonawcy plus obowiązek zawiadomienia.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟡 RYZYKA ŚREDNIE

#### 13. Wynagrodzenie ryczałtowe bez harmonogramu płatności — § 3
**Strona dotknięta:** obie. Zamawiający płaci całość bez etapów; Wykonawca czeka do 60 dni od doręczenia faktury i nie wie, kiedy może fakturować.
**Opis:** 480.000 zł netto; brak podatku VAT w treści (założenie 23% w rachunku), brak momentu wystawienia faktury, brak etapów, brak waloryzacji, brak zaliczki. 60 dni to górna granica B2B (por. rachunek), bez marginesu.
**Rekomendacja:** płatność etapowa powiązana z odbiorami (np. 30/40/30), termin 30 dni. Klauzula z bazy: `references/baza-klauzul/06-wynagrodzenie.md`.

#### 14. Poufność bez okresu, wyjątków i sankcji — § 6
**Strona dotknięta:** obie; w praktyce Zamawiający, bo § 8 ust. 2 przebija poufność.
**Opis:** Jedno zdanie. Brak definicji informacji poufnych, wyjątków (informacje publiczne, niezależnie opracowane, ujawnienie z mocy prawa), okresu po zakończeniu umowy, zwrotu materiałów, kary umownej.
**Rekomendacja:** model warstwowy okresów (np. 5 lat; bezterminowo dla tajemnicy przedsiębiorstwa), wyjątki, obowiązek zwrotu.

#### 15. Niepełne oznaczenie stron i umocowania — nagłówek
**Strona dotknięta:** obie.
**Opis:** Brak KRS, NIP, adresów, osób reprezentujących i podstawy umocowania (dane „fikcyjne" wg treści). Brak daty i miejsca zawarcia.
**Rekomendacja:** pełne dane z KRS, sprawdzenie umocowania.

#### 16. Pojęcia bez definicji — całość
**Strona dotknięta:** obie.
**Opis:** „Umowa", „Wdrożenie", „stworzone oprogramowanie", „Dzień" (liczenie terminów) bez definicji; § 1 ust. 2 „Strony wzajemnie zobowiązują się do współpracy" to pozorna wzajemność: żaden obowiązek Zamawiającego (dostęp, dane, osoby kontaktowe, decyzje w terminie) nie jest opisany, a jego niewykonanie nie ma skutku.
**Rekomendacja:** słownik pojęć; katalog zamknięty obowiązków Zamawiającego i skutek ich niewykonania (przesunięcie terminu).

### 🟢 RYZYKA NISKIE

#### 17. Redakcja — § 3 ust. 1 i całość
**Strona dotknięta:** obie.
**Opis:** Kwota tylko cyframi, bez zapisu słownego; „480.000 zł" bez zastrzeżenia „netto + VAT w obowiązującej stawce"; spójna nazwa stron zachowana.
**Rekomendacja:** kwota cyframi i słownie.

### ✓ Obszary bez zastrzeżeń
Tytuł prawny i przekwalifikowanie: n/d (brak body leasingu; kwalifikacja umowy o dzieło/zlecenie omówiona w ryzyku 5).
Reprezentacja, definicje, poufność, RODO, spory, wypowiedzenie, prawa autorskie, odpowiedzialność — wszystkie obszary mają ustalenia powyżej; żaden z dziewięciu obszarów nie jest bez zastrzeżeń.

### Miejsca, w których w trybie pełnym byłby STOP (tryb express — nie zatrzymywano się)
1. Czy strony mają polski kontekst (siedziby w Polsce, dane w polskiej infrastrukturze) — założono tak (ryzyko 11).
2. Strona zlecająca audyt — nieznana; audyt neutralny.
3. Zakres Załącznika nr 1 — nie dostarczono.
4. Rodzaj i wolumen danych osobowych w ERP — nieznane.

---

## OCENA BEZPIECZEŃSTWA: 4/100

Cztery ryzyka krytyczne (w tym trzy naruszenia norm bezwzględnych: art. 473 § 2 i 483 § 1 KC, art. 41 ust. 2 PrAut) i osiem wysokich; rachunek pokazuje ekspozycję Zamawiającego otwartą (10,4% wartości dziennie, bez sufitu) przy zerowej ekspozycji Wykonawcy poza winą umyślną.

**Werdykt:** NIE PODPISYWAĆ (🟥 CZERWONY)

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
