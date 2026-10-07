konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 2 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

---

[DRAFT — DO WERYFIKACJI] (tryb express; wszystkie powołania przepisów [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa ramowa T&M, rozwój oprogramowania (QUANTA DEV sp. z o.o. / MERIDIAN FINANCE S.A.)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; punkty krytyczne (kary poza capem bez sufitu, zakaz konkurencji z karą 300.000 zł, brak przeniesienia praw autorskich) wymagają negocjacji przed podpisem.

Audyt neutralny: przy każdej fladze wskazano stronę dotkniętą. Wykonawca = QUANTA DEV, Zamawiający = MERIDIAN FINANCE.

### 🧮 Rachunek ekspozycji

**Liczby wyjściowe z umowy:** stawka 220 zł netto/h (§ 1 ust. 2); 2 Specjalistów × 160 h/mies. (§ 1 ust. 2, wielkość szacunkowa); okres 24 mies. (§ 1 ust. 3); kara zwłokowa 0,5% wynagrodzenia miesięcznego/dzień (§ 2 ust. 1); kara jakościowa 5.000 zł/przypadek (§ 2 ust. 2); kara za konkurencję 300.000 zł/przypadek (§ 2 ust. 3); cap = 12-miesięczne wynagrodzenie (§ 3 ust. 1); wypowiedzenie przedłużenia 90 dni przed końcem okresu, podwyżka stawki +8% (§ 4); zakaz konkurencji 24 mies. po zakończeniu, bez wynagrodzenia (§ 5). Założenie: wynagrodzenie liczone wg szacunku z § 1 ust. 2 (umowa nie podaje innej podstawy); miesiąc = 30 dni.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Godziny miesięcznie | 2 × 160 h | 2 × 160 | 320 h |
| Wynagrodzenie miesięczne | 220 zł/h | 320 h × 220 zł | **70.400 zł** |
| Wartość umowy (24 mies.) | § 1 ust. 3 | 70.400 zł × 24 | **1.689.600 zł** |
| Wynagrodzenie roczne | — | 70.400 zł × 12 | 844.800 zł |
| Cap nominalny | 12 × wynagr. mies. | 70.400 zł × 12 | **844.800 zł = 50% wartości umowy** (1.689.600 × 0,5) |
| Kara zwłokowa dzienna | 0,5% × 70.400 zł | 70.400 × 0,005 | **352 zł/dzień** |
| Kara zwłokowa — 30 dni | — | 352 zł × 30 | 10.560 zł |
| Kara zwłokowa — próg 100% wynagr. mies. | — | 100% ÷ 0,5% | po 200 dniach = 70.400 zł (352 × 200) |
| Kara zwłokowa — horyzont 24 mies. (brak sufitu) | — | 352 zł × 720 dni | 253.440 zł = 15,0% wartości umowy (253.440 ÷ 1.689.600) |
| Kara jakościowa | 5.000 zł/przypadek | 5.000 ÷ 220 zł/h | = 22,7 h pracy (5.000 ÷ 220); 7,1% wynagr. mies. (5.000 ÷ 70.400); liczba przypadków bez sufitu; progi z Załącznika nr 2 — [BRAK DANYCH] |
| Kara jakościowa — 10 przypadków | — | 5.000 zł × 10 | 50.000 zł |
| Kara za konkurencję — 1 przypadek | 300.000 zł | 300.000 ÷ 70.400; ÷ 844.800; ÷ 1.689.600 | 4,26× wynagr. mies.; 35,5% capu; 17,8% wartości umowy |
| Kara za konkurencję — 3 przypadki | — | 300.000 zł × 3 | **900.000 zł > cap 844.800 zł** (o 55.200 zł; 900.000 − 844.800) |
| Okres obowiązywania zakazu konkurencji | 24 mies. umowy + 24 mies. po | 24 + 24 | min. 48 mies., bez wynagrodzenia = 0 zł |
| Scenariusz ekspozycji Wykonawcy (kary poza capem) | 3 × konkurencja + 30 dni zwłoki + 10 przypadków jakości | 900.000 + 10.560 + 50.000 | kary: 960.560 zł |
| Efektywna ekspozycja Wykonawcy | cap + kary poza capem + indemnity + odszkodowanie ponad karę | 844.800 + 960.560 + [indemnity bez limitu] + [odszk. uzupełniające bez limitu] | **≥ 1.805.360 zł = 1,07× wartości umowy** (1.805.360 ÷ 1.689.600 = 1,0685); w górę bez granicy |
| Asymetria (Wykonawca vs Zamawiający) | kary/cap Zamawiającego: brak | Wykonawca ≥ 1.805.360 zł; Zamawiający: kar 0 zł, cap [BRAK DANYCH] (jego świadczenie = zapłata) | nieobliczalny stosunek (dzielenie przez 0): jednostronnie |
| Wynagrodzenie po 1. przedłużeniu | 220 zł × 1,08 | 220 × 1,08 = 237,60 zł/h; 320 × 237,60 = 76.032 zł/mies.; × 12 | 912.384 zł/rok (+67.584 zł vs 844.800) |
| Po 2. przedłużeniu | 237,60 × 1,08 | 256,608 zł/h; 320 × 256,608 = 82.114,56 zł/mies.; × 12 | 985.374,72 zł/rok (+140.574,72 zł) |
| Po 3. przedłużeniu | 256,608 × 1,08 | 277,13664 zł/h; 320 × 277,13664 = 88.683,72 zł/mies.; × 12 | 1.064.204,70 zł/rok (+219.404,70 zł) |
| Skumulowana nadwyżka z 3 przedłużeń (rok 3–5) | — | 67.584 + 140.574,72 + 219.404,70 | 427.563,42 zł = 16,9% (427.563,42 ÷ 2.534.400; 2.534.400 = 3 × 844.800) ponad stawkę stałą; stawka po 3 przedłużeniach = 1,08³ = 1,2597 (+26,0%) |
| Cap w okresie przedłużenia (po 1. przedłużeniu) | 12 × 76.032 | = 912.384 zł | rośnie razem ze stawką |
| Data graniczna sprzeciwu wobec przedłużenia | 90 dni przed końcem 24. miesiąca | koniec okresu − 90 dni (ok. dzień 630 z 720) | data kalendarzowa: [BRAK DANYCH] (brak daty rozpoczęcia). Przegapienie = zobowiązanie na kolejne 12 mies. ≈ 912.384 zł i kolejne wydłużenie zakazu konkurencji |
| Termin płatności | — | — | [BRAK DANYCH] |

**Wniosek z rachunku:** cap nominalny 844.800 zł jest iluzoryczny. Kary (poza capem, sumowane, bez sufitu), odszkodowanie ponad karę i indemnity IP leżą obok niego. Już realistyczny scenariusz daje ≥ 1,07× wartości całej umowy po stronie Wykonawcy. Ekspozycja Zamawiającego jest odwrotnie nieograniczona kosztowo w górę przez automatyczną podwyżkę +8%. To kalibruje werdykt do CZERWONEGO.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kary poza capem, sumowane, bez sufitu; cap iluzoryczny — § 2 ust. 4, § 3 ust. 1
**Strona dotknięta:** Wykonawca.
**Opis:** Kary nie wliczają się do limitu, sumują się z każdej podstawy i dopuszczono odszkodowanie ponad karę (art. 484 § 1 KC [NIEZWERYFIKOWANE]). Żadna kara nie ma sufitu kwotowego ani procentowego.
**Skutek:** Efektywna ekspozycja ≥ 1.805.360 zł (1,07× wartości umowy) w scenariuszu z rachunku, a w górę bez granicy. Cap 844.800 zł chroni tylko część roszczeń niekarnych. Argument o rażącym wygórowaniu kar (art. 484 § 2 KC [NIEZWERYFIKOWANE]) to uprawnienie sądu, nie automat.
**Rekomendacja (preferowana):** wliczyć kary do capu; łączny sufit kar (np. 20% wartości umowy = 337.920 zł); kara jako wyłączne odszkodowanie za dane naruszenie.
**Fallback:** sufit kar odrębny od capu, ale nie wyższy niż cap; odszkodowanie ponad karę tylko przy winie umyślnej.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `11-odpowiedzialnosc.md`

#### 2. Zakaz konkurencji 24 + 24 mies. bez wynagrodzenia i kara 300.000 zł za każdy przypadek — § 5 ust. 1, § 2 ust. 3
**Strona dotknięta:** Wykonawca.
**Opis:** Zakaz obejmuje czas umowy i 24 mies. po niej (min. 48 mies.), bez ekwiwalentu (0 zł). „Działalność konkurencyjna wobec Zamawiającego" i „przypadek naruszenia" są niezdefiniowane. Zakaz kieruje się wobec software house'u, który żyje z obsługi wielu klientów, a przedłużenie umowy odsuwa jego koniec.
**Skutek:** 1 przypadek = 300.000 zł (4,26× wynagr. mies.; 17,8% wartości umowy); 3 przypadki = 900.000 zł > cap. Ryzyko nieskuteczności zakazu lub kary jako sprzecznych z zasadami współżycia społecznego i swobodą umów (art. 353¹, art. 58 § 2 KC [NIEZWERYFIKOWANE]) oraz miarkowania (art. 484 § 2 KC [NIEZWERYFIKOWANE]); do tego czasu to realny hamulec dla działalności Wykonawcy.
**Rekomendacja (preferowana):** zakaz tylko na czas umowy i tylko w wąsko zdefiniowanym zakresie (konkretny projekt/dane Zamawiającego); kara niższa i z sufitem.
**Fallback:** okres po umowie ≤ 6–12 mies. z wynagrodzeniem (np. ułamek średniego wynagrodzenia mies.); definicja podmiotów konkurencyjnych w załączniku.
**Klauzula z bazy:** `references/baza-klauzul/` — zakaz konkurencji / kary umowne

#### 3. Brak przeniesienia praw autorskich do tworzonego oprogramowania — cała umowa
**Strona dotknięta:** Zamawiający (pośrednio Wykonawca: spór o zakres praw).
**Opis:** Umowa dotyczy rozwoju oprogramowania, ale nie zawiera żadnego przeniesienia praw ani licencji, pól eksploatacji, momentu przejścia praw ani zgody na prawa zależne. Jest tylko indemnity z § 3 ust. 2.
**Skutek:** Bez wymienienia pól eksploatacji brak skutku rozporządzającego (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]); Zamawiający płaci 1.689.600 zł za kod, do którego może nie mieć praw.
**Rekomendacja (preferowana):** przeniesienie autorskich praw majątkowych z wyliczeniem pól eksploatacji, z chwilą odbioru/zapłaty, prawa zależne, zezwolenie na wykonywanie praw zależnych.
**Fallback:** licencja wyłączna, bezterminowa, nieodwołalna z prawem sublicencji.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟠 RYZYKA WYSOKIE

#### 4. Kara zwłokowa dzienna bez sufitu, bez związku z winą — § 2 ust. 1
**Strona dotknięta:** Wykonawca.
**Opis:** 0,5% wynagr. mies. za każdy rozpoczęty dzień (352 zł/dzień), bez górnej granicy; „Przyrost" i „harmonogram sprintu" niezdefiniowane; brak wyłączenia dla opóźnień z przyczyn po stronie Zamawiającego (dostęp, odbiór, decyzje); zwłoka zależy od okoliczności, za które dłużnik odpowiada (art. 476 KC [NIEZWERYFIKOWANE]), a w T&M Wykonawca zobowiązuje się do starannego działania, nie rezultatu.
**Skutek:** 10.560 zł/30 dni; po 200 dniach = 100% wynagr. mies. (70.400 zł); w horyzoncie 24 mies. do 253.440 zł (15,0% wartości umowy). Wynagrodzenie T&M zmienne, więc podstawa kary niepewna.
**Rekomendacja (preferowana):** sufit 10% wynagr. za dany Przyrost; kara tylko za zwłokę z winy Wykonawcy; definicje; okres karencji.
**Fallback:** sufit 20% łącznie, wyłączenie opóźnień spowodowanych przez Zamawiającego.
**Klauzula z bazy:** `10-kary-umowne.md`, `07-terminy-kamienie-milowe.md`

#### 5. Kara 5.000 zł za każdy przypadek jakości — próg w nieprzedłożonym załączniku — § 2 ust. 2
**Strona dotknięta:** Wykonawca (dla Zamawiającego: kara bez mierzalnego kryterium trudna do wyegzekwowania).
**Opis:** Kryterium = „wynik przeglądu poniżej progu z Załącznika nr 2" — załącznika brak, nie wiadomo, kto przegląda, jak często i czy przegląd jest dwustronny. Brak sufitu i liczby przypadków.
**Skutek:** 5.000 zł = 22,7 h pracy; 10 przypadków = 50.000 zł; razem z innymi karami poza capem. Kara bez progu do sprawdzenia jest przedmiotem sporu.
**Rekomendacja (preferowana):** załącznik z mierzalnymi progami, procedura poprawy (czas na usunięcie wad bez kary), sufit miesięczny.
**Fallback:** kara tylko po bezskutecznym terminie na poprawę.
**Klauzula z bazy:** `10-kary-umowne.md`, `13-odbior-gwarancja` (jeśli występuje w bazie)

#### 6. Indemnity IP bez limitu i bez procedury — § 3 ust. 2
**Strona dotknięta:** Wykonawca.
**Opis:** „Zwolni z wszelkiej odpowiedzialności" i „pokryje wszelkie koszty" roszczeń osób trzecich z IP. Brak: zawiadomienia, kontroli obrony, obowiązku zmniejszania szkody, wyłączeń (materiały i wymagania Zamawiającego, modyfikacje przez Zamawiającego, open source wskazany przez Zamawiającego), sufitu. Niejasne, czy podlega capowi z § 3 ust. 1 („łączna odpowiedzialność") — redakcja „wszelkie" sugeruje, że nie.
**Skutek:** Ekspozycja otwarta; w rachunku [bez limitu], co podnosi efektywną ekspozycję ponad 1.805.360 zł.
**Rekomendacja (preferowana):** indemnity w capie (lub superlimit, np. 2× wynagr. roczne = 1.689.600 zł), z procedurą i wyłączeniami.
**Fallback:** superlimit odrębny od capu, ale skończony.
**Klauzula z bazy:** `references/baza-klauzul/` — indemnifikacja (baza-wiedzy `07-indemnifikacja-kary-umowne.md`)

#### 7. Automatyczne przedłużenie i podwyżka stawki o 8% za każdy okres — § 4
**Strona dotknięta:** Zamawiający (a także Wykonawca: przedłużenie wydłuża zakaz konkurencji i kary).
**Opis:** Po 24 mies. umowa przedłuża się o 12 mies.; stawka rośnie o 8% względem poprzedniego okresu, bez wskaźnika rynkowego i bez prawa Zamawiającego do renegocjacji; okno sprzeciwu 90 dni przed końcem; niejasne, czy liczy się złożenie czy dotarcie oświadczenia (art. 61 KC [NIEZWERYFIKOWANE]).
**Skutek:** Rok 3: 912.384 zł (+67.584 zł); rok 4: 985.374,72 zł; rok 5: 1.064.204,70 zł. Skumulowana nadwyżka 427.563,42 zł (16,9%) ponad stawkę stałą. Przegapienie okna = ok. 912.384 zł zobowiązania.
**Rekomendacja (preferowana):** bez automatycznego przedłużenia (lub z przypomnieniem pisemnym), waloryzacja wg wskaźnika (np. CPI z górnym limitem), prawo wypowiedzenia.
**Fallback:** okno sprzeciwu 30 dni, podwyżka ≤ wskaźnik inflacji, jednorazowa.
**Klauzula z bazy:** `07-terminy-kamienie-milowe.md` / waloryzacja

### 🟡 RYZYKA ŚREDNIE

#### 8. Cap bez wyłączenia winy umyślnej; niejasna podstawa „12-miesięcznego wynagrodzenia" — § 3 ust. 1
**Strona dotknięta:** Zamawiający (cap ogranicza jego roszczenia); Wykonawca (niepewność kwoty).
**Opis:** Wyłączenie lub ograniczenie odpowiedzialności za winę umyślną jest nieważne (art. 473 § 2 KC [NIEZWERYFIKOWANE]); cap obejmuje „łączną odpowiedzialność" bez wyjątków (wina umyślna, poufność, IP). Nie wiadomo, czy to wynagrodzenie szacowane, faktycznie zapłacone, netto/brutto, z 12 mies. poprzedzających.
**Rekomendacja (preferowana):** wyraźne wyłączenia z capu + definicja podstawy.
**Fallback:** wyłączenie winy umyślnej i rażącego niedbalstwa.
**Klauzula z bazy:** `11-odpowiedzialnosc.md`

#### 9. Model T&M bez zasad rozliczeń — § 1 ust. 2
**Strona dotknięta:** obie (Zamawiający: brak kontroli budżetu; Wykonawca: brak gwarantowanego wolumenu przy zakazie konkurencji).
**Opis:** Zaangażowanie jest tylko „szacowane"; brak: ewidencji i akceptacji godzin, limitu budżetu/godzin, terminu płatności i fakturowania [BRAK DANYCH], zasad zmiany Specjalistów, waloryzacji w 24 mies. Wolumen 320 h/mies. nie wiąże.
**Rekomendacja:** limit godzin/budżetu, procedura akceptacji, termin płatności ≤ 30–60 dni.
**Klauzula z bazy:** `references/baza-klauzul/` — wynagrodzenie

#### 10. Brak wypowiedzenia i procedury exit w okresie 24 mies. — cała umowa
**Strona dotknięta:** obie.
**Opis:** Brak rozwiązania z ważnych przyczyn, okresu wypowiedzenia i skutków (zwrot materiałów, kod, rozliczenie WIP, przekazanie wiedzy); brak odpowiednika konsekwencji poza § 4. Przy umowie na 1.689.600 zł to zamrożenie. Jeśli umowa jest zleceniem, art. 746 KC [NIEZWERYFIKOWANE] pozwala wypowiedzieć w każdym czasie, ale bez uregulowania skutków strona narażona na roszczenie.
**Rekomendacja:** wypowiedzenie z 30–60-dniowym terminem + procedura exit.
**Klauzula z bazy:** `references/baza-klauzul/` — rozwiązanie umowy

#### 11. Ryzyko przekwalifikowania na stosunek pracy — § 1 ust. 2
**Strona dotknięta:** obie (ZUS, PIP; zwłaszcza Wykonawca i Zamawiający wobec Specjalistów).
**Opis:** Stałe 2 Specjalistów po 160 h/mies. (pełny etat), rozliczenie godzinowe, brak wskazania, że Specjaliści działają samodzielnie, bez podporządkowania Zamawiającego (art. 22 § 1 KP [NIEZWERYFIKOWANE]).
**Rekomendacja:** klauzula autonomii, brak wskazówek co do czasu/miejsca pracy, wyłączenie podporządkowania.
**Klauzula z bazy:** `references/baza-klauzul/` — body leasing / tytuł prawny

#### 12. Brak poufności i postanowień o danych osobowych — cała umowa
**Strona dotknięta:** Zamawiający (podmiot finansowy; dostęp do danych i kodu).
**Opis:** Brak klauzuli poufności, okresu po umowie, kary; jeżeli Wykonawca ma dostęp do danych osobowych (środowiska testowe/produkcyjne), brak umowy powierzenia (art. 28 RODO [NIEZWERYFIKOWANE]). Ocena RODO zależna od faktu dostępu do danych — [BRAK DANYCH].
**Rekomendacja:** NDA w umowie, powierzenie danych w załączniku.
**Klauzula z bazy:** `09-poufnosc.md`, `checklist-dpa-art28.md`

#### 13. Niezdefiniowane pojęcia — § 1, § 2
**Strona dotknięta:** obie (zwłaszcza Wykonawca przy karach).
**Opis:** „Przyrost", „sprint", „Specjaliści", „standardy jakości kodu", „podmioty konkurencyjne", „przypadek naruszenia" używane bez definicji; kary opierają się na tych pojęciach.
**Rekomendacja:** słownik pojęć.
**Klauzula z bazy:** `03-definicje.md`

### 🟢 RYZYKA NISKIE

#### 14. Niekompletne dane stron i brak załączników — nagłówek, § 2 ust. 2
**Strona dotknięta:** obie. Brak KRS/NIP, reprezentacji, miejsca i daty zawarcia, Załącznika nr 2 (dane w umowie oznaczone jako fikcyjne; flaga formalna).
**Klauzula z bazy:** `01-oznaczenie-stron.md`

#### 15. Sąd właściwy dla siedziby Zamawiającego — § 6 ust. 1
**Strona dotknięta:** Wykonawca (wygodniejsze forum dla Zamawiającego). Prawo polskie bez zastrzeżeń.
**Klauzula z bazy:** `references/baza-klauzul/` — spory

### ✓ Obszary bez zastrzeżeń

Prawo właściwe (polskie): brak zastrzeżeń. Pozostałe obszary z Kroku 1 mają flagi powyżej (odpowiedzialność i kary: 1, 2, 4–6, 8; prawa autorskie: 3; definicje: 13; reprezentacja: 14; wypowiedzenie i exit: 7, 10; RODO: 12; tytuł prawny: 11; poufność: 12; spory: 15).

---

## OCENA BEZPIECZEŃSTWA: 10/100

Trzy ryzyka krytyczne (kary poza capem bez sufitu, zakaz konkurencji z karą 300.000 zł bez ekwiwalentu, brak przeniesienia praw autorskich), cztery wysokie, sześć średnich i dwa niskie. Policzona ekspozycja Wykonawcy ≥ 1,07× wartości umowy przy nominalnym capie 50%.

**Werdykt:** NIE PODPISYWAĆ w obecnej formie (🟥 CZERWONY).

### Klauzule z bazy KTZR do uzupełnienia

🔴 Kary poza capem / sufit → `references/baza-klauzul/10-kary-umowne.md`, `11-odpowiedzialnosc.md`
🔴 Zakaz konkurencji → klauzula zakazu konkurencji z ekwiwalentem (baza klauzul)
🔴 Prawa autorskie → `references/baza-klauzul/08-prawa-autorskie-ip.md`
🟠 Indemnity, waloryzacja → `11-odpowiedzialnosc.md`, `07-terminy-kamienie-milowe.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
