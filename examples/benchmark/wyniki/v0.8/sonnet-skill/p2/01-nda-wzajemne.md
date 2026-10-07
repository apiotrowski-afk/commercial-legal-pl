konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 2 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite — każdy cytat przepisu oznaczony [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa o zachowaniu poufności (NDA) HELIX SOFT sp. z o.o. / BALTIC CAPITAL S.A.

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie: umowa nazwana „wzajemną" jest w treści jednostronna, kara umowna nie ma sufitu, a poufność wygasa z końcem Negocjacji.

Oznaczenia: **Ujawniająca** = HELIX SOFT (dalej: Helix), **Otrzymująca** = BALTIC CAPITAL (dalej: Baltic). Przy każdej fladze wskazano stronę dotkniętą.

Bramka ius cogens (R10): nie stwierdzono klauzuli nieważnej z mocy prawa. Kara umowna dotyczy zobowiązania niepieniężnego (art. 483 § 1 KC [NIEZWERYFIKOWANE]); umowa nie wyłącza miarkowania (art. 484 § 2 KC [NIEZWERYFIKOWANE]). Trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]): nieaktywny, obie strony to spółki kapitałowe. Test kumulatywny: aktywny, zob. flaga 3.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy / wartość transakcji | brak w umowie | — | [BRAK DANYCH] |
| Cap odpowiedzialności | brak (umowa go nie przewiduje) | — | brak limitu |
| Kara umowna za 1 naruszenie (Baltic) | 200.000 zł (§ 3 ust. 1) | 1 × 200.000 | 200.000 zł |
| Kara przy 5 naruszeniach | „za każde naruszenie", bez sufitu | 5 × 200.000 | 1.000.000 zł |
| Kara przy 10 naruszeniach | j.w. | 10 × 200.000 | 2.000.000 zł |
| Sufit kar | brak | — | brak; ekspozycja otwarta co do liczby naruszeń |
| Kary poza capem / indemnity | brak indemnity; odszkodowanie uzupełniające nie zastrzeżone | art. 484 § 1 KC [NIEZWERYFIKOWANE]: kara jest zatem jedyną sankcją | ekspozycja efektywna Baltic = n × 200.000 zł; ekspozycja Helix = 0 zł |
| Asymetria (Baltic vs Helix) | § 3 ust. 1 vs § 3 ust. 2 | 200.000 zł × n : 0 zł | stosunek nieskończony (Helix wyłączony z kar) |
| Okres poufności po zakończeniu Negocjacji | § 4 ust. 1: tylko „okres prowadzenia Negocjacji" | 0 dni „ogona" | 0 dni; data końca nieustalalna ([BRAK DANYCH] — brak daty i zdarzenia kończącego Negocjacje) |
| Terminy zawiadomień / zwrotu | „niezwłocznie", „na żądanie" | nie do policzenia | [BRAK DANYCH] — sygnał do flagi (antywzorzec) |

Wniosek z rachunku: jedyna kwota w umowie (200.000 zł) działa bez sufitu i wyłącznie przeciw Baltic, a ochrona Helix kończy się w dniu zakończenia Negocjacji (0 dni ogona). To kalibruje flagi 1, 2 i 4 do poziomów najwyższych.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna 200.000 zł „za każde naruszenie", bez sufitu i bez definicji „naruszenia" — § 3 ust. 1
**Strona dotknięta:** Baltic (nadmierna, otwarta ekspozycja); wtórnie Helix (kara jako jedyne roszczenie może być niższa od szkody).
**Opis:** Umowa przewiduje karę „w wysokości 200.000 zł za każde naruszenie". Nie ma sufitu łącznego, nie określono, co jest „jednym naruszeniem" (jedna informacja, jedno zdarzenie, jeden odbiorca, każdy dzień trwania), kara jest jednakowa dla naruszenia drobnego i rażącego, nie ma powiązania z winą ani ze szkodą. Brak zastrzeżenia odszkodowania uzupełniającego sprawia, że kara jest wyłączną sankcją (art. 484 § 1 KC [NIEZWERYFIKOWANE]); gdy szkoda Helix przewyższy 200.000 zł, różnica pozostaje niepokryta.
**Skutek:** Przy 5 naruszeniach 1.000.000 zł, przy 10 naruszeniach 2.000.000 zł (rachunek wyżej); spór o liczbę naruszeń. Miarkowanie przez sąd (art. 484 § 2 KC [NIEZWERYFIKOWANE]) jest uprawnieniem sądu, nie automatem.
**Rekomendacja (preferowana):** sufit łączny kar (np. kwota stała albo wskazany procent wartości transakcji), definicja „naruszenia" (jedno zdarzenie = jedno naruszenie), kara za naruszenie zawinione, rozdzielenie stawek według wagi naruszenia, wyraźne zastrzeżenie albo wyłączenie odszkodowania uzupełniającego, kara wzajemna.
**Fallback (minimum akceptowalne):** zachowanie 200.000 zł, ale z sufitem łącznym i definicją „naruszenia".
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/09-poufnosc.md`

#### 2. Poufność wygasa z końcem Negocjacji, brak „ogona" i brak określenia końca — § 4 ust. 1
**Strona dotknięta:** Helix (jako Ujawniająca, utrata ochrony); wtórnie obie strony (niepewność, kiedy obowiązek ustaje).
**Opis:** „Umowa obowiązuje przez okres prowadzenia Negocjacji." Pojęcie Negocjacji nie jest zdefiniowane, nie ma daty ani zdarzenia kończącego (zawiadomienie, podpisanie umowy inwestycyjnej, upływ terminu). Po zakończeniu Negocjacji nie ma żadnego obowiązku poufności.
**Skutek:** Baltic może po zakończeniu rozmów ujawnić lub wykorzystać informacje Helix; Helix ryzykuje utratę przymiotu tajemnicy przedsiębiorstwa z powodu braku starań o zachowanie poufności (art. 11 ust. 2 u.z.n.k. [NIEZWERYFIKOWANE]). Ochrona kończy się w dniu, w którym ryzyko wycieku jest największe (po nieudanych negocjacjach).
**Rekomendacja (preferowana):** obowiązek poufności przez okres Negocjacji i dodatkowo przez co najmniej 5 lat po ich zakończeniu, bezterminowo dla tajemnicy przedsiębiorstwa; zdefiniowane zdarzenie kończące Negocjacje.
**Fallback (minimum akceptowalne):** 3 lata po zakończeniu Negocjacji, z jednoznacznym zdarzeniem końca (pisemne zawiadomienie którejkolwiek ze Stron albo data graniczna).
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`, `references/baza-klauzul/12-wypowiedzenie-exit.md`

### 🟠 RYZYKA WYSOKIE

#### 3. Pozorna wzajemność: definicja i obowiązki tylko jednostronne — § 1 ust. 1–2, § 2
**Strona dotknięta:** Baltic (informacje Baltic niechronione; obowiązki spoczywają tylko na niej); Helix nie ma obowiązków wynikających z § 2.
**Opis:** § 1 ust. 1 mówi, że „Strony wzajemnie zobowiązują się" do poufności, ale § 1 ust. 2 definiuje Informacje Poufne jako informacje „przekazane przez Stronę Ujawniającą" (Helix), a cały § 2 obciąża tylko Stronę Otrzymującą (Baltic). Role są przypisane w komparycji na stałe, więc Baltic nie zostaje nigdy Ujawniającą. Efekt kumulatywny (§ 1 ust. 2 + § 2 + § 3 + § 5 ust. 2): jedna strona dźwiga obowiązki, sankcję i forum sporu, druga ma prawa.
**Skutek:** Informacje przekazywane przez Baltic (strategia inwestycyjna, warunki finansowania, dane funduszu) nie są chronione wcale; Helix może je ujawnić bez żadnej konsekwencji. Tytuł „wzajemne" wprowadza w błąd.
**Rekomendacja (preferowana):** prawdziwa wzajemność: definicja obejmująca informacje każdej ze Stron, każda strona jest Ujawniającą i Otrzymującą, symetryczne obowiązki i sankcje.
**Fallback:** NDA jednostronne uczciwie nazwane (jeśli to intencja stron), z odpowiednią korektą tytułu i § 1 ust. 1 oraz z mitygacją flag 1, 4 i 5.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 4. Wyłączenie Helix z kar umownych — § 3 ust. 2
**Strona dotknięta:** Baltic.
**Opis:** „Strona Ujawniająca nie ponosi kar umownych na podstawie niniejszej Umowy." Helix, mimo deklaracji wzajemności z § 1 ust. 1, jest zwolniona z sankcji. Rachunek: 200.000 zł × n po stronie Baltic wobec 0 zł po stronie Helix.
**Skutek:** Brak ekwiwalentu ochrony; naruszenie przez Helix (np. wykorzystanie informacji Baltic, ujawnienie faktu negocjacji) pozostaje bez sankcji umownej, a Baltic zostaje z trudniejszym dochodzeniem odszkodowania na zasadach ogólnych.
**Rekomendacja (preferowana):** kara wzajemna na identycznych zasadach (po poprawie flagi 1).
**Fallback:** brak kary po obu stronach i poleganie na odszkodowaniu na zasadach ogólnych (obie strony symetrycznie), albo kara wzajemna w niższej kwocie.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 5. Brak wyłączeń z poufności i brak katalogu uprawnionych odbiorców — § 1 ust. 2, § 2 ust. 1–2
**Strona dotknięta:** Baltic (ryzyko kary za ujawnienie informacji, które nie powinny być poufne albo muszą być ujawnione); Helix pośrednio (spór o zakres).
**Opis:** Informacje Poufne to „wszelkie informacje przekazane" w związku z Negocjacjami, bez oznaczania, bez wyłączeń (informacje publiczne, znane wcześniej, opracowane niezależnie, uzyskane od osoby trzeciej, ujawnienie wymagane prawem lub przez organ) i bez możliwości ujawnienia doradcom, członkom organów, audytorom czy podmiotom finansującym. Baltic S.A., prowadząc inwestycję, w praktyce musi uzyskiwać zgody wewnętrzne i korzystać z doradców.
**Skutek:** Każde ujawnienie, także informacji publicznej lub wymaganej prawem, może zostać zakwalifikowane jako „naruszenie" zagrożone karą 200.000 zł (flaga 1); odwrotnie, niezdefiniowany zakres utrudnia Helix dowód, co było poufne.
**Rekomendacja (preferowana):** katalog zamknięty wyłączeń (a–e), lista osób uprawnionych związanych poufnością, ciężar dowodu wyłączeń na stronie, która się na nie powołuje.
**Fallback:** wyłączenia (publiczne, wcześniej posiadane, wymagane prawem) bez katalogu odbiorców, z zastrzeżeniem odpowiedzialności za doradców.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

### 🟡 RYZYKA ŚREDNIE

#### 6. Pojęcia wielką literą bez definicji — Negocjacje, Materiały Robocze, Umowa — § 1, § 2 ust. 4, § 4
**Strona dotknięta:** obie, w szczególności Helix (niepewny zakres) i Baltic (niepewny zakres sankcji).
**Opis:** „Negocjacje" są użyte w § 1, § 4 bez definicji (komparycja mówi o „planowanych negocjacjach inwestycyjnych" małą literą); „Materiały Robocze" (§ 2 ust. 4) i „Umowa" (§ 4, § 5) nie są zdefiniowane (Złota Reguła nr 1). „Materiały Robocze" nie występują w definicji Informacji Poufnych, więc ich związek z poufnością jest niejasny.
**Skutek:** Spór interpretacyjny o zakres obowiązku zwrotu i o moment końca umowy (flaga 2).
**Rekomendacja:** słowniczek definicji; Materiały Robocze jako podzbiór Informacji Poufnych.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 7. Zobowiązanie starannego działania zamiast rezultatu — § 2 ust. 2
**Strona dotknięta:** Helix.
**Opis:** „dołoży starań, aby zabezpieczyć" Informacje Poufne przed dostępem osób trzecich. Obowiązek zabezpieczenia jest obowiązkiem starannego działania, bez standardu staranności i bez wskazania środków.
**Skutek:** Ujawnienie na skutek niedostatecznych zabezpieczeń trudno zakwalifikować jako naruszenie; Helix musi dowodzić braku starań.
**Rekomendacja:** „zabezpieczy ... z co najmniej taką starannością jak własne informacje poufne, nie mniejszą niż należyta staranność profesjonalisty" oraz określenie podstawowych środków.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 8. „Niezwłocznie" bez liczby dni oraz zawiadomienie jako samooskarżenie — § 2 ust. 3
**Strona dotknięta:** obie (Helix: brak mierzalnego terminu; Baltic: obowiązek zgłaszania zdarzeń wprost zagrożonych karą z § 3).
**Opis:** „niezwłocznie poinformuje ... o każdym przypadku ujawnienia"; brak terminu w godzinach lub dniach, brak formy i zakresu zgłoszenia. Obowiązek nie obejmuje podejrzenia naruszenia, a tylko faktu „ujawnienia".
**Skutek:** Spór o to, czy zgłoszenie było „niezwłoczne"; zgłoszenie działa jak przyznanie naruszenia i uruchamia karę 200.000 zł, co zniechęca do zgłaszania.
**Rekomendacja:** termin (np. 72 godziny od powzięcia wiadomości), forma dokumentowa, obejmuje podejrzenie, zgłoszenie w dobrej wierze nie jest samo w sobie podstawą kary.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 9. Zwrot materiałów: tylko „Materiały Robocze", tylko „na żądanie", bez terminu i zniszczenia — § 2 ust. 4
**Strona dotknięta:** Helix.
**Opis:** „Materiały Robocze podlegają zwrotowi na żądanie." Brak terminu zwrotu, brak obowiązku zniszczenia kopii (w tym cyfrowych), brak oświadczenia o zniszczeniu, a Informacje Poufne jako takie zwrotowi nie podlegają. Brak procedury exit po zakończeniu Negocjacji.
**Skutek:** Po zakończeniu Negocjacji Baltic zachowuje kopie dokumentów Helix bez żadnego obowiązku ich zwrotu lub usunięcia.
**Rekomendacja:** zwrot lub zniszczenie wszystkich Informacji Poufnych w terminie (np. 7 dni) od żądania lub zakończenia Negocjacji, z pisemnym potwierdzeniem; wyjątek dla kopii wymaganych prawem.
**Klauzula z bazy:** `references/baza-klauzul/18-zwrot-materialow.md`

#### 10. Forum sporów: sąd siedziby Strony Ujawniającej — § 5 ust. 2
**Strona dotknięta:** Baltic.
**Opis:** „sądem właściwym jest sąd siedziby Strony Ujawniającej". Ponieważ role są stałe (Ujawniająca = Helix, Gdynia), forum zawsze znajduje się u jednej strony. Zapis nie wskazuje rodzaju sądu (rejonowy / okręgowy), a przy sporze o 200.000 zł i więcej istotne jest, który sąd rozpoznaje sprawę. Prorogacja jest możliwa między przedsiębiorcami w formie pisemnej (art. 46 KPC [NIEZWERYFIKOWANE]).
**Skutek:** Przewaga miejscowa Helix; w NDA rzeczywiście wzajemnym forum „pozwanego" byłoby neutralne.
**Rekomendacja:** sąd właściwy dla siedziby pozwanego albo wskazany neutralny sąd (np. właściwy dla siedziby Strony, przeciwko której wniesiono pozew), z określeniem rodzaju sądu.
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

#### 11. Brak zastrzeżenia odszkodowania uzupełniającego — § 3 ust. 1
**Strona dotknięta:** Helix.
**Opis:** Umowa nie stanowi, że kara nie wyłącza dochodzenia odszkodowania przewyższającego karę. Zgodnie z regułą z art. 484 § 1 KC [NIEZWERYFIKOWANE] kara jest odszkodowaniem ryczałtowym, a dochodzenie więcej wymaga zastrzeżenia.
**Skutek:** Jeżeli wyciek informacji o wartości inwestycyjnej kosztuje Helix więcej niż 200.000 zł, nadwyżka pozostaje niepokryta. (Efekt odwrotny dla Baltic: ekspozycja ograniczona do n × 200.000 zł.)
**Rekomendacja:** świadomy wybór: wyraźne zastrzeżenie (z sufitem łącznym — zob. flaga 1) albo wyraźne wyłączenie.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 12. Niekompletne oznaczenie stron i zawarcia umowy — komparycja, brak sekcji podpisów
**Strona dotknięta:** obie.
**Opis:** Brak KRS i NIP, adresów, sposobu reprezentacji i umocowania osób podpisujących, daty i miejsca zawarcia (Złota Reguła nr 8). Dane stron oznaczone jako fikcyjne, ale w dokumencie rzeczywistym byłaby to wada.
**Skutek:** Ryzyko co do umocowania (reprezentacja spółki), trudność w identyfikacji stron w razie sporu i egzekucji.
**Rekomendacja:** pełne dane rejestrowe, reprezentacja zgodna z KRS, data i miejsce, bloki podpisowe.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### 🟢 RYZYKA NISKIE

#### 13. Forma zmian: „forma pisemna pod rygorem nieważności" — § 5 ust. 1
**Strona dotknięta:** obie.
**Opis:** Zastrzeżenie formy ad solemnitatem jest skuteczne, ale sztywne; brak wskazania, czy forma dokumentowa lub elektroniczna wystarcza; brak klauzuli o całości porozumienia i o zakazie cesji.
**Rekomendacja:** doprecyzować formę (pisemna z podpisami, ewentualnie dokumentowa), dodać klauzulę całości umowy i zakaz cesji bez zgody.

#### 14. Brak klauzuli AI i ochrony faktu prowadzenia rozmów
**Strona dotknięta:** Helix.
**Opis:** Umowa nie reguluje wprowadzania Informacji Poufnych do narzędzi AI ani nie obejmuje poufnością samego faktu i treści rozmów o inwestycji.
**Rekomendacja:** klauzula AI (narzędzia bez treningu na danych, zakaz treningu modeli własnych) oraz zapis chroniący fakt Negocjacji.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 15. Brak zapisu o braku licencji i braku obowiązku zawarcia umowy
**Strona dotknięta:** Helix (IP) oraz obie strony.
**Opis:** Brak oświadczenia, że ujawnienie informacji nie przenosi praw ani nie udziela licencji, i że żadna ze Stron nie jest zobowiązana do zawarcia umowy inwestycyjnej.
**Rekomendacja:** dodać oba zapisy.

### ✓ Obszary bez zastrzeżeń / n/d

- Prawa autorskie i IP: n/d (NDA nie przenosi praw; uwaga w fladze 15).
- RODO: n/d w treści (umowa nie reguluje danych osobowych; jeśli materiały je zawierają, rozważyć klauzulę informacyjną).
- Tytuł prawny i przekwalifikowanie: n/d.
- Odpowiedzialność i kary: flagi 1, 4, 11. Definicje: flaga 6. Reprezentacja: flaga 12. Wypowiedzenie i exit: flagi 2, 9. Poufność: flagi 2, 3, 5, 7, 8, 14. Spory: flaga 10.

### Zestawienie flag

🔴 KRYTYCZNE: 2 · 🟠 WYSOKIE: 3 · 🟡 ŚREDNIE: 7 · 🟢 NISKIE: 3 · razem: 15.

---

## OCENA BEZPIECZEŃSTWA: 28/100

Dwa ryzyka krytyczne (kara bez sufitu i poufność bez „ogona"), trzy wysokie (pozorna wzajemność, asymetria kar, brak wyłączeń) i siedem średnich. Umowa nie chroni skutecznie żadnej ze stron: Helix traci ochronę z końcem Negocjacji, Baltic ponosi otwartą ekspozycję bez korzyści z ochrony własnych informacji.

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI (🟥 CZERWONY).

Miejsca, w których w trybie standardowym nastąpiłby STOP (decyzje do podjęcia przez prowadzącego): czy intencją stron jest rzeczywiście NDA wzajemne czy jednostronne; wysokość i sufit kary; długość „ogona" poufności; wybór forum.

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
