## AUDYT RYZYK — Umowa ramowa T&M (Quanta Dev / Meridian Finance)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; cap odpowiedzialności jest iluzoryczny (kary i indemnity umownie wyłączone spod niego), umowa nie zawiera żadnej klauzuli praw autorskich ani poufności mimo 24-miesięcznej współpracy przy oprogramowaniu podmiotu finansowego.

*Audyt neutralny — wady oznaczone niezależnie od tego, którą stronę faktycznie krzywdzą; przy każdej wskazano stronę dotkniętą. Konstrukcja kar i wyłączeń w tej umowie jest wyraźnie jednostronna na korzyść Zamawiającego (Meridian Finance) — odnotowano to konsekwentnie.*

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | T&M, brak stałej kwoty; § 1 ust. 2: stawka 220 zł/h, szacunkowo 2 Specjalistów × 160 h/mies. | 220 × 320 h/mies. = 70.400 zł/mies. (szacunek, nie kwota kontraktowa) × 24 mies. | **≈ 1.689.600 zł** (szacunek orientacyjny, T&M nie gwarantuje tej kwoty) |
| Cap nominalny odpowiedzialności (§ 3 ust. 1) | 12-miesięczne wynagrodzenie | 12 × 70.400 (szacunek) | **≈ 844.800 zł** (szacunek) — **ale patrz niżej: cap iluzoryczny** |
| Kary poza capem (§ 2 ust. 4) | „Kary umowne podlegają sumowaniu i nie są wliczane do limitu odpowiedzialności z § 3" | (a) 0,5% × 70.400 = 352 zł/dzień zwłoki w Przyroście, **brak sufitu liczby dni**; (b) 5.000 zł/naruszenie jakości kodu, **brak sufitu liczby naruszeń**; (c) 300.000 zł/naruszenie zakazu konkurencji, **brak sufitu liczby naruszeń** | każda z trzech kar sumuje się i pozostaje **poza** capem 844.800 zł — np. już dwa naruszenia zakazu konkurencji (600.000 zł) + kilka naruszeń jakości kodu przewyższają cap nominalny |
| Indemnity IP bez limitu (§ 3 ust. 2) | „zwolni Zamawiającego z wszelkiej odpowiedzialności... i pokryje wszelkie związane z tym koszty" | brak wskazanej kwoty granicznej | **nieograniczona** — dodatkowa pozycja poza capem z § 3 ust. 1 |
| Odszkodowanie uzupełniające ponad kary (§ 2 ust. 4 zd. 2) | „Zamawiający może dochodzić odszkodowania przewyższającego kary umowne na zasadach ogólnych" | brak limitu | **nieograniczone** (art. 484 § 1 KC [NIEZWERYFIKOWANE] dopuszcza odszkodowanie uzupełniające, ale tu brak jakiegokolwiek sufitu łącznego) |
| Efektywna ekspozycja Wykonawcy | — | cap nominalny (844.800 zł, szacunek) + kary poza capem (potencjalnie setki tysięcy do ponad miliona zł w scenariuszu kumulacji) + indemnity bez limitu + odszkodowanie uzupełniające bez limitu | **EKSPOZYCJA NIEOGRANICZONA — cap z § 3 ust. 1 jest iluzoryczny**, bo wszystko istotne jest z niego umownie wyłączone |
| Asymetria (Wykonawca vs Zamawiający) | wszystkie kary i indemnity — wyłącznie po stronie Wykonawcy; brak jakiejkolwiek kary dla Zamawiającego | stosunek kar A/B = ∞ | 100% ryzyka finansowego z tytułu kar i indemnity po stronie Wykonawcy (Quanta Dev) |
| Daty graniczne | auto-renewal: brak sprzeciwu na 90 dni przed końcem 24-miesięcznego (a potem 12-miesięcznych) okresów (§ 4 ust. 1); brak wskazanej daty zawarcia/rozpoczęcia | okno 90-dniowe opisane, ale brak daty startowej w tekście uniemożliwia policzenie konkretnej daty granicznej | mechanizm auto-renewal jasny; **konkretna data ostatniego dnia na sprzeciw: [BRAK DANYCH]** (brak daty zawarcia w tekście) |

**Wniosek z rachunku:** § 2 ust. 4 wprost wyjmuje kary i pozwala na nieograniczone odszkodowanie uzupełniające **poza** capem z § 3 ust. 1, a § 3 ust. 2 dokłada nieograniczoną indemnifikację IP. W efekcie deklarowany cap „12-miesięczne wynagrodzenie" nic nie ogranicza w praktyce — to klasyczny przypadek capu iluzorycznego z R12: ładna liczba w jednym paragrafie, zerowa ochrona w rachunku całościowym. To samodzielnie kalibruje werdykt na 🟥, niezależnie od pozostałych braków.

### Bramka ius cogens (R10)

Kary umowne (§ 2 ust. 1–3) dotyczą zobowiązań niepieniężnych (dostawa Przyrostu, jakość kodu, zakaz konkurencji) — art. 483 § 1 KC [NIEZWERYFIKOWANE] nie jest naruszony wprost. Brak wyłączenia miarkowania kary z góry, brak skracania terminów przedawnienia, brak wyłączenia winy umyślnej. Trigger mikroprzedsiębiorcy — nie dotyczy (obie strony to spółki kapitałowe).

**Test pięciopunktowy — zakaz konkurencji bez ekwiwalentu (§ 5 ust. 1) w połączeniu z karą 300.000 zł (§ 2 ust. 3) i brakiem sufitu kar (§ 2 ust. 4).**
1. **Treść obiektywna:** zakaz świadczenia usług dla podmiotów konkurencyjnych przez cały okres Umowy (do 24 mies. + kolejne okresy przedłużenia) **oraz 24 miesiące po jej zakończeniu**, bez jakiegokolwiek wynagrodzenia za ten okres („Zakaz nie jest związany z dodatkowym wynagrodzeniem").
2. **Sposób wprowadzenia:** brak wskazania negocjacji — umowa ramowa T&M typowo ma charakter wzorca proponowanego przez Zamawiającego.
3. **Asymetria:** dotyczy wyłącznie Wykonawcy; brak jakiegokolwiek ograniczenia analogicznego dla Zamawiającego.
4. **Praktyka rynkowa:** zakaz konkurencji bez ekwiwalentu po zakończeniu współpracy, o długości równej okresowi samej umowy (24 miesiące), odbiega od standardu rynkowego dla umów B2B tego typu — zwykle wymaga ekwiwalentu lub jest istotnie krótszy.
5. **Efekt kumulatywny:** zakaz bez ekwiwalentu + kara 300.000 zł za naruszenie (bez sufitu liczby przypadków) + brak wliczenia tej kary do capu (§ 2 ust. 4) + nieograniczona indemnity (§ 3 ust. 2) razem tworzą sytuację, w której Wykonawca ponosi praktycznie nieograniczone ryzyko finansowe za świadczenie usług bez żadnej rekompensaty za samo ograniczenie swobody działalności gospodarczej po zakończeniu współpracy.

**Wniosek testu:** kombinacja tych elementów uzasadnia poważne wątpliwości co do zgodności z art. 3531 KC [NIEZWERYFIKOWANE] (granice swobody umów) i ryzyko oceny jako sprzeczne z zasadami współżycia społecznego (art. 58 § 2 KC [NIEZWERYFIKOWANE]) w części dotyczącej braku ekwiwalentu i braku sufitu kary — flagowane jako 🔴 z uwagi na efekt kumulatywny, nie jako pojedyncza, oczywista nieważność.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Cap odpowiedzialności iluzoryczny — § 2 ust. 4, § 3 ust. 1–2
**Opis:** patrz rachunek ekspozycji. Dotyczy Wykonawcy (Quanta Dev) — deklarowany cap 12-miesięcznego wynagrodzenia nie chroni go w praktyce, bo kary i indemnity IP są wyraźnie wyłączone spod limitu.
**Skutek:** ekspozycja finansowa Wykonawcy nieograniczona mimo istnienia klauzuli capu.
**Rekomendacja (preferowana):** wliczyć kary umowne i indemnity IP do jednego, łącznego capu odpowiedzialności; usunąć zdanie o odszkodowaniu uzupełniającym bez limitu lub ograniczyć je do wysokości capu.
**Fallback (minimum akceptowalne):** odrębny, ale skończony sub-limit dla kar (np. 20% wartości rocznej) i odrębny, skończony sub-limit dla indemnity IP.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Zakaz konkurencji bez ekwiwalentu, 24 miesiące, kara 300.000 zł bez sufitu liczby naruszeń — § 5 ust. 1, § 2 ust. 3
**Opis:** patrz test pięciopunktowy wyżej. Dotyczy Wykonawcy (Quanta Dev).
**Skutek:** ryzyko uznania klauzuli (lub jej części — brak ekwiwalentu i/lub brak sufitu kary) za sprzeczną z zasadami współżycia społecznego; niezależnie od wyniku sporu — realne ryzyko finansowe do czasu rozstrzygnięcia.
**Rekomendacja (preferowana):** wprowadzić ekwiwalent za okres zakazu po zakończeniu Umowy (np. miesięczne wynagrodzenie w wysokości % ostatniego wynagrodzenia), skrócić okres do 6–12 miesięcy, wprowadzić łączny sufit kary.
**Fallback (minimum akceptowalne):** minimum — sufit łącznej kary za naruszenia zakazu konkurencji (np. nie więcej niż 300.000 zł łącznie, nie „za każdy przypadek").
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 3. Brak jakiejkolwiek klauzuli praw autorskich — brak w tekście
**Opis:** Umowa dotyczy „rozwoju oprogramowania" (§ 1 ust. 1) przez 24 miesiące (z możliwym przedłużeniem), ale **nie zawiera żadnej klauzuli przeniesienia praw autorskich** ani licencji do wytworzonego kodu. Dotyczy Zamawiającego (Meridian Finance).
**Skutek:** bez wyraźnego przeniesienia praw (z polami eksploatacji — art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]) prawa do oprogramowania mogą pozostać przy Wykonawcy/twórcach (osobach fizycznych zatrudnionych/współpracujących z Wykonawcą) — Zamawiający może płacić przez 24+ miesięcy, nie nabywając praw do rezultatu prac.
**Rekomendacja (preferowana):** dodać klauzulę przeniesienia autorskich praw majątkowych z chwilą wytworzenia/zapłaty, z wyraźnym wskazaniem pól eksploatacji, oraz gwarancję czystości IP (brak GPL/AGPL) i licencję na komponenty open source.
**Fallback (minimum akceptowalne):** minimalny katalog pól adekwatny do przyszłego wykorzystania kodu przez Zamawiającego.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 4. Brak jakiejkolwiek klauzuli poufności — brak w tekście
**Opis:** Umowa 24-miesięczna (z możliwym przedłużeniem) dotycząca rozwoju oprogramowania dla instytucji finansowej (Meridian Finance S.A.) **nie zawiera żadnej klauzuli poufności**. Dotyczy Zamawiającego (Meridian Finance) — brak ochrony informacji poufnych, danych systemowych, architektury, danych biznesowych ujawnianych Wykonawcy w toku 24-miesięcznej współpracy.
**Skutek:** brak podstawy do dochodzenia roszczeń w razie ujawnienia informacji poufnych Zamawiającego przez Wykonawcę lub jego Specjalistów.
**Rekomendacja (preferowana):** dodać pełną klauzulę poufności — zakres, okres (min. 3–5 lat po zakończeniu, bezterminowo dla tajemnicy przedsiębiorstwa), wyłączenia, kara umowna za naruszenie.
**Fallback (minimum akceptowalne):** minimalna klauzula poufności z okresem 2 lata po zakończeniu.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Brak klauzuli RODO mimo prawdopodobnego dostępu do danych instytucji finansowej — brak w tekście
**Opis:** Zamawiający to instytucja finansowa (Meridian Finance S.A.) — rozwój oprogramowania typowo wymaga dostępu Wykonawcy do danych/systemów, które mogą obejmować dane osobowe klientów lub pracowników. Umowa nie zawiera żadnej klauzuli RODO. Dotyczy obu stron.
**Skutek:** ryzyko naruszenia RODO przy faktycznym dostępie do danych bez podstawy prawnej działania (art. 28 RODO [NIEZWERYFIKOWANE]).
**Rekomendacja (preferowana):** dodać umowę powierzenia (DPA) zgodną z art. 28 RODO, adekwatną do zakresu faktycznego dostępu Specjalistów do danych/systemów Zamawiającego.
**Fallback (minimum akceptowalne):** oświadczenie, że Wykonawca nie ma dostępu do danych osobowych (jeśli to prawda) — w przeciwnym razie DPA obowiązkowe.
**Klauzula z bazy:** `references/checklist-dpa-art28.md`

#### 2. Ryzyko przekwalifikowania — brak klauzuli autonomii Specjalistów, brak wyłączenia art. 22 § 1 KP — brak w tekście
**Opis:** Model T&M z dedykowanymi „2 Specjalistami × 160 godzin miesięcznie" przez 24 miesiące (potencjalnie dłużej po przedłużeniach) przypomina body leasing — pracę pod kierownictwem i w wymiarze zbliżonym do etatu. Umowa nie zawiera żadnej klauzuli podkreślającej autonomię organizacyjną Specjalistów ani wyłączenia elementów podporządkowania typowych dla stosunku pracy.
**Skutek:** przy kontroli (np. PIP, ZUS) ryzyko uznania relacji za noszącą cechy stosunku pracy — konsekwencje dla obu stron, głównie jednak dla podmiotów zatrudniających/kierujących Specjalistów.
**Rekomendacja (preferowana):** dodać klauzulę wyraźnie opisującą autonomię Specjalistów (brak stałych godzin narzuconych przez Zamawiającego, brak podporządkowania służbowego, samodzielna organizacja pracy w ramach sprintów) i wyłączenie art. 22 § 1 KP [NIEZWERYFIKOWANE] w relacji handlowej między spółkami.
**Fallback (minimum akceptowalne):** minimalna klauzula deklarująca brak podporządkowania.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 3. Brak sufitu liczby naruszeń jakości kodu i zwłoki w Przyroście — § 2 ust. 1–2
**Opis:** kara 0,5% wynagrodzenia miesięcznego za każdy rozpoczęty dzień zwłoki (§ 2 ust. 1) i 5.000 zł za każdy przypadek naruszenia jakości kodu (§ 2 ust. 2) — obie bez łącznego sufitu. Dotyczy Wykonawcy (Quanta Dev).
**Skutek:** przy powtarzających się naruszeniach w kolejnych sprintach na przestrzeni 24 miesięcy — kumulacja bez górnej granicy (patrz rachunek ekspozycji).
**Rekomendacja (preferowana):** wprowadzić łączny miesięczny lub roczny sufit dla każdej kategorii kary.
**Fallback (minimum akceptowalne):** sufit łączny dla wszystkich kar razem (nie tylko per kategoria).
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. „Przyrost" i „Specjalista" — pojęcia z wielkiej litery bez definicji — brak § Definicje
**Opis:** umowa nie zawiera § Definicje; pojęcia „Przyrost" (§ 2 ust. 1), „Specjalistów" (§ 1 ust. 2), „sprintu" (§ 2 ust. 1) używane są z wielkiej litery lub jako terminy techniczne bez formalnego zdefiniowania.
**Skutek:** niejasny zakres pojęć kluczowych dla naliczania kar (co dokładnie stanowi „Przyrost" i kiedy uznaje się go za dostarczony).
**Rekomendacja (preferowana):** dodać § Definicje z jasnym określeniem „Przyrostu", „Specjalisty", „Sprintu" i kryteriów odbioru.
**Fallback (minimum akceptowalne):** doprecyzować choćby najważniejsze pojęcie („Przyrost") w paragrafie, w którym jest używane.
**Klauzula z bazy:** `references/baza-klauzul/02-preambuly.md`

#### 2. Brak klauzuli terminu i sposobu płatności wynagrodzenia — brak w tekście
**Opis:** umowa określa stawkę godzinową i szacunkowe zaangażowanie, ale nie zawiera klauzuli fakturowania ani terminu płatności.
**Skutek:** niejasność co do cyklu rozliczeniowego (miesięczny? po sprincie?) i terminu płatności — potencjalne spory rozliczeniowe.
**Rekomendacja (preferowana):** dodać klauzulę wynagrodzenia z cyklem rozliczeniowym i terminem płatności (max 60 dni zgodnie z ustawą o przeciwdziałaniu nadmiernym opóźnieniom).
**Fallback (minimum akceptowalne):** odesłanie do standardowych warunków fakturowania Wykonawcy jako Załącznika.
**Klauzula z bazy:** `references/matematyka-kontraktowa.md`

### 🟢 RYZYKA NISKIE

#### 1. Brak wskazania umocowania osób podpisujących
**Opis:** brak sekcji reprezentacji/KRS w dostarczonym tekście (dane fikcyjne w nagłówku).
**Skutek:** przy realnym podpisie — ryzyko braku umocowania.
**Rekomendacja (preferowana):** uzupełnić dane rejestrowe i sposób reprezentacji.
**Fallback (minimum akceptowalne):** —
**Klauzula z bazy:** `references/baza-klauzul/01-strony-reprezentacja.md`

### ✓ Obszary bez zastrzeżeń

- **Spory** — prawo polskie, sąd właściwy dla siedziby Zamawiającego (§ 6 ust. 1) — jednostronny wybór forum, ale w granicach rynkowej praktyki, nie flagowany osobno wobec wagi pozostałych ryzyk

---

## OCENA BEZPIECZEŃSTWA: 8/100

Cztery ryzyka 🔴 (cap iluzoryczny, zakaz konkurencji bez ekwiwalentu z karą bez sufitu, całkowity brak klauzuli IP, całkowity brak klauzuli poufności) i trzy ryzyka 🟠 (brak RODO, ryzyko przekwalifikowania, brak sufitu kumulowanych kar) — to najbardziej ryzykowny dokument w tym zestawie. Braki nie są punktowe do poprawienia, lecz strukturalne: dwa całe obszary (prawa autorskie, poufność) są całkowicie nieobecne w 24-miesięcznej umowie o rozwój oprogramowania dla instytucji finansowej.

**Werdykt:** NIE PODPISYWAĆ w obecnej formie — wymaga gruntownej przeróbki, nie punktowej negocjacji.

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (cap iluzoryczny)
→ Zastosuj: `references/baza-klauzul/11-odpowiedzialnosc.md`

🔴 RYZYKO 3 (brak klauzuli IP)
→ Zastosuj: `references/baza-klauzul/08-prawa-autorskie-ip.md`

🔴 RYZYKO 4 (brak klauzuli poufności)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md`

🟠 RYZYKO 1 (brak RODO)
→ Zastosuj: `references/checklist-dpa-art28.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
