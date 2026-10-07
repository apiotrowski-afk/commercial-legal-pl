konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 1 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

---

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite — wszystkie powołania przepisów: [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa o zachowaniu poufności (NDA) HELIX SOFT sp. z o.o. / BALTIC CAPITAL S.A.

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie: nieograniczona, jednostronna kara 200.000 zł „za każde naruszenie", nałożona na zobowiązania bez wyłączeń i bez końca, wymaga przebudowy przed podpisem.

Bramka ius cogens (R10): bez trafienia. Kara dotyczy zobowiązania niepieniężnego (art. 483 § 1 KC [NIEZWERYFIKOWANE] — nie narusza); umowa nie wyłącza miarkowania (art. 484 § 2 KC [NIEZWERYFIKOWANE]) ani nie ogranicza winy umyślnej (art. 473 § 2 KC [NIEZWERYFIKOWANE]). Trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]) — n/d, obie strony to spółki kapitałowe. Ocena kumulatywna (test pięciopunktowy, krok 5) — patrz ryzyko 1.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | brak wynagrodzenia (NDA) | — | [BRAK DANYCH] |
| Cap nominalny | brak | — | brak sufitu |
| Kara za naruszenie poufności (Strona Otrzymująca) | 200.000 zł za każde naruszenie (§ 3 ust. 1) | 200.000 × N | N = 1: 200.000 zł; N = 3: 600.000 zł; N = 5: 1.000.000 zł (N liczone „za każde naruszenie"; umowa nie wiąże kary z dokumentem, zdarzeniem ani odbiorcą) |
| Kary poza capem | wszystkie (cap nie istnieje) | — | otwarta, rośnie liniowo z liczbą naruszeń |
| Odszkodowanie uzupełniające | brak zastrzeżenia | — | [BRAK DANYCH] — brak zapisu; skutek: patrz ryzyko 8 |
| Efektywna ekspozycja Strony Otrzymującej (BALTIC) | 200.000 zł × N | — | **200.000 zł × N, N nieograniczone; brak wartości umowy do porównania** |
| Asymetria (BALTIC vs HELIX) | 200.000 zł × N vs 0 zł (§ 3 ust. 2) | 200.000 : 0 | **nieskończona (dzielenie przez zero); HELIX nie ponosi żadnej kary** |
| Okres obowiązywania | „przez okres prowadzenia Negocjacji" (§ 4) | brak daty początku i końca | nie da się policzyć: [BRAK DANYCH] |
| Termin powiadomienia o ujawnieniu | „niezwłocznie" (§ 2 ust. 3) | — | nieobliczalny |
| Termin zwrotu Materiałów Roboczych | „na żądanie" (§ 2 ust. 4) | — | brak terminu: [BRAK DANYCH] |

Wniosek: umowa podaje jedną liczbę (200.000 zł), ale bez mnożnika, sufitu i definicji „naruszenia" ekspozycja BALTIC jest otwarta i nie da się jej ograniczyć w negocjacjach bez zmiany treści; druga strona nie ma ekspozycji żadnej. To podnosi ryzyko kary do 🔴.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna 200.000 zł „za każde naruszenie" — bez sufitu, jednostronna, bez wyłączeń — § 3 ust. 1 i 2 w zw. z § 1 ust. 2
**Strona dotknięta:** BALTIC CAPITAL S.A. (Strona Otrzymująca); korzysta HELIX SOFT.
**Opis:** § 3 ust. 1 nakłada karę „w wysokości 200.000 zł za każde naruszenie", a § 3 ust. 2 stanowi, że „Strona Ujawniająca nie ponosi kar umownych na podstawie niniejszej Umowy". Umowa nie definiuje „naruszenia" (każdy plik? każdy odbiorca? każda wiadomość? każdy dzień?), nie wprowadza sufitu łącznego, nie odnosi kary do rodzaju czy wagi uchybienia i nie wiąże jej z winą. Karą objęte jest „naruszenie obowiązku poufności" — a obowiązki w § 2 są częściowo miękkie („dołoży starań"), częściowo nieoznaczone („niezwłocznie", „na żądanie"). Informacje Poufne to „wszelkie informacje" (§ 1 ust. 2), bez wyłączeń i bez oznaczania, więc zakres, którego naruszenie zagrożone jest karą, jest nieograniczony (efekt kumulatywny: § 1 ust. 2 + § 2 + § 3 + § 4 łącznie wydrążają przewidywalność, choć każdy z osobna jest dopuszczalny).
**Skutek:** pojedyncze udostępnienie informacji doradcy, komitetowi inwestycyjnemu lub organowi (brak wyłączeń, ryzyko 4) może być liczone jako odrębne naruszenia; 5 naruszeń = 1.000.000 zł bez wykazania szkody. Przeciwko karze pozostaje wyłącznie miarkowanie przez sąd (art. 484 § 2 KC [NIEZWERYFIKOWANE]), które jest uprawnieniem sądu, a nie gwarancją.
**Rekomendacja (preferowana):** kara wzajemna (po stronie każdej ze Stron ujawniającej i otrzymującej); „naruszenie" zdefiniowane jako jedno zdarzenie lub ciąg powiązanych zdarzeń; sufit łączny (np. określona kwota lub wielokrotność wartości transakcji); kara tylko za naruszenie z winy, z zachowaniem odszkodowania uzupełniającego do wysokości szkody; rozdział kar za naruszenie istotne i uchybienia formalne (np. zwłoka w zwrocie).
**Fallback (minimum akceptowalne):** zachować 200.000 zł, ale z sufitem łącznym, definicją „jednego naruszenia" i wzajemnością; bez wzajemności — co najmniej sufit i definicja.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`; `references/baza-klauzul/09-poufnosc.md`

### 🟠 RYZYKA WYSOKIE

#### 2. Pozorna wzajemność — § 1 ust. 1 vs § 1 ust. 2, § 2, § 3 ust. 2
**Strona dotknięta:** obie; BALTIC (zobowiązania jednostronne), HELIX (nie ma jasnej podstawy do ochrony informacji uzyskanych w razie zmiany ról — zob. niżej).
**Opis:** § 1 ust. 1 mówi, że „Strony wzajemnie zobowiązują się" do poufności, ale § 1 ust. 2 definiuje Informacje Poufne jako informacje „przekazane przez Stronę Ujawniającą", a role są przypisane z nazwy (HELIX = Strona Ujawniająca, BALTIC = Strona Otrzymująca), nie z funkcji. Wszystkie obowiązki z § 2 i kara z § 3 ciążą wyłącznie na Stronie Otrzymującej. Informacje przekazane przez BALTIC (np. dane o funduszu, warunki finansowania, plany inwestycyjne) nie są objęte żadną ochroną. Deklarowana wzajemność nie ma pokrycia w treści.
**Skutek:** BALTIC ponosi wszystkie ryzyka i obowiązki; własne informacje BALTIC pozostają bez ochrony. HELIX może otrzymać informacje BALTIC bez obowiązków (np. ujawnić warunki oferty konkurentom BALTIC).
**Rekomendacja (preferowana):** prawdziwie wzajemna konstrukcja: „Strona Ujawniająca" i „Strona Otrzymująca" jako role per przekazanie; kary i obowiązki symetryczne; usunąć § 3 ust. 2.
**Fallback (minimum akceptowalne):** zachować jednostronność, ale (a) skreślić „wzajemnie" z § 1 ust. 1, aby tytuł nie wprowadzał w błąd, (b) dodać odrębną, choćby prostszą, ochronę informacji BALTIC bez kary.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 3. Nieoznaczony okres obowiązywania i brak poufności po jego zakończeniu — § 4 ust. 1
**Strona dotknięta:** obie (HELIX — informacje bez ochrony po zakończeniu rozmów; BALTIC — nie wie, kiedy zobowiązanie ustaje i od kiedy nie grozi mu kara).
**Opis:** „Umowa obowiązuje przez okres prowadzenia Negocjacji." „Negocjacje" nie mają definicji ani daty początku i końca; nie ma mechanizmu stwierdzenia zakończenia (oświadczenie, brak kontaktu przez X dni). Umowa nie mówi, co dzieje się z poufnością po zakończeniu: czy obowiązek trwa dalej (np. 3–5 lat, tajemnica przedsiębiorstwa bezterminowo — art. 11 ust. 2 u.z.n.k. [NIEZWERYFIKOWANE]), czy wygasa z Umową. Dosłowna wykładnia § 4 wskazuje, że po zakończeniu Negocjacji obowiązek wygasa.
**Skutek:** informacje HELIX mogą być swobodnie wykorzystane od dnia zakończenia Negocjacji (typowo właśnie wtedy, gdy inwestycja nie dochodzi do skutku); jednocześnie BALTIC nie wie, do kiedy ponosi ryzyko kary, bo moment zakończenia Negocjacji jest sporny.
**Rekomendacja (preferowana):** definicja „Negocjacji" i ich zakończenia (np. pisemne oświadczenie albo brak kontaktów przez 60 dni); poufność trwa X lat po zakończeniu, a dla tajemnicy przedsiębiorstwa bezterminowo.
**Fallback (minimum akceptowalne):** stały okres od daty zawarcia Umowy (np. 3 lata) niezależnie od dalszych zdarzeń.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (model warstwowy okresów); `references/baza-klauzul/12-wypowiedzenie-exit.md`

#### 4. Brak wyłączeń z poufności i brak katalogu dopuszczonych odbiorców — § 1 ust. 2, § 2 ust. 1–2
**Strona dotknięta:** BALTIC CAPITAL S.A. (Strona Otrzymująca).
**Opis:** Informacje Poufne to „wszelkie informacje przekazane przez Stronę Ujawniającą w związku z Negocjacjami" — bez wymogu oznaczenia, bez wyłączeń (informacje publiczne, znane wcześniej, uzyskane niezależnie lub od osoby trzeciej, ujawnienie wymagane prawem lub przez organ), bez wskazania osób, którym wolno je przekazać (zarząd, pracownicy, doradcy prawni i finansowi, podmioty finansujące, audytorzy). BALTIC jako spółka inwestycyjna działa przez doradców i organy wewnętrzne, a każde takie ujawnienie jest formalnie naruszeniem (sankcja z ryzyka 1).
**Skutek:** zagrożenie karą za zachowania, które inwestor wykonuje w zwykłym toku due diligence, oraz za ujawnienia wymagane przepisami; ciężar dowodu, że informacja jest publiczna, spoczywa de facto na BALTIC.
**Rekomendacja (preferowana):** katalog wyłączeń (publiczne, wcześniej znane, niezależnie opracowane, od osoby trzeciej, wymagane prawem); katalog dopuszczonych odbiorców zobowiązanych do poufności; odpowiedzialność Strony Otrzymującej za odbiorców.
**Fallback (minimum akceptowalne):** wyłączenia ustawowe i ujawnienie doradcom zawodowym związanym tajemnicą.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (wyłączenia z NDA IT KTZR)

### 🟡 RYZYKA ŚREDNIE

#### 5. „Dołoży starań" przy obowiązku zabezpieczenia — § 2 ust. 2
**Strona dotknięta:** HELIX SOFT sp. z o.o. (ochrona informacji słabsza); pośrednio BALTIC (niejasność, czy uchybienie starannością to „naruszenie" z § 3).
**Opis:** „Strona Otrzymująca dołoży starań, aby zabezpieczyć Informacje Poufne przed dostępem osób trzecich" to zobowiązanie starannego działania, a nie rezultatu; brak miary staranności (np. staranność własna, nie mniejsza niż profesjonalna), brak środków technicznych.
**Skutek:** wyciek przez osobę trzecią nie jest sam w sobie naruszeniem, jeśli BALTIC „dołożył starań"; spór o miarę staranności i o to, czy jej brak uruchamia karę.
**Rekomendacja (preferowana):** „zobowiązuje się zabezpieczyć" z miarą staranności i określeniem środków.
**Fallback (minimum akceptowalne):** „dołoży należytej staranności, nie mniejszej niż w odniesieniu do własnych informacji poufnych".
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 6. „Niezwłocznie" i obowiązek zawiadomienia o „każdym przypadku ujawnienia" — § 2 ust. 3
**Strona dotknięta:** BALTIC CAPITAL S.A.
**Opis:** Termin nieobliczalny; zakres „każdego przypadku ujawnienia" nie wskazuje, czy chodzi o ujawnienia nieuprawnione, czy o każde (także dozwolone), ani od kiedy biegnie (od powzięcia wiadomości? od zdarzenia?). Obowiązek zawiadomienia o własnym uchybieniu bez jasnych skutków, w połączeniu z karą z § 3, jest ryzykiem samooskarżenia.
**Skutek:** spór, czy zwłoka w zawiadomieniu jest odrębnym naruszeniem (a więc kolejne 200.000 zł).
**Rekomendacja (preferowana):** termin w godzinach lub dniach roboczych od powzięcia wiadomości, zakres: nieuprawnione ujawnienie, utrata, uzasadnione podejrzenie; wyraźnie bez kary odrębnej za samą zwłokę.
**Fallback (minimum akceptowalne):** 3 dni robocze od powzięcia wiadomości.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (powiadomienie 72 h / 24 h)

#### 7. Pojęcia bez definicji i zwrot materiałów bez terminu i wyjątków — § 2 ust. 4, § 1, § 4
**Strona dotknięta:** obie.
**Opis:** „Negocjacje" (§ 1, § 4) oraz „Materiały Robocze" (§ 2 ust. 4) pisane wielką literą, bez definicji. Nie wiadomo, czy Materiały Robocze to notatki BALTIC, modele finansowe, kopie dokumentów HELIX, czy wyniki analiz zawierające Informacje Poufne. Zwrot „na żądanie" — bez terminu, bez usunięcia kopii elektronicznych i kopii zapasowych, bez wyjątku na archiwizację wymaganą prawem lub polityką wewnętrzną, bez potwierdzenia. Preambuła używa „negocjacji inwestycyjnych" małą literą, a treść wielką — dryf terminologiczny.
**Skutek:** spór o zakres zwrotu; ryzyko, że niemożliwy do wykonania zwrot (np. kopie zapasowe) jest naruszeniem zagrożonym karą z § 3.
**Rekomendacja (preferowana):** definicje w § 1; zwrot lub usunięcie w terminie (np. 14 dni) z pisemnym potwierdzeniem; wyjątek dla kopii archiwalnych (nadal poufnych) i wymaganych prawem.
**Fallback (minimum akceptowalne):** zdefiniować „Negocjacje" i „Materiały Robocze"; termin 14 dni.
**Klauzula z bazy:** `references/baza-klauzul/18-zwrot-materialow.md`; `references/baza-klauzul/03-definicje.md`

#### 8. Brak zastrzeżenia odszkodowania uzupełniającego i brak klauzuli „bez licencji" — § 3, § 5
**Strona dotknięta:** HELIX SOFT sp. z o.o.
**Opis:** Umowa zastrzega karę, ale nie zastrzega prawa do odszkodowania przewyższającego karę. Bez takiego zastrzeżenia wierzyciel co do zasady może żądać tylko zastrzeżonej kary (art. 484 § 1 KC [NIEZWERYFIKOWANE]). Brak też postanowienia, że ujawnienie nie daje licencji ani praw do informacji (know-how, kod, model biznesowy), ani zakazu inżynierii wstecznej.
**Skutek:** szkoda HELIX z wycieku know-how może być wielokrotnie wyższa niż 200.000 zł, a niedochodzalna; ryzyko odmiennej strony sporu, w której kara staje się „sufitem".
**Rekomendacja (preferowana):** wyraźne zastrzeżenie odszkodowania uzupełniającego na zasadach ogólnych oraz klauzula o braku przeniesienia praw.
**Fallback (minimum akceptowalne):** samo zastrzeżenie odszkodowania uzupełniającego (rozważyć je łącznie z sufitem z ryzyka 1 jako wymianę ustępstw).
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`; `references/baza-klauzul/09-poufnosc.md` (brak zobowiązania do kontraktowania, brak licencji)

#### 9. Forum sporów wyłącznie dla jednej strony i niejasna właściwość — § 5 ust. 2
**Strona dotknięta:** BALTIC CAPITAL S.A. (siedziba w Sopocie), przy sporze wszczętym przez HELIX (Gdynia).
**Opis:** „sądem właściwym jest sąd siedziby Strony Ujawniającej" — a jedyną Stroną Ujawniającą jest HELIX. Sformułowanie nie wskazuje rodzaju sądu (rejonowy/okręgowy) ani miejscowości, jedynie odsyła do siedziby (Gdynia). Przy karze 200.000 zł właściwość rzeczowa wymaga oddzielnej oceny.
**Skutek:** BALTIC pozwany w siedzibie kontrahenta; różnica kosztów i logistyki niewielka (Gdynia–Sopot), więc ryzyko jest raczej symboliczne niż finansowe.
**Rekomendacja (preferowana):** sąd właściwy dla pozwanego albo wskazany z nazwy sąd (np. „Sąd Okręgowy w Gdańsku").
**Fallback (minimum akceptowalne):** wskazać sąd z nazwy, bez rozróżnienia stron.
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

#### 10. Brak oznaczenia reprezentacji, danych rejestrowych oraz daty i miejsca zawarcia — oznaczenie stron
**Strona dotknięta:** obie.
**Opis:** Strony wskazane tylko z nazwy i miasta (dopisek „dane fikcyjne" odnotowany; poza tym brak KRS, NIP, adresu, osób reprezentujących i podstawy ich umocowania; brak daty i miejsca zawarcia).
**Skutek:** trudność w identyfikacji stron i w wykazaniu umocowania; spór o skuteczność zobowiązania.
**Rekomendacja (preferowana):** pełne oznaczenie (KRS, NIP, adres, reprezentacja), data i miejsce zawarcia.
**Fallback (minimum akceptowalne):** KRS i imiona osób podpisujących.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### 🟢 RYZYKA NISKIE

#### 11. Forma zmian „pod rygorem nieważności" bez wskazania formy dla oświadczeń i bez klauzuli o cesji — § 5 ust. 1
**Strona dotknięta:** obie.
**Opis:** Zmiany wymagają formy pisemnej pod rygorem nieważności; brak wskazania, czy wystarczy forma dokumentowa (e-mail) dla żądań i zawiadomień z § 2 (zwrot, powiadomienie), brak zakazu cesji praw i obowiązków bez zgody, brak klauzuli o całości porozumienia.
**Skutek:** drobne wątpliwości co do skuteczności korespondencji.
**Rekomendacja (preferowana):** forma dokumentowa dla zawiadomień, zakaz cesji bez zgody.
**Fallback (minimum akceptowalne):** doprecyzować adresy do doręczeń.
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

#### 12. Brak postanowienia o danych osobowych — cała umowa
**Strona dotknięta:** obie.
**Opis:** Przy negocjacjach inwestycyjnych przekazywane są zwykle dane osobowe (wspólnicy, kadra, klienci); brak wskazania, że każda Strona przetwarza je jako odrębny administrator wyłącznie w celu Negocjacji. Powołanie art. 28 RODO [NIEZWERYFIKOWANE] co do zasady nie jest potrzebne, o ile role to odrębni administratorzy.
**Skutek:** niewielki, jeśli dane osobowe nie są przekazywane.
**Rekomendacja (preferowana):** jedno zdanie o roli odrębnych administratorów.
**Fallback (minimum akceptowalne):** pominąć, jeśli dane osobowe nie są przedmiotem ujawnienia.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md` (rola przy danych osobowych); `references/baza-klauzul/14-rodo.md`

### ✓ Obszary bez zastrzeżeń

- Prawa autorskie / IP — n/d jako obszar przeniesienia praw (umowa ich nie przenosi); sprawa „braku licencji" ujęta w ryzyku 8.
- Tytuł prawny i przekwalifikowanie — n/d (NDA, brak świadczenia osobistego).
- Prawo właściwe: ✓ prawo polskie, bez zastrzeżeń.
- Normy bezwzględne (art. 473 § 2, 483 § 1, 484 § 2, 119 KC [NIEZWERYFIKOWANE]): ✓ brak naruszenia.
- Wypowiedzenie i exit: wskazano w ryzykach 3 i 7 (brak mechanizmu wypowiedzenia i zakończenia Negocjacji, zwrot materiałów).

Pokrycie dziewięciu obszarów (R9): odpowiedzialność i kary (1, 8) · prawa autorskie (n/d) · definicje i logika (2, 7) · reprezentacja (10) · wypowiedzenie i exit (3, 7) · RODO (12) · tytuł prawny (n/d) · poufność (3, 4, 5, 6) · spory (9; prawo właściwe ✓).

---

## OCENA BEZPIECZEŃSTWA: 45/100

Jedno ryzyko krytyczne (−17), trzy wysokie (−21), sześć średnich (−12), dwa niskie (−1) daje około 49 pkt, skorygowane w dół do 45 ze względu na efekt kumulatywny (jednostronna kara bez sufitu + zakres „wszelkich informacji" + brak wyłączeń). Werdykt kolorystyczny wynika z reguły (jedno 🔴 = CZERWONY).

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (kara bez sufitu, jednostronna)
→ `references/baza-klauzul/10-kary-umowne.md` (kara z sufitem i odszkodowaniem uzupełniającym) + `references/baza-klauzul/09-poufnosc.md`

🟠 RYZYKO 2 (pozorna wzajemność)
→ `references/baza-klauzul/09-poufnosc.md` (NDA IT KTZR — wzajemność, role per przekazanie)

🟠 RYZYKO 3 (okres po zakończeniu)
→ `references/baza-klauzul/09-poufnosc.md` — model warstwowy okresów (5–10 lat / bezterminowo dla tajemnicy przedsiębiorstwa)

🟠 RYZYKO 4 (wyłączenia i odbiorcy)
→ `references/baza-klauzul/09-poufnosc.md` — wyłączenia (a)–(e) z NDA IT KTZR

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
