```
konfiguracja: fable-skill
commit skilla: fa26dc0
przebieg: 1 z 1
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"
```

## AUDYT RYZYK — Umowa o zachowaniu poufności (NDA) HELIX SOFT sp. z o.o. / BALTIC CAPITAL S.A.

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie. Umowa nazywa się wzajemna, ale chroni wyłącznie informacje HELIX SOFT, a i tę ochronę gubi w chwili zakończenia negocjacji. Przed podpisem trzeba renegocjować okres poufności, definicje i konstrukcję kary.

**Tryb i założenia:** tryb PRAWNIK · tryb express (jeden przebieg, bez STOP-ów) · audyt neutralny (przy każdej fladze wskazana strona dotknięta) · brak `practice-profile.md`, więc stosuję domyślne wartości KTZR · brak MCP `legal-cite`, więc każdy przepis oznaczam [NIEZWERYFIKOWANE] · pamięć kancelarii (Krok 0) pominięta, bo polecenie zakazuje wychodzenia poza treść umowy.

**Oznaczenia stron w raporcie:** HELIX SOFT sp. z o.o. = „Strona Ujawniająca" (dalej: **Helix**); BALTIC CAPITAL S.A. = „Strona Otrzymująca" (dalej: **Baltic**). Role są przypisane w komparycji na stałe, do konkretnych spółek, a nie do funkcji pełnionej przy danym ujawnieniu. Z tego wynika większość wad opisanych niżej.

---

### 🧮 Rachunek ekspozycji

**Liczby wyciągnięte z umowy:** kara umowna 200.000 zł „za każde naruszenie" (§ 3 ust. 1) · kara Helix: 0 zł (§ 3 ust. 2) · okres obowiązywania: „przez okres prowadzenia Negocjacji" (§ 4 ust. 1), bez daty i bez okresu po zakończeniu · termin notyfikacji: „niezwłocznie" (§ 2 ust. 3) · termin zwrotu: „na żądanie" (§ 2 ust. 4). Wartości umowy ani planowanej inwestycji umowa nie podaje.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | NDA bez wynagrodzenia; wartość inwestycji nieznana | — | [BRAK DANYCH] |
| Cap nominalny (Baltic) | brak limitu | — | **brak capu** |
| Kara za 1 naruszenie (Baltic) | 200.000 zł | 200.000 × 1 | 200.000 zł |
| Kumulacja kar (Baltic) — bez sufitu | 200.000 zł × n naruszeń | scenariusze (założenie: n = liczba odrębnie policzonych naruszeń): n = 3 → 600.000 zł · n = 5 → 1.000.000 zł · n = 10 → 2.000.000 zł | **200.000 zł × n, bez górnej granicy** |
| Odszkodowanie poza karą (Baltic) | brak zastrzeżenia odszkodowania uzupełniającego | za naruszenia objęte karą: tylko kara (art. 484 § 1 KC [NIEZWERYFIKOWANE]); za naruszenia spoza zakresu kary (np. § 2 ust. 1, ust. 3, ust. 4, jeśli nie są „obowiązkiem poufności"): odszkodowanie na zasadach ogólnych (art. 471 KC [NIEZWERYFIKOWANE]) bez limitu | bez limitu |
| Efektywna ekspozycja Baltic | — | 200.000 zł × n + odszkodowanie ogólne bez limitu | **nieograniczona** |
| Maks. odzysk Helix za 1 naruszenie objęte karą | 200.000 zł | brak zastrzeżenia odszkodowania uzupełniającego → szkoda ponad karę nie podlega naprawieniu (art. 484 § 1 KC [NIEZWERYFIKOWANE]) | **200.000 zł, niezależnie od rozmiaru szkody** |
| Ekspozycja Helix | § 3 ust. 2: brak kar; § 2 nie nakłada na Helix żadnego obowiązku | kary: 0 zł; obowiązki: 0 z 4 | **0 zł** |
| Asymetria kar | Baltic: 200.000 zł × n · Helix: 0 zł | 200.000 × n : 0 | **stosunek nieokreślony (∞)** |
| Asymetria obowiązków | § 2 ust. 1–4: 4 obowiązki | Baltic 4 : Helix 0 | 4 : 0 |
| Okres poufności po zakończeniu Negocjacji | brak | 0 dni (punkt odniesienia KTZR dla NDA: 5 lat ≈ 1 826 dni) | **0 dni** |
| Koniec okresu obowiązywania | „okres prowadzenia Negocjacji"; pojęcie niezdefiniowane, brak mechanizmu stwierdzenia końca | data graniczna nieobliczalna | [BRAK DANYCH] |
| Data zawarcia | brak daty w komparycji | początek okresu nieustalony | [BRAK DANYCH] |
| Termin notyfikacji naruszenia | „niezwłocznie" | nie da się policzyć (punkt odniesienia KTZR: 72 h) | [BRAK DANYCH] |
| Termin zwrotu materiałów | „na żądanie" | brak liczby dni (punkt odniesienia KTZR: 7 dni roboczych) | [BRAK DANYCH] |

**Wniosek z rachunku:** ekspozycja jest skrajnie jednostronna. Baltic odpowiada bez sufitu (200.000 zł za każde naruszenie, przy nieustalonej regule liczenia naruszeń), Helix nie odpowiada wcale. Jednocześnie ochrona Helix ma dwa twarde ograniczenia: wygasa razem z Negocjacjami (0 dni po ich zakończeniu) i jest zamknięta kwotą 200.000 zł za naruszenie, bo umowa nie zastrzega odszkodowania uzupełniającego. Obie strony mają więc poważny, choć różny problem. Rachunek wspiera werdykt 🟥.

---

### Bramka ius cogens (R10)

- Kara umowna zabezpiecza zobowiązanie niepieniężne (poufność), więc nie narusza art. 483 § 1 KC [NIEZWERYFIKOWANE] ✓
- Umowa nie wyłącza miarkowania kary (art. 484 § 2 KC [NIEZWERYFIKOWANE]) ✓
- Umowa nie wyłącza odpowiedzialności za winę umyślną (art. 473 § 2 KC [NIEZWERYFIKOWANE]) ✓
- Brak modyfikacji terminów przedawnienia, przeniesienia praw autorskich, terminów zapłaty ✓
- **Trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]): nieaktywny.** Obie strony to spółki kapitałowe (sp. z o.o., S.A.).
- **Test kumulatywny (art. 353¹ KC w zw. z art. 58 § 2 KC [NIEZWERYFIKOWANE]):** deklaracja wzajemności (§ 1 ust. 1) w połączeniu z jednostronną definicją (§ 1 ust. 2), jednostronnymi obowiązkami (§ 2) i wyraźnym zwolnieniem Helix z kar (§ 3 ust. 2) daje systemową asymetrię. Między profesjonalistami, przy umowie negocjowanej, nie przesądzam o nieważności. To wada konstrukcyjna do negocjacji, ujęta niżej jako 🟠 nr 1.

**Wynik bramki:** brak trafień w katalog norm bezwzględnie obowiązujących. Werdykt 🟥 wynika z ryzyka krytycznego, nie z nieważności.

---

### 🔴 RYZYKA KRYTYCZNE

#### 1. Poufność wygasa razem z Negocjacjami, bez okresu po ich zakończeniu — § 4 ust. 1 (w zw. z § 1, § 2)
**Strona dotknięta:** Helix (przede wszystkim). Baltic pośrednio, bo nie wie, kiedy obowiązek się kończy.
**Opis:** „Umowa obowiązuje przez okres prowadzenia Negocjacji." Umowa nie przewiduje żadnego okresu poufności po zakończeniu rozmów ani rozróżnienia między tajemnicą przedsiębiorstwa a pozostałymi informacjami. Do tego „Negocjacje" nie mają definicji (zob. 🟠 nr 2), więc nie wiadomo, kiedy się kończą (zerwanie rozmów? brak kontaktu przez X dni? zawarcie umowy inwestycyjnej?). Brak też daty zawarcia, a więc i początku okresu.
**Skutek:** jeśli negocjacje inwestycyjne się nie powiodą, Baltic zostaje z pełnym obrazem Helix (dane finansowe, technologia, klienci), a z chwilą ich zakończenia odpada obowiązek poufności, ograniczenie celu wykorzystania (§ 2 ust. 1), obowiązek zwrotu (§ 2 ust. 4) i kara 200.000 zł (§ 3). Ochrona kończy się dokładnie wtedy, gdy ryzyko wykorzystania informacji jest najwyższe. Pozostaje ustawowa ochrona tajemnicy przedsiębiorstwa (art. 11 u.z.n.k. [NIEZWERYFIKOWANE]), która wymaga wykazania jej przesłanek, w tym podjętych działań ochronnych, i nie daje kary umownej. Rachunek: 0 dni ochrony po zakończeniu, wobec 5 lat w standardzie KTZR.
**Rekomendacja (preferowana):** poufność przez czas trwania Umowy i 5 lat od zakończenia Negocjacji, niezależnie od przyczyny. Dla tajemnicy przedsiębiorstwa ochrona bezterminowa. Zdefiniować zdarzenie kończące Negocjacje, np. pisemne oświadczenie którejkolwiek Strony o ich zakończeniu albo zawarcie umowy inwestycyjnej. Dodać datę zawarcia i objąć ochroną informacje przekazane przed tą datą (retroaktywność).
**Fallback (minimum akceptowalne):** 3 lata po zakończeniu Negocjacji dla wszystkich Informacji Poufnych, z wyraźnym zastrzeżeniem, że obowiązek zwrotu lub usunięcia i kara umowna przeżywają zakończenie Umowy.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR — 5 lat; Poufność techniczna — 10 lat + bezterminowo dla tajemnicy przedsiębiorstwa; Zobowiązanie jednostronne — retroaktywność)

---

### 🟠 RYZYKA WYSOKIE

#### 1. Pozorna wzajemność: umowa chroni wyłącznie informacje Helix — § 1 ust. 1 vs § 1 ust. 2, § 2, § 3 ust. 2
**Strona dotknięta:** Baltic.
**Opis:** § 1 ust. 1 deklaruje: „Strony wzajemnie zobowiązują się do zachowania w poufności Informacji Poufnych przekazanych w związku z Negocjacjami." Jednak według definicji (§ 1 ust. 2) „Informacje Poufne oznaczają wszelkie informacje przekazane przez Stronę Ujawniającą", a Stroną Ujawniającą jest na stałe Helix. Wszystkie obowiązki z § 2 obciążają tylko Stronę Otrzymującą (Baltic), a § 3 ust. 2 wprost stanowi: „Strona Ujawniająca nie ponosi kar umownych na podstawie niniejszej Umowy." Literalnie § 1 ust. 1 zobowiązuje Helix do poufności co do jego własnych informacji, co nie ma sensu gospodarczego i otwiera spór o wykładnię (art. 65 § 2 KC [NIEZWERYFIKOWANE]).
**Skutek:** informacje, które Baltic przekaże w negocjacjach (warunki oferty, wycena, struktura finansowania, tożsamość współinwestorów, sam fakt zainteresowania inwestycją), nie są Informacjami Poufnymi w rozumieniu Umowy. Helix może je np. pokazać konkurencyjnym inwestorom bez sankcji (kara 0 zł). Baltic zostaje z ochroną ustawową przy negocjacjach (art. 72¹ KC [NIEZWERYFIKOWANE]), ale tylko gdy wyraźnie zastrzeże poufność, i bez kary umownej. Rachunek asymetrii: kary 200.000 zł × n : 0 zł, obowiązki 4 : 0.
**Rekomendacja (preferowana):** przebudować NDA na rzeczywiście wzajemne. Role „Strony Ujawniającej" i „Strony Otrzymującej" mają odnosić się do funkcji przy danym ujawnieniu („każda ze Stron, w zakresie, w jakim ujawnia / otrzymuje informacje"), a nie do konkretnej spółki. Obowiązki z § 2 i kara z § 3 mają obciążać obie Strony jednakowo. Skreślić § 3 ust. 2.
**Fallback (minimum akceptowalne):** jeżeli Helix nie zgodzi się na pełną symetrię: odrębna, węższa kategoria informacji Baltic (warunki oferty, fakt i treść rozmów) objęta tymi samymi obowiązkami, z karą w niższej wysokości.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR; zakres „sam fakt prowadzenia rozmów, jak również ich treść"), `references/baza-klauzul/10-kary-umowne.md` (NDA IT KTZR — „Strona naruszająca")

#### 2. Pojęcia pisane wielką literą bez definicji: „Negocjacje", „Materiały Robocze" — § 1 ust. 1–2, § 2 ust. 1, § 2 ust. 4, § 4 ust. 1
**Strona dotknięta:** obie Strony. Helix traci pewność co do zakresu i czasu ochrony, Baltic co do granic dozwolonego wykorzystania.
**Opis:** preambuła mówi tylko o „planowanymi negocjacjami inwestycyjnymi" (małą literą, bez „dalej: „Negocjacje""). Na niezdefiniowanym pojęciu „Negocjacje" opierają się trzy kluczowe elementy: zakres Informacji Poufnych (§ 1 ust. 2), dozwolony cel wykorzystania (§ 2 ust. 1: „wyłącznie w celu prowadzenia Negocjacji") i czas trwania Umowy (§ 4 ust. 1). „Materiały Robocze" (§ 2 ust. 4) nie mają definicji ani związku z „Informacjami Poufnymi". Narusza to Złotą Regułę 1.
**Skutek:** spór o to, jaka inwestycja jest przedmiotem rozmów (bezpośrednia w Helix? w spółkę zależną? inne transakcje?), czy informacja przekazana przy innej okazji jest chroniona, kiedy rozmowy się skończyły, co podlega zwrotowi. Każda z tych niejasności bezpośrednio przekłada się na to, czy kara 200.000 zł w ogóle się należy.
**Rekomendacja (preferowana):** zdefiniować „Negocjacje" (przedmiot planowanej transakcji, strony, początek, zdarzenia kończące) oraz „Materiały Robocze" jako wszelkie notatki, analizy, kompilacje i inne materiały sporządzone przez Stronę Otrzymującą na podstawie Informacji Poufnych lub je zawierające. Zastrzec domniemanie poufności w razie wątpliwości.
**Fallback (minimum akceptowalne):** definicja „Negocjacji" w preambule („dalej: „Negocjacje"") z opisem planowanej transakcji i objęcie zwrotem z § 2 ust. 4 wprost „Informacji Poufnych oraz Materiałów Roboczych".
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`, `references/baza-klauzul/02-preambuly.md`, `references/baza-klauzul/09-poufnosc.md` (Poufność techniczna — domniemanie poufności)

#### 3. Brak wyłączeń spod Informacji Poufnych przy definicji „wszelkie informacje" — § 1 ust. 2
**Strona dotknięta:** Baltic.
**Opis:** definicja obejmuje „wszelkie informacje" przekazane w związku z Negocjacjami i nie zawiera żadnego wyłączenia: informacje publicznie dostępne, znane Stronie Otrzymującej wcześniej, opracowane niezależnie, uzyskane od osoby trzeciej bez obowiązku poufności, ujawnienia wymagane przepisami prawa lub żądaniem sądu albo organu.
**Skutek:** formalnie naruszeniem jest posłużenie się informacją publiczną albo ujawnienie wymuszone przez sąd, organ nadzoru lub przepisy (w tym obowiązki informacyjne, jakie może mieć spółka akcyjna), a każde takie zdarzenie to potencjalnie 200.000 zł. Baltic może się bronić tym, że nie odpowiada za okoliczności, za które nie ponosi odpowiedzialności (art. 471 KC [NIEZWERYFIKOWANE]), ale ciężar sporu spada na niego. Brak też podziału ciężaru dowodu wyłączeń.
**Rekomendacja (preferowana):** standardowy katalog pięciu wyłączeń z bazy KTZR, ciężar dowodu wyłączeń po stronie Strony Otrzymującej (dla równowagi), procedura ujawnienia wymaganego prawem: uprzednie powiadomienie Strony Ujawniającej, o ile przepisy tego nie zakazują, i ujawnienie w minimalnym zakresie.
**Fallback (minimum akceptowalne):** co najmniej wyłączenia (a) informacje publiczne bez naruszenia Umowy i (e) ujawnienie wymagane przepisami prawa lub prawomocnym orzeczeniem albo decyzją organu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR — wyłączenia (a)–(e) z ciężarem dowodu)

#### 4. Brak kręgu osób uprawnionych do dostępu i obowiązku ich związania — § 2
**Strona dotknięta:** obie Strony. Baltic: ryzyko kary za zwykłą obsługę transakcji. Helix: brak łańcucha poufności.
**Opis:** umowa nie mówi, komu Strona Otrzymująca może udostępnić Informacje Poufne: pracownikom, członkom organów, komitetowi inwestycyjnemu, doradcom prawnym i finansowym, audytorom, bankowi finansującemu, podmiotom powiązanym. Nie nakłada też obowiązku związania tych osób poufnością ani nie przesądza odpowiedzialności za nie.
**Skutek:** dla Baltic: przy literalnej wykładni każde przekazanie informacji doradcy przy due diligence może zostać uznane za naruszenie, czyli 200.000 zł za każde (zob. 🟠 nr 5). Dla Helix: informacje trafiają do nieoznaczonego kręgu osób trzecich bez obowiązku ich zobowiązania. Odpowiedzialność Baltic za osoby, którymi się posługuje, wynika wprawdzie z art. 474 KC [NIEZWERYFIKOWANE], ale nie obejmuje ona samodzielnych doradców działających na własny rachunek w każdej konfiguracji.
**Rekomendacja (preferowana):** dozwolone ujawnienie wyłącznie osobom, których udział w Negocjacjach jest niezbędny (zasada „need to know"), po zobowiązaniu ich do poufności co najmniej w zakresie Umowy (lub gdy podlegają ustawowej tajemnicy zawodowej). Strona Otrzymująca odpowiada za ich naruszenia jak za własne.
**Fallback (minimum akceptowalne):** zamknięta lista kategorii odbiorców (pracownicy, członkowie organów, doradcy profesjonalni związani tajemnicą zawodową) z obowiązkiem poinformowania ich o poufności.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (Klauzula wzorcowa, pkt (c); Body Leasing — związanie Specjalistów odrębnym NDA)

#### 5. Kara 200.000 zł „za każde naruszenie" bez sufitu i bez reguły liczenia naruszeń — § 3 ust. 1
**Strona dotknięta:** Baltic.
**Opis:** „W przypadku naruszenia obowiązku poufności Strona Otrzymująca zapłaci Stronie Ujawniającej karę umowną w wysokości 200.000 zł za każde naruszenie." Umowa nie mówi, co jest jednym naruszeniem (jedno zdarzenie? każdy dokument? każdy odbiorca? każdy dzień trwania?), i nie ustala łącznego limitu kar.
**Skutek:** jedno zdarzenie, np. wysłanie data roomu pięciu osobom, może być liczone jako 1 albo jako 5 naruszeń, czyli 200.000 zł albo 1.000.000 zł. Przy n = 10: 2.000.000 zł. Ekspozycja Baltic nie ma górnej granicy. Pozostaje miarkowanie (art. 484 § 2 KC [NIEZWERYFIKOWANE]), ale to uprawnienie sądu, nie automat.
**Rekomendacja (preferowana):** reguła liczenia („za każdy przypadek naruszenia, przy czym naruszenia wynikające z jednego zdarzenia lub z ciągu powiązanych działań traktuje się jako jeden przypadek") i łączny limit kar, np. 3 × kara jednostkowa.
**Fallback (minimum akceptowalne):** sama reguła liczenia naruszeń (jedno zdarzenie = jedna kara), bez łącznego limitu.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md` (NDA IT KTZR — „za każdy przypadek naruszenia"; red flag: brak capów na kary)

#### 6. Brak odszkodowania uzupełniającego i niejasny zakres kary („obowiązek poufności") — § 3 ust. 1
**Strona dotknięta:** Helix.
**Opis:** (a) Umowa nie zastrzega prawa do dochodzenia odszkodowania przenoszącego wysokość kary. (b) Kara dotyczy „naruszenia obowiązku poufności", a § 2 rozróżnia kilka obowiązków: ograniczenie celu wykorzystania (ust. 1), zabezpieczenie (ust. 2), notyfikację (ust. 3), zwrot (ust. 4). Wykorzystanie informacji do innego celu bez ich ujawnienia, np. przy inwestycji w konkurenta Helix, nie musi zostać uznane za naruszenie „obowiązku poufności".
**Skutek:** (a) przy szkodzie przewyższającej karę, np. utracie wartości technologii albo przejęciu klientów, odzysk Helix jest zamknięty kwotą 200.000 zł za naruszenie (art. 484 § 1 KC [NIEZWERYFIKOWANE]). (b) Najbardziej prawdopodobne w transakcji inwestycyjnej naruszenie, czyli wykorzystanie wiedzy z due diligence, może w ogóle nie być objęte karą i wymagać dowodu szkody na zasadach ogólnych.
**Rekomendacja (preferowana):** „Zapłata kary umownej nie wyłącza prawa do dochodzenia odszkodowania uzupełniającego na zasadach ogólnych" oraz objęcie karą naruszenia któregokolwiek z obowiązków z § 2, w szczególności wykorzystania Informacji Poufnych w innym celu niż Negocjacje.
**Fallback (minimum akceptowalne):** odszkodowanie uzupełniające przy winie umyślnej lub rażącym niedbalstwie, a zakres kary rozszerzony co najmniej o naruszenie § 2 ust. 1.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md` (NDA IT KTZR — odszkodowanie uzupełniające)

---

### 🟡 RYZYKA ŚREDNIE

#### 1. „Dołoży starań" zamiast zobowiązania z miernikiem staranności — § 2 ust. 2
**Strona dotknięta:** Helix.
**Opis:** „Strona Otrzymująca dołoży starań, aby zabezpieczyć Informacje Poufne przed dostępem osób trzecich." To zobowiązanie starannego działania bez miernika: nie wiadomo, jakich starań, w jakim standardzie.
**Skutek:** przy wycieku Baltic wykaże, że „starał się", a Helix musi udowodnić niedołożenie starań. Trudniej o karę i odszkodowanie.
**Rekomendacja (preferowana):** „zobowiązuje się zabezpieczyć… stosując co najmniej taką samą staranność, z jaką chroni własne informacje poufne, jednak nie mniejszą niż należyta staranność wymagana od profesjonalisty".
**Fallback (minimum akceptowalne):** „z należytą starannością" (art. 355 § 2 KC [NIEZWERYFIKOWANE]) zamiast „dołoży starań".
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR — miernik staranności)

#### 2. Notyfikacja „niezwłocznie", tylko o „ujawnieniu", bez współpracy — § 2 ust. 3
**Strona dotknięta:** Helix.
**Opis:** obowiązek „niezwłocznie poinformuje Stronę Ujawniającą o każdym przypadku ujawnienia Informacji Poufnych" nie ma terminu liczonego w godzinach lub dniach, nie obejmuje utraty, kradzieży, nieuprawnionego dostępu ani uzasadnionego podejrzenia naruszenia, nie określa formy i nie przewiduje obowiązku współpracy przy ograniczaniu skutków. Nie wiadomo też, czy chodzi o ujawnienie nieuprawnione, czy każde (także dozwolone).
**Skutek:** spór o to, czy notyfikacja po tygodniu była „niezwłoczna". Helix dowiaduje się o incydencie za późno, by ograniczyć szkodę. Rachunek: [BRAK DANYCH] (punkt odniesienia KTZR: 72 h).
**Rekomendacja (preferowana):** pisemne powiadomienie nie później niż w ciągu 72 godzin od powzięcia informacji o nieuprawnionym ujawnieniu, utracie, kradzieży lub uzasadnionym podejrzeniu naruszenia, z obowiązkiem współpracy przy ograniczeniu skutków.
**Fallback (minimum akceptowalne):** termin 5 dni roboczych w formie dokumentowej.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR — 72 h; Poufność techniczna — 24 h)

#### 3. Zwrot ograniczony do „Materiałów Roboczych", bez usunięcia, terminu i potwierdzenia — § 2 ust. 4
**Strona dotknięta:** Helix (zakres i egzekwowalność zwrotu). Baltic (brak wyjątku dla kopii, które musi zachować).
**Opis:** „Materiały Robocze podlegają zwrotowi na żądanie." Zwrot nie obejmuje wprost samych Informacji Poufnych ani ich kopii elektronicznych, nie ma obowiązku trwałego usunięcia z systemów, terminu, pisemnego potwierdzenia ani automatyzmu po zakończeniu Negocjacji. Obowiązek wygasa razem z Umową (§ 4), więc żądanie zgłoszone po zakończeniu rozmów może być bezskuteczne. Z drugiej strony brak wyjątku dla kopii, które Strona Otrzymująca musi zachować na podstawie przepisów (archiwizacja, kopie zapasowe).
**Skutek:** po nieudanych negocjacjach Helix nie ma skutecznego narzędzia odzyskania lub usunięcia danych. Baltic ryzykuje zarzut naruszenia, jeśli zachowa kopie wymagane prawem.
**Rekomendacja (preferowana):** zwrot lub trwałe usunięcie wszystkich Informacji Poufnych i Materiałów Roboczych w terminie 7 dni roboczych od zakończenia Negocjacji lub od żądania, z pisemnym potwierdzeniem. Wyjątek: kopie, których zachowania wymagają przepisy, nadal objęte poufnością. Obowiązek przeżywa rozwiązanie Umowy.
**Fallback (minimum akceptowalne):** zwrot lub usunięcie na żądanie w terminie 14 dni, z potwierdzeniem w formie dokumentowej.
**Klauzula z bazy:** `references/baza-klauzul/18-zwrot-materialow.md` (NDA IT KTZR)

#### 4. Brak zastrzeżenia braku obowiązku zawarcia umowy inwestycyjnej i braku licencji — cała Umowa
**Strona dotknięta:** obie Strony (głównie Baltic co do obowiązku kontraktowania, Helix co do praw do informacji).
**Opis:** umowa nie stanowi, że jej zawarcie nie zobowiązuje do zawarcia umowy inwestycyjnej ani do kontynuowania rozmów, ani że przekazanie informacji nie oznacza udzielenia licencji ani przejścia praw do technologii Helix.
**Skutek:** pole do sporu, czy zerwanie rozmów było sprzeczne z dobrymi obyczajami (art. 72 § 2 KC [NIEZWERYFIKOWANE]), oraz do argumentu, że udostępnienie materiałów objętych prawami autorskimi lub know-how upoważniało do korzystania z nich.
**Rekomendacja (preferowana):** dwa zdania z bazy KTZR: „Żadna ze Stron nie jest wskutek zawarcia Umowy zobligowana do zawarcia umowy ani do prowadzenia dalszych rozmów" oraz „Umowa nie skutkuje przejściem jakichkolwiek praw… ani nie oznacza udzielenia licencji".
**Fallback (minimum akceptowalne):** sam zapis o braku licencji i przejścia praw.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (Zobowiązanie jednostronne — brak zobowiązania do kontraktowania)

#### 5. Brak klauzuli o narzędziach AI — cała Umowa (§ 2)
**Strona dotknięta:** Helix (oraz Baltic, jeśli jego informacje zostaną objęte ochroną).
**Opis:** umowa nie reguluje wprowadzania Informacji Poufnych do narzędzi AI. Wklejenie dokumentacji z due diligence do publicznego chatbota trenującego na danych użytkownika nie jest przy tym brzmieniu oczywistym „ujawnieniem osobie trzeciej".
**Skutek:** informacja realnie wychodzi spod kontroli stron, a kwalifikacja tego jako naruszenia (i podstawy kary 200.000 zł) jest sporna.
**Rekomendacja (preferowana):** dwuczłonowa klauzula KTZR: narzędzia zewnętrzne tylko przy wyłączonym trenowaniu na danych, modele własne — bezwzględny zakaz trenowania na Informacjach Poufnych.
**Fallback (minimum akceptowalne):** zakaz wprowadzania Informacji Poufnych do narzędzi AI, których dostawca wykorzystuje dane do trenowania modeli.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (Klauzula AI w NDA — zakaz karmienia modeli)

#### 6. Komparycja niekompletna: brak daty i miejsca zawarcia, KRS/NIP, reprezentacji i podpisów — komparycja
**Strona dotknięta:** obie Strony.
**Opis:** umowa nie ma daty ani miejsca zawarcia, numerów KRS i NIP, wskazania osób reprezentujących i podstawy ich umocowania ani bloku podpisów (Złota Reguła 8). Dane spółek oznaczono jako fikcyjne, ale brak elementów jest konstrukcyjny, nie tylko danych.
**Skutek:** brak daty uniemożliwia ustalenie początku obowiązywania, a przy § 4 również końca. Brak umocowania rodzi ryzyko zarzutu działania bez umocowania przy dochodzeniu kary.
**Rekomendacja (preferowana):** pełna komparycja (nazwa, siedziba, KRS, NIP, REGON, reprezentanci i podstawa umocowania), data i miejsce zawarcia, blok podpisów.
**Fallback (minimum akceptowalne):** data zawarcia, KRS oraz imiona i nazwiska osób podpisujących z funkcją.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

---

### 🟢 RYZYKA NISKIE

#### 1. Jednostronna i nieprecyzyjna klauzula sądu — § 5 ust. 2
**Strona dotknięta:** Baltic.
**Opis:** „sądem właściwym jest sąd siedziby Strony Ujawniającej", czyli zawsze sąd właściwy dla Helix (Gdynia), także w sporze o informacje Baltic, gdyby zostały objęte ochroną. Sformułowanie „sąd siedziby" nie mówi o właściwości miejscowej sądu „właściwego dla siedziby". Przy roszczeniu z jednej kary (200.000 zł) właściwy rzeczowo będzie sąd okręgowy (art. 17 pkt 4 KPC [NIEZWERYFIKOWANE]).
**Skutek:** przy bliskości siedzib (Gdynia–Sopot) obciążenie praktyczne niewielkie. Ryzyko sporu o właściwość jest marginalne.
**Rekomendacja (preferowana):** „sąd powszechny właściwy miejscowo dla siedziby pozwanego" albo dla siedziby Strony, której Informacje Poufne dotyczą.
**Fallback (minimum akceptowalne):** pozostawić sąd właściwy dla siedziby Helix, poprawiając brzmienie na „sąd powszechny właściwy dla siedziby".
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

#### 2. Niekompletne postanowienia końcowe: doręczenia, cesja, klauzula salwatoryjna — § 5
**Strona dotknięta:** obie Strony.
**Opis:** brak klauzuli doręczeń z rygorem skuteczności (zasada KTZR: nie wolno jej pominąć), zakazu cesji bez zgody i klauzuli salwatoryjnej.
**Skutek:** spór o skuteczność doręczenia wezwania do zapłaty kary lub żądania zwrotu. Możliwość przeniesienia praw z Umowy, w tym roszczenia o karę, na podmiot trzeci.
**Rekomendacja (preferowana):** dodać klauzulę doręczeń (adresy, obowiązek zawiadomienia o zmianie, rygor skuteczności), zakaz cesji bez pisemnej zgody i klauzulę salwatoryjną z bazy NDA IT KTZR.
**Fallback (minimum akceptowalne):** sama klauzula doręczeń.
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md` (Zasada KTZR — doręczenia; NDA IT KTZR — cesja, salwatoryjna)

#### 3. Brak określenia roli Stron przy danych osobowych — cała Umowa
**Strona dotknięta:** obie Strony.
**Opis:** materiały z negocjacji inwestycyjnych zwykle zawierają dane osobowe (pracownicy, kluczowi współpracownicy, klienci Helix). Umowa nie określa, w jakiej roli Baltic je przetwarza.
**Skutek:** niejasność, czy potrzebna jest umowa powierzenia. W typowym układzie Baltic będzie odrębnym administratorem, więc ryzyko jest raczej porządkowe niż sankcyjne.
**Rekomendacja (preferowana):** zapis, że Strona Otrzymująca przetwarza dane zawarte w Informacjach Poufnych jako odrębny administrator, wyłącznie w celu Negocjacji, z zasadą minimalizacji (np. dane zanonimizowane w data roomie).
**Fallback (minimum akceptowalne):** sam zapis o roli odrębnego administratora i ograniczeniu celu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (Zobowiązanie jednostronne — rola przy danych osobowych), `references/checklist-dpa-art28.md` (kwalifikacja ról)

---

### Bramka kompletności (R9) — dziewięć obszarów

| Obszar | Status |
|---|---|
| Odpowiedzialność i kary | ⚠️ 🟠 nr 5, 🟠 nr 6 (oraz asymetria — 🟠 nr 1) |
| Prawa autorskie | — n/d co do przeniesienia praw; brak zastrzeżenia braku licencji ujęty w 🟡 nr 4 |
| Definicje i logika | ⚠️ 🟠 nr 1, 🟠 nr 2, 🟠 nr 3 |
| Reprezentacja | ⚠️ 🟡 nr 6 |
| Wypowiedzenie i exit | ⚠️ 🔴 nr 1 (koniec obowiązywania), 🟡 nr 3 (zwrot) |
| RODO | ⚠️ 🟢 nr 3 |
| Tytuł prawny i przekwalifikowanie | — n/d (NDA między spółkami kapitałowymi, bez świadczenia pracy) |
| Poufność | ⚠️ 🔴 nr 1, 🟠 nr 3, 🟠 nr 4, 🟡 nr 1, 🟡 nr 2, 🟡 nr 5 |
| Spory | ⚠️ 🟢 nr 1; ✓ prawo polskie jako właściwe — brak zastrzeżeń |

**Skan antywzorców językowych:** „dołoży starań" (§ 2 ust. 2) → 🟡 nr 1 · „niezwłocznie" (§ 2 ust. 3) → 🟡 nr 2 · „wzajemnie" przy obowiązkach i sankcjach jednej strony (§ 1 ust. 1, § 3 ust. 2) → 🟠 nr 1 · pojęcia pisane wielką literą bez definicji („Negocjacje", „Materiały Robocze") → 🟠 nr 2 · „wszelkie informacje" (§ 1 ust. 2) → 🟠 nr 3.

**Spójność odesłań:** umowa nie zawiera odesłań wewnętrznych ani załączników. Złote Reguły 3 i 4 bez zastrzeżeń. Kryteria automatycznego uruchomienia workflow weryfikacji odesłań nie są spełnione.

### ✓ Obszary bez zastrzeżeń

Bramka ius cogens: brak trafień · Prawo właściwe (§ 5 ust. 2): prawo polskie, brak zastrzeżeń · Forma zmian (§ 5 ust. 1): forma pisemna pod rygorem nieważności, brak zastrzeżeń · Dopuszczalność kary umownej co do zasady (zobowiązanie niepieniężne): brak zastrzeżeń.

---

## OCENA BEZPIECZEŃSTWA: 32/100

Rachunek: 100 − 18 (🔴 × 1) − 36 (🟠 × 6 po 6 pkt) − 12 (🟡 × 6 po 2 pkt) − 1,5 (🟢 × 3 po 0,5 pkt) ≈ 32. O ocenie przesądziły dwie wady konstrukcyjne: poufność kończy się z chwilą zakończenia Negocjacji, a deklarowana wzajemność jest pozorna, bo całe ryzyko jest po stronie Baltic, a cała ochrona po stronie Helix. Do tego dochodzą niezdefiniowane „Negocjacje", od których zależy zakres, cel i czas Umowy. Każda strona ma tu inny, ale realny problem.

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI (🟥 CZERWONY — nie podpisywać w obecnej formie)

---

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (poufność wygasa z Negocjacjami)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` — NDA IT KTZR (5 lat od zakończenia rozmów) lub model warstwowy z Poufności technicznej (10 lat / bezterminowo dla tajemnicy przedsiębiorstwa); retroaktywność z sekcji „Zobowiązanie jednostronne"

🟠 RYZYKO 1 (pozorna wzajemność)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` + `references/baza-klauzul/10-kary-umowne.md` — NDA IT KTZR z karą dla „Strony naruszającej"

🟠 RYZYKO 2 (definicje)
→ Zastosuj: `references/baza-klauzul/03-definicje.md`, `references/baza-klauzul/02-preambuly.md`

🟠 RYZYKO 3 (wyłączenia)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` — NDA IT KTZR, wyłączenia (a)–(e) z ciężarem dowodu

🟠 RYZYKA 5–6 (konstrukcja kary)
→ Zastosuj: `references/baza-klauzul/10-kary-umowne.md` — NDA IT KTZR (za każdy przypadek + odszkodowanie uzupełniające), z dodaną regułą liczenia i limitem łącznym

🟡 RYZYKO 3 (zwrot materiałów)
→ Zastosuj: `references/baza-klauzul/18-zwrot-materialow.md` — NDA IT KTZR (7 dni roboczych, trwałe usunięcie, potwierdzenie)

### Miejsca, w których w trybie standardowym zatrzymałbym się na decyzję (R6)

1. **Dla której strony pracujemy?** Audyt jest neutralny. Przy mandacie Helix priorytetem są 🔴 nr 1, 🟠 nr 2 i 🟠 nr 6, a symetryzacji (🟠 nr 1) można bronić jako ustępstwa. Przy mandacie Baltic priorytetem są 🟠 nr 1, 🟠 nr 3, 🟠 nr 4 i 🟠 nr 5.
2. **Wysokość kary i limit łączny:** przy braku danych o wartości inwestycji ([BRAK DANYCH]) nie da się ocenić, czy 200.000 zł jest kwotą adekwatną. Potrzebna decyzja biznesowa.
3. **Długość okresu poufności po zakończeniu Negocjacji:** 3, 5 czy 10 lat oraz czy wydzielamy tajemnicę przedsiębiorstwa jako bezterminową.
4. **Brak `practice-profile.md`:** zastosowano domyślne progi KTZR. Do rozważenia jednorazowe uruchomienie `workflows/konfiguracja-kancelarii.md`.

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
