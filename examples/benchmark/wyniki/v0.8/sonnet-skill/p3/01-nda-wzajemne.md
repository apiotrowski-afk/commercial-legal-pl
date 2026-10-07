konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 3 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express; audyt neutralny; brak MCP legal-cite — każde powołanie przepisu oznaczono [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa o zachowaniu poufności (NDA) HELIX SOFT sp. z o.o. / BALTIC CAPITAL S.A.

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; dwa ryzyka krytyczne (nieograniczona kara za każde naruszenie oraz ustanie poufności z końcem negocjacji bez okresu ochrony po nich) wymagają przeredagowania przed podpisem.

Role: HELIX SOFT = Strona Ujawniająca (dalej Helix), BALTIC CAPITAL = Strona Otrzymująca (dalej Baltic). Tytuł i § 1 ust. 1 deklarują wzajemność, ale konstrukcja ról jest jednokierunkowa.

### 🧮 Rachunek ekspozycji

Liczby i terminy z umowy: kara 200.000 zł „za każde naruszenie" (§ 3 ust. 1); kara Strony Ujawniającej: 0 zł (§ 3 ust. 2); okres obowiązywania: „okres prowadzenia Negocjacji" (§ 4 ust. 1); wartość umowy, cap, wynagrodzenie, termin wypowiedzenia, okres poufności po zakończeniu: brak.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy / wartość transakcji | brak | — | [BRAK DANYCH] |
| Cap nominalny | brak | — | [BRAK DANYCH] — brak sufitu kar i odpowiedzialności |
| Kara za 1 naruszenie (Baltic) | 200.000 zł | — | 200.000 zł |
| Kary maksymalne | „za każde naruszenie", bez sufitu, bez definicji „naruszenia" | założenie: n naruszeń × 200.000 zł; np. n = 5 (np. 5 przekazanych dokumentów lub 5 odbiorców) | 1.000.000 zł; n = 10 → 2.000.000 zł; wzrost liniowy, bez granicy |
| Kara Helix | § 3 ust. 2 | 0 zł × n | 0 zł |
| Asymetria (Baltic vs Helix) | kary 200.000 zł vs 0 zł | 200.000 / 0 | ∞ (kary wyłącznie po jednej stronie) |
| Odszkodowanie ponad karę | umowa milczy | art. 484 § 1 KC [NIEZWERYFIKOWANE]: bez zastrzeżenia — tylko kara | kara = jedyne roszczenie; Helix nie odzyska szkody powyżej 200.000 zł za naruszenie |
| Okres ochrony po zakończeniu Negocjacji | brak | 0 dni | 0 dni; data końca niemożliwa do wyliczenia (koniec „Negocjacji" nieokreślony) |
| Termin informowania o ujawnieniu | „niezwłocznie" (§ 2 ust. 3) | nieobliczalne | [BRAK DANYCH] — antywzorzec |

Wniosek: ekspozycja Baltic jest otwarta (liniowa, bez sufitu, minimum 200.000 zł już przy pierwszym naruszeniu); ekspozycja Helix wynika z braku ochrony po końcu negocjacji — po ich zakończeniu Baltic nie ponosi żadnej sankcji. Oba kierunki wskazują na CZERWONY.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara 200.000 zł „za każde naruszenie" bez sufitu, bez definicji naruszenia, jednostronna — § 3 ust. 1–2
**Strona dotknięta:** Baltic (płatnik kary); pośrednio Helix (kara jest jedynym roszczeniem — brak odszkodowania uzupełniającego).
**Opis:** Kara za „każde naruszenie" bez sufitu i bez określenia, czym jest jedno naruszenie (jeden dokument? jeden odbiorca? jedno zdarzenie?). Kara dotyczy wyłącznie Strony Otrzymującej (§ 3 ust. 2), choć § 1 ust. 1 deklaruje wzajemność. Kara nie rozróżnia naruszenia umyślnego od nieumyślnego ani drobnego od istotnego; tożsama stawka za zwłokę w informowaniu i za wyciek całości danych. Umowa nie przewiduje odszkodowania uzupełniającego, więc dla Helix kara jest limitem roszczeń (art. 484 § 1 KC [NIEZWERYFIKOWANE]).
**Skutek:** Baltic: kumulacja n × 200.000 zł (5 naruszeń = 1.000.000 zł); przy rażącym wygórowaniu możliwe miarkowanie przez sąd, ale to uprawnienie sądu, nie automat (art. 484 § 2 KC [NIEZWERYFIKOWANE]). Helix: realna szkoda z wycieku (np. ujawnienie know-how) może wielokrotnie przewyższyć 200.000 zł, bez możliwości dochodzenia reszty.
**Rekomendacja (preferowana):** kara za naruszenie zdefiniowane zdarzeniowo (np. „za każde zdarzenie naruszenia") ze sufitem łącznym, kara dwustronna (symetryczna wobec obu Stron jako odbiorców), z wyraźnym zastrzeżeniem odszkodowania uzupełniającego do wysokości szkody.
**Fallback:** kara jednostronna zostaje, ale z sufitem łącznym (np. wielokrotność jednej kary) oraz wyraźną definicją pojedynczego naruszenia.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `09-poufnosc.md`

#### 2. Poufność wygasa z końcem Negocjacji, bez okresu ochrony po nich — § 4 ust. 1
**Strona dotknięta:** Helix (jako ujawniający, w praktyce główny dysponent informacji); w razie ujawniania przez Baltic jego własnych informacji — także Baltic.
**Opis:** Umowa obowiązuje „przez okres prowadzenia Negocjacji". Nie ma okresu poufności po zakończeniu (tail), a moment zakończenia Negocjacji jest nieokreślony („Negocjacje" bez definicji). W dniu zerwania rozmów obowiązek poufności ustaje, a informacje (finansowe, technologiczne) pozostają u Baltic bez żadnej ochrony; sankcja z § 3 dotyczy naruszenia „obowiązku poufności", który już nie obowiązuje. Przesłanki wygaśnięcia nie da się wskazać datą.
**Skutek:** Helix traci ochronę dokładnie wtedy, gdy ryzyko jest największe (po nieudanych negocjacjach, gdy Baltic może mieć interes w wykorzystaniu informacji); brak uwzględnienia ochrony tajemnicy przedsiębiorstwa (ustawa o zwalczaniu nieuczciwej konkurencji [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** definicja „Negocjacji" i zdarzenia kończącego; obowiązek poufności przez określony okres po zakończeniu (np. kilka lat), a dla tajemnic przedsiębiorstwa bezterminowo do ich ujawnienia nie z winy Strony.
**Fallback:** stały okres po zakończeniu (np. 3 lata) dla wszystkich informacji.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (model warstwowy okresów)

### 🟠 RYZYKA WYSOKIE

#### 1. Pozorna wzajemność i jednostronna definicja Informacji Poufnych — § 1 ust. 1–2, § 3 ust. 2
**Strona dotknięta:** Baltic (jego własne informacje, np. dane o inwestorach i strategii, nie są chronione); Helix w zakresie asymetrycznych obowiązków pozostaje chroniony.
**Opis:** § 1 ust. 1: „Strony wzajemnie zobowiązują się", ale § 1 ust. 2 definiuje Informacje Poufne jako przekazane „przez Stronę Ujawniającą", a obowiązki z § 2 i kara z § 3 obciążają tylko Stronę Otrzymującą; role są przypisane na stałe. Antywzorzec „pozorna wzajemność". Informacje ujawniane przez Baltic nie są chronione.
**Skutek:** NDA nie spełnia deklarowanej funkcji wzajemnej; Baltic zostaje bez ochrony własnych danych, albo (jeśli strony miały zamiar wzajemności) spór interpretacyjny.
**Rekomendacja:** role zależne od kierunku przekazu („Strona Ujawniająca/Otrzymująca" w odniesieniu do każdego przekazu) i symetryczne obowiązki oraz kary, albo przyznanie wprost, że umowa jest jednostronna i usunięcie „wzajemnie".
**Fallback:** umowa jednostronna z wyraźną etykietą i wyważoną karą (zob. krytyczne 1).
**Klauzula z bazy:** `09-poufnosc.md`, `03-definicje.md`

#### 2. Brak wyłączeń z poufności i wyjątków dozwolonego ujawnienia — § 1–2
**Strona dotknięta:** Baltic (odpowiada karą za informacje publiczne, własne lub ujawniane z mocy prawa); Helix częściowo (spór o zakres).
**Opis:** Definicja obejmuje „wszelkie informacje" bez wyłączeń: informacje publiczne, znane Baltic wcześniej, niezależnie opracowane, uzyskane legalnie od osoby trzeciej, ujawnienie na żądanie organu lub z mocy prawa. Brak znakowania lub zakresu przedmiotowego.
**Skutek:** każda taka informacja to „Informacja Poufna"; jej użycie lub ujawnienie = naruszenie z karą 200.000 zł; obowiązek ujawnienia organom (np. nadzorczym lub sądowi) kolidowałby z karą.
**Rekomendacja:** standardowy katalog wyłączeń i wyjątek dla ujawnień wymaganych prawem z obowiązkiem uprzedniego powiadomienia.
**Fallback:** minimum: informacje publiczne i wcześniej posiadane.
**Klauzula z bazy:** `09-poufnosc.md`

#### 3. Miękki standard zabezpieczenia i nieoznaczony termin zgłoszenia — § 2 ust. 2–3
**Strona dotknięta:** Helix (słabe zobowiązanie ochronne); Baltic (niejasny trigger kary).
**Opis:** „Dołoży starań, aby zabezpieczyć" to zobowiązanie starannego działania zamiast rezultatu (antywzorzec „dołoży starań"), a „niezwłocznie" bez liczby dni (antywzorzec). Ponadto obowiązek zgłoszenia dotyczy tylko „ujawnienia", nie podejrzenia czy ryzyka. Niespójność: § 2 ust. 2 słabe, a § 3 karze każde naruszenie (z § 2 ust. 1 i ust. 3) bez wskazania, czy samo niedołożenie starań to naruszenie.
**Skutek:** Helix trudniej wykazać niewykonanie; Baltic nie wie, kiedy ponosi karę.
**Rekomendacja:** określony standard (np. środki co najmniej takie jak dla własnych informacji o najwyższej poufności), termin liczbowy (np. 24–48 godzin od powzięcia wiedzy), objęcie podejrzenia naruszenia.
**Fallback:** zachować „dołoży starań", ale z konkretnym terminem zgłoszenia.
**Klauzula z bazy:** `09-poufnosc.md`

#### 4. Niepełny exit: zwrot tylko „Materiałów Roboczych", na żądanie; brak zniszczenia — § 2 ust. 4
**Strona dotknięta:** Helix.
**Opis:** „Materiały Robocze" nie są zdefiniowane i nie wiadomo, czy to Informacje Poufne, notatki Baltic czy dokumenty Helix. Zwrot tylko na żądanie, bez terminu, bez usunięcia kopii, bez oświadczenia o zniszczeniu, bez wyjątku na kopie archiwalne.
**Skutek:** po zakończeniu rozmów Informacje Poufne pozostają u Baltic; w połączeniu z krytycznym 2 brak jakiejkolwiek kontroli.
**Rekomendacja:** definicja, zwrot/zniszczenie wszystkich nośników w określonym terminie od żądania lub zakończenia, oświadczenie na piśmie.
**Fallback:** zwrot lub zniszczenie na żądanie w terminie 14 dni.
**Klauzula z bazy:** `09-poufnosc.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. Pojęcia pisane wielką literą bez definicji — „Negocjacje", „Materiały Robocze" — § 1, § 2 ust. 4, § 4
**Strona dotknięta:** obie (Helix w zakresie czasu ochrony i zakresu zwrotu; Baltic w zakresie zakresu kary).
**Opis:** „Negocjacje" (cel, zakres, termin końca) i „Materiały Robocze" bez definicji; wprowadzenie zdawkowe („planowane negocjacje inwestycyjne"). Cel wykorzystania z § 2 ust. 1 oparty na nieokreślonym pojęciu.
**Rekomendacja:** słowniczek z definicjami i zdarzeniem kończącym Negocjacje.

#### 2. Brak katalogu osób uprawnionych do dostępu (doradcy, pracownicy, podmioty powiązane) — § 2
**Strona dotknięta:** Baltic (inwestor zwykle musi udostępniać informacje doradcom, komitetom, finansującym).
**Opis:** Umowa nie przewiduje dopuszczalnego udostępnienia osobom trzecim ani odpowiedzialności za nie; każde udostępnienie doradcy to potencjalne naruszenie z karą.
**Rekomendacja:** katalog „Osób Upoważnionych" związanych równoważnym obowiązkiem, odpowiedzialność Strony za ich działania.

#### 3. Forum: sąd siedziby Strony Ujawniającej — § 5 ust. 2
**Strona dotknięta:** Baltic (musi pozywać i bronić się w Gdyni).
**Opis:** Jednostronna jurysdykcja na korzyść Helix; przy wzajemnym NDA i zmiennych rolach rodzi niepewność, kto jest „Stroną Ujawniającą" w danym sporze. Prawo polskie bez zastrzeżeń.
**Rekomendacja:** sąd właściwy dla siedziby pozwanego lub sąd w stałej lokalizacji; ewentualnie mediacja.

#### 4. Brak danych identyfikujących strony i umocowania — komparycja
**Strona dotknięta:** obie.
**Opis:** Brak KRS, NIP, adresów, wskazania osób reprezentujących i podstawy umocowania (dane oznaczone jako fikcyjne w tytule). Przy wnioskowaniu o zapłatę kary sąd wymaga oznaczenia stron i skuteczności zawarcia umowy.
**Rekomendacja:** pełne dane rejestrowe i podpisy osób uprawnionych do reprezentacji (KRS).

#### 5. Brak klauzuli o braku licencji/praw do informacji i o niezobowiązywaniu do transakcji — całość
**Strona dotknięta:** Helix (ryzyko roszczeń Baltic o kontynuację, wykorzystanie koncepcji), Baltic (ryzyko roszczeń o odpowiedzialność przedkontraktową).
**Opis:** Brak postanowienia, że ujawnienie nie przenosi praw (w tym IP) i nie zobowiązuje do zawarcia transakcji; brak oświadczenia o dokładności informacji.
**Rekomendacja:** standardowe klauzule „brak licencji" i „brak zobowiązania do transakcji".

### 🟢 RYZYKA NISKIE

#### 1. Forma pisemna zmian pod rygorem nieważności — § 5 ust. 1
**Strona dotknięta:** obie (neutralnie).
**Opis:** Zastrzeżenie formy ad solemnitatem (art. 76 KC [NIEZWERYFIKOWANE]); doprecyzować, czy dopuszczalna forma elektroniczna lub dokumentowa, oraz czy dotyczy także zrzeczenia się formy.
**Rekomendacja:** doprecyzować dopuszczalność formy elektronicznej.

#### 2. Brak klauzul o wypowiedzeniu, cesji i egzemplarzach — całość
**Strona dotknięta:** obie.
**Opis:** Umowa nie reguluje wcześniejszego rozwiązania ani zakazu przeniesienia praw i obowiązków, ani liczby egzemplarzy.
**Rekomendacja:** dopisać klauzule końcowe.

### ✓ Obszary bez zastrzeżeń / n/d

- Bramka ius cogens: kara za zobowiązanie niepieniężne (poufność) nie narusza art. 483 § 1 KC [NIEZWERYFIKOWANE]; brak wyłączenia miarkowania (art. 484 § 2 KC [NIEZWERYFIKOWANE]); brak próby wyłączenia winy umyślnej; trigger art. 385(5) KC [NIEZWERYFIKOWANE] nieaktywny (obie strony to spółki kapitałowe).
- Prawa autorskie: n/d. RODO: n/d (umowa nie przewiduje powierzenia; informacje mogą zawierać dane osobowe, ale to poza treścią umowy). Tytuł prawny i przekwalifikowanie: n/d.
- Wynagrodzenie, kamienie milowe, terminy płatności: n/d (umowa nieodpłatna).

---

## OCENA BEZPIECZEŃSTWA: 28/100

Dwa ryzyka krytyczne (nieograniczona kara za nieokreślone „naruszenie" oraz brak ochrony po zakończeniu Negocjacji), cztery wysokie (pozorna wzajemność, brak wyłączeń, miękkie standardy, niepełny exit). Konstrukcja deklaruje wzajemność, a faktycznie obciąża Baltic ekspozycją otwartą, zaś Helix pozostawia bez ochrony po rozmowach.

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI — 🟥 CZERWONY (nie podpisywać w obecnej formie).

### Klauzule z bazy KTZR do uzupełnienia

🔴 Kara bez sufitu → `references/baza-klauzul/10-kary-umowne.md`
🔴 Brak okresu poufności po końcu → `references/baza-klauzul/09-poufnosc.md` (model warstwowy)
🟠 Definicje i wyłączenia, zwrot materiałów → `09-poufnosc.md`, `03-definicje.md`

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
