konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 1 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite)

## AUDYT RYZYK — Umowa ramowa T&M, rozwój oprogramowania (QUANTA DEV sp. z o.o. / MERIDIAN FINANCE S.A.)

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie; wymaga negocjacji punktów krytycznych (kary poza capem, zakaz konkurencji z karą 300.000 zł) przed podpisem.

Strony: Wykonawca = QUANTA DEV; Zamawiający = MERIDIAN FINANCE. Wszystkie powołania przepisów poniżej: [NIEZWERYFIKOWANE].

### 🧮 Rachunek ekspozycji

Liczby z umowy: stawka 220 zł netto/h (§ 1 ust. 2) · 2 Specjalistów × 160 h/mies. · 24 mies. (§ 1 ust. 3) · kara 0,5% wynagr. mies./dzień (§ 2 ust. 1) · 5.000 zł/przypadek (§ 2 ust. 2) · 300.000 zł/przypadek (§ 2 ust. 3) · cap 12-mies. wynagrodzenia (§ 3 ust. 1) · odnowienie 12 mies., okno 90 dni, +8% (§ 4) · zakaz konkurencji 24 mies. po zakończeniu (§ 5).

Założenia: wynagrodzenie miesięczne liczę wg szacunku z § 1 ust. 2 (umowa nie definiuje „wynagrodzenia miesięcznego" ani „12-miesięcznego wynagrodzenia", więc przyjmuję wersję szacowaną; wykonanie faktyczne może się różnić).

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Godziny miesięcznie | 2 × 160 h | 2 × 160 | 320 h |
| Wynagrodzenie miesięczne (netto) | 220 zł/h | 320 × 220 | 70.400 zł |
| Wynagrodzenie roczne | — | 70.400 × 12 | 844.800 zł |
| Wartość umowy (24 mies.) | § 1 ust. 3 | 70.400 × 24 = 844.800 × 2 | **1.689.600 zł** |
| Cap nominalny | 12-mies. wynagrodzenia | 70.400 × 12 | **844.800 zł** (50% wartości umowy: 844.800 / 1.689.600) |
| Kara za zwłokę — dziennie | 0,5% × wyn. mies. | 0,005 × 70.400 | 352 zł/dzień (na każdy Przyrost) |
| Kara za zwłokę — 30 dni | — | 352 × 30 | 10.560 zł |
| Kara za zwłokę — 365 dni | — | 352 × 365 | 128.480 zł |
| Kara za zwłokę — 24 mies. (730 dni) | — | 352 × 730 | 256.960 zł (jeden ciągły Przyrost; brak sufitu) |
| Dni zwłoki, by kara = 1 wyn. mies. | — | 70.400 / 352 | 200 dni (kary z różnych Przyrostów sumują się) |
| Kara za jakość | 5.000 zł/przypadek | 5.000 / 70.400 | 7,1% wyn. mies. za każdy przypadek; liczba przypadków [BRAK DANYCH] (brak sufitu, brak definicji „przypadku", Załącznik nr 2 nie dołączony) |
| Kara za zakaz konkurencji | 300.000 zł/przypadek | 300.000 / 70.400 · 300.000 / 844.800 | 4,26 wyn. mies. · 35,5% rocznego wynagrodzenia — za jedno naruszenie |
| Ilustracja: 2 naruszenia zakazu konkurencji | — | 300.000 × 2 | 600.000 zł (71,0% rocznego wynagrodzenia: 600.000 / 844.800) |
| Scenariusz ilustracyjny kar poza capem (założenie: 26 przypadków jakości przy sprintach 2-tyg. w ciągu 24 mies. — założenie własne, umowa nie podaje długości sprintu) | — | 10.560 (30 dni zwłoki) + 26 × 5.000 (= 130.000) + 2 × 300.000 (= 600.000) | 10.560 + 130.000 + 600.000 = **740.560 zł** |
| Efektywna ekspozycja (scenariusz) | cap + kary poza capem (+ indemnity + odszkodowanie uzupełniające) | 844.800 + 740.560 | **1.585.360 zł = 0,94× wartości umowy** (1.585.360 / 1.689.600); 1,88× wartości rocznej (1.585.360 / 844.800); bez uwzględnienia indemnity i odszkodowania ponad karę, które nie mają górnej granicy |
| Asymetria (Wykonawca vs Zamawiający) | kary i cap tylko po stronie Wykonawcy | Zamawiający: kary 0 zł, cap [BRAK DANYCH] | stosunek kar: 740.560 : 0 — relacji nie da się wyrazić liczbą; umowa nie przewiduje żadnej sankcji wobec Zamawiającego (np. za zwłokę w płatności) |
| Odnowienie 1 (miesiące 25–36) | stawka +8% | 220 × 1,08 = 237,60 zł/h; 320 × 237,60 = 76.032 zł/mies.; 76.032 × 12 | 912.384 zł/rok (o 67.584 zł więcej: 912.384 − 844.800) |
| Odnowienie 2 (miesiące 37–48) | +8% „względem okresu poprzedniego" (składany) | 237,60 × 1,08 = 256,608 ≈ 256,61 zł/h; 844.800 × 1,08 × 1,08 = 844.800 × 1,1664 | 985.374,72 zł/rok (o 140.574,72 zł więcej niż rok bazowy) |
| Wartość po 48 mies. (2 odnowienia) | — | 1.689.600 + 912.384 + 985.374,72 | 3.587.358,72 zł (2,12× wartości bazowej: 3.587.358,72 / 1.689.600) |
| Okno na sprzeciw wobec odnowienia | 90 dni przed końcem okresu | 24 mies. ≈ 730 dni − 90 dni | ostatni dzień oświadczenia ≈ dzień 640 od zawarcia (ok. 21. miesiąca); data kalendarzowa [BRAK DANYCH] — umowa nie podaje daty rozpoczęcia. Przegapienie = kolejne 12 mies. = 912.384 zł zobowiązania |
| Zakaz konkurencji — łączny czas związania | okres umowy + 24 mies. | 24 + 24 (bez odnowień) / 48 + 24 (z 2 odnowieniami) | 48 mies. / 72 mies., bez dodatkowego wynagrodzenia (§ 5 ust. 1) |
| Termin płatności | — | — | [BRAK DANYCH] (brak terminu zapłaty i trybu fakturowania) |
| Okres wypowiedzenia | — | — | [BRAK DANYCH] (brak klauzuli wypowiedzenia na czas 24 mies.) |

Wniosek z rachunku: cap 844.800 zł (50% wartości umowy) wygląda na ograniczenie, ale kary są poza nim (§ 2 ust. 4), sumują się, nie mają sufitu, a odszkodowanie uzupełniające dochodzi osobno; już w umiarkowanym scenariuszu ekspozycja Wykonawcy (1.585.360 zł) zbliża się do wartości całej umowy i przekracza wartość roczną prawie dwukrotnie. Cap jest w praktyce iluzoryczny, co przesuwa werdykt na CZERWONY.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kary umowne poza capem, sumowane, bez sufitu, z odszkodowaniem uzupełniającym — § 2 ust. 4 w zw. z § 3 ust. 1
**Strona dotknięta:** Wykonawca (korzyść: Zamawiający).
**Opis:** Kary z § 2 ust. 1–3 „podlegają sumowaniu i nie są wliczane do limitu" z § 3; Zamawiający może ponadto żądać odszkodowania przewyższającego karę (art. 484 § 1 KC [NIEZWERYFIKOWANE]). Brak sufitu dla jakiejkolwiek z trzech kar. Kara za zwłokę sięga 200 dni = 70.400 zł (jeden miesiąc wynagrodzenia) na każdy Przyrost; kara jakościowa nie ma limitu liczby przypadków.
**Skutek:** Realna ekspozycja Wykonawcy nie jest ograniczona (scenariusz: 1.585.360 zł = 0,94× wartości umowy, a to bez odszkodowania ponad karę). Argument o rażącym wygórowaniu i miarkowaniu (art. 484 § 2 KC [NIEZWERYFIKOWANE]) jest uprawnieniem sądu, nie automatem; nie należy na nim opierać zabezpieczenia.
**Rekomendacja (preferowana):** wliczyć kary do capu; globalny sufit kar (np. 10–20% wartości rocznej); kary nie kumulują się za to samo zdarzenie; odszkodowanie uzupełniające tylko do wysokości capu.
**Fallback (minimum akceptowalne):** kary poza capem, ale z odrębnym sufitem kar łącznych (np. równym 6-miesięcznemu wynagrodzeniu = 6 × 70.400 = 422.400 zł) i sufitem dla kary dziennej (np. 10% wyn. mies.).
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Zakaz konkurencji 24 miesiące po umowie, bez wynagrodzenia, z karą 300.000 zł za każdy przypadek — § 5 ust. 1 w zw. z § 2 ust. 3
**Strona dotknięta:** Wykonawca (korzyść: Zamawiający).
**Opis:** Zakaz obowiązuje w trakcie umowy i 24 mies. po niej, „nie jest związany z dodatkowym wynagrodzeniem". „Podmioty prowadzące działalność konkurencyjną" niezdefiniowane (brak katalogu, brak ograniczenia terytorialnego i przedmiotowego); „przypadek naruszenia" niezdefiniowany (każdy kontrakt? każdy dzień? każda faktura?). Kara 300.000 zł = 4,26 wyn. mies. i 35,5% rocznego wynagrodzenia za jedno naruszenie. Kara nie podlega capowi i sumuje się.
**Skutek:** Przy dwóch naruszeniach 600.000 zł (71,0% rocznego wynagrodzenia). Zakaz po zakończeniu, bez ekwiwalentu i bez ograniczeń, jest wystawiony na zarzut sprzeczności z zasadami współżycia i granicami swobody umów (art. 353¹, art. 58 § 2 KC [NIEZWERYFIKOWANE]) oraz miarkowania kary (art. 484 § 2 KC [NIEZWERYFIKOWANE]); w sytuacji gdy zakaz jest nieskuteczny, kara nie ma podstawy, ale ryzyko sporu pozostaje po stronie Wykonawcy. Wraz z odnowieniami związanie sięga 72 mies. (48 + 24). Wykonawca w branży IT może być faktycznie wyłączony z rynku usług dla sektora finansowego.
**Rekomendacja (preferowana):** usunąć zakaz po zakończeniu umowy; w trakcie umowy zawęzić do wymienionych konkurentów, projektów i terytorium.
**Fallback (minimum akceptowalne):** zakaz 6–12 mies. po umowie, z wynagrodzeniem (np. 25–50% średniego wynagrodzenia miesięcznego = 17.600–35.200 zł/mies.), definicją konkurenta, karą jednorazową i limitem kar łącznych.
**Klauzula z bazy:** `references/baza-klauzul/` (zakaz konkurencji / kary umowne — INDEX.md)

### 🟠 RYZYKA WYSOKIE

#### 1. Nielimitowana indemnifikacja IP — „wszelkie koszty" — § 3 ust. 2
**Strona dotknięta:** Wykonawca (korzyść: Zamawiający).
**Opis:** „Zwolni z wszelkiej odpowiedzialności" i „pokryje wszelkie związane z tym koszty" za roszczenia osób trzecich z IP; brak wyłączeń (kod dostarczony przez Zamawiającego, jego specyfikacje, modyfikacje po stronie Zamawiającego), brak procedury (zawiadomienie, kontrola obrony, ugoda za zgodą). Relacja do capu niejasna: § 3 ust. 1 mówi o „łącznej odpowiedzialności", ale § 2 ust. 4 wyłącza z capu tylko kary, więc spór interpretacyjny co do tego, czy indemnity mieści się w 844.800 zł.
**Skutek:** Potencjalnie ekspozycja ponad cap (otwarta kwota) w razie sporu IP z osobą trzecią. Kwota [BRAK DANYCH].
**Rekomendacja (preferowana):** indemnity w capie, z procedurą i wyłączeniami; jawne wskazanie relacji do § 3 ust. 1.
**Fallback (minimum akceptowalne):** super-cap (np. 2× cap = 1.689.600 zł) wyłącznie dla IP, z procedurą i wyłączeniem materiałów Zamawiającego.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`; `references/baza-wiedzy/07-indemnifikacja-kary-umowne.md`

#### 2. Brak postanowień o prawach autorskich do wytworzonego oprogramowania — cała umowa
**Strona dotknięta:** Zamawiający (zwłaszcza); pośrednio Wykonawca (spór o zakres).
**Opis:** Umowa o rozwój oprogramowania nie zawiera przeniesienia autorskich praw majątkowych ani licencji, nie wymienia pól eksploatacji, nie reguluje momentu przejścia praw ani praw zależnych. Bez wyraźnego wskazania pól eksploatacji i formy pisemnej skutek rozporządzający nie powstaje (art. 41 ust. 2, art. 53 PrAut [NIEZWERYFIKOWANE]). Brak też gwarancji czystości IP i klauzuli anty-copyleft, mimo że § 3 ust. 2 zakłada odpowiedzialność za IP.
**Skutek:** Zamawiający płaci co najmniej 1.689.600 zł za 24 mies., a nie nabywa praw do kodu; Wykonawca jest narażony na spory o zakres korzystania.
**Rekomendacja (preferowana):** dodać przeniesienie praw z listą pól eksploatacji, moment przejścia (np. z zapłatą), zobowiązanie do niewykonywania praw osobistych, gwarancje IP i anty-copyleft.
**Fallback (minimum akceptowalne):** licencja wyłączna, bezterminowa, z wymienionymi polami eksploatacji i prawem do modyfikacji, z przeniesieniem własności w późniejszym terminie.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 3. Automatyczne odnowienie bez wypowiedzenia, z automatyczną podwyżką 8% — § 4 ust. 1–2 (oraz brak klauzuli wypowiedzenia)
**Strona dotknięta:** Zamawiający (koszt, podwyżka); Wykonawca (związanie zakazem konkurencji po odnowieniu do 72 mies.).
**Opis:** Umowa trwa 24 mies., potem odnawia się na 12 mies., chyba że sprzeciw złożono na 90 dni przed końcem (ostatni dzień ≈ dzień 640 od zawarcia). Stawka rośnie o 8% w każdym okresie przedłużenia, „względem okresu poprzedniego", czyli składanie (+16,64% po dwóch odnowieniach: 1,08 × 1,08 = 1,1664). Brak prawa wypowiedzenia w trakcie okresów (art. 746 KC dla zlecenia [NIEZWERYFIKOWANE] — kwalifikacja umowy niejasna), brak wypowiedzenia z ważnych powodów, brak procedury exit (przekazanie kodu, dokumentacji, WIP). Podwyżka nie jest powiązana z żadnym wskaźnikiem ani z jakością.
**Skutek:** Przegapienie okna = kolejne 912.384 zł zobowiązania; po drugim odnowieniu rocznie 985.374,72 zł (o 140.574,72 zł więcej niż rok bazowy). Wykonawca przy przegapionym oknie: dodatkowe 12 mies. zakazu konkurencji plus 24 mies. po.
**Rekomendacja (preferowana):** wypowiedzenie 30–60 dni dla obu stron w każdym czasie; waloryzacja wskaźnikowa (np. CPI) z limitem, dwustronna; brak automatycznego odnowienia lub krótkie okno przypominające.
**Fallback (minimum akceptowalne):** okno sprzeciwu skrócone (30 dni) z obowiązkowym przypomnieniem Zamawiającemu od Wykonawcy; podwyżka maks. 5% nieskładanie albo CPI z pułapem.
**Klauzula z bazy:** `references/baza-klauzul/` (czas trwania i wypowiedzenie — INDEX.md)

#### 4. T&M bez mechanizmów kontroli godzin, płatności i budżetu — § 1 ust. 2
**Strona dotknięta:** Zamawiający (koszt otwarty); Wykonawca (brak gwarancji obrotu i terminu zapłaty).
**Opis:** „Szacowane zaangażowanie" 2 × 160 h nie jest ani minimum, ani maksimum. Brak: limitu godzin lub budżetu, akceptacji ewidencji czasu, prawa Zamawiającego do kwestionowania godzin, trybu fakturowania, terminu zapłaty, odsetek, zasad godzin nadliczbowych, zmiany składu zespołu, kwalifikacji „Specjalisty". Wielkość 70.400 zł mies. to tylko szacunek; przekroczenie np. o 25% daje 320 × 1,25 = 400 h × 220 = 88.000 zł/mies. (+17.600 zł), bez limitu.
**Skutek:** Zamawiający nie ma kontroli nad kosztem; Wykonawca nie ma ustalonego terminu zapłaty (termin płatności [BRAK DANYCH]; ustawowe limity zatorowe nie zostały przesądzone w umowie [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** miesięczny budżet godzin (not-to-exceed), zatwierdzanie raportów w 5–7 dni, termin płatności 30 dni, zasady zmian zespołu.
**Fallback (minimum akceptowalne):** zgoda Zamawiającego na przekroczenie > 10% godzin; płatność w 30–60 dni od faktury.
**Klauzula z bazy:** `references/baza-klauzul/` (wynagrodzenie, T&M — INDEX.md)

### 🟡 RYZYKA ŚREDNIE

#### 1. Cap bez carve-outu dla winy umyślnej i niedookreślony — § 3 ust. 1
**Strona dotknięta:** oboje (Zamawiający: ograniczone odszkodowanie do 844.800 zł; Wykonawca: niepewność co do podstawy).
**Opis:** „12-miesięczne wynagrodzenie" niedookreślone (szacowane, zapłacone, należne? z jakich 12 mies.?). Cap „łączny" nie wyłącza winy umyślnej; wyłączenie lub ograniczenie odpowiedzialności za szkodę wyrządzoną umyślnie jest niedopuszczalne (art. 473 § 2 KC [NIEZWERYFIKOWANE]), więc klauzula jest nieskuteczna w tym zakresie z mocy prawa (art. 58 § 3 KC [NIEZWERYFIKOWANE]). Cap nie obejmuje też poufności i IP. Przy bazie 70.400 zł mies. wartość capu wynosi 844.800 zł, ale w pierwszych miesiącach „zapłacone wynagrodzenie" bywa niższe.
**Skutek:** Spór o wysokość capu; w ocenie sądu cap może nie działać dla winy umyślnej.
**Rekomendacja (preferowana):** zdefiniować cap (wynagrodzenie należne za 12 mies. poprzedzających zdarzenie), jawnie wyłączyć winę umyślną, osobny super-cap dla poufności/IP/RODO.
**Fallback (minimum akceptowalne):** cap = wartość szacowana z § 1 (844.800 zł) jako kwota stała.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Niespójność modelu T&M z karami za rezultat — § 1 ust. 1 w zw. z § 2 ust. 1–2
**Strona dotknięta:** Wykonawca (kary za rezultat przy wynagrodzeniu za czas pracy); Zamawiający (sporne podstawy roszczeń).
**Opis:** Wykonawca jest rozliczany za godziny (staranne działanie), a karany za zwłokę „w dostarczeniu Przyrostu" i za wynik przeglądu kodu (rezultat). Umowa nie określa typu (zlecenie / usługi nieuregulowane / dzieło — art. 750, 627 KC [NIEZWERYFIKOWANE]), ani kto odpowiada za opóźnienia po stronie Zamawiającego (zależności, akceptacja, środowiska). Kara za zwłokę liczona od „wynagrodzenia miesięcznego" (niezdefiniowanego; 70.400 zł w szacunku) niezależnie od wartości opóźnionego Przyrostu: 352 zł/dzień przy Przyroście o wartości np. 1 sprintu 2-tyg. (ok. 35.200 zł: 70.400 / 2) to 1% wartości Przyrostu dziennie. Brak wyłączenia kary, gdy opóźnienie wynika z przyczyn leżących po stronie Zamawiającego lub siły wyższej.
**Skutek:** Kary wymierzane bez związku z faktyczną szkodą; ryzyko sporu o skuteczność kar.
**Rekomendacja (preferowana):** kary tylko za wyodrębnione kamienie milowe z jasnym kryterium akceptacji; wyłączenie przyczyn po stronie Zamawiającego; wskazanie typu umowy.
**Fallback (minimum akceptowalne):** zachować kary, ale z wyłączeniem przyczyn niezależnych od Wykonawcy i z sufitem.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Niezdefiniowane pojęcia i brakujący załącznik — § 1, § 2, § 5
**Strona dotknięta:** oboje (kary: Wykonawca).
**Opis:** „Przyrost", „harmonogram sprintu", „Specjalista", „wynagrodzenie miesięczne", „podmiot prowadzący działalność konkurencyjną", „przypadek naruszenia", „rozpoczęty dzień zwłoki" (kalendarzowy czy roboczy?) bez definicji. Załącznik nr 2 (próg jakości kodu) jest przywołany w § 2 ust. 2, lecz nie ma go w tekście; kara 5.000 zł nie ma więc obiektywnego kryterium.
**Skutek:** Nie da się policzyć górnej granicy kar jakościowych; spory o wykładnię (art. 65 KC [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** słownik pojęć i dołączenie Załącznika nr 2 przed podpisem.
**Fallback (minimum akceptowalne):** zawieszenie kar z § 2 ust. 2 do czasu uzgodnienia Załącznika nr 2.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 4. Brak poufności, RODO i ochrony tajemnicy — cała umowa
**Strona dotknięta:** Zamawiający (instytucja finansowa, dane klientów i systemów); Wykonawca (brak ram, ryzyko niezamierzonego naruszenia).
**Opis:** Brak klauzuli poufności (okres po zakończeniu, wyłączenia, kary), brak umowy powierzenia danych lub oświadczenia, że dane osobowe nie będą przetwarzane (art. 28 RODO [NIEZWERYFIKOWANE]), brak zasad dostępu do środowisk, podwykonawców, bezpieczeństwa (finansowy Zamawiający). Nie dotyczy kar (nie ma ich w poufności), lecz ryzyko jest po stronie Zamawiającego.
**Skutek:** Niekontrolowany dostęp Wykonawcy do danych; ewentualne naruszenie RODO. Kwota [BRAK DANYCH].
**Rekomendacja (preferowana):** NDA/poufność z okresem po umowie, powierzenie danych (art. 28 RODO [NIEZWERYFIKOWANE]) albo zakaz dostępu do danych osobowych.
**Fallback (minimum akceptowalne):** krótka klauzula poufności 3–5 lat i zakaz przetwarzania danych osobowych bez odrębnej umowy.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`; `references/checklist-dpa-art28.md`

### 🟢 RYZYKA NISKIE

#### 1. Sąd właściwy dla siedziby Zamawiającego — § 6 ust. 1
**Strona dotknięta:** Wykonawca (dojazd i koszty), lekko.
**Opis:** Brak wskazania sądu (miejscowo i rzeczowo), brak mediacji; „sąd właściwy dla siedziby Zamawiającego" wystarcza do wskazania miejsca, ale jest niejednoznaczne przy rozstrzyganiu spraw zasadniczo kierowanych do sądu gospodarczego.
**Skutek:** Drobne koszty; spór o właściwość jest mało prawdopodobny.
**Rekomendacja (preferowana):** wskazać sąd, eskalację i mediację.
**Fallback (minimum akceptowalne):** zostawić, dodać etap negocjacji 30 dni.
**Klauzula z bazy:** `references/baza-klauzul/` (rozstrzyganie sporów — INDEX.md)

#### 2. Brak oznaczenia stron (KRS/NIP/adresy) i reprezentacji — nagłówek umowy
**Strona dotknięta:** oboje.
**Opis:** Dane stron „fikcyjne" bez KRS/NIP/adresów i umocowania osób podpisujących; w obiegu rzeczywistym należy je uzupełnić i zweryfikować.
**Skutek:** Ryzyko formalne przy wersji produkcyjnej.
**Rekomendacja (preferowana):** pełne oznaczenie stron i wskazanie reprezentacji.
**Fallback (minimum akceptowalne):** załączenie odpisów KRS.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`

### ✓ Obszary bez zastrzeżeń

Przekwalifikowanie na stosunek pracy (art. 22 § 1 KP [NIEZWERYFIKOWANE]): n/d (usługi zespołu Wykonawcy, nie body leasing; wskazówka w § 2 pkt 2 powyżej o niejasnym typie umowy). Terminy zapłaty ponad 60 dni: n/d (umowa nie podaje terminu — zob. 🟠 4). Zakaz niedopuszczalnych kar za zobowiązanie pieniężne (art. 483 § 1 KC [NIEZWERYFIKOWANE]): brak trafienia (kary dotyczą świadczeń niepieniężnych). Zrzeczenie miarkowania (art. 484 § 2 KC [NIEZWERYFIKOWANE]): brak trafienia. Trigger art. 385⁵ KC: nieaktywny (obie strony spółki kapitałowe).

Bramka kompletności (9 obszarów): odpowiedzialność i kary — 🔴 1, 🟠 1, 🟡 1–2 · prawa autorskie — 🟠 2 · definicje i logika — 🟡 3 · reprezentacja — 🟢 2 · wypowiedzenie i exit — 🟠 3 · RODO — 🟡 4 · tytuł prawny — 🟡 2 · poufność — 🟡 4 · spory — 🟢 1.

---

## OCENA BEZPIECZEŃSTWA: 28/100

Dwa ryzyka krytyczne (kary poza capem bez sufitu; zakaz konkurencji z karą 300.000 zł bez wynagrodzenia), cztery wysokie i cztery średnie; cap 844.800 zł jest iluzoryczny po rachunku (ekspozycja scenariuszowa 1.585.360 zł). Umowa jest wyraźnie jednostronna na korzyść Zamawiającego co do kar i zakazu konkurencji, a jednocześnie niepełna co do praw autorskich, poufności i płatności, co obciąża Zamawiającego.

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI (reguła werdyktu: co najmniej jedno ryzyko 🔴 = 🟥 CZERWONY)

Liczba flag: 12 (🔴 2, 🟠 4, 🟡 4, 🟢 2).

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
