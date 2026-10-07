konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 1 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

---

[DRAFT — DO WERYFIKACJI]

## AUDYT RYZYK — Umowa o świadczenie usług utrzymania (ORION SYSTEMS sp. z o.o. / FERRUM LOGISTICS sp. z o.o.)

> **WERDYKT: 🟩 ZIELONY** — umowa wyważona i spójna, do podpisania po uzupełnieniu dwóch punktów (prawa do poprawek, ewentualna umowa powierzenia danych) i drobnych poprawkach redakcyjnych. Brak ryzyk krytycznych i wysokich.

Tryb express, audyt neutralny (przy każdej fladze wskazano stronę dotkniętą). Usługodawca = ORION, Usługobiorca = FERRUM. Każde powołanie przepisu oznaczono [NIEZWERYFIKOWANE] (brak MCP legal-cite).

### Bramka ius cogens (R10)

- Wyłączenie winy umyślnej (art. 473 § 2 KC [NIEZWERYFIKOWANE]): § 5 ust. 1 wprost wyłącza szkodę umyślną z limitu — zgodne. Jedyna uwaga: § 5 ust. 2 (zob. flaga 🟢 nr 4).
- Kara umowna za zobowiązanie pieniężne (art. 483 § 1 KC [NIEZWERYFIKOWANE]): kara dotyczy zwłoki w usunięciu awarii (zobowiązanie niepieniężne) — brak naruszenia.
- Miarkowanie (art. 484 § 2 KC [NIEZWERYFIKOWANE]): umowa go nie wyłącza — brak naruszenia. Odszkodowanie uzupełniające ponad karę (art. 484 § 1 KC [NIEZWERYFIKOWANE]) umowa dopuszcza wprost — zgodne.
- Termin płatności 30 dni: poniżej granicy 60 dni z ustawy o przeciwdziałaniu nadmiernym opóźnieniom [NIEZWERYFIKOWANE] — brak naruszenia.
- Przedawnienie, prawa osobiste, pola eksploatacji: umowa tego nie dotyka (zob. flaga 🟡 nr 1).
- Trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]): obie strony to spółki z o.o. — nieaktywny.
- Efekt kumulatywny (test pięciopunktowy): cap, kara i wyłączenie lucrum cessans są wzajemnie spójne i proporcjonalne; brak systemowej asymetrii.

Wniosek: brak klauzul nieważnych z mocy prawa.

### 🧮 Rachunek ekspozycji

Liczby z umowy: wynagrodzenie 8.000 zł netto/mies. (§ 4 ust. 1); kara 1.000 zł za rozpoczęty Dzień Roboczy zwłoki, sufit 20% wynagrodzenia rocznego netto (§ 3 ust. 3); cap 12-miesięcznego wynagrodzenia netto (§ 5 ust. 1); wypowiedzenie 3 miesiące na koniec miesiąca (§ 7 ust. 2); płatność 30 dni (§ 4 ust. 2); konsultacje do 10 h/mies. (§ 2 ust. 1).

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy (rok) | 8.000 zł netto/mies. | 8.000 × 12 | **96.000 zł netto** (czas nieokreślony — wartość całkowita `[BRAK DANYCH]`) |
| Cap nominalny (Usługodawca) | 12 × wynagrodzenie netto | 12 × 8.000 | **96.000 zł = 1,0× wartości rocznej** |
| Sufit kar | 20% wynagrodzenia rocznego | 0,20 × 96.000 | **19.200 zł** |
| Kumulacja kary | 1.000 zł/dzień do sufitu | 19.200 / 1.000 = 19,2 | sufit osiągnięty w 20. rozpoczętym Dniu Roboczym zwłoki (19 dni = 19.000 zł; 20. dzień tylko 200 zł) |
| Kara a dzienne wynagrodzenie | 1.000 zł/dzień vs 8.000 zł/mies. | 8.000 / ok. 22 Dni Robocze ≈ 364 zł | kara ≈ 2,7× dziennej wartości wynagrodzenia — współmierna, nie rażąca |
| Efektywna ekspozycja Usługodawcy | cap + kary poza capem + wyłączenia | patrz niżej | **96.000 zł (jeśli kary wliczają się do capu) do 115.200 zł (96.000 + 19.200, jeśli kary są poza capem) = 1,0–1,2× wartości rocznej**; plus nieograniczona szkoda umyślna i naruszenie § 6 (poufność) `[BRAK DANYCH]` co do kwoty |
| Lucrum cessans | wyłączone (§ 5 ust. 2) | — | ekspozycja ogranicza się do szkody rzeczywistej; w praktyce pułap nominalny nie jest iluzoryczny, bo szkoda z przestoju magazynu to w dużej części utracone korzyści |
| Asymetria (Usługodawca vs Usługobiorca) | Usługodawca: cap 96.000 zł, kary max 19.200 zł; Usługobiorca: brak capu i kar | — | Usługobiorca odpowiada de facto tylko za zapłatę wynagrodzenia (ekspozycja 8.000 zł/mies. + odsetki ustawowe); asymetria odpowiada rozkładowi ról, nie jest wadą |
| Wypowiedzenie | 3 mies. na koniec miesiąca, obie strony | zobowiązanie w okresie wypowiedzenia 3 × 8.000 = 24.000 zł; przy zaokrągleniu do końca miesiąca do ok. 4 mies. = 32.000 zł | wypowiedzenie złożone 31.10 kończy umowę 31.01 (3 mies.); złożone 01.11 — upływ 01.02, skutek 28.02 (ok. 4 mies.) przy założeniu zaokrąglania w górę `[założenie]` |
| Termin płatności | 30 dni od doręczenia faktury | 30 < 60 | w normie |
| Konsultacje ponad 10 h/mies. | brak stawki | — | `[BRAK DANYCH]` |
| Okno SLA | reakcja 4 h w 8:00–16:00, usunięcie 2 Dni Robocze | awaria w piątek 15:00 → usunięcie najpóźniej we wtorek (2 Dni Robocze); kara za sobotę i niedzielę nie biegnie | max przerwa bez kary: do 4 dni kalendarzowych (pt–wt) |

Wniosek z rachunku: liczby są proporcjonalne i wzajemnie spójne (cap = 1× roczna wartość, kara do 20% rocznej wartości, wypowiedzenie 3 mies.). Nic w rachunku nie podnosi flag powyżej 🟡. Jedyna niepewność liczbowa (czy kary wliczają się do capu: 96.000 vs 115.200 zł) to różnica 19.200 zł — flaga 🟢.

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

Brak.

### 🟡 RYZYKA ŚREDNIE

#### 1. Brak regulacji praw do poprawek i modyfikacji Systemu — § 2 ust. 1
**Strona dotknięta:** przede wszystkim Usługobiorca (częściowo Usługodawca).
**Opis:** Usługodawca instaluje poprawki i usuwa błędy, czyli tworzy lub modyfikuje kod. Umowa nie mówi, kto jest właścicielem poprawek, ani nie udziela licencji ani nie przenosi praw z wymienieniem pól eksploatacji (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]); nie ma też gwarancji czystości IP ani klauzuli o komponentach open source. Usługobiorca mógłby po zakończeniu umowy nie mieć prawa dalej korzystać z poprawek wytworzonych przez Usługodawcę (albo odwrotnie: Usługodawca nie ma jasności, czy może używać know-how z poprawek u innych klientów).
**Skutek:** spór o uprawnienia do kodu przy wypowiedzeniu lub zmianie dostawcy.
**Rekomendacja (preferowana):** dodać klauzulę: poprawki i modyfikacje Systemu — przeniesienie majątkowych praw autorskich na Usługobiorcę z wyliczeniem pól eksploatacji (lub licencja bezterminowa), z zastrzeżeniem narzędzi i know-how Usługodawcy; gwarancja czystości IP.
**Fallback (minimum akceptowalne):** nieodwołalna, bezterminowa licencja niewyłączna na poprawki dla Usługobiorcy, z wyraźnie wymienionymi polami eksploatacji.
**Klauzula z bazy:** `references/baza-klauzul/` — plik o prawach autorskich/IP (wg INDEX.md).

#### 2. Brak umowy powierzenia przetwarzania danych osobowych — cała umowa (zwłaszcza § 2 ust. 1, § 7 ust. 3)
**Strona dotknięta:** obie (administrator: Usługobiorca; podmiot przetwarzający: Usługodawca).
**Opis:** Oprogramowanie magazynowe zwykle zawiera dane osobowe (pracownicy, kierowcy, kontrahenci). Utrzymanie i konsultacje z dostępem do produkcji mogą oznaczać przetwarzanie w imieniu Usługobiorcy. Umowa nie zawiera ani klauzuli powierzenia, ani odesłania do odrębnej umowy (art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]). § 7 ust. 3 mówi o zwrocie i usunięciu „danych", ale bez kwalifikacji ról, listy podwykonawców, zasad zgłaszania naruszeń. Flaga warunkowa: z samej umowy nie wynika, czy Usługodawca ma realny dostęp do danych osobowych (`[BRAK DANYCH]`).
**Skutek:** przetwarzanie bez wymaganej umowy to naruszenie po obu stronach; ryzyko kary administracyjnej (art. 83 RODO [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** jeśli dostęp do danych osobowych jest możliwy — załącznik z umową powierzenia (art. 28 RODO [NIEZWERYFIKOWANE]); jeśli nie — oświadczenie, że Usługodawca nie przetwarza danych osobowych i procedura na wypadek dostępu incydentalnego.
**Fallback (minimum akceptowalne):** zobowiązanie stron do zawarcia umowy powierzenia w terminie 14 dni od podpisania, przed pierwszym dostępem do danych.
**Klauzula z bazy:** `references/baza-klauzul/` — plik RODO/powierzenie oraz `references/checklist-dpa-art28.md`.

### 🟢 RYZYKA NISKIE

#### 1. Brak Załącznika nr 1 w dostarczonym tekście — § 1 ust. 1
**Strona dotknięta:** obie.
**Opis:** definicja „Systemu" odsyła do Załącznika nr 1, którego nie ma w analizowanym tekście; zakres utrzymania jest więc nieweryfikowalny (R11 — nie przypisuję treści, której nie widzę). Jeśli załącznik istnieje w podpisywanej wersji, flaga odpada.
**Rekomendacja:** dołączyć załącznik (wersja, moduły, środowiska, interfejsy). **Fallback:** opis Systemu w § 1 ust. 1.

#### 2. Niepełne dane i reprezentacja stron — komparycja
**Strona dotknięta:** obie.
**Opis:** brak KRS, NIP, adresów i sposobu reprezentacji (tu: „dane fikcyjne"). Przy podpisaniu rzeczywistej umowy konieczne (Złota Reguła nr 8).
**Rekomendacja:** uzupełnić KRS/NIP/adresy i wskazać reprezentację (odpis KRS). **Fallback:** dołączyć odpisy KRS do umowy.

#### 3. Niejasna relacja kar do capu i okres odniesienia sufitu — § 3 ust. 3 vs § 5 ust. 1
**Strona dotknięta:** głównie Usługobiorca (utrata kar po wyczerpaniu sufitu), pośrednio Usługodawca (niepewność ekspozycji).
**Opis:** (a) umowa nie mówi, czy kary wliczają się do limitu 96.000 zł (ekspozycja 96.000 vs 115.200 zł); (b) „łącznie nie więcej niż 20% wynagrodzenia rocznego" nie wskazuje, czy sufit liczy się na rok, na awarię, czy na cały okres umowy (przy czasie nieokreślonym). Jeśli na cały okres — jedna poważna awaria (20 dni) wyczerpuje sankcję na zawsze i późniejsze zwłoki są bezkarne poza odszkodowaniem.
**Rekomendacja:** doprecyzować: sufit na każdy rok obowiązywania; kary wliczają się (albo nie wliczają się) do limitu z § 5 ust. 1. **Fallback:** samo wskazanie, że kary wliczają się do limitu.

#### 4. Wyłączenie utraconych korzyści bez zastrzeżenia winy umyślnej — § 5 ust. 2
**Strona dotknięta:** Usługobiorca.
**Opis:** wyjątek dla winy umyślnej jest w ust. 1, ale ust. 2 (wyłączenie lucrum cessans) go nie powtarza. W zakresie szkody umyślnej wyłączenie byłoby i tak nieskuteczne (art. 473 § 2 KC [NIEZWERYFIKOWANE]), więc to kwestia redakcyjna i interpretacyjna, nie wada ważności.
**Rekomendacja:** dopisać „z wyjątkiem szkody wyrządzonej umyślnie". **Fallback:** brak — zmiana kosmetyczna.

#### 5. Luki operacyjne w zakresie usług — § 2 ust. 1, § 3
**Strona dotknięta:** obie.
**Opis:** SLA dotyczy tylko Awarii Krytycznej; dla „innych błędów" brak terminów i priorytetów. Brak trybu i kanału zgłoszeń (od kiedy liczy się zgłoszenie). Konsultacje ponad 10 h/mies. bez stawki (`[BRAK DANYCH]`) — nie wiadomo, czy to odmowa świadczenia czy płatna usługa. SLA tylko w godz. 8:00–16:00 w Dni Robocze: dla magazynu pracującego w weekendy ryzyko biznesowe po stronie Usługobiorcy (to świadomy wybór handlowy, nie wada).
**Rekomendacja:** dodać kanał zgłoszeń z chwilą doręczenia, kategorie błędów z terminami, stawkę za nadwyżkę godzin. **Fallback:** sam kanał zgłoszeń i stawka za nadwyżkę.

#### 6. Brak terminu zwrotu i usunięcia danych — § 7 ust. 3
**Strona dotknięta:** Usługobiorca.
**Opis:** „zwróci … i usunie" bez terminu i bez potwierdzenia usunięcia. Konstrukcja wyjątku (kopie wymagane przepisami, z informacją o podstawie i okresie) jest prawidłowa.
**Rekomendacja:** termin (np. 14 dni od zakończenia) i pisemne potwierdzenie usunięcia. **Fallback:** sam termin.

### ✓ Obszary bez zastrzeżeń

- **Odpowiedzialność i kary:** cap 12 mies. wynagrodzenia, wyjątek dla winy umyślnej i poufności, kara współmierna z sufitem, odszkodowanie uzupełniające dopuszczone zgodnie z art. 484 § 1 KC [NIEZWERYFIKOWANE] — w porządku (poza flagami 🟢 nr 3 i 4). Uwaga informacyjna: wyłączenie naruszenia § 6 z capu oznacza nieograniczoną odpowiedzialność Usługodawcy za wyciek informacji poufnych — rynkowe, ale warto, by zarząd Usługodawcy o tym wiedział.
- **Tytuł prawny:** usługi o charakterze starannego działania z wyodrębnionym rezultatem dla Awarii Krytycznej (§ 2 ust. 2) — kwalifikacja jasna i spójna z karą za zwłokę; art. 750 KC [NIEZWERYFIKOWANE]. Body leasing/przekwalifikowanie na stosunek pracy — n/d.
- **Poufność:** wzajemna, 3 lata po zakończeniu, tajemnica przedsiębiorstwa bezterminowo, standardowe wyłączenia — w porządku. Brak kary umownej za naruszenie to wybór (egzekucja przez odszkodowanie), nie wada.
- **Wypowiedzenie i exit:** symetryczne, 3 miesiące, procedura zwrotu danych jest (poza flagą 🟢 nr 6). Przy czasie nieokreślonym brak wypowiedzenia natychmiastowego z ważnych przyczyn — dopuszczalne, 3 mies. jest akceptowalne dla obu stron.
- **Spory i prawo:** prawo polskie, sąd siedziby Usługodawcy; obie spółki mają siedzibę w Gdańsku, więc właściwość jest praktycznie neutralna. Zmiana umowy pod rygorem nieważności formy pisemnej (art. 76 KC [NIEZWERYFIKOWANE] — dla pewności: zmiany e-mailem byłyby nieskuteczne) — operacyjnie uciążliwe, ale nie wada.
- **Definicje i logika:** wszystkie terminy pisane wielką literą mają definicję (System, Usługi, Dzień Roboczy, Awaria Krytyczna); „Usługodawca/Usługobiorca" stosowane spójnie; odesłania § 3 ust. 3 → § 5 ust. 1 oraz § 5 ust. 1 → § 6 prowadzą do właściwych przepisów. „Umowa" (z wielkiej litery) w § 5–8 nie jest zdefiniowana — uchybienie redakcyjne bez znaczenia merytorycznego.
- **Wynagrodzenie:** ryczałt stały bez waloryzacji przy czasie nieokreślonym obciąża Usługodawcę (inflacja), ale łagodzi to możliwość wypowiedzenia po 3 miesiącach — brak flagi.

---

## OCENA BEZPIECZEŃSTWA: 84/100

Brak ryzyk krytycznych i wysokich; dwa ryzyka średnie (prawa do poprawek, powierzenie danych — drugie warunkowe) i sześć drobnych. Rachunek ekspozycji potwierdza współmierność cap, kar i wypowiedzenia. Ocena zgodna z werdyktem ZIELONYM (zero 🔴, zero 🟠).

**Werdykt:** DO PODPISANIA z drobnymi poprawkami (po uzupełnieniu praw do poprawek i ustaleniu kwestii powierzenia danych).

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
