```
konfiguracja: fable-skill
commit skilla: fa26dc0
przebieg: 1 z 1
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"
```

## AUDYT RYZYK — Umowa ramowa T&M — rozwój oprogramowania (QUANTA DEV sp. z o.o. / MERIDIAN FINANCE S.A.)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie. Umowa nie przenosi na Zamawiającego praw do kodu, a Wykonawca ma cap, który po zsumowaniu kar spoza limitu, indemnity bez sufitu i zakazu konkurencji z karą 300 000 zł za przypadek przestaje cokolwiek ograniczać. Oba problemy trzeba wynegocjować przed podpisem.

Tryb: express (jeden przebieg, bez STOP-ów) · audyt neutralny (przy każdej fladze wskazana strona dotknięta) · tryb PRAWNIK · brak `practice-profile.md`, więc stosuję domyślne progi KTZR · brak MCP `legal-cite`, więc każde powołanie przepisu oznaczam [NIEZWERYFIKOWANE].

---

### Krok 0b — Bramka ius cogens (R10)

| Norma | Wynik skanu |
|---|---|
| art. 473 § 2 KC [NIEZWERYFIKOWANE]: zakaz wyłączenia lub ograniczenia odpowiedzialności za szkodę umyślną | ❌ **TRAFIENIE.** § 3 ust. 1 ogranicza łączną odpowiedzialność Wykonawcy bez wyjątku dla winy umyślnej, więc w tym zakresie postanowienie jest nieważne (art. 58 § 3 KC [NIEZWERYFIKOWANE]). Zob. 🔴 4. |
| art. 483 § 1 KC [NIEZWERYFIKOWANE]: kara za zobowiązanie pieniężne | ✓ brak. Wszystkie kary z § 2 zabezpieczają zobowiązania niepieniężne (terminowość, jakość, zakaz konkurencji). |
| art. 484 § 2 KC [NIEZWERYFIKOWANE]: wyłączenie miarkowania z góry | ✓ brak takiego zastrzeżenia. |
| art. 119 KC [NIEZWERYFIKOWANE]: zmiana terminów przedawnienia | ✓ brak. |
| art. 16 i art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE] | ✓ brak próby obejścia, bo umowa w ogóle nie reguluje praw autorskich. To osobna, poważna luka, nie naruszenie normy (zob. 🔴 1). |
| ustawa o przeciwdziałaniu nadmiernym opóźnieniom: terminy zapłaty | ✓ brak przekroczenia, ale tylko dlatego, że umowa nie przewiduje żadnego terminu zapłaty (zob. 🟠 7). |
| RODO art. 28 ust. 3 [NIEZWERYFIKOWANE] | [BRAK DANYCH]. Umowa nie mówi, czy Wykonawca ma dostęp do danych osobowych (zob. 🟡 1). |
| Trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]) | — nieaktywny. Obie strony to spółki kapitałowe (sp. z o.o. i S.A.). |

**Test kumulatywny (§ 2 + § 3 + § 5 łącznie):** po stronie sankcji umowa przechyla się na korzyść Zamawiającego. Wykonawcę obciążają trzy kary poza capem, które się sumują, odszkodowanie uzupełniające, indemnity bez limitu i zakaz konkurencji bez ekwiwalentu. Zamawiającego nie obciąża żadna kara. Po stronie komercyjnej i IP przechył idzie w drugą stronę: podwyżka 8% działa tylko w górę, auto-renewal nie daje prawa wypowiedzenia, prawa do kodu zostają przy Wykonawcy, a Zamawiający nie ma terminu ani procedury akceptacji godzin. Każda klauzula z osobna mieści się co do zasady w swobodzie umów (art. 353¹ KC [NIEZWERYFIKOWANE]). Najbliżej granicy art. 58 § 2 KC [NIEZWERYFIKOWANE] jest suma § 2 ust. 3, § 2 ust. 4 i § 5: zakaz konkurencji bez wynagrodzenia, z karą 300 000 zł za każdy przypadek, poza capem.

---

### 🧮 Rachunek ekspozycji (R12)

**Liczby wyciągnięte z umowy:** stawka 220 zł netto/h (§ 1 ust. 2) · 2 Specjalistów × 160 h/mies., zaangażowanie szacowane, nie gwarantowane (§ 1 ust. 2) · okres 24 mies. (§ 1 ust. 3) · kara 0,5% wynagrodzenia miesięcznego za dzień zwłoki, bez sufitu (§ 2 ust. 1) · kara 5 000 zł za przypadek naruszenia jakości (§ 2 ust. 2) · kara 300 000 zł za przypadek naruszenia zakazu konkurencji (§ 2 ust. 3) · cap = 12-miesięczne wynagrodzenie (§ 3 ust. 1) · auto-renewal 12 mies., sprzeciw najpóźniej 90 dni przed końcem (§ 4 ust. 1) · podwyżka stawki o 8% za każdy okres przedłużenia (§ 4 ust. 2) · zakaz konkurencji przez okres umowy + 24 mies. (§ 5).

**Brakuje w umowie:** daty zawarcia i dnia rozpoczęcia · terminu płatności · minimalnego i maksymalnego wolumenu godzin · częstotliwości przeglądów kodu i progu jakości (Załącznik nr 2 nie został dołączony) · definicji „wynagrodzenia miesięcznego” i „12-miesięcznego wynagrodzenia” · marży Wykonawcy. Każda z tych pozycji to [BRAK DANYCH].

**Założenie bazowe (jawne):** wynagrodzenie miesięczne liczę według szacowanego zaangażowania z § 1 ust. 2. W modelu T&M realna kwota co miesiąc będzie inna, więc wszystkie wyniki poniżej są szacunkiem na tej podstawie.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Godziny miesięcznie | 2 Specjalistów × 160 h | 2 × 160 | **320 h** |
| Wynagrodzenie miesięczne (szac.) | 220 zł/h × 320 h | 220 × 320 | **70 400 zł netto** |
| Wartość umowy — okres podstawowy (szac.) | 24 mies. | 70 400 × 24 | **1 689 600 zł netto** |
| Cap nominalny (wariant A: 12 × szac. wynagrodzenie) | „12-miesięcznego wynagrodzenia” | 70 400 × 12 | **844 800 zł** = 844 800 / 1 689 600 = **50%** wartości umowy |
| Cap nominalny (wariant B: wynagrodzenie faktycznie wypłacone za 12 mies. wstecz) | jw. (umowa nie rozstrzyga) | np. w 3. miesiącu: 70 400 × 3 | **211 200 zł**, czyli 25% wariantu A. Cap rośnie z czasem i przez pierwszy rok jest niższy od wariantu A. |
| Kara za zwłokę — stawka dzienna | 0,5% wynagrodzenia miesięcznego | 0,005 × 70 400 | **352 zł/dzień** |
| Kara za zwłokę — 30 dni | jw. | 352 × 30 | 10 560 zł |
| Kara za zwłokę — 90 dni | jw. | 352 × 90 | 31 680 zł |
| Kara za zwłokę — 365 dni | jw. | 352 × 365 | 128 480 zł |
| Kara za zwłokę — maksimum teoretyczne, jeden strumień, cały okres podstawowy (założenie: 730 dni; dokładna liczba zależy od daty startu [BRAK DANYCH]) | brak sufitu | 352 × 730 | **256 960 zł** |
| Kara za zwłokę — dwa Przyrosty opóźnione jednocześnie | kara „za zwłokę w dostarczeniu Przyrostu”, czyli prawdopodobnie liczona od każdego Przyrostu osobno | 352 × 2 | 704 zł/dzień. Każdy kolejny równoległy Przyrost dodaje 352 zł/dzień. |
| Kara jakościowa — jednostkowo | 5 000 zł za przypadek | 5 000 / 70 400; 5 000 / 220 | = **7,1%** wynagrodzenia miesięcznego = równowartość **22,7 h** pracy |
| Kara jakościowa — scenariusz: 1 przypadek na sprint 2-tygodniowy przez 24 mies. (częstotliwość przeglądów [BRAK DANYCH]) | brak sufitu | 104 tyg. / 2 = 52 sprinty; 52 × 5 000 | **260 000 zł** |
| Kara jakościowa — scenariusz: 1 przypadek tygodniowo | jw. | 104 × 5 000 | 520 000 zł |
| Kara za zakaz konkurencji — 1 przypadek | 300 000 zł | 300 000 / 70 400; 300 000 / 1 689 600 | = **4,26** wynagrodzenia miesięcznego = **17,8%** wartości umowy |
| Kara za zakaz konkurencji — 3 przypadki (np. trzech klientów z branży Zamawiającego) | „za każdy przypadek naruszenia”, sumowanie | 3 × 300 000 | **900 000 zł**, czyli 900 000 / 844 800 = **1,07× cap**. Sama ta kara przekracza limit. |
| Kary poza capem — scenariusz bazowy (zwłoka max 1 strumień + jakość 1/sprint + 1 naruszenie zakazu) | § 2 ust. 4: sumowanie, poza capem | 256 960 + 260 000 + 300 000 | **816 960 zł** = 0,97× cap |
| Indemnity IP (§ 3 ust. 2) | „wszelkiej odpowiedzialności”, „wszelkie (…) koszty” | sufit: brak; relacja do capu niejasna | **otwarta / [BRAK DANYCH]** |
| Odszkodowanie uzupełniające ponad kary (§ 2 ust. 4) | „na zasadach ogólnych” | relacja do capu niejasna | **otwarte / [BRAK DANYCH]** |
| Wina umyślna | ustawowo poza capem (art. 473 § 2 KC [NIEZWERYFIKOWANE]) | — | **bez limitu** |
| **Efektywna ekspozycja Wykonawcy (scenariusz bazowy)** | — | cap 844 800 + kary 816 960 | **1 661 760 zł** = 1 661 760 / 844 800 = **1,97× cap nominalny** = 1 661 760 / 1 689 600 = **98,4% szacowanej wartości umowy (0,98×)** + indemnity bez sufitu + odszkodowanie uzupełniające + wina umyślna. **Górnej granicy brak.** |
| Asymetria kar | Wykonawca: 3 rodzaje kar; Zamawiający: 0 | 816 960 zł : 0 zł | stosunek **nieoznaczony (∞)**. Zamawiający nie ma ani jednej kary. |
| Asymetria zakazów | Wykonawca: zakaz konkurencji na okres umowy + 24 mies.; Zamawiający: brak | min. 24 + 24 | Wykonawca jest związany **co najmniej 48 mies.** bez dodatkowego wynagrodzenia |
| Data graniczna — sprzeciw wobec przedłużenia | 90 dni przed końcem okresu | 730 − 90 | **dzień ok. 640.** umowy (ok. koniec 21. miesiąca). Daty kalendarzowej nie da się ustalić, bo umowa nie wskazuje daty zawarcia [BRAK DANYCH]. |
| Stawka po 1. przedłużeniu | +8% | 220 × 1,08 | **237,60 zł/h**. Miesięcznie: 237,60 × 320 = **76 032 zł**; za 12 mies.: 76 032 × 12 = **912 384 zł** |
| Koszt przegapienia okna (Zamawiający) | jw. | 912 384 zł za okres; w tym podwyżka: (76 032 − 70 400) × 12 = 5 632 × 12 | **912 384 zł** zobowiązania (szac.), w tym **67 584 zł** samej podwyżki |
| Stawka po 2. przedłużeniu | +8% „względem okresu poprzedniego”, czyli składane | 237,60 × 1,08 | **256,61 zł/h** (256,608). Miesięcznie: 256,608 × 320 = 82 114,56 zł; rocznie: 985 374,72 zł |
| Stawka po 3. przedłużeniu | jw. | 220 × 1,08³ = 220 × 1,259712 | **277,14 zł/h** (+26,0% względem stawki wyjściowej). Miesięcznie: 88 683,72 zł; rocznie: 1 064 204,70 zł |
| Okres podstawowy + 1 przedłużenie (szac.) | — | 1 689 600 + 912 384 | **2 601 984 zł netto** |
| Termin płatności | brak | — | **[BRAK DANYCH]** |

**Wniosek z rachunku:** cap w § 3 ust. 1 wygląda na limit, ale nim nie jest. Same kary spoza capu w umiarkowanym scenariuszu wynoszą 0,97× cap. Trzy naruszenia zakazu konkurencji przekraczają cap w pojedynkę, a indemnity, odszkodowanie uzupełniające i wina umyślna nie mają sufitu. Efektywna ekspozycja Wykonawcy to co najmniej 1,97× cap, czyli 98% szacowanej wartości całej umowy, i nie ma górnej granicy. Według R12 cap jest iluzoryczny, co daje flagę 🔴. Po stronie Zamawiającego rachunek pokazuje drugie ryzyko: składaną podwyżkę i auto-renewal bez prawa wypowiedzenia. Jedno przegapione okno 90 dni wiąże go zobowiązaniem rzędu 912 384 zł.

---

### 🔴 RYZYKA KRYTYCZNE

#### 1. Brak przeniesienia autorskich praw majątkowych i brak licencji do kodu — umowa jako całość (brak postanowienia)
**Strona dotknięta:** Zamawiający.
**Opis:** umowa o rozwój oprogramowania wartą ok. 1 689 600 zł netto nie zawiera ani jednego postanowienia o prawach autorskich: brak przeniesienia, pól eksploatacji, licencji, momentu przejścia praw, przekazania kodu źródłowego i klauzuli open source. Przeniesienie wymaga wyraźnego wymienienia pól eksploatacji (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]) i formy pisemnej (art. 53 PrAut [NIEZWERYFIKOWANE]). Bez tego prawa do programu zostają przy Wykonawcy albo jego twórcach (por. art. 74 ust. 3 PrAut [NIEZWERYFIKOWANE] dla programów pracowniczych).
**Skutek:** Zamawiający płaci za kod, którego nie posiada. W najlepszym razie korzysta z niego na podstawie dorozumianej licencji o niejasnym zakresie, bez prawa do modyfikacji przez innego dostawcę. Po zakończeniu umowy grozi mu vendor lock-in. Na tym tle § 3 ust. 2 wygląda paradoksalnie: Wykonawca odpowiada za naruszenia IP w kodzie, którego prawa zachowuje.
**Rekomendacja (preferowana):** przeniesienie autorskich praw majątkowych do każdego Przyrostu z chwilą zapłaty wynagrodzenia za okres, w którym powstał, z zamkniętym wyliczeniem pól eksploatacji, prawem do utworów zależnych, wydaniem kodu źródłowego, zobowiązaniem do niewykonywania praw osobistych i klauzulą anty-copyleft.
**Fallback (minimum akceptowalne):** wyłączna, nieodwołalna licencja z wymienionymi polami eksploatacji, prawem modyfikacji przez podmioty trzecie i przekazaniem kodu źródłowego, w formie pisemnej (art. 67 ust. 5 PrAut [NIEZWERYFIKOWANE]).
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 2. Cap iluzoryczny — efektywna ekspozycja otwarta — § 2 ust. 4 w zw. z § 3 ust. 1–2
**Strona dotknięta:** Wykonawca.
**Opis:** „Kary umowne podlegają sumowaniu i nie są wliczane do limitu odpowiedzialności z § 3”. Do tego „Zamawiający może dochodzić odszkodowania przewyższającego kary umowne na zasadach ogólnych” (opt-in z art. 484 § 1 KC [NIEZWERYFIKOWANE]). Żadna z trzech kar nie ma sufitu (rachunek wyżej), a indemnity z § 3 ust. 2 nie ma limitu kwotowego.
**Skutek:** zgodnie z rachunkiem efektywna ekspozycja w scenariuszu bazowym wynosi 1 661 760 zł, czyli 1,97× cap i 98,4% szacowanej wartości umowy, a do tego dochodzą pozycje bez sufitu. Limit 844 800 zł nie chroni Wykonawcy przed realnym scenariuszem sporu.
**Rekomendacja (preferowana):** kary wliczane do capu; łączny sufit kar 10–20% wynagrodzenia z 12 miesięcy; indemnity IP objęte capem albo odrębnym sublimitem; skreślenie odszkodowania uzupełniającego (kara jako wyłączny środek, z wyjątkiem winy umyślnej).
**Fallback (minimum akceptowalne):** kary poza capem, ale z łącznym sufitem (np. 30% wartości umowy za okres 12 mies.); odszkodowanie uzupełniające objęte capem z § 3 ust. 1; sublimit indemnity (np. 1× cap).
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`, `references/baza-klauzul/10-kary-umowne.md`

#### 3. Zakaz konkurencji: 24 mies. po umowie, bez ekwiwalentu, zakres niezdefiniowany, kara 300 000 zł za każdy przypadek — § 5 w zw. z § 2 ust. 3
**Strona dotknięta:** Wykonawca (ekspozycja finansowa i ograniczenie działalności) oraz Zamawiający (ryzyko, że zakaz i kara okażą się nieegzekwowalne).
**Opis:** Wykonawca, czyli software house, nie może świadczyć usług na rzecz „podmiotów prowadzących działalność konkurencyjną wobec Zamawiającego” przez okres umowy i 24 miesiące po niej. „Zakaz nie jest związany z dodatkowym wynagrodzeniem”. Pojęcie działalności konkurencyjnej nie ma definicji ani granic przedmiotowych i terytorialnych. Przy Zamawiającym z sektora finansowego może to oznaczać zakaz obsługi całego sektora przez co najmniej 48 mies. (24 + 24), a dłużej przy każdym przedłużeniu z § 4. Kara 300 000 zł to 4,26× wynagrodzenia miesięcznego, sumuje się, działa poza capem i ma doliczane odszkodowanie uzupełniające.
**Skutek:** dla Wykonawcy trzy przypadki dają 900 000 zł, czyli więcej niż cały cap (1,07×). Dla Zamawiającego: przy braku ekwiwalentu, niedookreślonym zakresie i długim okresie sąd może uznać zakaz za sprzeczny z zasadami współżycia lub naturą stosunku (art. 353¹ i art. 58 § 2 KC [NIEZWERYFIKOWANE]), a karę za rażąco wygórowaną i ją zmiarkować (art. 484 § 2 KC [NIEZWERYFIKOWANE]). Zamawiający może więc zostać bez ochrony, na którą liczył.
**Rekomendacja (preferowana):** zamknięta definicja działalności konkurencyjnej (lista podmiotów lub produktów, segment, terytorium); okres po umowie 6–12 mies.; zakaz ograniczony do Specjalistów pracujących dla Zamawiającego; kara proporcjonalna (np. 1–2× wynagrodzenie miesięczne) z łącznym sufitem.
**Fallback (minimum akceptowalne):** utrzymanie 24 mies. tylko z odrębnym ekwiwalentem za okres po umowie, zamkniętą listą konkurentów i karą objętą capem.
**Klauzula z bazy:** `references/baza-klauzul/13-non-solicitation.md` (wariant „Zakaz konkurencji dostawcy IT — zakres rozszerzony” z definicją Działalności Konkurencyjnej; red flag: okres > 24 mies. i brak wynagrodzenia karencyjnego)

#### 4. Cap bez wyjątku dla winy umyślnej — § 3 ust. 1 (bramka ius cogens)
**Strona dotknięta:** Wykonawca (fałszywe poczucie limitu) i obie strony (wada redakcyjna rodząca spór o zakres nieważności).
**Opis:** „Łączna odpowiedzialność Wykonawcy ograniczona jest do 12-miesięcznego wynagrodzenia” bez wyłączenia szkód wyrządzonych umyślnie. Ograniczenie odpowiedzialności za szkodę umyślną jest nieważne (art. 473 § 2 KC [NIEZWERYFIKOWANE]), co do zasady tylko w tym zakresie (art. 58 § 3 KC [NIEZWERYFIKOWANE]).
**Skutek:** przy szkodzie umyślnej cap nie działa. Pozostała część limitu co do zasady się utrzymuje, ale druga strona dostaje argument do podważania całego § 3 ust. 1. Nie da się tego wynegocjować, bo to norma bezwzględna.
**Rekomendacja (preferowana):** dopisać wprost: „Ograniczenie nie dotyczy szkód wyrządzonych umyślnie”, a dla ochrony Zamawiającego rozszerzyć wyjątek na rażące niedbalstwo.
**Fallback (minimum akceptowalne):** sam wyjątek dla winy umyślnej, zgodny z ustawą.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (klauzula wzorcowa z wyłączeniem winy umyślnej)

---

### 🟠 RYZYKA WYSOKIE

#### 1. Kara za zwłokę w dostarczeniu Przyrostu sprzeczna z modelem T&M, bez sufitu i bez wyłączenia zwłoki z przyczyn Zamawiającego — § 2 ust. 1
**Strona dotknięta:** Wykonawca (ekspozycja); Zamawiający (wykonalność kary).
**Opis:** w modelu Time & Material (§ 1 ust. 1) Wykonawca sprzedaje godziny, czyli staranne działanie, a zakres i priorytety sprintu wyznacza zwykle Zamawiający. Kara „0,5% wynagrodzenia miesięcznego za każdy rozpoczęty dzień zwłoki” wiąże się z rezultatem („Przyrostu”) i „harmonogramu sprintu”, których umowa nie definiuje. Baza kary („wynagrodzenia miesięcznego”) w T&M zmienia się co miesiąc. Kara nie ma sufitu i najpewniej nalicza się od każdego Przyrostu osobno.
**Skutek:** 352 zł/dzień na jeden Przyrost; 256 960 zł przy maksimum teoretycznym jednego strumienia; każdy równoległy Przyrost dodaje 352 zł/dzień. Kara biegnie także wtedy, gdy zwłokę wywołał Zamawiający (zmiana backlogu, brak odbioru, brak dostępu). Dla Zamawiającego: niedookreślone podstawy kary (Przyrost, harmonogram) utrudnią jej wyegzekwowanie.
**Rekomendacja (preferowana):** w T&M zastąpić karę za zwłokę mechanizmem SLA lub obniżeniem stawki za godziny niezafakturowane albo skreślić ją; jeśli zostaje, to z definicjami (Przyrost, Sprint, Harmonogram), wyłączeniem zwłoki z przyczyn Zamawiającego, bazą „wynagrodzenie netto za poprzedni miesiąc kalendarzowy” i sufitem.
**Fallback (minimum akceptowalne):** sufit kary za zwłokę 10% wynagrodzenia miesięcznego na Przyrost i 20% łącznie w miesiącu, liczony do capu.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 2. Kara jakościowa oparta na nieistniejącym Załączniku nr 2, bez limitu liczby przypadków — § 2 ust. 2
**Strona dotknięta:** Wykonawca (ekspozycja); Zamawiający (wymagalność kary).
**Opis:** kara 5 000 zł za „wynik przeglądu poniżej progu z Załącznika nr 2”. Załącznika nie dołączono, a Załącznika nr 1 umowa w ogóle nie wymienia, więc oba są osierocone (Złota Reguła 4). Nie wiadomo, kto, jak często i jakim narzędziem przeprowadza przegląd ani czy Wykonawca może poprawić kod przed naliczeniem kary.
**Skutek:** 5 000 zł to 7,1% wynagrodzenia miesięcznego, czyli 22,7 h pracy za jeden przegląd. Przy jednym przypadku na sprint daje to 260 000 zł, a przy jednym tygodniowo 520 000 zł, wszystko poza capem. Dla Zamawiającego: bez progu kara jest nieoznaczona i trudna do dochodzenia.
**Rekomendacja (preferowana):** dołączyć Załącznik nr 2 z mierzalnym progiem (np. metryki narzędzia statycznej analizy), procedurą przeglądu, terminem na poprawkę i karą dopiero za brak poprawki; dodać łączny sufit miesięczny.
**Fallback (minimum akceptowalne):** kara tylko za powtórne niespełnienie progu w tym samym Przyroście, z sufitem miesięcznym (np. 10% wynagrodzenia miesięcznego).
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Indemnity IP otwarta: bez limitu, bez procedury, bez wyłączeń — § 3 ust. 2
**Strona dotknięta:** Wykonawca.
**Opis:** Wykonawca „zwolni Zamawiającego z wszelkiej odpowiedzialności” i „pokryje wszelkie związane z tym koszty, w tym koszty obsługi prawnej”. Brakuje relacji do capu (sformułowanie „Łączna odpowiedzialność” w ust. 1 sugeruje, że cap obejmuje indemnity, ale tego nie przesądza), obowiązku zawiadomienia, kontroli nad obroną (defense control) i wyłączeń dla naruszeń wynikających z materiałów, specyfikacji lub poleceń Zamawiającego. W T&M te ostatnie są typowe, bo zakres wyznacza Zamawiający.
**Skutek:** ekspozycja bez sufitu [BRAK DANYCH], również za naruszenia, które spowodował Zamawiający. Spór o to, czy § 3 ust. 2 mieści się w limicie z ust. 1.
**Rekomendacja (preferowana):** indemnity ograniczone do naruszeń spowodowanych przez Wykonawcę, z wyłączeniem materiałów i poleceń Zamawiającego; zawiadomienie w 14 dni; obronę przejmuje Wykonawca; sublimit albo objęcie capem.
**Fallback (minimum akceptowalne):** indemnity poza capem, ale z procedurą (zawiadomienie, defense control, zakaz ugody bez zgody) i wyłączeniem dla materiałów Zamawiającego.
**Klauzula z bazy:** `references/baza-wiedzy/07-indemnifikacja-kary-umowne.md` (wzorzec indemnity IP), `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 4. Auto-renewal z automatyczną, składaną podwyżką 8% i oknem 90 dni, którego nie da się policzyć w kalendarzu — § 4 ust. 1–2
**Strona dotknięta:** Zamawiający (koszt i lock-in); obie strony (brak daty startu).
**Opis:** po 24 mies. umowa przedłuża się o 12 mies., „chyba że którakolwiek ze Stron złoży oświadczenie o nieprzedłużaniu najpóźniej na 90 dni przed końcem bieżącego okresu”. Stawka rośnie „o 8% względem okresu poprzedniego”, czyli składanie, bez związku ze wskaźnikiem (np. inflacją) i tylko w górę. Umowa nie podaje daty zawarcia ani początku biegu, więc ostatniego dnia na sprzeciw nie da się ustalić w kalendarzu (ok. dzień 640.).
**Skutek:** przegapienie okna oznacza 912 384 zł (szac.) za kolejne 12 mies., w tym 67 584 zł samej podwyżki. Po trzech przedłużeniach stawka wynosi 277,14 zł/h (+26,0%), a koszt roczny 1 064 204,70 zł. Każde przedłużenie wydłuża też zakaz konkurencji z § 5, co obciąża Wykonawcę.
**Rekomendacja (preferowana):** przedłużenie tylko za pisemnym porozumieniem; ewentualna waloryzacja raz w roku o wskaźnik inflacji GUS, dwustronna, z limitem; data zawarcia i data rozpoczęcia w umowie.
**Fallback (minimum akceptowalne):** okno sprzeciwu 30 dni, waloryzacja maks. 5% i nieskładana, plus prawo wypowiedzenia w okresie przedłużenia (zob. 🟠 5).
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md`, `references/baza-klauzul/06-wynagrodzenie.md`

#### 5. Brak wypowiedzenia, rozwiązania za naruszenie i procedury exit — umowa jako całość (brak postanowienia)
**Strona dotknięta:** obie strony; mocniej Zamawiający (brak przekazania kodu i wiedzy).
**Opis:** umowa terminowa (24 mies. + przedłużenia) bez prawa wypowiedzenia, bez rozwiązania w trybie natychmiastowym (istotne naruszenie, upadłość) i bez obowiązków przy zakończeniu: przekazania kodu, dokumentacji, dostępów i wsparcia migracji. Zostaje tylko ustawowe wypowiedzenie z ważnych powodów (art. 746 § 3 w zw. z art. 750 KC [NIEZWERYFIKOWANE]), sporne co do przesłanek i grożące roszczeniem odszkodowawczym.
**Skutek:** żadna strona nie wyjdzie z umowy wartej 1 689 600 zł bez sporu, nawet przy rażących naruszeniach. Zamawiający po zakończeniu nie ma tytułu do przejęcia kodu (por. 🔴 1).
**Rekomendacja (preferowana):** wypowiedzenie przez każdą ze Stron z okresem 1–3 mies.; rozwiązanie natychmiastowe po bezskutecznym wezwaniu (np. 14 dni); exit plan z przekazaniem kodu, dokumentacji i dostępów oraz wsparciem migracyjnym.
**Fallback (minimum akceptowalne):** wypowiedzenie z okresem 3 mies., najwcześniej po 12 mies., plus obowiązkowy exit plan.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md`, `references/baza-klauzul/18-zwrot-materialow.md`

#### 6. Brak klauzuli poufności — umowa jako całość (brak postanowienia)
**Strona dotknięta:** Zamawiający (instytucja z branży finansowej, która daje dostęp do kodu i systemów); pośrednio Wykonawca (brak ochrony jego know-how).
**Opis:** umowa zabezpiecza karą 300 000 zł zakaz konkurencji, ale nie zawiera żadnego obowiązku poufności: brak definicji informacji poufnych, okresu, wyłączeń i kary.
**Skutek:** ochrona tylko ustawowa (tajemnica przedsiębiorstwa, która wymaga wykazania przesłanek i podjętych środków). W sporze Zamawiający nie ma umownej podstawy ani kary za wyciek.
**Rekomendacja (preferowana):** obustronna poufność z modelem warstwowym okresów (np. 5 lat po umowie, bezterminowo dla tajemnicy przedsiębiorstwa), wyłączeniami standardowymi i karą proporcjonalną.
**Fallback (minimum akceptowalne):** poufność w okresie umowy + 3 lata, bez kary, ale z odszkodowaniem na zasadach ogólnych poza capem.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

#### 7. Brak mechanizmu rozliczeń: termin płatności, fakturowanie, akceptacja godzin, limit budżetu — § 1 ust. 2 (luka)
**Strona dotknięta:** Wykonawca (brak terminu zapłaty) i Zamawiający (otwarty koszt).
**Opis:** umowa podaje stawkę i szacowane (niewiążące) zaangażowanie, ale nie podaje terminu płatności, okresu rozliczeniowego, podstawy fakturowania (raport godzin), procedury akceptacji godzin ani limitu godzin lub budżetu bez zgody Zamawiającego. Nie określa też, czy szacunek 320 h/mies. jest dla któregoś ze Specjalistów minimum.
**Skutek:** Wykonawca nie ma umownego terminu zapłaty i zostaje przy regułach ustawowych. Zamawiający nie ma umownego sufitu kosztu: szacunek 1 689 600 zł netto za 24 mies. nikogo nie wiąże, a w razie sporu o godziny nie ma procedury. Do tego wynagrodzenie miesięczne jest bazą kary z § 2 ust. 1 i capu z § 3 ust. 1, więc nieostra podstawa rozliczeń przenosi się na obie te klauzule.
**Rekomendacja (preferowana):** rozliczenie miesięczne na podstawie zaakceptowanego raportu godzin (milcząca akceptacja po np. 5 dniach roboczych), termin płatności 14–30 dni od doręczenia faktury, miesięczny limit godzin wymagający pisemnej zgody na przekroczenie.
**Fallback (minimum akceptowalne):** termin płatności 30 dni, raport godzin jako podstawa faktury, informacja o przekroczeniu szacunku o więcej niż 10%.
**Klauzula z bazy:** `references/baza-klauzul/06-wynagrodzenie.md`

---

### 🟡 RYZYKA ŚREDNIE

#### 1. RODO — brak regulacji przy możliwym dostępie do danych osobowych — umowa jako całość (brak postanowienia)
**Strona dotknięta:** Zamawiający (jako administrator); Wykonawca (jako potencjalny procesor bez instrukcji).
**Opis:** umowa nie mówi, czy Specjaliści mają dostęp do środowisk z danymi osobowymi (produkcja, kopie testowe) [BRAK DANYCH]. Jeśli tak i jeśli relacja to administrator–procesor, potrzebna jest umowa powierzenia (art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]).
**Skutek:** przy powierzeniu bez umowy obie strony narażają się na sankcje administracyjne (art. 83 ust. 4 lit. a RODO [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** kwalifikacja ról i, w razie powierzenia, umowa z art. 28 jako załącznik; najlepiej zakaz pracy na danych produkcyjnych bez anonimizacji.
**Fallback (minimum akceptowalne):** oświadczenie, że Wykonawca nie ma dostępu do danych osobowych, z obowiązkiem zawarcia umowy powierzenia przed takim dostępem.
**Klauzula z bazy:** `references/baza-klauzul/14-rodo.md`, `references/checklist-dpa-art28.md`

#### 2. Pojęcia bez definicji i nieostre bazy kwotowe — § 1 ust. 2, § 2 ust. 1–2, § 3 ust. 1
**Strona dotknięta:** obie strony.
**Opis:** „Specjalistów”, „Przyrostu”, „Stron” są pisane wielką literą, a umowa ich nie definiuje (Złota Reguła 1). Nie zdefiniowano też „harmonogramu sprintu”, „wynagrodzenia miesięcznego” (szacowanego, fakturowane czy zapłacone; netto czy brutto) ani „12-miesięcznego wynagrodzenia” (pierwsze 12 mies., ostatnie 12 mies. czy 12 × średnia). Brakuje § Definicje.
**Skutek:** wartość capu waha się co najmniej między 211 200 zł (wariant B w 3. miesiącu) a 844 800 zł (wariant A). Podstawa kar jest sporna. Każda ze stron może wybrać wykładnię dla siebie korzystniejszą.
**Rekomendacja (preferowana):** § Definicje z pojęciami: Specjalista, Sprint, Przyrost, Harmonogram, Wynagrodzenie Miesięczne (netto, zafakturowane za dany miesiąc), Limit Odpowiedzialności (np. wynagrodzenie netto zapłacone w 12 mies. poprzedzających zdarzenie, nie mniej niż [kwota]).
**Fallback (minimum akceptowalne):** co najmniej definicje bazy capu i bazy kary z § 2 ust. 1.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 3. Kolizja § 2 ust. 4 i § 3 ust. 1 — czy odszkodowanie uzupełniające mieści się w capie — § 2 ust. 4 zd. 2 w zw. z § 3 ust. 1
**Strona dotknięta:** obie strony (spór interpretacyjny); finansowo Wykonawca.
**Opis:** § 2 ust. 4 wyłącza z limitu tylko „kary umowne”, a jednocześnie pozwala dochodzić odszkodowania ponad kary „na zasadach ogólnych”. Nie wiadomo, czy ta nadwyżka podlega capowi z § 3 ust. 1, czy też odesłanie do zasad ogólnych oznacza brak limitu.
**Skutek:** różnica między wykładniami jest równa całej nadwyżce szkody ponad kary, a tej kwoty nie da się z góry policzyć [BRAK DANYCH].
**Rekomendacja (preferowana):** dopisać wprost, że odszkodowanie uzupełniające podlega limitowi z § 3 ust. 1.
**Fallback (minimum akceptowalne):** odszkodowanie uzupełniające ograniczone do szkody rzeczywistej, z wyłączeniem utraconych korzyści.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

---

### 🟢 RYZYKA NISKIE

#### 1. Niepełna komparycja i brak daty oraz miejsca zawarcia — nagłówek umowy
**Strona dotknięta:** obie strony.
**Opis:** brak KRS, NIP, adresów, osób reprezentujących i podstawy umocowania, a także daty i miejsca zawarcia (Złota Reguła 8). Dane stron oznaczono jako fikcyjne. Brak daty ma przy tym skutek merytoryczny dla § 4 (zob. 🟠 4).
**Rekomendacja / Fallback:** uzupełnić komparycję według wzoru; minimum to KRS i imiona oraz nazwiska reprezentantów.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

#### 2. Forum sporu przy siedzibie Zamawiającego — § 6 ust. 1
**Strona dotknięta:** Wykonawca (niewielka niedogodność procesowa).
**Opis:** „sąd właściwy dla siedziby Zamawiającego”. Prawo polskie jest właściwe i to nie budzi zastrzeżeń. Forum jest jednostronnie wygodne dla Zamawiającego, co w B2B jest typowe i akceptowalne.
**Rekomendacja / Fallback:** neutralnie: sąd właściwy dla pozwanego albo mediacja przed wniesieniem pozwu; akceptowalne w obecnym brzmieniu.
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

---

### Bramka kompletności (R9) — dziewięć obszarów

| Obszar | Status |
|---|---|
| Odpowiedzialność i kary | ❌ 🔴 2, 🔴 3, 🔴 4, 🟠 1, 🟠 2, 🟠 3, 🟡 3 |
| Prawa autorskie | ❌ 🔴 1 |
| Definicje i logika | ⚠️ 🟡 2; osierocony Załącznik nr 2 w 🟠 2 |
| Reprezentacja | ⚠️ 🟢 1 |
| Wypowiedzenie i exit | ❌ 🟠 4, 🟠 5 |
| RODO | ⚠️ 🟡 1 (warunkowo, [BRAK DANYCH]) |
| Tytuł prawny i przekwalifikowanie | ✓ brak zastrzeżeń. Obie strony to spółki kapitałowe, a Specjaliści to personel Wykonawcy, więc ryzyko z art. 22 § 1 KP [NIEZWERYFIKOWANE] nie dotyczy stron tej umowy. Kwalifikacja: umowa o świadczenie usług (art. 750 KC [NIEZWERYFIKOWANE]), spójna z T&M; z tym modelem kłóci się tylko kara rezultatowa z § 2 ust. 1 (🟠 1). |
| Poufność | ❌ 🟠 6 |
| Spory | ✓ prawo polskie bez zastrzeżeń; forum w 🟢 2 |

### ✓ Obszary bez zastrzeżeń

Tytuł prawny i przekwalifikowanie: brak zastrzeżeń · Prawo właściwe (polskie): brak zastrzeżeń · Bramka ius cogens w zakresie art. 483 § 1, art. 484 § 2, art. 119 KC, art. 16 PrAut i terminów zapłaty: brak trafień.

### Miejsca, w których normalnie zatrzymałbym się na decyzję (tryb express, R6)

1. Dla której strony pracujemy. Audyt jest neutralny, ale kolejność negocjacji zależy od klienta: dla Zamawiającego najpierw 🔴 1 i 🟠 4–6, dla Wykonawcy najpierw 🔴 2–3 i 🟠 1–3.
2. Czy szacunek 2 × 160 h ma wiązać jako minimum. Od tego zależy baza capu i kar w całym rachunku.
3. Czy Wykonawca będzie miał dostęp do danych osobowych (🟡 1).
4. Treść Załącznika nr 2 i data zawarcia. Bez nich rachunku kary jakościowej i okna z § 4 nie da się domknąć.

---

## OCENA BEZPIECZEŃSTWA: 15/100

Cztery ryzyka krytyczne: brak praw do kodu, cap iluzoryczny przy ekspozycji co najmniej 1,97× capu bez górnej granicy, zakaz konkurencji z karą 300 000 zł za przypadek oraz trafienie w art. 473 § 2 KC. Do tego siedem ryzyk wysokich, w tym brak poufności, exitu i mechanizmu rozliczeń. Według skali (🔴 −15–20 pkt, 🟠 −5–10 pkt) wynik spada do przedziału 0–29. Umowa ma 6 paragrafów i reguluje głównie sankcje, a pomija podstawowe elementy umowy IT.

**Werdykt:** NIE PODPISYWAĆ w obecnej formie. Wymaga gruntownej przeróbki (IP, poufność, exit, rozliczenia) i negocjacji punktów krytycznych.

---

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (brak praw do kodu)
→ `references/baza-klauzul/08-prawa-autorskie-ip.md`: przeniesienie z polami eksploatacji, kod źródłowy, anty-copyleft

🔴 RYZYKO 2 i 4 (cap iluzoryczny, brak wyjątku winy umyślnej)
→ `references/baza-klauzul/11-odpowiedzialnosc.md`: klauzula wzorcowa z capem 12 mies. i wyjątkami; `references/baza-klauzul/10-kary-umowne.md`: sufit kar

🔴 RYZYKO 3 (zakaz konkurencji)
→ `references/baza-klauzul/13-non-solicitation.md`: wariant z definicją Działalności Konkurencyjnej, okres maks. 24 mies., preferowany krótszy

🟠 RYZYKO 4–7 (renewal, exit, poufność, rozliczenia)
→ `references/baza-klauzul/12-wypowiedzenie-exit.md` · `references/baza-klauzul/09-poufnosc.md` · `references/baza-klauzul/06-wynagrodzenie.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
