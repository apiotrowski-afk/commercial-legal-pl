konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 3 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite: każde powołanie przepisu oznaczono [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa ramowa T&M, rozwój oprogramowania (QUANTA DEV sp. z o.o. / MERIDIAN FINANCE S.A.)

> **WERDYKT: CZERWONY** — nie podpisywać w obecnej formie; punkty krytyczne (kary poza capem bez sufitu, kara 300.000 zł za zakaz konkurencji, nieograniczony indemnity IP, brak przeniesienia praw autorskich) wymagają negocjacji przed podpisem.

Strony: Wykonawca = QUANTA DEV (dostawca), Zamawiający = MERIDIAN FINANCE (klient). Przy każdej fladze wskazano stronę dotkniętą.

### Rachunek ekspozycji

Składniki wyjściowe (z umowy): stawka 220 zł netto/h (§ 1 ust. 2); 2 Specjalistów × 160 h/mies. (§ 1 ust. 2); okres 24 mies. (§ 1 ust. 3); kara za zwłokę 0,5% wynagrodzenia miesięcznego za rozpoczęty dzień (§ 2 ust. 1); kara jakościowa 5.000 zł (§ 2 ust. 2); kara za konkurencję 300.000 zł (§ 2 ust. 3); cap 12-miesięczne wynagrodzenie (§ 3 ust. 1); podwyżka 8% w okresie przedłużenia (§ 4 ust. 2); okno sprzeciwu 90 dni (§ 4 ust. 1); zakaz konkurencji 24 mies. po zakończeniu (§ 5).

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Godziny miesięcznie | 2 × 160 h | 2 × 160 | 320 h |
| Wynagrodzenie miesięczne (szacunek) | 220 zł/h | 320 h × 220 zł | **70.400 zł** netto |
| Wynagrodzenie roczne | 12 mies. | 12 × 70.400 zł | 844.800 zł |
| Wartość umowy (24 mies.) | 24 mies. | 24 × 70.400 zł (= 2 × 844.800 zł) | **1.689.600 zł** netto |
| Cap nominalny | 12-mies. wynagrodzenie | 12 × 70.400 zł | **844.800 zł = 50,0% wartości umowy** (przy założeniu, że „12-miesięczne wynagrodzenie" = szacunek; umowa nie określa podstawy) |
| Kara za zwłokę, 1 dzień | 0,5% × wynagrodzenie miesięczne | 0,005 × 70.400 zł | 352 zł/dzień |
| Kara za zwłokę, 30 dni | brak sufitu | 30 × 352 zł | 10.560 zł (15% mies.) |
| Kara za zwłokę, 200 dni | brak sufitu | 200 × 352 zł = 70.400 zł | 100% wynagrodzenia miesięcznego; sufitu brak, liczba Przyrostów w 24 mies. = [BRAK DANYCH], każdy Przyrost liczy się osobno |
| Kara jakościowa, 1 przypadek | 5.000 zł | 5.000 zł / 220 zł/h = 22,7 h | 5.000 zł (= ok. 22,7 godziny pracy); liczba przypadków i sufit = [BRAK DANYCH] |
| Kara za konkurencję, 1 przypadek | 300.000 zł | 300.000 / 70.400 = 4,26 mies.; 300.000 / 844.800 = 35,5% capu; 300.000 / 1.689.600 = 17,8% wartości umowy | 300.000 zł = 852 dni zwłoki (300.000 / 352 = 852,3) |
| Kara za konkurencję, 3 przypadki | 3 × 300.000 zł | 3 × 300.000 zł | 900.000 zł > cap 844.800 zł (o 55.200 zł); okres zakazu: 24 mies. trwania umowy + 24 mies. po (łącznie min. 48 mies.) |
| Kary poza capem (max) | sumują się, bez sufitu, poza capem (§ 2 ust. 4) | brak sufitu = ekspozycja otwarta | [BRAK DANYCH] liczby zdarzeń; scenariusz poniżej |
| Odszkodowanie ponad kary | dopuszczone (§ 2 ust. 4) | — | nieograniczone w ramach capu 844.800 zł (o ile cap obejmuje odszkodowanie, a nie kary) |
| Indemnity IP (§ 3 ust. 2) | „wszelka odpowiedzialność", „wszelkie koszty" | — | bez sufitu; relacja do capu niejasna (patrz ryzyko 3) |
| Efektywna ekspozycja Wykonawcy (scenariusz ilustracyjny: 1 naruszenie konkurencji + 30 dni zwłoki + 5 przypadków jakości, cap w pełni wykorzystany) | cap + kary poza capem | 844.800 + 300.000 + 10.560 + 25.000 (5 × 5.000) = 1.180.360 zł | **1.180.360 zł = 0,70× wartości umowy (1.180.360 / 1.689.600 = 0,6986)**, bez indemnity IP, które jest dodatkowo otwarte |
| Asymetria (Wykonawca vs Zamawiający) | kary i indemnity wyłącznie po stronie Wykonawcy; zobowiązań karnych Zamawiającego brak | ekspozycja Wykonawcy 1.180.360 zł (scenariusz) vs 0 zł kar Zamawiającego | stosunek nieskończony (brak jakiejkolwiek kary po stronie Zamawiającego, brak terminu płatności) |
| Podwyżka 8%, okres 2 (mies. 25–36) | 220 zł × 1,08 | 220 × 1,08 = 237,60 zł/h | +17,60 zł/h |
| Okres 2, wynagrodzenie miesięczne | 320 h × 237,60 zł | 320 × 237,60 | 76.032 zł (+5.632 zł mies. vs 70.400 zł) |
| Okres 2, wynagrodzenie roczne | 12 × 76.032 zł | 12 × 76.032 | **912.384 zł** (+67.584 zł vs 844.800 zł) |
| Okres 3 (mies. 37–48), stawka | 237,60 × 1,08 | 237,60 × 1,08 = 256,608 | 256,61 zł/h (+16,6% vs 220 zł: 256,608 / 220 = 1,1664) |
| Okres 3, wynagrodzenie roczne | 320 h × 256,608 zł × 12 | 82.114,56 zł × 12 | **985.374,72 zł** (+140.574,72 zł vs 844.800 zł) |
| Wartość nieskutecznego sprzeciwu po 24 mies. | kolejny okres 12 mies. | 12 × 76.032 zł | 912.384 zł zobowiązania „wpada" automatycznie |
| Data graniczna sprzeciwu | 90 dni przed końcem okresu | koniec okresu − 90 dni; przykład: umowa od 1.01.2027 kończy się 31.12.2028, ostatni dzień 2.10.2028 (31.12 − 90 dni = 2.10) | data zależy od daty zawarcia umowy = [BRAK DANYCH]; sprzeciw najpóźniej 90 dni przed końcem |
| Termin płatności, odbiór, rozliczenie godzin | brak w umowie | — | [BRAK DANYCH] |

Wniosek z rachunku: cap 844.800 zł wygląda na 50% wartości umowy, ale jest iluzoryczny, bo kary (każda osobno, sumowane, bez sufitu) i odszkodowanie ponad kary idą poza nim, a indemnity IP jest otwarty. Pojedyncze naruszenie zakazu konkurencji (300.000 zł) odpowiada 35,5% capu, a trzy takie naruszenia przekraczają cap. Po stronie Zamawiającego rachunek pokazuje drugi problem: automatyczna podwyżka o 8% w każdym okresie przedłużenia kumuluje się do +16,6% po dwóch przedłużeniach (okres 3), a przegapienie okna 90 dni zobowiązuje do 912.384 zł.

### RYZYKA KRYTYCZNE

#### 1. Kary umowne poza capem, sumujące się, bez sufitu, plus odszkodowanie ponad karę — § 2 ust. 4, § 3 ust. 1
**Strona dotknięta:** Wykonawca (QUANTA DEV).
**Opis:** Kary nie wliczają się do limitu, sumują się i nie mają własnego sufitu; Zamawiający może dochodzić odszkodowania ponad kary (art. 484 § 1 KC [NIEZWERYFIKOWANE]). Cap z § 3 ust. 1 chroni więc tylko przed częścią ekspozycji.
**Skutek:** Efektywna ekspozycja wielokrotnie przekracza cap: w scenariuszu ilustracyjnym 1.180.360 zł (0,70× wartości umowy) przy samych karach, bez indemnity IP; kary dzienne z § 2 ust. 1 rosną bez granicy.
**Rekomendacja (preferowana):** Włączyć kary do capu i wprowadzić łączny sufit kar (np. 10-20% wynagrodzenia z danego okresu); kary za zwłokę z sufitem odrębnym; odszkodowanie ponad karę wyłączyć albo ograniczyć do capu.
**Fallback (minimum akceptowalne):** Osobny sufit kar (np. 20% wartości umowy), kary nie sumują się za to samo zdarzenie, kara zaliczana na poczet odszkodowania.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Kara 300.000 zł za każdy przypadek naruszenia zakazu konkurencji, zakaz 24 mies. po umowie, bez wynagrodzenia — § 2 ust. 3, § 5 ust. 1
**Strona dotknięta:** Wykonawca (QUANTA DEV).
**Opis:** Zakaz obejmuje „podmioty prowadzące działalność konkurencyjną wobec Zamawiającego" (zakres nieokreślony; dla dostawcy IT obsługującego sektor finansowy to potencjalnie cały rynek), trwa 48 mies. łącznie (24 mies. umowy + 24 mies. po), a wprost „nie jest związany z dodatkowym wynagrodzeniem". Kara jest stała (300.000 zł = 4,26 mies. wynagrodzenia), za każdy przypadek, bez sufitu.
**Skutek:** Trzy przypadki = 900.000 zł (więcej niż cap). Zakaz po ustaniu umowy, bez ekwiwalentu, ryzykuje uznanie za sprzeczny z zasadami współżycia społecznego (art. 353^1 i 58 § 2 KC [NIEZWERYFIKOWANE]); kara podlega miarkowaniu jako rażąco wygórowana (art. 484 § 2 KC [NIEZWERYFIKOWANE]), ale to uprawnienie sądu, nie automat, i wymaga procesu. Do czasu rozstrzygnięcia Wykonawca niesie ryzyko i koszt sporu.
**Rekomendacja (preferowana):** Usunąć zakaz po ustaniu umowy; w okresie trwania zawęzić do wąsko zdefiniowanych konkurentów imiennie; kara jednorazowa z sufitem (np. wielokrotność miesięcznego wynagrodzenia, nie więcej niż 1-2 mies.); ekwiwalent za okres po umowie.
**Fallback (minimum akceptowalne):** Zakaz po umowie do 6-12 mies. z ekwiwalentem min. 50% średniego wynagrodzenia za okres zakazu, lista konkurentów w załączniku, łączny sufit kar z § 5.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria: zakaz konkurencji / kary umowne; sprawdzić INDEX.md)

#### 3. Nieograniczony indemnity IP i niejasna relacja do capu — § 3 ust. 2, § 3 ust. 1
**Strona dotknięta:** Wykonawca (QUANTA DEV).
**Opis:** „Zwolni z wszelkiej odpowiedzialności" i „pokryje wszelkie związane z tym koszty, w tym koszty obsługi prawnej". Brak sufitu, brak procedury (zawiadomienie, kontrola obrony, ugoda za zgodą Wykonawcy), brak wyłączeń (np. za materiały i specyfikacje dostarczone przez Zamawiającego, za modyfikacje po stronie Zamawiającego). Zarazem § 3 ust. 1 mówi o „łącznej odpowiedzialności" ograniczonej do 12 mies. — wewnętrzna sprzeczność: czy indemnity mieści się w capie, czy nie, umowa nie rozstrzyga.
**Skutek:** Ekspozycja potencjalnie nieograniczona na roszczenia osób trzecich (IP w finansach, w tym licencje, patenty); spór o relację do capu.
**Rekomendacja (preferowana):** Indemnity w capie albo z własnym, odrębnym sufitem (super-cap); procedura roszczeń osób trzecich; wyłączenia za wkład Zamawiającego.
**Fallback (minimum akceptowalne):** Odrębny sufit indemnity (np. 2× cap), procedura i wyłączenia zachowane.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`, `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Brak przeniesienia praw autorskich i licencji do kodu — cała umowa (brak postanowienia)
**Strona dotknięta:** Zamawiający (MERIDIAN FINANCE); pośrednio Wykonawca (niepewność statusu, ryzyko roszczeń).
**Opis:** Umowa o rozwój oprogramowania nie zawiera żadnej klauzuli o przeniesieniu autorskich praw majątkowych ani licencji, pól eksploatacji, momentu przejścia praw, praw zależnych. Wzmianka o IP pojawia się wyłącznie w indemnity (§ 3 ust. 2), co zakłada, że prawa gdzieś przechodzą, ale nie mówi którędy. Bez wskazania pól eksploatacji przeniesienie jest nieskuteczne w tym zakresie (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]); prawa autorskie powstają po stronie twórców, a nie po stronie klienta.
**Skutek:** Zamawiający płaci co najmniej 1.689.600 zł za kod, do którego nie ma tytułu prawnego; Wykonawca ponosi indemnity za IP, którego status sam nie kontroluje.
**Rekomendacja (preferowana):** Dodać przeniesienie autorskich praw majątkowych z wyliczeniem pól eksploatacji (art. 74 ust. 4 PrAut [NIEZWERYFIKOWANE]), moment przejścia (np. z zapłatą), zgoda na prawa zależne, wyłączenie komponentów open source z przeniesienia, gwarancje czystości IP.
**Fallback (minimum akceptowalne):** Licencja wyłączna, bezterminowa, nieodwołalna z pełnymi polami eksploatacji do czasu przeniesienia praw.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### RYZYKA WYSOKIE

#### 5. Auto-przedłużenie z automatyczną podwyżką 8% w każdym okresie — § 4 ust. 1-2
**Strona dotknięta:** Zamawiający (MERIDIAN FINANCE) co do kosztu; Wykonawca co do blokady (zakaz konkurencji biegnie wraz z umową).
**Opis:** Po 24 mies. umowa przedłuża się o 12 mies., stawka rośnie o 8% względem okresu poprzedniego, bez zależności od wskaźnika, bez uzgodnienia; sprzeciw tylko 90 dni przed końcem.
**Skutek:** 220 zł → 237,60 zł → 256,61 zł/h; okres 2: 912.384 zł (+67.584 zł); okres 3: 985.374,72 zł (+140.574,72 zł vs rok bazowy). Przegapienie okna = zobowiązanie na 912.384 zł; dla Wykonawcy zakaz konkurencji przedłuża się razem z umową.
**Rekomendacja (preferowana):** Przedłużenie tylko za pisemnym porozumieniem albo przedłużenie z jednoznacznym przypomnieniem; waloryzacja do wskaźnika (np. CPI) z limitem, dwustronna.
**Fallback (minimum akceptowalne):** Okno sprzeciwu 30-60 dni, obowiązek przypomnienia przez stronę ze wzmocnionej pozycji, podwyżka max wg wskaźnika.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria: czas trwania / waloryzacja)

#### 6. Kara za zwłokę nieadekwatna do modelu T&M, podstawa naliczenia niezdefiniowana — § 2 ust. 1, § 1 ust. 2
**Strona dotknięta:** Wykonawca (QUANTA DEV).
**Opis:** T&M rozlicza nakład pracy (staranne działanie), a kara za „zwłokę w dostarczeniu Przyrostu względem harmonogramu sprintu" przypisuje rezultat. „Przyrost", „harmonogram sprintu" i „wynagrodzenie miesięczne" nie są zdefiniowane: wynagrodzenie miesięczne w T&M jest zmienne (faktyczne godziny vs szacunek 70.400 zł). „Za każdy rozpoczęty dzień" liczy też dni wolne. Zwłoka zależy od współdziałania Zamawiającego (kryteria akceptacji, dostęp do środowisk), a umowa nie wyłącza kary przy jego opóźnieniach.
**Skutek:** 352 zł/dzień (wg szacunku) w sprincie, bez sufitu, w każdym sprincie osobno; spór o podstawę (szacunek czy faktyczne wynagrodzenie).
**Rekomendacja (preferowana):** Zdefiniować Przyrost i harmonogram, wyłączyć zwłokę zależną od Zamawiającego, kara dzienna z sufitem na sprint i łącznym; podstawa = wynagrodzenie faktycznie należne za dany miesiąc.
**Fallback (minimum akceptowalne):** Sufit 10% wynagrodzenia miesięcznego na sprint; dni robocze.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 7. Kara jakościowa 5.000 zł „za każdy przypadek" z niedołączonym Załącznikiem nr 2 — § 2 ust. 2
**Strona dotknięta:** Wykonawca (QUANTA DEV).
**Opis:** Próg z Załącznika nr 2 nie występuje w dokumencie [BRAK DANYCH]; „przypadek" nie jest zdefiniowany (jeden przegląd? jedna linia? jedno zgłoszenie?). Brak sufitu, brak trybu naprawy (czas na poprawkę przed naliczeniem).
**Skutek:** 5.000 zł (22,7 h pracy) za każdy przypadek, kumulacja z karą za zwłokę i odszkodowaniem; kara od progu, który nie jest zdefiniowany, nadaje stronie otwartą dyskrecję.
**Rekomendacja (preferowana):** Dołączyć załącznik z mierzalnymi kryteriami, okres naprawy (np. 5 dni roboczych) przed naliczeniem, sufit miesięczny kar jakościowych.
**Fallback (minimum akceptowalne):** Kara tylko za niewykonanie poprawki w terminie; sufit miesięczny.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/` (kategoria: odbiór / jakość)

#### 8. Brak minimalnego wolumenu, budżetu, terminu płatności i procedury rozliczenia godzin — § 1 ust. 2 (i brak postanowienia)
**Strona dotknięta:** Obie strony: Wykonawca (brak gwarantowanego przychodu przy związaniu zakazem konkurencji); Zamawiający (brak budżetu maksymalnego i zatwierdzania godzin).
**Opis:** „Szacowane zaangażowanie" nie jest zobowiązaniem. Umowa nie określa terminu płatności, fakturowania, ewidencji i akceptacji czasu, limitu godzin bez zgody, nadgodzin, zmiany składu zespołu. Termin płatności [BRAK DANYCH] (do oceny pod kątem 60 dni w B2B — ustawa o terminach zapłaty [NIEZWERYFIKOWANE]).
**Skutek:** Wykonawca: przychód od 0 do 70.400 zł/mies. przy 48-miesięcznym zakazie konkurencji. Zamawiający: niekontrolowany koszt przy braku sufitu godzin.
**Rekomendacja (preferowana):** Minimum zaangażowania lub opłata za gotowość; budżet miesięczny z akceptacją przekroczeń; ewidencja czasu i termin płatności 30 dni.
**Fallback (minimum akceptowalne):** Budżet szacunkowy z obowiązkiem powiadomienia przy 80% oraz termin płatności 30-60 dni.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria: wynagrodzenie / płatności)

#### 9. Brak wypowiedzenia w trakcie obowiązywania i brak trybu wyjścia — § 1 ust. 3, § 4
**Strona dotknięta:** Obie strony.
**Opis:** Umowa na 24 mies. bez prawa wypowiedzenia ani rozwiązania za ważnych przyczyn (poza sprzeciwem wobec przedłużenia), bez konsekwencji zakończenia (przekazanie kodu, dokumentacji, transfer wiedzy). Obie strony tkwią w umowie 24 mies., a po przedłużeniu kolejne 12 mies.
**Skutek:** Zamawiający nie może zakończyć współpracy przy słabej jakości inaczej niż karami po stronie Wykonawcy; Wykonawca nie może wyjść z toksycznej współpracy, a jego zakaz konkurencji trwa. Termin graniczny: zob. rachunek (90 dni przed końcem okresu).
**Rekomendacja (preferowana):** Wypowiedzenie z 30-60-dniowym okresem po stronie obu stron, rozwiązanie za naruszenie po wezwaniu, klauzula exit (przekazanie kodu).
**Fallback (minimum akceptowalne):** Wypowiedzenie po 12 mies. z 90-dniowym okresem, exit assistance płatny godzinowo.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria: czas trwania i rozwiązanie)

### RYZYKA ŚREDNIE

#### 10. Niezdefiniowany cap: „12-miesięczne wynagrodzenie" — § 3 ust. 1
**Strona dotknięta:** Obie strony (Wykonawca: niepewność; Zamawiający: cap może okazać się niski).
**Opis:** Nie wiadomo, czy to wynagrodzenie szacunkowe (844.800 zł), faktycznie zapłacone w 12 mies. poprzedzających zdarzenie, czy należne. W pierwszych miesiącach wartość „faktycznie zapłacona" jest bliska zeru; po zdarzeniu mogą być inne wartości. Brak rozróżnienia: cap na zdarzenie, na okres, łączny.
**Skutek:** Cap od 0 do 844.800 zł w zależności od wykładni; spór o podstawę.
**Rekomendacja (preferowana):** Cap = wynagrodzenie netto zapłacone lub należne za 12 mies. poprzedzających zdarzenie, minimum kwotowe (np. 844.800 zł).
**Fallback (minimum akceptowalne):** Kwota stała, równa szacunkowi.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 11. Brak definicji i ostatecznych odesłań — § 1, § 2, § 5
**Strona dotknięta:** Obie strony.
**Opis:** Niezdefiniowane: Przyrost, Specjalista, harmonogram sprintu, wynagrodzenie miesięczne, podmiot konkurencyjny, przypadek naruszenia. Odesłanie do Załącznika nr 2 bez załącznika. Brak postanowień o składzie zespołu, zastępowalności Specjalistów, trybie zmian, akceptacji (spór o to, czy Przyrost został „dostarczony").
**Skutek:** Spory o stosowanie kar (patrz ryzyka 6, 7, 2).
**Rekomendacja (preferowana):** Słownik definicji, załączniki (harmonogram, kryteria jakości, lista konkurentów), procedura odbioru.
**Fallback (minimum akceptowalne):** Definicje Przyrostu i konkurenta oraz dołączenie Załącznika nr 2.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 12. Brak poufności i postanowień o danych osobowych — cała umowa
**Strona dotknięta:** Zamawiający (instytucja finansowa; dane i tajemnica przedsiębiorstwa); w mniejszym stopniu Wykonawca.
**Opis:** Umowa nie zawiera klauzuli poufności ani postanowień o powierzeniu danych (art. 28 RODO [NIEZWERYFIKOWANE]), chociaż wytwarzanie oprogramowania dla podmiotu finansowego zwykle wiąże się z dostępem do środowisk i danych. Dla S.A. z branży finansowej możliwe wymogi outsourcingowe [BRAK DANYCH, poza treścią umowy].
**Skutek:** Brak kontraktowej ochrony informacji; ryzyko regulacyjne po stronie Zamawiającego.
**Rekomendacja (preferowana):** Klauzula poufności (okres min. po zakończeniu umowy), umowa powierzenia, o ile Wykonawca przetwarza dane.
**Fallback (minimum akceptowalne):** Odesłanie do osobnego NDA i DPA w terminie przed startem prac.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`, `references/checklist-dpa-art28.md`

### RYZYKA NISKIE

#### 13. Sąd właściwy wg siedziby Zamawiającego — § 6 ust. 1
**Strona dotknięta:** Wykonawca (QUANTA DEV): koszt dojazdu i pozycja w sporze; po stronie Zamawiającego to korzyść.
**Opis:** Jednostronne forum, bez trybu mediacji i bez wskazania sądu właściwego rzeczowo (w tym sądu wg wartości sporu).
**Skutek:** Marginalny koszt; wzmacnia przewagę Zamawiającego w sporze o kary.
**Rekomendacja (preferowana):** Sąd siedziby pozwanego lub neutralny; mediacja przed wszczęciem sporu.
**Fallback (minimum akceptowalne):** Pozostawić forum, o ile zostanie zrównoważone innymi punktami.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria: spory i prawo właściwe)

#### 14. Dane stron i formalności — preambuła
**Strona dotknięta:** Obie strony.
**Opis:** Brak KRS, NIP, adresów, danych reprezentantów, daty i miejsca zawarcia (dokument fikcyjny: [BRAK DANYCH]); brak daty rozpoczęcia, więc nie da się wskazać dat granicznych (okno sprzeciwu).
**Skutek:** Przy rzeczywistej umowie — ryzyko co do reprezentacji i terminów.
**Rekomendacja (preferowana):** Uzupełnić dane i weryfikować reprezentację z KRS.
**Fallback (minimum akceptowalne):** j.w.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### Obszary bez zastrzeżeń / n/d

- Reprezentacja: ryzyko 14 (brak danych, nie można ocenić).
- Tytuł prawny i przekwalifikowanie: usługa rozwoju oprogramowania w T&M (usługi nieuregulowane, art. 750 KC [NIEZWERYFIKOWANE]); brak sygnałów przekwalifikowania na umowę o pracę; brak zastrzeżeń poza niedopasowaniem kar do modelu (ryzyko 6).
- Norma bezwzględna (art. 473 § 2 KC, art. 483 § 1 KC [NIEZWERYFIKOWANE]): umowa nie wyłącza wprost winy umyślnej ani nie zastrzega kary od zobowiązania pieniężnego; brak trafienia ius cogens. Skan mikroprzedsiębiorcy (art. 385^5 KC [NIEZWERYFIKOWANE]): obie strony to spółki kapitałowe — n/d.
- Pozostałe obszary objęte ryzykami powyżej.

---

## OCENA BEZPIECZEŃSTWA: 18/100

Cztery ryzyka krytyczne (po ok. 15-20 pkt), pięć wysokich i trzy średnie dają ocenę w paśmie „niebezpieczna". Cap pozorny, kary otwarte, zakaz konkurencji o wartości 300.000 zł za przypadek i brak tytułu do kodu to problemy, które nie wymagają kosmetyki, tylko przebudowy.

**Werdykt:** NIE PODPISYWAĆ w obecnej formie (CZERWONY).

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
