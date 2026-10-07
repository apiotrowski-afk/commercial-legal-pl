konfiguracja: fable-skill
commit skilla: fa26dc0
przebieg: 1 z 1
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

---

## AUDYT RYZYK — Umowa o świadczenie usług utrzymania (ORION SYSTEMS sp. z o.o. / FERRUM LOGISTICS sp. z o.o.)

> **WERDYKT: 🟩 ZIELONY** — do podpisania z drobnymi poprawkami: doprecyzować arytmetykę limitów (§ 3 ust. 3, § 5 ust. 1) i uregulować prawa do poprawek; przed podpisem potwierdzić, czy Usługodawca uzyska dostęp do danych osobowych (jeżeli tak — umowa powierzenia jest warunkiem, zob. 🟢 4).

**Tryb i założenia.** Tryb express (bez STOP-ów), audyt neutralny — przy każdej fladze wskazana strona dotknięta. Brak `practice-profile.md` → standardowe progi KTZR. Brak MCP legal-cite → każdy przepis oznaczony [NIEZWERYFIKOWANE]. Pamięć kancelarii — pominięta (benchmark, zamknięte wejście). Obie strony to spółki z o.o. → trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]) nieaktywny.

---

### ⚖️ Bramka ius cogens (R10)

| Norma | Wynik | Uzasadnienie |
|---|---|---|
| art. 473 § 2 KC [NIEZWERYFIKOWANE] — wina umyślna | ✓ brak trafienia | § 5 ust. 1 zd. 2 wprost wyłącza cap dla szkody umyślnej. § 5 ust. 2 (utracone korzyści) nie zawiera tego wyjątku, ale nie próbuje objąć winy umyślnej; w tym zakresie i tak nie działa (art. 58 § 3 KC [NIEZWERYFIKOWANE]), a systemowa wykładnia § 5 prowadzi do tego samego wyniku. Ochrona Usługobiorcy zostaje z mocy ustawy, więc to wada redakcyjna (🟢 1), a nie nieważność wymagająca negocjacji. |
| art. 483 § 1 KC [NIEZWERYFIKOWANE] — kara za świadczenie pieniężne | ✓ | Kara z § 3 ust. 3 zabezpiecza usunięcie Awarii Krytycznej, czyli świadczenie niepieniężne. |
| art. 484 § 2 KC [NIEZWERYFIKOWANE] — miarkowanie | ✓ | Miarkowanie nie zostało wyłączone. |
| art. 119 KC [NIEZWERYFIKOWANE] — przedawnienie | ✓ | Umowa nie modyfikuje terminów przedawnienia. |
| art. 16, art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE] | — n/d | Umowa nie przenosi praw (to luka, nie naruszenie — zob. 🟡 2). |
| ustawa o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych, art. 7 ust. 2 [NIEZWERYFIKOWANE] | ✓ | Termin płatności 30 dni < 60 dni. |
| art. 28 ust. 3 RODO [NIEZWERYFIKOWANE] | ? warunkowo | Zależy od faktu, którego umowa nie przesądza (🟢 4). |
| art. 353¹ + art. 58 § 2 KC [NIEZWERYFIKOWANE] / test kumulatywny | ✓ | Brak systemowej asymetrii: cap Usługodawcy = 100% rocznego wynagrodzenia, wyłączenia spod capu zgodne z KTZR, wypowiedzenie symetryczne, kary umiarkowane i z sufitem. Suma klauzul nie przechyla umowy. |

---

### 🧮 Rachunek ekspozycji (R12)

**Liczby z umowy:** 8.000 zł netto/mies. (ryczałt) · płatność 30 dni od doręczenia faktury · kara 1.000 zł za rozpoczęty Dzień Roboczy zwłoki, sufit 20% wynagrodzenia rocznego netto · cap 12 × wynagrodzenie miesięczne netto · reakcja 4 h (DR, 8:00–16:00) · usunięcie 2 DR · konsultacje do 10 h/mies. · wypowiedzenie 3 mies. na koniec miesiąca · poufność 3 lata po zakończeniu, tajemnica przedsiębiorstwa bezterminowo · czas nieokreślony od 01-06-2026.

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 8.000 zł netto/mies., czas nieokreślony | 12 × 8.000 | **96.000 zł netto/rok**; wartość całkowita [BRAK DANYCH]. Minimum (wypowiedzenie doręczone 01-06-2026 → 01-09-2026 → skutek 30-09-2026) = 4 × 8.000 = **32.000 zł** |
| Cap nominalny (§ 5 ust. 1) | „równowartości 12-miesięcznego wynagrodzenia netto" | 12 × 8.000 | **96.000 zł** = 1,0× rocznego wynagrodzenia |
| Sufit kar (§ 3 ust. 3) | 20% wynagrodzenia rocznego netto | 0,20 × 96.000 | **19.200 zł** = 2,4 × wynagrodzenie miesięczne |
| Kumulacja kary | 1.000 zł/DR | 19 DR = 19.000 zł; 20. DR dolicza tylko 200 zł | sufit osiągnięty w **20. Dniu Roboczym** zwłoki (~4 tygodnie kalendarzowe); kara dzienna = 12,5% wynagrodzenia miesięcznego |
| Kara a cap (wariant A: kara mieści się w capie) | „Łączna odpowiedzialność … z Umowy" | max 96.000 | **96.000 zł** |
| Kara a cap (wariant B: kara obok capu, odszkodowanie uzupełniające do 96.000) | § 3 ust. 3 zd. 2 | 19.200 + 96.000 | **115.200 zł** = 1,2× rocznego wynagrodzenia |
| Okres odniesienia sufitu kar i capu | „łącznie" / „Łączna" — brak okresu | przy 5 latach umowy (480.000 zł): limit łączny 19.200 zł = 4% wynagrodzeń; limit roczny do 96.000 zł = 20% | rozrzut **19.200 zł vs 96.000 zł** kar w 5 lat (🟡 1) |
| Wyłączenia z capu | szkoda umyślna, naruszenie § 6 | bez limitu kwotowego | [BRAK DANYCH] — ekspozycja otwarta; przy § 6 tylko szkoda rzeczywista (§ 5 ust. 2) |
| Indemnity | brak | — | 0 zł |
| **Efektywna ekspozycja Usługodawcy** | — | cap + kary + wyłączenia | **96.000–115.200 zł = 1,0–1,2× rocznego wynagrodzenia** + otwarta dla winy umyślnej i § 6 |
| Ekspozycja Usługobiorcy | brak capu, brak kar | zobowiązanie główne pieniężne: 8.000 zł + VAT/mies.; opóźnienie → odsetki i rekompensata ustawowa [NIEZWERYFIKOWANE] | [BRAK DANYCH] co do kwot odsetek; za § 6 odpowiada bez limitu, łącznie z utraconymi korzyściami |
| Asymetria (Usługodawca vs Usługobiorca) | kary 19.200 zł vs 0 zł; cap 96.000 zł vs brak | brak kar po stronie Usługobiorcy wynika z art. 483 § 1 KC [NIEZWERYFIKOWANE] (świadczenie pieniężne) | asymetria **uzasadniona naturą świadczeń**; jedyna realna różnica: utracone korzyści przy § 6 (🟢 1) |
| Wypowiedzenie (data graniczna) | 3 mies., skutek na koniec miesiąca | np. doręczenie 07-10-2026 → 07-01-2027 → skutek **31-01-2027** | realny okres 3 mies. – ok. 3 mies. i 4 tyg.; „ogon" kosztowy 24.000–32.000 zł netto (symetryczny) |
| SLA — najgorszy przypadek kalendarzowy | reakcja 4 h w oknie 8–16 DR; usunięcie 2 DR | zgłoszenie w piątek o 16:01 → reakcja do poniedziałku 12:00 [ZAŁOŻENIE: zegar biegnie tylko w oknie]; 2 DR = pon., wt. → kara od środy | przestój przyjęć/wydań do **ok. 4 dni kalendarzowych bez naruszenia**; przy dniach ustawowo wolnych dłużej |
| Płatność | 30 dni od doręczenia faktury | ≤ 60 dni | ✓; moment wystawienia faktury [BRAK DANYCH] |
| Poufność | 3 lata po zakończeniu | przy skutku wypowiedzenia 31-01-2027 → do 31-01-2030 | tajemnica przedsiębiorstwa — bezterminowo |
| Godziny konsultacji | do 10 h/mies. | stawka ponad limit / przenoszenie niewykorzystanych godzin | [BRAK DANYCH] |

**Wniosek z rachunku:** cap nie jest iluzoryczny. Ekspozycja Usługodawcy mieści się w 1,0–1,2× rocznego wynagrodzenia, kary są umiarkowane (sufit 2,4 miesięcznego wynagrodzenia) i nie wychodzą poza rozsądny horyzont. Jedyny rozjazd liczbowy wynika z niedookreślenia okresu odniesienia i relacji kary do capu: do 19.200 zł w jednym roku i do ok. 77.000 zł w horyzoncie 5 lat. To poziom 🟡, nie 🟠.

---

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

Brak.

### 🟡 RYZYKA ŚREDNIE

#### 1. Limity „łącznie" / „Łączna" bez okresu odniesienia; niejasna relacja kary do capu — § 3 ust. 3, § 5 ust. 1
**Strona dotknięta:** obie (wynik zależy od przyjętej wykładni).
**Opis:** Sufit kar brzmi „łącznie nie więcej niż 20% wynagrodzenia rocznego netto", a cap — „Łączna odpowiedzialność Usługodawcy z Umowy ograniczona jest do równowartości 12-miesięcznego wynagrodzenia netto". Umowa jest zawarta na czas nieokreślony i nie wskazuje, czy limity liczy się raz na cały czas trwania umowy, w każdym roku, czy (przy karze) dla każdej Awarii Krytycznej osobno. Nie rozstrzyga też, czy kara zalicza się do capu: zwrot „odszkodowanie uzupełniające do wysokości limitu z § 5 ust. 1" da się czytać jako „kara + odszkodowanie ≤ 96.000 zł" albo „kara 19.200 zł + odszkodowanie do 96.000 zł".
**Skutek:** przy odczycie „na cały czas trwania" sankcja wyczerpuje się raz na zawsze. Po osiągnięciu 19.200 zł (np. w 2. roku) kolejne zwłoki nie kosztują Usługodawcę nic ponad odszkodowanie na zasadach ogólnych, a cap 96.000 zł obejmuje całe, potencjalnie wieloletnie, utrzymanie — to ryzyko Usługobiorcy. Przy odczycie „per Awaria" i „kara obok capu" ekspozycja Usługodawcy rośnie do 115.200 zł i więcej — to ryzyko Usługodawcy. Spór o wykładnię (art. 65 KC [NIEZWERYFIKOWANE]) dotyczy kwot rzędu 19.200–77.000 zł.
**Rekomendacja (preferowana):** dopisać okres odniesienia i relację, np. sufit kar „w każdym roku obowiązywania Umowy, liczonym od dnia jej zawarcia"; cap „w odniesieniu do zdarzeń zaistniałych w każdym roku obowiązywania Umowy"; jedno zdanie, czy kary zalicza się na poczet limitu z § 5 ust. 1. Sama decyzja „zalicza / nie zalicza" jest handlowa; ważne, żeby zapadła na piśmie.
**Fallback (minimum akceptowalne):** zostawić limity łączne, ale dopisać zdanie o zaliczaniu kar na poczet capu (usuwa rozrzut 19.200 zł).
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (klauzula wzorcowa — cap liczony od wynagrodzenia z ostatnich 12 miesięcy); `references/baza-klauzul/10-kary-umowne.md` (klauzula wzorcowa — sufit kary i odszkodowanie uzupełniające).

#### 2. Brak regulacji praw do poprawek i modyfikacji Systemu — § 2 ust. 1 (luka)
**Strona dotknięta:** Usługobiorca (ciągłość korzystania i utrzymania po zmianie dostawcy); Usługodawca (brak oświadczenia Usługobiorcy o uprawnieniu do zlecania modyfikacji Systemu).
**Opis:** Usługi obejmują „usuwanie Awarii Krytycznych i innych błędów, instalację poprawek", czyli w praktyce zmiany kodu lub konfiguracji Systemu. Umowa nie mówi, komu przysługują prawa do poprawek wytworzonych przez Usługodawcę, czy Usługobiorca może je dalej modyfikować i przekazać następcy, ani czy Usługobiorca jest uprawniony zezwolić na modyfikację Systemu (jeśli System jest licencjonowany od osoby trzeciej). Art. 75 ust. 1 PrAut [NIEZWERYFIKOWANE] pozwala legalnemu użytkownikowi poprawiać błędy, ale nie rozstrzyga praw Usługodawcy do kodu, który sam napisał.
**Skutek:** zostaje licencja dorozumiana o spornym zakresie. Licencję udzieloną na czas nieoznaczony można wypowiedzieć na rok naprzód, na koniec roku kalendarzowego (art. 68 ust. 1 PrAut [NIEZWERYFIKOWANE]). Po rozstaniu nowy dostawca modyfikuje System z cudzymi poprawkami bez jasnego tytułu. Po drugiej stronie: Usługodawca, modyfikując licencjonowany System bez upoważnienia producenta, naraża się na roszczenia osoby trzeciej. Ryzyko dotyczy tylko poprawek, które są utworem (`references/baza-wiedzy/15-ochrona-utworu-test.md`). Proste zmiany konfiguracji tego progu zwykle nie przekraczają.
**Rekomendacja (preferowana):** przeniesienie autorskich praw majątkowych do poprawek z chwilą zapłaty wynagrodzenia za miesiąc, w którym je wykonano, na wymienionych polach eksploatacji (zwłaszcza modyfikowanie) z prawem zależnym (art. 41 ust. 2, art. 46 PrAut [NIEZWERYFIKOWANE]) oraz oświadczenie Usługobiorcy, że jest uprawniony do zlecania modyfikacji Systemu.
**Fallback (minimum akceptowalne):** niewyłączna licencja na poprawki, nieograniczona czasowo, bez prawa wypowiedzenia, z prawem modyfikacji i dalszego udostępnienia podmiotowi utrzymującemu System, w formie pisemnej.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md` — „Pełne przeniesienie praw z zachowaniem pól eksploatacji i praw zależnych (maintenance IT)" (dopasować do skali umowy; wariant white-label i AI zbędny).

### 🟢 RYZYKA NISKIE

#### 1. Wyłączenie utraconych korzyści bez wyjątków — § 5 ust. 2
**Strona dotknięta:** Usługobiorca.
**Opis:** Wyjątek z § 5 ust. 1 zd. 2 („Ograniczenie nie dotyczy szkody wyrządzonej umyślnie ani naruszenia § 6") odnosi się gramatycznie do capu. Ust. 2 („Usługodawca nie odpowiada za utracone korzyści Usługobiorcy") wyjątku nie ma. Wobec szkody umyślnej wyłączenie i tak nie działa (art. 473 § 2 w zw. z art. 58 § 3 KC [NIEZWERYFIKOWANE]), więc ten element jest tylko redakcyjny. Druga warstwa ma znaczenie handlowe: przy naruszeniu § 6 cap jest zdjęty, ale utracone korzyści pozostają wyłączone. Skutkiem naruszenia poufności bywa właśnie utrata kontraktów, więc wyjęcie § 6 spod capu chroni w praktyce tylko szkodę rzeczywistą. Usługobiorca za to samo naruszenie odpowiada w pełnym zakresie.
**Skutek:** brak realnej luki przy winie umyślnej (chroni ustawa); przy § 6 węższa ochrona Usługobiorcy niż sugeruje ust. 1.
**Rekomendacja (preferowana):** „z wyjątkiem szkody wyrządzonej umyślnie oraz szkody wynikłej z naruszenia § 6".
**Fallback (minimum akceptowalne):** sam wyjątek dla szkody umyślnej (porządkuje stan prawny) i świadoma decyzja, że przy § 6 utracone korzyści pozostają wyłączone.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (klauzula wzorcowa — wyłączenie utraconych korzyści „chyba że szkoda wynikła z działania umyślnego Strony"); `references/baza-wiedzy/05-cap-lucrum-wina-umyslna.md`.

#### 2. Mechanika SLA i błędy niekrytyczne — § 2 ust. 1, § 3 ust. 1–2
**Strona dotknięta:** Usługobiorca (pkt a, c, d, f); obie (pkt b, e).
**Opis:** (a) brak kanału i formy zgłoszenia oraz reguły dla zgłoszeń poza oknem 8:00–16:00, więc spór o początek biegu terminów jest dowodowy; (b) brak definicji „usunięcia" (obejście czy trwała naprawa); (c) czas reakcji 4 h nie ma skutku umownego, a jego naruszenie rodzi odpowiedzialność tylko na zasadach ogólnych, w granicach capu; (d) pozostałe błędy (poza Awarią Krytyczną) nie mają czasu reakcji ani usunięcia; (e) zwrot „w wymiarze do 10 godzin miesięcznie" gramatycznie może dotyczyć całego katalogu usług. Wykładnia z § 2 ust. 2 i § 3 przemawia za odniesieniem limitu wyłącznie do konsultacji (art. 65 § 2 KC [NIEZWERYFIKOWANE]), ale nie ma stawki za godziny ponad limit; (f) okno 8–16 w Dni Robocze przy działalności magazynowej oznacza do ok. 4 dni kalendarzowych przestoju bez naruszenia (rachunek wyżej). To decyzja biznesowa, nie wada prawna.
**Skutek:** spory dowodowe i interpretacyjne przy pierwszej poważnej awarii; błędy niekrytyczne bez egzekwowalnego terminu.
**Rekomendacja (preferowana):** kanał zgłoszeń, reguła „zgłoszenie po 16:00 uważa się za dokonane o 8:00 najbliższego Dnia Roboczego", definicja usunięcia (dopuszczalne obejście + trwała naprawa w oznaczonym terminie), kategoria błędów niekrytycznych z terminami, doprecyzowanie, że limit 10 h dotyczy konsultacji, i stawka ponad limit.
**Fallback (minimum akceptowalne):** kanał zgłoszeń + reguła liczenia czasu + jedno zdanie o zakresie limitu 10 h.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` — „SLA — gwarantowana dostępność systemu i czasy reakcji (maintenance IT)" (kategoryzacja Wada Krytyczna / Istotna / Kosmetyczna).

#### 3. Exit bez terminu, formatu i wsparcia przejściowego — § 7 ust. 3
**Strona dotknięta:** Usługobiorca.
**Opis:** Obowiązek zwrotu dokumentacji i danych oraz usunięcia kopii jest dobrze pomyślany (z wyjątkiem retencji ustawowej i obowiązkiem wskazania podstawy). Brakuje terminu, formatu zwrotu, pisemnego potwierdzenia usunięcia i wsparcia przy przekazaniu Systemu następcy. Usługobiorca nie ma też obowiązku zwrotu informacji poufnych Usługodawcy (drobne). Brak klauzuli rozwiązania natychmiastowego nie jest luką, bo wypowiedzenie z ważnych powodów zostaje z mocy ustawy (art. 746 § 3 w zw. z art. 750 KC [NIEZWERYFIKOWANE]).
**Skutek:** „Po zakończeniu Umowy" bez daty daje Usługodawcy swobodę co do terminu, a Usługobiorcy ryzyko opóźnionej migracji.
**Rekomendacja (preferowana):** termin (np. 14 dni), format umożliwiający dalsze utrzymanie przez osobę trzecią, pisemne potwierdzenie usunięcia, wsparcie przejściowe w limicie godzin.
**Fallback (minimum akceptowalne):** termin + format + potwierdzenie usunięcia.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md` — „Kompleksowy exit plan (maintenance IT / SaaS)" w wersji okrojonej (pełna wersja jest za ciężka na tę skalę umowy); `references/baza-klauzul/18-zwrot-materialow.md`.

#### 4. RODO — brak postanowień, kwalifikacja zależna od faktów — cała umowa (warunkowo)
**Strona dotknięta:** obie.
**Opis:** Umowa nie reguluje danych osobowych. Z treści nie wynika, czy System zawiera dane osobowe ani czy Usługodawca ma do nich dostęp, choć § 7 ust. 3 zakłada, że Usługodawca posiada „dane" Usługobiorcy i ich kopie. Ocena poziomu wymaga faktu spoza umowy.
**Skutek:** jeżeli Usługodawca przetwarza dane osobowe w imieniu Usługobiorcy, potrzebna jest umowa z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE]. Jej brak to naruszenie po obu stronach (art. 83 ust. 4 lit. a RODO [NIEZWERYFIKOWANE]) i wtedy poziom tej flagi rośnie do 🟠, a werdykt do 🟨.
**Rekomendacja (preferowana):** potwierdzić fakt; jeżeli dane osobowe są w Systemie — umowa powierzenia jako załącznik, zawarta przed udostępnieniem Systemu.
**Fallback (minimum akceptowalne):** klauzula odsyłająca do umowy powierzenia z obowiązkiem jej zawarcia przed rozpoczęciem świadczenia.
**Klauzula z bazy:** `references/baza-klauzul/14-rodo.md` (klauzula wzorcowa); siatka: `references/checklist-dpa-art28.md`.

#### 5. Niekompletna komparycja — oznaczenie stron
**Strona dotknięta:** obie.
**Opis:** brak KRS, NIP, adresów, osób reprezentujących i podstawy umocowania oraz bloku podpisów (Złota Reguła 8). W tekście są oznaczenia „(dane fikcyjne)", więc to brak wzorca, nie umowy docelowej.
**Skutek:** ryzyko podpisu przez osobę nieumocowaną (art. 103 KC [NIEZWERYFIKOWANE]) i sporu o identyfikację strony.
**Rekomendacja (preferowana):** uzupełnić z odpisu KRS aktualnego na dzień podpisu.
**Fallback (minimum akceptowalne):** — (wymóg formalny, nie przedmiot negocjacji).
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`.

#### 6. Definicje i Załącznik nr 1 — § 1
**Strona dotknięta:** obie (zakres świadczenia).
**Opis:** „Umowa" i „Strona/Strony" pisane wielką literą bez definicji (Złota Reguła 1; znaczenie oczywiste). Ważniejsze: System to „oprogramowanie magazynowe Usługobiorcy opisane w Załączniku nr 1". Załącznik nie został dostarczony, więc zakres Usług i Awarii Krytycznej opiera się na dokumencie, którego audyt nie obejmuje. § 8 ust. 3 nie wspomina o załącznikach.
**Skutek:** spór o zakres utrzymania (moduły, interfejsy, środowiska), jeśli Załącznik okaże się niepełny lub nie zostanie podpisany.
**Rekomendacja (preferowana):** dołączyć i parafować Załącznik nr 1; dodać „(dalej: „Umowa")" i definicję Stron.
**Fallback (minimum akceptowalne):** sam Załącznik nr 1 podpisany razem z Umową.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`.

### ✓ Obszary bez zastrzeżeń

- **Tytuł prawny i przekwalifikowanie:** umowa o świadczenie usług między dwiema spółkami (art. 750 KC [NIEZWERYFIKOWANE]). Konstrukcja mieszana z § 2 ust. 2 (staranne działanie + rezultat przy Awarii Krytycznej) jest dopuszczalna i nie przekształca umowy w umowę o dzieło. Ryzyka stosunku pracy brak.
- **Poufność:** wzajemna realnie (obowiązek obu Stron), okres warstwowy (3 lata / tajemnica przedsiębiorstwa bezterminowo) zgodny z modelem KTZR, pełny katalog wyłączeń. Brak kary umownej rekompensuje wyjęcie § 6 spod capu.
- **Spory:** prawo polskie; sąd właściwy dla siedziby Usługodawcy — formalnie korzystny dla Usługodawcy, ale obie siedziby są w Gdańsku, więc bez praktycznego skutku.
- **Wypowiedzenie:** symetryczne, 3 miesiące na koniec miesiąca, rozsądne dla utrzymania systemu magazynowego (exit — 🟢 3).
- **Kary umowne (konstrukcja):** kara za świadczenie niepieniężne, z sufitem, z zastrzeżonym odszkodowaniem uzupełniającym (art. 484 § 1 KC [NIEZWERYFIKOWANE]), bez wyłączenia miarkowania. Kara należy się za dzień „zwłoki" (art. 476 KC [NIEZWERYFIKOWANE]), czyli tylko za opóźnienie zawinione. To chroni Usługodawcę przed karą za opóźnienia spowodowane przez Usługobiorcę, więc osobna klauzula siły wyższej nie jest potrzebna.
- **Wynagrodzenie i płatność:** ryczałt z VAT, 30 dni od doręczenia prawidłowej faktury. Brak waloryzacji przy czasie nieokreślonym to ryzyko inflacyjne Usługodawcy, równoważone jego prawem wypowiedzenia.
- **Spójność:** terminologia jednolita (Usługodawca / Usługobiorca), odesłania § 1 pkt 2 → § 2, § 2 ust. 2 → § 3, § 3 ust. 3 → § 5 ust. 1, § 5 ust. 1 → § 6 prowadzą do istniejących postanowień. Antywzorce językowe („niezwłocznie", „dołoży starań", „według uznania", pozorna wzajemność) — brak trafień.

### Bramka kompletności (R9)

| Obszar | Status |
|---|---|
| Odpowiedzialność i kary | 🟡 1 · 🟢 1 |
| Prawa autorskie | 🟡 2 |
| Definicje i logika | 🟢 6 · 🟢 2 (pkt e) |
| Reprezentacja | 🟢 5 |
| Wypowiedzenie i exit | 🟢 3 (wypowiedzenie ✓) |
| RODO | 🟢 4 (warunkowo) |
| Tytuł prawny i przekwalifikowanie | ✓ brak zastrzeżeń |
| Poufność | ✓ brak zastrzeżeń |
| Spory | ✓ brak zastrzeżeń |

---

## OCENA BEZPIECZEŃSTWA: 93/100

Umowa jest zrównoważona i dobrze skonstruowana: cap 1× rocznego wynagrodzenia z prawidłowymi wyłączeniami, umiarkowane kary z sufitem, symetryczne wypowiedzenie, warstwowa poufność. Odjęte punkty: 2 × 🟡 (po −2: arytmetyka limitów, prawa do poprawek) i 6 × 🟢 (po −0,5). Żadna flaga nie jest dealbreakerem. Werdykt zmienia się tylko, jeżeli Usługodawca przetwarza dane osobowe bez umowy powierzenia (🟢 4 → 🟠, werdykt → 🟨).

**Werdykt:** DO PODPISANIA z drobnymi poprawkami.

### Klauzule z bazy KTZR do uzupełnienia

🟡 RYZYKO 1 (okres odniesienia limitów, kara a cap)
→ `references/baza-klauzul/11-odpowiedzialnosc.md` — klauzula wzorcowa (cap z 12 miesięcy) + `references/baza-klauzul/10-kary-umowne.md` — klauzula wzorcowa (sufit kary)

🟡 RYZYKO 2 (prawa do poprawek)
→ `references/baza-klauzul/08-prawa-autorskie-ip.md` — „Pełne przeniesienie praw … (maintenance IT)" albo licencja jako fallback

🟢 RYZYKA 1–6
→ `11-odpowiedzialnosc.md` (wyjątek umyślności, SLA) · `12-wypowiedzenie-exit.md` + `18-zwrot-materialow.md` (exit) · `14-rodo.md` (warunkowo) · `01-oznaczenie-stron.md` · `03-definicje.md`

### Miejsca, w których w trybie standardowym nastąpiłby STOP (tryb express)

1. Dla której strony pracujemy — audyt prowadzony neutralnie; przy mandacie jednej strony rekomendacje 🟡 1 i 🟢 1 trzeba ustawić pod jej interes.
2. Fakt przetwarzania danych osobowych w Systemie — rozstrzyga poziom 🟢 4 i ewentualnie werdykt.
3. Treść Załącznika nr 1 — zakres Usług nie jest możliwy do oceny bez niego.
4. Wybór wariantu limitów (roczny czy łączny; kara w capie czy obok) — decyzja handlowa.
5. Czy generować poprawione klauzule dla 🟡 1 i 🟡 2.

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
