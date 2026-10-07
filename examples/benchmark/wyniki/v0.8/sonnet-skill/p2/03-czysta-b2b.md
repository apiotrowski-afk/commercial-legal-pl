konfiguracja: sonnet-skill
commit skilla: 06a7e59
przebieg: 2 z 3
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"

[DRAFT — DO WERYFIKACJI] (tryb express, audyt neutralny, bez MCP legal-cite — każde powołanie przepisu oznaczone [NIEZWERYFIKOWANE])

## AUDYT RYZYK — Umowa o świadczenie usług utrzymania (ORION SYSTEMS sp. z o.o. / FERRUM LOGISTICS sp. z o.o.)

> **WERDYKT: 🟨 ŻÓŁTY** — do negocjacji: brak dealbreakerów i brak nieważności, ale sześć ryzyk średnich (głównie po stronie Usługobiorcy: ochrona odszkodowawcza i SLA słabsze, niż sugeruje brzmienie) wymaga poprawek przed podpisem.

### Bramka ius cogens (R10)

- Wyłączenie winy umyślnej: § 5 ust. 1 zawiera wyjątek („Ograniczenie nie dotyczy szkody wyrządzonej umyślnie ani naruszenia § 6.") — zgodne z art. 473 § 2 KC [NIEZWERYFIKOWANE]. Wyjątek: zob. flaga 🟡 nr 1 (§ 5 ust. 2 stoi poza tym wyjątkiem).
- Kara umowna (§ 3 ust. 3) zabezpiecza zobowiązanie niepieniężne (usunięcie awarii) — art. 483 § 1 KC [NIEZWERYFIKOWANE]: bez zastrzeżeń. Miarkowanie nie jest wyłączone — art. 484 § 2 KC [NIEZWERYFIKOWANE]: bez zastrzeżeń. Odszkodowanie uzupełniające zastrzeżone wyraźnie — art. 484 § 1 KC [NIEZWERYFIKOWANE]: bez zastrzeżeń.
- Termin zapłaty 30 dni (§ 4 ust. 2) — poniżej granicy 60 dni z ustawy o terminach zapłaty w transakcjach handlowych [NIEZWERYFIKOWANE]: bez zastrzeżeń.
- Prawa osobiste / pola eksploatacji: umowa nie dotyka przeniesienia praw — zob. flaga 🟡 nr 5 (luka, nie naruszenie).
- Trigger art. 385(5) KC [NIEZWERYFIKOWANE]: nieaktywny — obie strony to spółki z o.o., nie osoby fizyczne.
- Trafień w katalog ius cogens: 0.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy (rocznie) | 8.000 zł netto / mies. | 8.000 × 12 | 96.000 zł netto / rok (umowa na czas nieokreślony — wartość całkowita [BRAK DANYCH]) |
| Cap nominalny | 12-miesięczne wynagrodzenie netto (§ 5 ust. 1) | 8.000 × 12 | 96.000 zł = 1,0× wartości rocznej |
| Kara dzienna | 1.000 zł / rozpoczęty Dzień Roboczy zwłoki (§ 3 ust. 3) | 1.000 / 8.000 | 12,5% wynagrodzenia miesięcznego za każdy dzień |
| Sufit kar | 20% wynagrodzenia rocznego netto | 0,20 × 96.000 | 19.200 zł |
| Dni do wyczerpania sufitu | — | 19.200 / 1.000 = 19,2 → 20. rozpoczęty Dzień Roboczy (19 × 1.000 = 19.000; w 20. dniu tylko 200 zł do sufitu) | 20 Dni Roboczych zwłoki = ok. 4 tygodnie kalendarzowe; łącznie z 2 DR na usunięcie ok. 22 DR |
| Kary poza capem? | „Łączna odpowiedzialność ... z Umowy" (§ 5 ust. 1) | wariant A: kary w capie; wariant B: kary obok capu | A: 96.000 zł; B: 96.000 + 19.200 = 115.200 zł (1,2× wartości rocznej). Umowa nie rozstrzyga wprost — dyferencja 19.200 zł |
| Odszkodowanie uzupełniające | do limitu z § 5 ust. 1 | — | w granicach capu; bez utraconych korzyści (§ 5 ust. 2) |
| Wyłączenia z capu | szkoda umyślna; naruszenie § 6 | — | ekspozycja nieograniczona kwotowo (obie strony wzajemnie w zakresie § 6; szkoda umyślna po stronie Usługodawcy) |
| Efektywna ekspozycja Usługodawcy | — | cap + ewentualnie kary poza capem + wyłączenia | 96.000–115.200 zł = 1,0–1,2× wartości rocznej, plus pozycje nieograniczone (umyślność, poufność) |
| Cap vs kara maksymalna | — | 96.000 / 19.200 | 5,0× — sufit kary stanowi 1/5 capu; kara jest tylko ryczałtem na „dolnym" poziomie szkody |
| Asymetria (Usługodawca vs Usługobiorca) | cap, kary i sufit tylko dla Usługodawcy; Usługobiorca ma obowiązek zapłaty (pieniężny, bez kar umownych) i poufności | — | kary: 19.200 zł vs 0 zł; cap: 96.000 zł vs [BRAK DANYCH] (brak capu dla Usługobiorcy; jego ekspozycja ograniczona faktycznie do długu 8.000 zł / mies. i § 6) |
| Wypowiedzenie | 3 mies. ze skutkiem na koniec miesiąca (§ 7 ust. 2) | przykład: wypowiedzenie doręczone 15.01.2027 → 3 mies. upływają 15.04.2027 → skutek 30.04.2027 | okres realny 3–4 mies. = 24.000–32.000 zł wynagrodzenia do zapłaty w okresie wypowiedzenia; symetryczny |
| Termin płatności | 30 dni od doręczenia faktury | — | 30 dni (≤ 60, bez zastrzeżeń) |
| Konsultacje w ryczałcie | do 10 godz. mies. (§ 2 ust. 1) | 8.000 / 10 | 800 zł / godz. jako górna efektywna stawka za konsultacje, jeżeli ryczałt miałby pokrywać wyłącznie konsultacje; limit godzin dla usuwania błędów i poprawek [BRAK DANYCH] |
| Przykład SLA — awaria w piątek 15:00 | reakcja 4 h w DR 8:00–16:00; usunięcie 2 DR od zgłoszenia | 1 h w piątek + 3 h w poniedziałek (do 11:00); usunięcie do końca wtorku (przy liczeniu od następnego DR) | ok. 4 doby kalendarzowe bez zwłoki w rozumieniu umowy (piątek 15:00 → wtorek); kary dopiero od środy |

Wniosek z rachunku: cap 1,0× wartości rocznej jest rynkowy i nominalnie nieiluzoryczny; sufit kar (19.200 zł) jest niski wobec capu (5×) i wobec potencjalnej szkody z przestoju magazynu, a sama szkoda z przestoju to w przeważającej części utracone korzyści — wyłączone przez § 5 ust. 2. Rachunek nie daje podstaw do 🟠/🔴, ale uzasadnia flagę 🟡 nr 1 i nr 2.

### 🔴 RYZYKA KRYTYCZNE

Brak.

### 🟠 RYZYKA WYSOKIE

Brak.

### 🟡 RYZYKA ŚREDNIE

#### 1. Wyłączenie utraconych korzyści + efekt kumulatywny z SLA i capem — § 5 ust. 2 (w zw. z § 3, § 5 ust. 1)
**Strona dotknięta:** Usługobiorca (korzysta Usługodawca).
**Opis:** „Usługodawca nie odpowiada za utracone korzyści Usługobiorcy." Wyłączenie jest samo w sobie dopuszczalne w B2B, ale (a) stoi poza wyjątkiem z § 5 ust. 1 (który odnosi się do „ograniczenia", nie do wyłączenia) — brzmienie pozwala czytać ust. 2 jako obejmujące także szkodę umyślną, co w tym zakresie jest nieważne (art. 473 § 2 KC [NIEZWERYFIKOWANE], art. 58 § 3 KC [NIEZWERYFIKOWANE]); (b) w systemie magazynowym główna szkoda z awarii przyjęć/wydań to właśnie utracone korzyści i koszty przestoju, więc „odszkodowanie uzupełniające ... w przypadku gdy szkoda przewyższa karę" (§ 3 ust. 3) jest w praktyce wąskie. Test pięciopunktowy, krok 5 (efekt kumulatywny): SLA tylko w DR 8:00–16:00 (§ 3 ust. 1–2) + kara dzienna z sufitem 19.200 zł + wyłączenie lucrum cessans + cap 96.000 zł razem dają ochronę wyraźnie mniejszą, niż sugeruje każda klauzula osobno — nie do poziomu nieważności (spółki kapitałowe, praktyka rynkowa, brak trigger art. 385(5) KC [NIEZWERYFIKOWANE]), ale istotnie.
**Skutek:** szkoda z przestoju magazynu w praktyce odzyskiwalna głównie w postaci kary (max 19.200 zł) i szkody rzeczywistej do capu.
**Rekomendacja (preferowana):** dopisać do § 5 ust. 2 „z wyjątkiem szkody wyrządzonej umyślnie"; rozważyć wyłączenie z ust. 2 kosztów przestoju i kar umownych zapłaconych klientom Usługobiorcy wskutek Awarii Krytycznej (jako szkoda rzeczywista) albo odrębny podlimit.
**Fallback (minimum akceptowalne):** sam wyjątek dla winy umyślnej + jednoznaczne wskazanie, że koszty przestoju i kary zapłacone osobom trzecim mieszczą się w szkodzie rzeczywistej.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Luka w SLA: okno 8:00–16:00 w DR, brak kary za reakcję, brak terminów dla innych błędów, brak trybu zgłoszenia — § 1 ust. 4, § 2 ust. 1, § 3 ust. 1–3
**Strona dotknięta:** Usługobiorca (częściowo Usługodawca — spór o moment zgłoszenia).
**Opis:** (a) Czas reakcji i usunięcia liczony wyłącznie w Dni Robocze „w godzinach 8:00–16:00" — przy magazynie pracującym poza tymi godzinami (czy tak jest: [BRAK DANYCH]) awaria w piątek po południu daje ok. 4 doby kalendarzowe bez zwłoki (rachunek wyżej); (b) kara dotyczy wyłącznie zwłoki w usunięciu — przekroczenie 4-godzinnego czasu reakcji nie ma sankcji; (c) „Awaria Krytyczna" to wyłącznie błąd w „zakresie przyjęć lub wydań magazynowych" — „inne błędy" (§ 2 ust. 1) nie mają żadnego terminu; (d) umowa nie wskazuje kanału zgłoszenia ani dowodu momentu zgłoszenia, a „od zgłoszenia" jest punktem startu obu terminów i kar.
**Skutek:** spór o to, kiedy biegnie zwłoka; brak narzędzia nacisku na reakcję; poważny błąd poza definicją Awarii Krytycznej (np. rozjazd stanów magazynowych) bez terminu usunięcia.
**Rekomendacja (preferowana):** zdefiniować kanał zgłoszeń (adres e-mail / system zgłoszeń, moment doręczenia); dodać poziom „Awaria Istotna" z terminami; rozważyć wsparcie poza DR dla Awarii Krytycznej (dopłata ryczałtowa); kara lub kredyt za przekroczenie reakcji.
**Fallback (minimum akceptowalne):** kanał zgłoszeń i moment doręczenia + wskazanie, że godziny pracy magazynu (jeśli inne) uwzględniono w SLA albo jawne potwierdzenie, że poza oknem nie ma wsparcia.
**Klauzula z bazy:** `references/baza-klauzul/` (kategoria SLA / parametry usługi — wg INDEX.md)

#### 3. Załącznik nr 1 wskazany, ale niedołączony; przedmiot (System) nieoznaczony — § 1 ust. 1
**Strona dotknięta:** obie strony.
**Opis:** „System" definiowany przez odesłanie do Załącznika nr 1 („opisane w Załączniku nr 1"); w dostarczonym tekście załącznika brak. Zakres Systemu determinuje zakres Usług, definicję Awarii Krytycznej, SLA i odpowiedzialność (Złota Reguła 4 — osierocony załącznik).
**Skutek:** bez załącznika nieoznaczony przedmiot świadczenia; spór o to, czy dany moduł / integracja / środowisko należy do Systemu.
**Rekomendacja (preferowana):** dołączyć załącznik z wersją, modułami, środowiskami, integracjami i wyłączeniami; podpisany razem z umową.
**Fallback (minimum akceptowalne):** jednozdaniowy opis Systemu w treści umowy (nazwa, wersja, środowisko produkcyjne) do czasu uzupełnienia załącznika.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

#### 4. Brak umowy powierzenia danych osobowych (lub oświadczenia o braku dostępu do danych) — cała umowa, § 7 ust. 3
**Strona dotknięta:** obie (Usługobiorca jako administrator; Usługodawca jako ewentualny podmiot przetwarzający).
**Opis:** utrzymanie oprogramowania magazynowego z reguły oznacza dostęp (nawet incydentalny) do baz zawierających dane osobowe pracowników, kierowców i kontrahentów. Umowa nie zawiera powierzenia ani zastrzeżenia, że dostępu do danych osobowych nie będzie. Jeżeli dostęp faktycznie występuje, brak instrumentu z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE] to naruszenie po stronie obu podmiotów (sankcja z art. 83 ust. 4 RODO [NIEZWERYFIKOWANE]). Z samej umowy nie wynika, czy dane osobowe są przetwarzane — [BRAK DANYCH]; stąd poziom 🟡 z możliwością eskalacji do 🟠 po potwierdzeniu dostępu.
**Skutek:** ryzyko administracyjne i odszkodowawcze; brak ustalonych zasad bezpieczeństwa, subprocesorów i zgłaszania naruszeń.
**Rekomendacja (preferowana):** umowa powierzenia jako załącznik albo odrębne porozumienie; w § 7 ust. 3 odesłanie do niej.
**Fallback (minimum akceptowalne):** oświadczenie, że Usługodawca nie przetwarza danych osobowych Usługobiorcy, oraz zakaz dostępu do danych produkcyjnych bez odrębnego porozumienia.
**Klauzula z bazy:** `references/baza-klauzul/` (RODO / powierzenie) oraz `references/checklist-dpa-art28.md`

#### 5. Brak regulacji praw do poprawek i modyfikacji tworzonych w ramach utrzymania — § 2 ust. 1
**Strona dotknięta:** Usługobiorca.
**Opis:** Usługodawca „instaluje poprawki" i usuwa błędy, a więc tworzy kod będący opracowaniem Systemu. Umowa nie przenosi praw do poprawek ani nie udziela licencji z wymienionymi polami eksploatacji (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]; art. 2 ust. 2 PrAut [NIEZWERYFIKOWANE]), nie reguluje kodu źródłowego ani dokumentacji powstałej w trakcie. Wzmianka o zwrocie „dokumentacji i danych" w § 7 ust. 3 nie rozwiązuje kwestii praw. Nie jest to naruszenie ius cogens, tylko luka.
**Skutek:** po zakończeniu umowy Usługobiorca może nie mieć jednoznacznego prawa do dalszego korzystania z poprawek, ani do ich modyfikacji przez innego wykonawcę.
**Rekomendacja (preferowana):** przeniesienie praw majątkowych do poprawek na Usługobiorcę z wyliczeniem pól eksploatacji (forma pisemna) albo licencja bezterminowa; zwolnienie z praw osobistych w dopuszczalnym zakresie.
**Fallback (minimum akceptowalne):** licencja niewyłączna, nieodwołalna, bezterminowa na poprawki z wyliczonymi polami eksploatacji + zakaz wyłączania poprawek po zakończeniu umowy.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 6. Brak obowiązków współdziałania Usługobiorcy i wyłączeń z SLA; brak limitu godzin dla błędów — § 2 ust. 1, § 3
**Strona dotknięta:** Usługodawca.
**Opis:** kara za każdy rozpoczęty DR zwłoki działa bez wyłączeń: umowa nie przewiduje obowiązku zapewnienia dostępu zdalnego/środowiska, informacji o zmianach infrastruktury, ani wyłączenia zwłoki z przyczyn po stronie Usługobiorcy, osób trzecich (np. dostawca infrastruktury) lub siły wyższej; odpowiedzialność za zwłokę wynika wtedy wyłącznie z ogólnych zasad (art. 476 KC [NIEZWERYFIKOWANE]; art. 483 § 1 KC [NIEZWERYFIKOWANE]) i jej zakres jest sporny. Limit „do 10 godzin miesięcznie" dotyczy konsultacji; usuwanie błędów i poprawki są w ryczałcie bez limitu — przy 8.000 zł miesięcznie ryzyko nadmiernego obciążenia po stronie Usługodawcy.
**Skutek:** spór o zwłokę; ekspozycja Usługodawcy do 19.200 zł kar za zdarzenia poza jego kontrolą.
**Rekomendacja (preferowana):** klauzula o współdziałaniu (dostępy, osoba kontaktowa, informacja o zmianach) + katalog wyłączeń z SLA (przyczyny po stronie Usługobiorcy, osób trzecich, siła wyższa) + zasady rozliczania pracy ponad ryczałt.
**Fallback (minimum akceptowalne):** zdanie, że termin SLA ulega zawieszeniu na czas braku współdziałania Usługobiorcy.
**Klauzula z bazy:** `references/baza-klauzul/` (SLA / obowiązki stron — wg INDEX.md)

### 🟢 RYZYKA NISKIE

#### 7. Brak terminu zwrotu i usunięcia danych po zakończeniu umowy — § 7 ust. 3
**Strona dotknięta:** Usługobiorca.
**Opis:** „Po zakończeniu Umowy Usługodawca zwróci ... dokumentację i dane" — bez terminu (antywzorzec: termin nieoznaczony), bez formatu i potwierdzenia usunięcia. Samo zastrzeżenie dotyczące kopii wymaganych przepisami jest wyważone (obowiązek poinformowania z podaniem podstawy i okresu).
**Rekomendacja:** termin (np. 14 dni), format, pisemne potwierdzenie usunięcia.

#### 8. Dane stron i definicje formalne — preambuła, § 1
**Strona dotknięta:** obie strony.
**Opis:** brak KRS/NIP, adresów i wskazania reprezentacji (Złota Reguła 8) — w dostarczonym tekście adnotacja „dane fikcyjne", więc to uwaga formalna; „Umowa" i „Strony" pisane wielką literą bez definicji (Złota Reguła 1, drobna).
**Rekomendacja:** uzupełnić dane i umocowanie; dopisać definicje lub „(dalej: „Umowa")".

#### 9. Niejednoznaczne, czy kary wliczają się w cap — § 3 ust. 3 w zw. z § 5 ust. 1
**Strona dotknięta:** obie (Usługodawca vs Usługobiorca — różnica 19.200 zł).
**Opis:** „Łączna odpowiedzialność ... z Umowy" sugeruje wliczenie kar, ale wprost tego nie mówi; spór o 96.000 zł vs 115.200 zł. Odesłanie z § 3 ust. 3 do „limitu z § 5 ust. 1" dotyczy tylko odszkodowania uzupełniającego.
**Rekomendacja:** dopisać „łącznie z karami umownymi" albo wprost „obok".

#### 10. Brak waloryzacji ryczałtu i wypowiedzenia z ważnych przyczyn — § 4 ust. 1, § 7 ust. 2
**Strona dotknięta:** Usługodawca (waloryzacja); Usługobiorca (brak szybkiej drogi wyjścia).
**Opis:** ryczałt 8.000 zł stały przy umowie na czas nieokreślony; zmiana ceny tylko przez aneks (§ 8 ust. 1) lub wypowiedzenie 3–4 mies. Brak wypowiedzenia natychmiastowego z ważnych przyczyn (np. powtarzające się Awarie Krytyczne) — Usługobiorca trwa w umowie 24.000–32.000 zł. Układ rynkowy i symetryczny; wskazuję do świadomej decyzji, nie jako wadę.
**Rekomendacja:** waloryzacja o wskaźnik (np. CPI raz w roku) lub prawo wypowiedzenia z ważnych przyczyn.

### ✓ Obszary bez zastrzeżeń (R9)

- **Odpowiedzialność i kary** — poza flagami 1, 2, 6, 9: cap 12 mies. rynkowy, wyjątek dla winy umyślnej i § 6 zgodny z ius cogens, sufit kar 20% jest wprost określony, miarkowanie nie wyłączone, kara za zobowiązanie niepieniężne.
- **Prawa autorskie** — poza flagą 5 (luka co do poprawek) — brak klauzul sprzecznych z prawem.
- **Definicje i logika** — odesłania wewnętrzne (§ 2 ust. 2 → § 3; § 3 ust. 3 → § 5 ust. 1; § 5 ust. 1 → § 6; § 1 ust. 2 → § 2) prowadzą do istniejących przepisów; Dzień Roboczy i Awaria Krytyczna zdefiniowane; poza flagami 3 i 8.
- **Reprezentacja** — poza flagą 8.
- **Wypowiedzenie i exit** — okres 3 mies. symetryczny, procedura zwrotu danych jest (flagi 7 i 10 to dopracowania).
- **RODO** — poza flagą 4.
- **Tytuł prawny i przekwalifikowanie** — § 2 ust. 2 jasno rozdziela staranne działanie (usługi) i rezultat (usunięcie Awarii Krytycznej w terminie); konstrukcja usług o charakterze zlecenia (art. 750 KC [NIEZWERYFIKOWANE]) spójna; brak ryzyka przekwalifikowania.
- **Poufność** — okres umowy + 3 lata, tajemnica bezterminowo, typowe wyłączenia (informacje publiczne, od osób trzecich, niezależnie opracowane, ujawnienie wymagane prawem); wzajemna — w porządku.
- **Spory** — prawo polskie, sąd powszechny dla siedziby Usługodawcy; obie strony mają siedzibę w Gdańsku, więc w praktyce brak asymetrii. Płatność 30 dni — w porządku.

---

## OCENA BEZPIECZEŃSTWA: 80/100

Zero nieważności i zero ryzyk krytycznych/wysokich; punkty tracą głównie luki: ochrona odszkodowawcza i SLA Usługobiorcy słabsze, niż sugeruje brzmienie (flagi 1, 2), brak załącznika, brak regulacji powierzenia danych i praw do poprawek. Umowa jest wyważona i rynkowa; poprawki są konkretne i niedrogie.

**Werdykt:** DO NEGOCJACJI (🟨 ŻÓŁTY) — flagi: 🔴 0 · 🟠 0 · 🟡 6 · 🟢 4 (łącznie 10).

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*

[DRAFT — DO WERYFIKACJI]
