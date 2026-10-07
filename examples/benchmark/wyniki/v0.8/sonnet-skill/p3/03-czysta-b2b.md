konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 3 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite: każde powołanie przepisu oznaczone [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa o świadczenie usług utrzymania (ORION SYSTEMS sp. z o.o. / FERRUM LOGISTICS sp. z o.o.)

> **WERDYKT: 🟩 ZIELONY** — do podpisania; dwie uwagi 🟡 (§ 5 ust. 2 i brak klauzuli o prawach do poprawek) warto domknąć przed podpisem, żadna nie jest dealbreakerem.

Bramka ius cogens (R10): brak trafienia. Strony to spółki kapitałowe, więc trigger art. 385⁵ KC [NIEZWERYFIKOWANE] nie jest aktywny. Brak kary za zobowiązanie pieniężne, brak wyłączenia miarkowania, brak skracania przedawnienia, termin płatności 30 dni (poniżej granicy 60 dni). Jedyne miejsce graniczne to § 5 ust. 2, opisane niżej jako 🟡, a nie 🔴 (uzasadnienie przy fladze).

### 🧮 Rachunek ekspozycji

Liczby z tekstu umowy: ryczałt 8.000 zł netto/mies.; kara 1.000 zł za rozpoczęty Dzień Roboczy zwłoki; sufit kar 20% wynagrodzenia rocznego netto; cap 12-miesięcznego wynagrodzenia netto; reakcja 4 h; usunięcie 2 Dni Robocze; płatność 30 dni; wypowiedzenie 3 miesiące na koniec miesiąca; poufność 3 lata po zakończeniu (tajemnica przedsiębiorstwa — bezterminowo); do 10 godzin konsultacji miesięcznie.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość roczna | 8.000 zł netto/mies. | 8.000 × 12 | **96.000 zł netto** |
| Wartość całej umowy | czas nieokreślony | — | [BRAK DANYCH] (wartość minimalna, do końca okresu wypowiedzenia: 24.000–32.000 zł, zob. niżej) |
| Cap nominalny (§ 5 ust. 1) | 12 × wynagrodzenie netto | 12 × 8.000 | **96.000 zł = 1,0× wartości rocznej** |
| Sufit kar (§ 3 ust. 3) | 20% wynagrodzenia rocznego netto | 0,20 × 96.000 | **19.200 zł = 2,4 × wynagrodzenie miesięczne** |
| Kara dzienna | 1.000 zł / rozpoczęty Dzień Roboczy | 1.000 / 8.000 | 12,5% wynagrodzenia miesięcznego za dzień |
| Dni do osiągnięcia sufitu | — | 19.200 / 1.000 | 19,2, czyli sufit uruchamia się w 20. rozpoczętym dniu zwłoki (19 dni = 19.000 zł; 20. dzień obcięty do 19.200 zł) |
| Efektywna ekspozycja Usługodawcy — wariant A (kary wliczają się do capu) | — | cap 96.000 | 96.000 zł = 1,0× |
| Efektywna ekspozycja — wariant B (kary poza capem) | — | 96.000 + 19.200 | **115.200 zł = 1,2× wartości rocznej** |
| Poza capem | szkoda umyślna; naruszenie § 6 | — | [BRAK DANYCH] — kwota otwarta, bez sufitu |
| Odszkodowanie za utracone korzyści | wyłączone (§ 5 ust. 2) | — | 0 zł (dla Usługobiorcy, z zastrzeżeniem flagi 🟡 1) |
| Asymetria kar/odpowiedzialności | kary tylko po stronie Usługodawcy | 19.200 : 0 | Usługobiorca nie ma kar; jego zobowiązanie to zapłata (cap go nie dotyczy). Rozkład naturalny dla umowy usług, bez cech fałszywej wzajemności |
| Wypowiedzenie | 3 mies., koniec miesiąca, symetryczne | np. oświadczenie doręczone 07.10.2026 → 3 mies. upływają 07.01.2027 → skutek 31.01.2027 (założenie: okres liczony od doręczenia, skutek na najbliższy koniec miesiąca po jego upływie) | umowa trwa po wypowiedzeniu ok. 3–4 miesięcy = **24.000–32.000 zł** wynagrodzenia |
| Płatność | 30 dni od doręczenia faktury | < 60 dni | w normie, brak flagi |
| Poufność po umowie | 3 lata; tajemnica bezterminowo | — | „bezterminowo" zaznaczone jawnie, dotyczy tylko tajemnicy przedsiębiorstwa |
| Efektywna stawka za godzinę, jeżeli limit 10 godzin obejmuje całość usług | 8.000 / 10 h | 8.000 / 10 | 800 zł/h (tylko przy odczytaniu z flagi 🟢 1 w najszerszym sensie) |
| Maksymalny przestój bez kary (zgłoszenie w piątek po 16:00) | reakcja 4 h w godz. 8–16 Dni Robocze; usunięcie 2 Dni Robocze | piątek po 16:00 → reakcja najwcześniej poniedziałek 12:00; 2 Dni Robocze → do końca wtorku | do ok. 4 dób kalendarzowych (dłużej przy dniu ustawowo wolnym) przed wystąpieniem zwłoki |

**Wniosek z rachunku:** cap nie jest iluzoryczny. Efektywna ekspozycja Usługodawcy mieści się w 1,0–1,2× wartości rocznej, a otwarte są tylko dwa zdarzenia (szkoda umyślna i naruszenie poufności), zwyczajowo wyjęte z limitu. Kary są proporcjonalne (maks. 2,4 miesięcznego wynagrodzenia). Rachunek nie podnosi żadnej flagi do 🟠.

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

Brak.

### 🟡 RYZYKA ŚREDNIE

#### 1. Wyłączenie utraconych korzyści bez zastrzeżenia o winie umyślnej — § 5 ust. 2
**Strona dotknięta:** Usługobiorca (traci środek ochrony); w razie sporu także Usługodawca (niepewność zakresu klauzuli).
**Opis:** Zastrzeżenie o szkodzie umyślnej stoi w ust. 1 („Ograniczenie nie dotyczy…") i odnosi się do capu. Ust. 2 („Usługodawca nie odpowiada za utracone korzyści") jest osobnym wyłączeniem, którego zastrzeżenie literalnie nie obejmuje. W zakresie szkody umyślnej wyłączenie byłoby bezskuteczne z mocy prawa (art. 473 § 2 KC, art. 58 § 3 KC [NIEZWERYFIKOWANE]), więc to wada redakcyjna, a nie nieważność klauzuli w całości. Dlatego nie podnoszę jej do 🔴: systemowa wykładnia z ust. 1 wskazuje wolę stron zachowania odpowiedzialności za winę umyślną, a sankcja działa automatycznie w wąskim zakresie.
**Skutek (liczbowo):** Przy awarii systemu magazynowego główną szkodą Usługobiorcy są utracone korzyści (przestój przyjęć i wydań). Usługobiorca ma wtedy kary do 19.200 zł oraz szkodę rzeczywistą w granicach capu 96.000 zł. Utracone korzyści: 0 zł, nawet przy rażącym niedbalstwie Usługodawcy.
**Rekomendacja (preferowana):** Zastrzeżenie o szkodzie umyślnej rozciągnąć na ust. 1 i 2 („Ograniczenia i wyłączenia z ust. 1 i 2 nie dotyczą…"). Rozważyć sprecyzowanie, czy wyłączenie obejmuje także rażące niedbalstwo.
**Fallback (minimum akceptowalne):** Zostawić wyłączenie utraconych korzyści, ale dopisać zastrzeżenie o winie umyślnej do ust. 2.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Brak postanowienia o prawach do poprawek i innych rezultatach prac — cała umowa (zakres § 2 ust. 1)
**Strona dotknięta:** Usługobiorca (może nie mieć tytułu do korzystania z poprawek po zakończeniu umowy); Usługodawca (niepewność, co wolno mu wykorzystać ponownie).
**Opis:** § 2 ust. 1 obejmuje „instalację poprawek" i usuwanie błędów. Umowa nie mówi, kto jest właścicielem praw do poprawek tworzonych przez Usługodawcę ani na jakich polach eksploatacji Usługobiorca może z nich korzystać. Brak też wzmianki o pochodzeniu i składnikach open source w poprawkach. Gdyby przeniesienie lub licencja miały nastąpić, wymagają wskazania pól eksploatacji (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]); bez tego Usługobiorca opiera się na domniemanej licencji. Brak danych, kto jest autorem Systemu (umowa nazywa go „oprogramowaniem Usługobiorcy"); to ogranicza skalę oceny.
**Skutek:** [BRAK DANYCH] co do wartości; ryzyko dotyczy możliwości korzystania z poprawek po wypowiedzeniu (3–4 miesiące od oświadczenia) i sporu o prawo do ich wykorzystania.
**Rekomendacja (preferowana):** Dodać postanowienie: przeniesienie praw majątkowych do poprawek z wyliczeniem pól eksploatacji (lub licencja wyłączna bezterminowa), z gwarancją czystości IP i klauzulą anty-copyleft.
**Fallback (minimum akceptowalne):** Niewyłączna, bezterminowa, nieodwołalna licencja do korzystania z poprawek w Systemie z wyliczonymi polami eksploatacji.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟢 RYZYKA NISKIE

#### 1. Niejasny zakres limitu 10 godzin i brak terminów dla „innych błędów" — § 2 ust. 1, § 3
**Strona dotknięta:** oboje (Usługodawca: ryzyko pracy ponad ryczałt; Usługobiorca: brak terminu dla błędów niekrytycznych).
**Opis:** „w wymiarze do 10 godzin miesięcznie" stoi na końcu wyliczenia i najpewniej odnosi się tylko do konsultacji, ale składnia dopuszcza też odczyt na całość usług. Jednocześnie § 2 ust. 2 czyni usunięcie Awarii Krytycznej rezultatem, co wyklucza limit godzinowy dla awarii. Terminy z § 3 dotyczą wyłącznie Awarii Krytycznej, a „inne błędy" nie mają ani terminu reakcji, ani usunięcia.
**Rekomendacja:** Przesunąć „do 10 godzin miesięcznie" bezpośrednio za „konsultacje techniczne" i dopisać, że usuwanie Awarii Krytycznych nie zalicza się do limitu; dodać termin reakcji dla pozostałych błędów.

#### 2. Relacja kar umownych do capu odpowiedzialności — § 3 ust. 3, § 5 ust. 1
**Strona dotknięta:** oboje (różnica 19.200 zł).
**Opis:** Umowa nie rozstrzyga, czy kary wliczają się do „łącznej odpowiedzialności z Umowy" (cap 96.000 zł), czy są obok niego (115.200 zł łącznie). Ust. 3 mówi o odszkodowaniu uzupełniającym „do wysokości limitu z § 5 ust. 1", co wskazuje na wspólny limit, ale nie mówi tego wprost.
**Rekomendacja:** Dopisać jedno zdanie: „Kary umowne wliczają się do limitu z § 5 ust. 1" (albo odwrotnie, zgodnie z wolą stron).

#### 3. Formalia: brak Załącznika nr 1, niezdefiniowane „Umowa" i „Strony", brak danych rejestrowych — preambuła, § 1 ust. 1
**Strona dotknięta:** oboje.
**Opis:** § 1 ust. 1 definiuje System przez Załącznik nr 1, którego w przekazanym tekście nie ma (jeśli istnieje poza tekstem — uwaga bezprzedmiotowa). Pojęcia „Umowa" i „Strony" są używane wielką literą bez definicji. W oznaczeniu stron nie ma KRS, NIP ani sposobu reprezentacji (strony oznaczono jako fikcyjne, więc to uwaga formalna). „Wynagrodzenie roczne netto" w § 3 ust. 3 nie jest zdefiniowane, ale daje się wyliczyć (96.000 zł).
**Rekomendacja:** Dołączyć załącznik, dopisać „(dalej: „Umowa")" i „(dalej łącznie: „Strony")", uzupełnić dane rejestrowe i reprezentację.

#### 4. Naruszenie poufności poza capem bez sufitu — § 5 ust. 1, § 6
**Strona dotknięta:** Usługodawca (kwota otwarta wobec rocznej wartości umowy 96.000 zł).
**Opis:** Wyjęcie naruszenia poufności z limitu to standard rynkowy, a obowiązek jest obustronny i ma wyłączenia (§ 6 ust. 2). Skutek: ekspozycja Usługodawcy w tym obszarze jest nieograniczona, choć wynagrodzenie roczne to 96.000 zł. Usługodawca ma dostęp do danych magazynowych klienta.
**Rekomendacja:** Opcjonalnie wprowadzić osobny, wyższy limit (np. wielokrotność capu) zamiast braku limitu; to uwaga negocjacyjna dla Usługodawcy, nie wada umowy.

### ✓ Obszary bez zastrzeżeń

- **Kary umowne:** proporcjonalne, z sufitem 20% (19.200 zł), dotyczą zobowiązania niepieniężnego, odszkodowanie uzupełniające dozwolone wprost (art. 484 § 1 KC [NIEZWERYFIKOWANE]); kary nie obejmują zobowiązania pieniężnego, nie wyłączono miarkowania.
- **Cap odpowiedzialności:** nominalnie 1,0× rocznego wynagrodzenia, z właściwym wyłączeniem szkody umyślnej (ust. 1); po rachunku nie jest iluzoryczny.
- **Wynagrodzenie i płatność:** ryczałt, 30 dni, w normie. Brak waloryzacji przy umowie na czas nieokreślony to ryzyko Usługodawcy (stała stawka 8.000 zł), ale ma on symetryczne prawo wypowiedzenia z 3-miesięcznym okresem, więc nie flaguję.
- **Wypowiedzenie i exit:** wypowiedzenie symetryczne, okres 3 miesiące, zwrot dokumentacji i danych oraz usunięcie kopii z wyjątkiem wymaganych przepisami (z obowiązkiem poinformowania o podstawie i okresie). Procedura exit zamknięta.
- **Poufność:** okres po zakończeniu (3 lata), bezterminowo dla tajemnicy przedsiębiorstwa, wyłączenia zwyczajowe. W porządku.
- **Tytuł prawny:** usługa utrzymania z jednoznacznym rozdzieleniem staranności i rezultatu (§ 2 ust. 2); brak ryzyka przekwalifikowania.
- **Spory:** prawo polskie, sąd właściwy dla siedziby Usługodawcy; brak jurysdykcji zagranicznej i klauzuli arbitrażowej. Wybór siedziby Usługodawcy jest korzystniejszy dla Usługodawcy, ale obie strony mają siedzibę w Gdańsku, więc praktyczny skutek zerowy.
- **Reprezentacja:** zob. 🟢 3 (uwaga formalna).
- **RODO:** n/d wg treści umowy (brak mowy o danych osobowych). Jeżeli Usługodawca ma dostęp do danych osobowych w Systemie (pracownicy, kontrahenci, kierowcy), konieczna jest umowa powierzenia (art. 28 RODO [NIEZWERYFIKOWANE]). To zależy od faktów spoza tekstu, więc nie podnoszę flagi.
- **SLA:** okno 8–16 w Dni Robocze przy systemie magazynowym to wybór komercyjny (zob. rachunek: do ok. 4 dób przestoju bez kary), nie wada prawna; Usługobiorca powinien zważyć, czy takie okno odpowiada jego pracy magazynu.

---

## OCENA BEZPIECZEŃSTWA: 88/100

Umowa spójna, z proporcjonalnymi karami i nieiluzorycznym capem; dwie uwagi 🟡 (luka w klauzuli § 5 ust. 2, brak regulacji praw do poprawek) i cztery 🟢 nie zmieniają jej charakteru.

**Werdykt:** DO PODPISANIA z drobnymi poprawkami

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
