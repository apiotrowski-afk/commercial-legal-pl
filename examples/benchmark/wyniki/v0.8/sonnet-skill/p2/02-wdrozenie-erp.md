konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 2 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, bez MCP legal-cite; każde powołanie przepisu oznaczone [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa wdrożeniowa ERP (NOVA RETAIL sp. z o.o. / CODEX WORKS sp. z o.o.)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; umowa zawiera klauzule nieważne z mocy prawa i wydrąża zobowiązanie Wykonawcy przy pełnym obciążeniu Zamawiającego.

Audyt neutralny: przy każdej fladze wskazano stronę dotkniętą. Przeważająca część wad godzi w Zamawiającego; wada godząca w Wykonawcę: flaga 12.

### 🧮 Rachunek ekspozycji

Liczby z umowy: wynagrodzenie 480.000 zł netto (ryczałt); płatność 60 dni od doręczenia faktury; kara Zamawiającego 50.000 zł/dzień, bez sufitu; kary Wykonawcy: 0 zł; cap odpowiedzialności Wykonawcy: brak (odpowiada tylko za winę umyślną); termin wykonania: „niezwłocznie" (brak liczby); okres wypowiedzenia Wykonawcy: brak (każdy czas); okres poufności: brak.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto | — | 480.000 zł netto |
| Kara dzienna Zamawiającego jako % wartości | 50.000 zł/dzień | 50.000 / 480.000 | **10,42% wartości za każdy dzień** |
| Dzień, w którym kara dorównuje wartości umowy | — | 480.000 / 50.000 | 9,6 dnia, czyli 10. dzień opóźnienia |
| Kara max po 10 dniach | 50.000 × 10 | 500.000 zł | 104% wartości |
| Kara max po 30 dniach | 50.000 × 30 | 1.500.000 zł | **312,5% wartości** |
| Kara max po 60 dniach | 50.000 × 60 | 3.000.000 zł | 625% wartości |
| Sufit kary | brak | — | **ekspozycja otwarta** [BRAK SUFITU] |
| Kary Wykonawcy (max) | „nie ponosi kar" | — | 0 zł |
| Cap Wykonawcy / efektywna ekspozycja Wykonawcy | tylko wina umyślna | szkoda z winy nieumyślnej (w tym rażącej) = 0 zł; szkoda z winy umyślnej podwykonawcy = 0 zł | **efektywna ekspozycja Wykonawcy za nieumyślne niewykonanie: 0 zł** przy 480.000 zł zapłaconym |
| Asymetria kar | A (Zamawiający) vs B (Wykonawca) | 50.000/dzień vs 0 | nieskończona (dzielenie przez 0); Zamawiający: do ∞, Wykonawca: 0 |
| Termin płatności | 60 dni od doręczenia faktury | 60 dni | na granicy limitu B2B (zob. flaga 15) [NIEZWERYFIKOWANE]; data zależy od doręczenia faktury, a moment wystawienia faktury nie jest w umowie określony [BRAK DANYCH] |
| Termin wykonania | „niezwłocznie" | nieliczalny | [BRAK DANYCH] — brak daty końcowej i kamieni milowych |
| Wypowiedzenie Wykonawcy | „w każdym czasie" | okres wypowiedzenia 0 dni | [BRAK DANYCH] o okresie; skutek natychmiastowy, także w połowie projektu |
| Wypowiedzenie Zamawiającego | zakaz do końca Wdrożenia | — | koniec Wdrożenia nieoznaczony (brak terminu), więc zamknięcie bezterminowe |
| Odsetki / koszty zastępczego wykonania | nie podano | — | [BRAK DANYCH] |

Wniosek: ryzyko pieniężne rozkłada się wyłącznie na Zamawiającego. Przy zwłoce w zapłacie 480.000 zł jego dług może po 10 dniach wzrosnąć do ponad 2× wartości umowy (480.000 + 500.000), a po 30 dniach do ok. 3,1× (480.000 + 1.500.000 = 1.980.000 zł, czyli 412,5% wartości), bez sufitu. Wykonawca za nieumyślne niewykonanie lub wadliwe wykonanie nie zapłaci nic. Rachunek wymusza flagi 🔴 (nie 🟠) dla kary i odpowiedzialności.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna za opóźnienie w zapłacie, 50.000 zł/dzień, bez sufitu, jednostronna — § 5 ust. 2
**Strona dotknięta:** Zamawiający (płatnik); pośrednio Wykonawca, który traci pewność skuteczności klauzuli.
**Opis:** Kara zastrzeżona za opóźnienie w płatności, czyli za zobowiązanie pieniężne. Kara umowna zabezpiecza zobowiązania niepieniężne (art. 483 § 1 KC [NIEZWERYFIKOWANE]); za zwłokę w zapłacie należą się odsetki. Stawka 10,42% wartości dziennie, bez sufitu, po 10 dniach przekracza wartość umowy. „Wykonawca nie ponosi kar" czyni klauzulę jednostronną, a „Strony wzajemnie…" z § 1 ust. 2 pozorną wzajemnością.
**Skutek:** Klauzula nieważna (art. 483 § 1 w zw. z art. 58 KC [NIEZWERYFIKOWANE]); a gdyby sąd potraktował ją jako zastrzeżoną w innej funkcji, rażące wygórowanie uzasadnia miarkowanie (art. 484 § 2 KC [NIEZWERYFIKOWANE]), które jest uprawnieniem sądu, nie automatem. Do rozstrzygnięcia ryzyko sporu o kilka milionów złotych.
**Rekomendacja (preferowana):** Skreślić karę; zostawić odsetki ustawowe za opóźnienie. Kary za zwłokę wprowadzić po stronie Wykonawcy (za opóźnienie względem harmonogramu).
**Fallback (minimum akceptowalne):** Odsetki za opóźnienie plus symetryczna kara dzienna po stronie Wykonawcy w niskiej stawce procentowej z sufitem (np. 10–20% wartości) za terminy kamieni milowych.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 2. Odpowiedzialność Wykonawcy wyłącznie za winę umyślną; wyłączenie winy umyślnej podwykonawców — § 5 ust. 1
**Strona dotknięta:** Zamawiający.
**Opis:** Wykonawca odpowiada tylko za szkody wyrządzone umyślnie, a umyślne działania podwykonawców są wyłączone. Efektywnie odpowiedzialność ex contractu z tytułu niewykonania lub nienależytego wykonania (art. 471 KC [NIEZWERYFIKOWANE]) przestaje istnieć: ani niedbalstwo, ani rażące niedbalstwo nie rodzą odpowiedzialności. Wyłączenie umyślności osób, którymi dłużnik się posługuje (art. 474 KC), podlega odrębnej ocenie; w zakresie, w jakim sięga winy umyślnej samego Wykonawcy lub jego organu, jest sprzeczne z art. 473 § 2 KC [NIEZWERYFIKOWANE].
**Skutek:** Wada wdrożenia ERP (utrata danych, przestój sprzedaży, błędne księgowania) nie obciąża Wykonawcy. Nieważność w zakresie sprzecznym z art. 473 § 2 (art. 58 § 3 KC [NIEZWERYFIKOWANE]), ale pozostały zakres wyłączenia działa.
**Rekomendacja (preferowana):** Odpowiedzialność na zasadach ogólnych, cap np. 100–150% wynagrodzenia; poza capem wina umyślna, naruszenie poufności, IP i RODO. Odpowiedzialność za podwykonawców jak za własne działania.
**Fallback (minimum akceptowalne):** Cap na poziomie wynagrodzenia (480.000 zł), wyłączenie lucrum cessans za wyjątkiem szkód z winy rażącej i umyślnej, pełna odpowiedzialność za podwykonawców.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 3. Przeniesienie praw autorskich bez pól eksploatacji, warunkowane zapłatą — § 4 ust. 1
**Strona dotknięta:** Zamawiający (nabywca); Wykonawca jest dotknięty wtórnie niepewnością zakresu (zbyt szeroko opisane „wszelkie prawa bez ograniczeń").
**Opis:** „Wszelkie prawa autorskie … bez ograniczeń" bez wymienienia pól eksploatacji. Ogólna formuła nie zastępuje wyraźnego wskazania pól (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]); pola nieznane w chwili zawarcia umowy nie są objęte (art. 41 ust. 4 PrAut [NIEZWERYFIKOWANE]). Brak także: oznaczenia utworów (tylko „stworzone oprogramowanie", czyli nie obejmuje komponentów zewnętrznych i standardowego rdzenia ERP), gwarancji czystości IP, klauzuli anty-copyleft, nośnika wymogu formy pisemnej (art. 53 PrAut [NIEZWERYFIKOWANE]). Moment przejścia „z chwilą zapłaty" jest niejasny (zapłaty czego: całości, faktury, raty?), a do tego czasu Zamawiający nie ma nawet licencji na korzystanie z wdrożonego systemu.
**Skutek:** Realne ryzyko braku skutecznego przeniesienia praw mimo zapłaty 480.000 zł; brak legalnej podstawy do korzystania, modyfikacji i utrzymania systemu.
**Rekomendacja (preferowana):** Wyliczyć pola eksploatacji (art. 74 ust. 4 PrAut [NIEZWERYFIKOWANE] dla programów komputerowych), rozdzielić utwory zamawiane od komponentów zewnętrznych (licencja), dodać gwarancję IP i anty-copyleft, przejście z chwilą odbioru lub zapłaty określonej kwoty z licencją tymczasową do czasu przejścia; wyłączyć prawa osobiste (zobowiązanie do niewykonywania, nie zbycie — art. 16 PrAut [NIEZWERYFIKOWANE]).
**Fallback (minimum akceptowalne):** Pełna lista pól eksploatacji i licencja niewyłączna od odbioru do momentu zapłaty.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Prawo Wykonawcy do trenowania modeli AI na danych Zamawiającego, „niezależnie od pozostałych postanowień"; brak umowy powierzenia — § 8 ust. 2 (w zw. z § 6)
**Strona dotknięta:** Zamawiający oraz osoby, których dane dotyczą (klienci, pracownicy retailowego Zamawiającego).
**Opis:** Klauzula nadpisuje poufność (§ 6) i wszystkie inne zapisy, bez zakresu danych, bez anonimizacji, bez celu, bez okresu, bez możliwości sprzeciwu. System ERP w infrastrukturze sprzedawcy przetwarza dane osobowe, a umowa nie zawiera postanowień powierzenia (art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]). Procesor, który określa własne cele przetwarzania, jest uznawany za administratora (art. 28 ust. 10 RODO [NIEZWERYFIKOWANE]) bez podstawy prawnej (art. 6 RODO [NIEZWERYFIKOWANE]).
**Skutek:** Naruszenie RODO po obu stronach (kara administracyjna do 10 mln EUR / 2% obrotu — art. 83 ust. 4 lit. a RODO [NIEZWERYFIKOWANE]); utrata tajemnicy przedsiębiorstwa Zamawiającego (ceny, marże, lista klientów) w modelu osoby trzeciej, czego nie da się cofnąć.
**Rekomendacja (preferowana):** Skreślić ust. 2; dodać umowę powierzenia zgodną z art. 28 RODO (cel wyłącznie wdrożenie, subprocesorzy, usunięcie/zwrot po zakończeniu, audyt), zakaz użycia danych do trenowania.
**Fallback (minimum akceptowalne):** Wyłącznie dane zanonimizowane i zagregowane, bez danych osobowych i tajemnicy przedsiębiorstwa, za odrębną pisemną zgodą i z prawem wycofania.
**Klauzula z bazy:** `references/baza-klauzul/` (RODO / powierzenie — zob. INDEX), `references/checklist-dpa-art28.md`

#### 5. Zobowiązanie wydrążone: „dołoży starań", „niezwłocznie", brak specyfikacji, odbioru i gwarancji — § 1, § 2, § 3
**Strona dotknięta:** Zamawiający (płaci 480.000 zł ryczałtu za starania); Wykonawca dotknięty wtórnie ryzykiem sporu o zakres.
**Opis:** (a) „Dołoży starań w celu wdrożenia" to zobowiązanie starannego działania, nie rezultatu; przy ERP z ryczałtem rezultat powinien być przedmiotem umowy. (b) Termin „niezwłocznie po podpisaniu" jest nieliczalny (art. 455 KC [NIEZWERYFIKOWANE]); brak daty końcowej i harmonogramu. (c) Zakres w „Załączniku nr 1", którego tekst nie został dołączony do umowy [BRAK DANYCH]. (d) Brak kamieni milowych, procedury odbioru, klasyfikacji wad, gwarancji i rękojmi; wynagrodzenie nie jest powiązane z odbiorem. (e) Brak jakiejkolwiek sankcji za zwłokę Wykonawcy. Przy kwalifikacji jako zlecenie brak rezultatu oznacza, że Zamawiający nie ma roszczenia o działający system.
**Skutek:** Wykonawca spełnia umowę „starając się", fakturuje całość, a Zamawiający nie ma ani terminu do egzekwowania, ani kryterium wady, ani sankcji. Razem z flagą 2 (brak odpowiedzialności) i 6 (wyjście w każdej chwili) tworzy układ, w którym Wykonawca niczym nie ryzykuje (efekt kumulatywny § 1 + § 2 + § 3 + § 5 ust. 1 + § 7).
**Rekomendacja (preferowana):** „Wykonawca zobowiąże się wdrożyć … i osiągnąć rezultat opisany w Załączniku nr 1"; harmonogram z kamieniami milowymi i datą końcową; protokoły odbioru, kryteria akceptacji, klasyfikacja wad; płatność etapowa; gwarancja min. 12–24 mies.; kary za zwłokę Wykonawcy z sufitem.
**Fallback (minimum akceptowalne):** Data końcowa i odbiór końcowy z protokołem, płatność 30–40% po odbiorze, gwarancja min. 12 mies.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md` (oraz klauzule odbioru i gwarancji z INDEX)

#### 6. Asymetria wypowiedzenia: Zamawiający nie może, Wykonawca może w każdym czasie bez przyczyny — § 7
**Strona dotknięta:** Zamawiający (zamknięty w umowie bez wyjścia, a Wykonawca wychodzi, kiedy chce).
**Opis:** Zamawiający nie może wypowiedzieć przed zakończeniem Wdrożenia, a „zakończenie" nie jest oznaczone w żaden sposób. Wykonawca wypowiada w każdym czasie bez przyczyny, bez okresu wypowiedzenia, bez rozliczenia, bez obowiązku wydania wykonanych prac i kodu (por. § 4 ust. 2). Zakaz wypowiedzenia z ważnych powodów może być bezskuteczny (art. 746 § 3 KC [NIEZWERYFIKOWANE]); jest także w kolizji z prawem odstąpienia (art. 491, 635 KC [NIEZWERYFIKOWANE]), co umowa pomija milczeniem. Kwalifikacja (zlecenie / dzieło) rozstrzyga o zakresie tych uprawnień, a umowa jej nie rozstrzyga.
**Skutek:** Wykonawca może porzucić projekt w połowie, zatrzymać zapłatę (wynagrodzenie ryczałtowe bez etapów) i nie ponieść żadnej odpowiedzialności (§ 5 ust. 1: szkoda nieumyślna = 0 zł).
**Rekomendacja (preferowana):** Symetria: wypowiedzenie obu stron z ważnych powodów (katalog), prawo odstąpienia Zamawiającego przy opóźnieniu i wadach, okres wypowiedzenia i procedura exit (wydanie prac, rozliczenie proporcjonalne do odebranych etapów).
**Fallback (minimum akceptowalne):** Prawo Zamawiającego do odstąpienia przy opóźnieniu > 30 dni; Wykonawca wypowiada tylko z ważnych powodów z 60-dniowym okresem i z obowiązkiem wydania stanu prac.
**Klauzula z bazy:** `references/baza-klauzul/` (wypowiedzenie i exit — zob. INDEX)

### 🟠 RYZYKA WYSOKIE

#### 7. Prawo stanu Delaware i sąd w Wilmington dla umowy spółek (z założenia krajowych) — § 8 ust. 1
**Strona dotknięta:** obie, bardziej Zamawiający (słabszy w sporze, płacący koszty).
**Opis:** Brak elementu obcego w treści umowy (obie spółki z o.o., wdrożenie w infrastrukturze Zamawiającego); wybór prawa obcego przy czysto krajowym stosunku bywa ograniczony (art. 3 ust. 3 rozporządzenia Rzym I [NIEZWERYFIKOWANE]); wskazany sąd jest nieproporcjonalnie odległy i kosztowny, a prawo i klauzule (kary, art. 473/483 KC) oceniane byłyby inaczej niż zakładają strony. Dodatkowo spór o wykonalność w Polsce.
**Skutek:** Koszt i trudność dochodzenia roszczeń (np. 480.000 zł) przewyższają wartość sporu; niepewność, które normy bezwzględnie obowiązujące wchodzą w grę.
**Rekomendacja (preferowana):** Prawo polskie, sąd właściwy dla siedziby pozwanego lub konkretny sąd w Polsce; ewentualnie arbitraż z oznaczeniem sądu polubownego.
**Fallback (minimum akceptowalne):** Prawo polskie + sąd wskazany z nazwy w Polsce.
**Klauzula z bazy:** `references/baza-klauzul/` (prawo właściwe i spory — zob. INDEX)

#### 8. Wynagrodzenie ryczałtowe bez harmonogramu płatności i bez powiązania z odbiorem — § 3
**Strona dotknięta:** Zamawiający.
**Opis:** Całość 480.000 zł netto, a moment wystawienia faktury nie jest określony [BRAK DANYCH]. Wykonawca może zafakturować od razu po podpisaniu, a termin 60 dni biegnie od doręczenia faktury. Brak zaliczek, etapów i potrąceń z tytułu wad.
**Skutek:** Pełna cena płatna za niewykonaną pracę; przy opóźnieniu zapłaty biegnie nieważna, ale rodząca spór kara (flaga 1).
**Rekomendacja (preferowana):** Płatność etapowa po protokołach odbioru; fakturowanie dopiero po odbiorze; prawo wstrzymania płatności w razie wad.
**Fallback (minimum akceptowalne):** Min. 30% po odbiorze końcowym; zatrzymanie 10% na okres gwarancji.
**Klauzula z bazy:** `references/baza-klauzul/04-wynagrodzenie.md` (zob. INDEX)

#### 9. Wsparcie powdrożeniowe „według wyłącznego uznania" Wykonawcy — § 5 ust. 3
**Strona dotknięta:** Zamawiający.
**Opis:** Zakres wsparcia ustala Wykonawca bez kryteriów, bez SLA, bez cennika, bez czasów reakcji; usytuowanie w paragrafie o odpowiedzialności sugeruje wyłączenie obowiązków. Wsparcie jest niezbędne po uruchomieniu ERP.
**Skutek:** Brak obowiązku naprawy błędów po wdrożeniu; Zamawiający uzależniony od woli Wykonawcy.
**Rekomendacja (preferowana):** Oddzielna umowa maintenance/SLA lub załącznik (zakres, godziny, czasy reakcji i naprawy, cennik poza zakresem).
**Fallback (minimum akceptowalne):** Obowiązek usuwania błędów krytycznych w oznaczonym terminie w okresie gwarancji.
**Klauzula z bazy:** `references/baza-klauzul/` (SLA / utrzymanie — zob. INDEX)

#### 10. Kod źródłowy „może, ale nie jest zobowiązany" przekazać — § 4 ust. 2
**Strona dotknięta:** Zamawiający.
**Opis:** Uprawnienie udaje obowiązek. Bez kodu źródłowego (i dokumentacji) prawa z § 4 ust. 1 są w praktyce bezużyteczne: brak możliwości utrzymania, zmiany, zmiany dostawcy (vendor lock-in).
**Skutek:** Uzależnienie od Wykonawcy, który jednocześnie może wypowiedzieć umowę w każdym czasie (§ 7 ust. 2) i ustalać zakres wsparcia (§ 5 ust. 3).
**Rekomendacja (preferowana):** Obowiązek wydania kodu i dokumentacji przy odbiorze, repozytorium; escrow dla komponentów Wykonawcy.
**Fallback (minimum akceptowalne):** Escrow kodu uruchamiany wypowiedzeniem, upadłością lub zaprzestaniem wsparcia.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟡 RYZYKA ŚREDNIE

#### 11. Poufność bez okresu, definicji, wyłączeń i sankcji — § 6
**Strona dotknięta:** obie strony; w praktyce Zamawiający (przekazuje dane biznesowe), a ochrona zostaje zneutralizowana przez § 8 ust. 2.
**Opis:** „Informacje przekazane w związku z Umową" bez definicji, bez wyłączeń (informacje publiczne, niezależnie opracowane), bez okresu po zakończeniu umowy i bez sankcji.
**Skutek:** Trudna egzekucja; spór o zakres.
**Rekomendacja (preferowana):** Definicja informacji poufnych, wyłączenia, okres trwania obowiązku po zakończeniu umowy (np. 5 lat; bezterminowo dla tajemnicy przedsiębiorstwa), kara lub odpowiedzialność poza capem; pierwszeństwo nad § 8.
**Fallback (minimum akceptowalne):** Definicja + wyłączenia + 3 lata po zakończeniu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 12. Ryczałt przy otwartym zakresie i uwagach „na bieżąco" — § 2 ust. 2, § 3 ust. 1
**Strona dotknięta:** Wykonawca.
**Opis:** Zamawiający zgłasza uwagi „na bieżąco" bez trybu, terminów i skutków; brak procedury zmian (change request), brak katalogu obowiązków współdziałania Zamawiającego (dostęp, dane, decyzje). Przy ryczałcie i nieoznaczonym zakresie ryzyko rozrostu prac (scope creep) spada na Wykonawcę.
**Skutek:** Spór o to, co mieści się w 480.000 zł; zarzut opóźnienia z winy Zamawiającego bez podstawy.
**Rekomendacja (preferowana):** Procedura zmian (wycena, akceptacja), zamknięty katalog obowiązków Zamawiającego z terminami, domniemanie akceptacji po upływie terminu.
**Fallback (minimum akceptowalne):** Termin 5 dni roboczych na uwagi po każdym kamieniu milowym; zmiany tylko pisemnie.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 13. Niejasna kwalifikacja umowy (dzieło / zlecenie) i niezdefiniowane pojęcia — § 1, całość
**Strona dotknięta:** obie.
**Opis:** „Dołoży starań" (zlecenie, art. 734/750 KC [NIEZWERYFIKOWANE]) kontra ryczałt za „wdrożenie" (dzieło, art. 627 KC [NIEZWERYFIKOWANE]). Pojęcia „Wdrożenie" i „Umowa" pisane wielką literą bez definicji; brak słowniczka; „Załącznik nr 1" nie jest dołączony.
**Skutek:** Spór o reżim (odbiór, rękojmia, wypowiedzenie, odstąpienie).
**Rekomendacja (preferowana):** Wprost wskazać charakter (umowa o dzieło / mieszana) i zdefiniować pojęcia.
**Fallback (minimum akceptowalne):** Słowniczek i dołączenie załącznika.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 14. Niekompletne oznaczenie stron i reprezentacji — nagłówek
**Strona dotknięta:** obie.
**Opis:** Brak KRS, NIP, adresów, osób reprezentujących i podstawy umocowania (dane oznaczone jako fikcyjne, więc ocena dotyczy konstrukcji dokumentu).
**Skutek:** Ryzyko zarzutu wadliwej reprezentacji; trudność w dochodzeniu roszczeń.
**Rekomendacja (preferowana):** Pełne oznaczenie stron z KRS/NIP/adresem i reprezentacją.
**Fallback (minimum akceptowalne):** KRS i NIP oraz oświadczenie o umocowaniu.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### 🟢 RYZYKA NISKIE

#### 15. Termin płatności 60 dni na granicy limitu — § 3 ust. 2
**Strona dotknięta:** Wykonawca (długie finansowanie cudzego projektu).
**Opis:** 60 dni od doręczenia faktury mieści się w granicach ustawy o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych (art. 7 ust. 2 [NIEZWERYFIKOWANE]); przy relacji duży dłużnik / MŚP wierzyciel to wartość sztywna (ust. 2a). Nie jest wadą, ale wymaga zgodności z tym limitem.
**Skutek:** Brak, o ile faktura jest doręczana niezwłocznie po odbiorze.
**Rekomendacja (preferowana):** Zostawić 30 dni od doręczenia faktury po odbiorze.
**Fallback (minimum akceptowalne):** 60 dni od faktury wystawionej po odbiorze.
**Klauzula z bazy:** `references/baza-klauzul/04-wynagrodzenie.md`

#### 16. Pozorna wzajemność i puste postanowienie o współpracy — § 1 ust. 2
**Strona dotknięta:** obie (redakcyjnie).
**Opis:** „Strony wzajemnie zobowiązują się do współpracy" bez treści, przy jednostronnym ukształtowaniu pozostałych postanowień (kary, odpowiedzialność, wypowiedzenie).
**Skutek:** Brak egzekwowalnego obowiązku; mylący sygnał symetrii.
**Rekomendacja (preferowana):** Zastąpić katalogiem obowiązków współdziałania z terminami (zob. flaga 12).
**Fallback (minimum akceptowalne):** Pozostawić z odesłaniem do załącznika.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

### ✓ Obszary bez zastrzeżeń

Brak obszarów całkowicie czystych. Każdy z dziewięciu obszarów bramki kompletności ma flagę: odpowiedzialność i kary (1, 2), prawa autorskie (3, 10), definicje i logika (13, 16), reprezentacja (14), wypowiedzenie i exit (6), RODO (4), tytuł prawny (13), poufność (11), spory (7). Efekt kumulatywny (test pięciopunktowy, krok 5): § 1 + § 2 + § 3 + § 5 + § 7 łącznie pozbawiają Zamawiającego realnego środka ochrony, mimo że część postanowień z osobna dałaby się obronić; w razie sporu rośnie argument o sprzeczności z zasadami współżycia społecznego (art. 58 § 2, art. 353¹ KC [NIEZWERYFIKOWANE]). Trigger mikroprzedsiębiorcy (art. 385⁵ KC): nie dotyczy, obie strony to spółki z o.o.

Bramka ius cogens (R10) uruchomiona: trafienia przy § 5 ust. 2 (art. 483 § 1 KC), § 5 ust. 1 (art. 473 § 2 KC), § 4 ust. 1 (art. 41 ust. 2 PrAut), § 8 ust. 2 (art. 28 RODO).

---

## OCENA BEZPIECZEŃSTWA: 5/100

Sześć flag krytycznych, w tym cztery będące naruszeniem normy bezwzględnej lub jej obejściem, cztery wysokie; ryzyko pieniężne rozłożone wyłącznie na Zamawiającego (kara bez sufitu, brak odpowiedzialności Wykonawcy, 0 zł ekspozycji Wykonawcy przy 480.000 zł zapłaconym). Jedyne elementy neutralne to termin płatności i wyłączenie poufności z pozorną wzajemnością.

**Werdykt:** NIE PODPISYWAĆ (🟥 CZERWONY: co najmniej jedno ryzyko 🔴 oraz naruszenie normy bezwzględnej).

### Klauzule z bazy KTZR do uzupełnienia

🔴 Kara i odpowiedzialność → `references/baza-klauzul/10-kary-umowne.md`, `11-odpowiedzialnosc.md`
🔴 Prawa autorskie → `references/baza-klauzul/08-prawa-autorskie-ip.md`
🔴 Dane / AI → `references/checklist-dpa-art28.md` oraz klauzule RODO z INDEX
🔴 Terminy, odbiór, wypowiedzenie → `references/baza-klauzul/07-terminy-kamienie-milowe.md` i klauzule z INDEX
🟡 Poufność → `references/baza-klauzul/09-poufnosc.md`

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
