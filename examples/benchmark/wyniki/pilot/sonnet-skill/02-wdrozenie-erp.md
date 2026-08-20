## AUDYT RYZYK — Umowa wdrożeniowa ERP (Nova Retail / Codex Works)

> **WERDYKT: 🟥 CZERWONY** — nie podpisywać w obecnej formie; trzy odrębne próby obejścia norm bezwzględnie obowiązujących (kara za dług pieniężny, brak pól eksploatacji, przetwarzanie danych bez podstawy) czynią dokument niebezpiecznym dla Zamawiającego niezależnie od pozycji negocjacyjnej.

*Audyt neutralny — wady oznaczone niezależnie od tego, którą stronę faktycznie krzywdzą; przy każdej wskazano stronę dotkniętą. Ta umowa jest wyjątkowo jednostronna na korzyść Wykonawcy (Codex Works) — odnotowano to konsekwentnie przy każdym ryzyku.*

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto (§ 3 ust. 1) | — | 480.000 zł |
| Cap odpowiedzialności Wykonawcy | brak kwotowego capu — § 5 ust. 1 ogranicza zakres wyłącznie do winy umyślnej (i to z wyłączeniem podwykonawców) | zakres, nie kwota | [BRAK DANYCH] co do kwoty; zakres odpowiedzialności Wykonawcy skrajnie wąski |
| Kara umowna Zamawiającego (§ 5 ust. 2) | 50.000 zł / dzień opóźnienia w **płatności**, brak sufitu | 50.000 zł × N dni — np. 10 dni = 500.000 zł (104% wartości umowy); 30 dni = 1.500.000 zł (312% wartości umowy) | ekspozycja Zamawiającego **przewyższa wartość całej umowy już po ok. 10 dniach zwłoki w zapłacie** — i to za samo tylko opóźnienie płatności |
| Kara umowna Wykonawcy za opóźnienie w dostawie | brak — termin realizacji to „niezwłocznie" (§ 2 ust. 1), bez konkretnej daty i bez sankcji | — | 0 zł niezależnie od długości opóźnienia |
| Asymetria (Zamawiający vs Wykonawca) | kary: 50.000 zł/dzień (bez sufitu) vs 0 zł | stosunek kar A/B = ∞ | 100% ryzyka finansowego z tytułu kar po stronie Zamawiającego |
| Daty graniczne | termin wdrożenia: „niezwłocznie" (nieoznaczony); płatność: 60 dni od faktury (§ 3 ust. 2) | 60 dni = górna granica dopuszczalna w B2B wg ustawy o przeciwdziałaniu nadmiernym opóźnieniom (art. 7 ust. 2) — na granicy, nie przekracza | termin wdrożenia niepoliczalny (brak liczby dni); termin płatności formalnie w normie |

**Wniosek z rachunku:** kara 50.000 zł/dzień za opóźnienie w zapłacie jest — niezależnie od jej wysokości — **nieważna z mocy prawa** (art. 483 § 1 KC — zob. bramka ius cogens niżej), bo dotyczy zobowiązania pieniężnego. Nawet po odjęciu tej klauzuli z rachunku, samo zestawienie „brak terminu i brak kary dla Wykonawcy" + „kara wyłącznie dla Zamawiającego" pokazuje umowę skonstruowaną jednostronnie na korzyść Wykonawcy.

### Bramka ius cogens (R10)

Umowa zawiera **trzy** odrębne próby obejścia norm bezwzględnie obowiązujących:

1. **Kara umowna za zobowiązanie pieniężne — § 5 ust. 2.** „Zamawiający zapłaci karę umowną 50.000 zł za każdy dzień opóźnienia w płatności" — kara umowna zastrzeżona za opóźnienie w **zapłacie**, czyli za niewykonanie zobowiązania pieniężnego. Art. 483 § 1 KC [NIEZWERYFIKOWANE] dopuszcza karę umowną wyłącznie dla zobowiązań niepieniężnych; za opóźnienie w zapłacie należą się odsetki (art. 481 KC [NIEZWERYFIKOWANE]), nie kara umowna. **Skutek: nieważność klauzuli** (art. 58 § 1 lub § 3 KC [NIEZWERYFIKOWANE]) — decyduje funkcja klauzuli, nie jej nazwa.
2. **Brak pól eksploatacji przy przeniesieniu praw autorskich — § 4 ust. 1.** „Wykonawca przenosi na Zamawiającego wszelkie prawa autorskie do stworzonego oprogramowania bez ograniczeń" — brak wyraźnego wskazania pól eksploatacji (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]). Ogólna formuła „wszelkie prawa bez ograniczeń" **nie zastępuje** identyfikacji pól. **Skutek: brak skutecznego przeniesienia praw w zakładanym zakresie** — mimo zapłaty 480.000 zł Zamawiający może nie nabyć praw do oprogramowania, za które zapłacił.
3. **Przetwarzanie danych bez podstawy / poza celem umowy — § 8 ust. 2.** „Niezależnie od pozostałych postanowień Umowy, Wykonawca zachowuje prawo do wykorzystania danych Zamawiającego do trenowania modeli AI" — brak wskazanej podstawy prawnej, brak zgody, sprzeczne z § 6 ust. 1 (poufność), sprzeczne z zasadą celowości i minimalizacji RODO. Jeśli dane obejmują dane osobowe — narusza RODO art. 28 [NIEZWERYFIKOWANE] (brak instrumentu powierzenia) oraz zasadę ograniczenia celu (RODO art. 5 ust. 1 lit. b [NIEZWERYFIKOWANE]). **Skutek: ryzyko sankcji administracyjnej** (RODO art. 83 ust. 4 lit. a [NIEZWERYFIKOWANE]) oraz naruszenie samej Umowy (klauzula sprzeczna z § 6).

Trigger mikroprzedsiębiorcy (art. 3855 KC [NIEZWERYFIKOWANE]) — nie dotyczy, obie strony to spółki z o.o.

**Test pięciopunktowy — wybór prawa obcego (§ 8 ust. 1).** Umowa między dwiema polskimi spółkami, wdrożenie realizowane „w infrastrukturze Zamawiającego" (a więc w Polsce) — poddana prawu stanu Delaware i sądowi w Wilmington. (1) Treść: całkowita zmiana reżimu prawnego bez związku gospodarczego ze stanem Delaware. (2) Sposób wprowadzenia: brak wskazania negocjacji tego punktu — wygląda na wzorzec narzucony przez Wykonawcę. (3) Asymetria: dla Zamawiającego dochodzenie roszczeń w Wilmington jest kosztowo i praktycznie zaporowe. (4) Praktyka rynkowa: nietypowe dla umowy między dwiema krajowymi spółkami bez elementu transgranicznego. (5) Efekt kumulatywny: w połączeniu z jednostronną karą (§ 5 ust. 2) i wąskim zakresem odpowiedzialności Wykonawcy (§ 5 ust. 1) — wybór prawa obcego dodatkowo utrudnia Zamawiającemu dochodzenie ochrony. Niezależnie od skuteczności takiej klauzuli w świetle prawa prywatnego międzynarodowego (możliwe zastosowanie bezwzględnie obowiązujących przepisów polskich mimo wyboru prawa obcego — art. 3 ust. 3 Rozporządzenia Rzym I [NIEZWERYFIKOWANE], gdy wszystkie elementy stanu faktycznego są związane z jednym państwem) — klauzula jest czerwoną flagą sama w sobie.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna za zobowiązanie pieniężne — § 5 ust. 2
**Opis:** patrz bramka ius cogens pkt 1. Dotyczy Zamawiającego (Nova Retail) jako strony obciążonej — ale sama klauzula jest nieważna, więc realnym problemem jest niepewność interpretacyjna i ryzyko, że Wykonawca będzie próbował ją egzekwować mimo wadliwości.
**Skutek:** nieważność klauzuli; spór o to, czy strony w jej miejsce zastosują odsetki ustawowe.
**Rekomendacja (preferowana):** usunąć karę za opóźnienie w płatności; pozostawić odsetki ustawowe za opóźnienie w transakcjach handlowych.
**Fallback (minimum akceptowalne):** jeśli Wykonawca nalega na sankcję — odsetki umowne (nie kara) w rozsądnej wysokości.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`

#### 2. Brak pól eksploatacji przy przeniesieniu praw autorskich — § 4 ust. 1
**Opis:** patrz bramka ius cogens pkt 2. Dotyczy Zamawiającego (Nova Retail) — ryzyko, że mimo zapłaty 480.000 zł nie nabywa skutecznie praw do oprogramowania.
**Skutek:** brak nabycia praw w zakładanym zakresie; ryzyko, że Wykonawca zachowuje uprawnienia do dalszego wykorzystania/licencjonowania tego samego kodu.
**Rekomendacja (preferowana):** wymienić wprost pola eksploatacji (utrwalanie, zwielokrotnianie, wprowadzanie do pamięci komputera, publiczne udostępnianie w sieci itd. — adekwatnie do sposobu korzystania z ERP), zachować formę pisemną.
**Fallback (minimum akceptowalne):** minimalny katalog pól odpowiadający faktycznemu modelowi wdrożenia (instalacja, modyfikacja, uruchamianie, sporządzanie kopii zapasowych).
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 3. Wykorzystanie danych Zamawiającego do trenowania AI bez podstawy — § 8 ust. 2
**Opis:** patrz bramka ius cogens pkt 3. Dotyczy Zamawiającego (Nova Retail) — utrata kontroli nad własnymi danymi biznesowymi/operacyjnymi wprowadzonymi do systemu ERP.
**Skutek:** ryzyko naruszenia RODO (jeśli dane obejmują dane osobowe), naruszenie zasady poufności z § 6, ryzyko wykorzystania danych konkurencyjnie (dane sprzedażowe/magazynowe Nova Retail w modelu AI Wykonawcy).
**Rekomendacja (preferowana):** usunąć klauzulę w całości; jeśli Wykonawca chce trenować modele — odrębna, jawna zgoda z określonym zakresem, anonimizacją/pseudonimizacją i prawem sprzeciwu.
**Fallback (minimum akceptowalne):** wyłącznie dane zanonimizowane, wyłącznie za odrębną pisemną zgodą, z prawem cofnięcia.
**Klauzula z bazy:** `references/checklist-dpa-art28.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Brak terminu wdrożenia i degradacja do starannego działania — § 1 ust. 1, § 2 ust. 1
**Opis:** „Wykonawca dołoży starań w celu wdrożenia systemu ERP" (§ 1 ust. 1) oraz „Wykonawca wykona Wdrożenie niezwłocznie po podpisaniu Umowy" (§ 2 ust. 1) — rezultat (wdrożenie systemu) sformułowany jako staranne działanie, bez konkretnej daty. Dotyczy Zamawiającego (Nova Retail).
**Skutek:** brak egzekwowalnego terminu; trudność w dochodzeniu roszczeń z tytułu opóźnienia, bo obowiązek nie jest rezultatem.
**Rekomendacja (preferowana):** zobowiązanie rezultatu z konkretnym harmonogramem/kamieniami milowymi i datą końcową.
**Fallback (minimum akceptowalne):** minimum — konkretna liczba dni/tygodni od podpisania Umowy zamiast „niezwłocznie".
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 2. Skrajnie wąski zakres odpowiedzialności Wykonawcy — § 5 ust. 1
**Opis:** „Wykonawca ponosi odpowiedzialność wyłącznie za szkody wyrządzone umyślnie, z wyłączeniem winy umyślnej podwykonawców" — odpowiedzialność Wykonawcy ograniczona do minimum wymaganego przez art. 473 § 2 KC [NIEZWERYFIKOWANE] (co samo w sobie jest zgodne z prawem jako floor, nie excludes), ale dodatkowo wyłącza winę umyślną podwykonawców, choć art. 474 KC [NIEZWERYFIKOWANE] każe co do zasady odpowiadać za osoby, którymi dłużnik posługuje się przy wykonaniu zobowiązania, jak za własne działania. Dotyczy Zamawiającego (Nova Retail).
**Skutek:** przy niedbałym lub nawet umyślnym działaniu podwykonawcy Wykonawcy — Zamawiający może nie mieć skutecznego roszczenia wobec Wykonawcy.
**Rekomendacja (preferowana):** rozszerzyć odpowiedzialność co najmniej do rażącego niedbalstwa i wprowadzić cap kwotowy (np. 12-miesięczne wynagrodzenie) obejmujący też działania podwykonawców.
**Fallback (minimum akceptowalne):** utrzymać wyłączenie zwykłego niedbalstwa, ale nie wyłączać winy umyślnej podwykonawców.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 3. Zakres wsparcia powdrożeniowego wg wyłącznego uznania — § 5 ust. 3
**Opis:** „Zakres wsparcia powdrożeniowego Wykonawca ustala według wyłącznego uznania" — uznaniowość bez kryteriów. Dotyczy Zamawiającego (Nova Retail).
**Skutek:** Wykonawca może dowolnie ograniczać wsparcie po wdrożeniu bez możliwości kwestionowania.
**Rekomendacja (preferowana):** zakres wsparcia określony w Umowie/Załączniku (SLA, liczba godzin, czas reakcji).
**Fallback (minimum akceptowalne):** minimalny katalog gwarantowanego wsparcia + tryb rozszerzenia za dodatkowym wynagrodzeniem.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 4. Asymetria prawa wypowiedzenia — § 7 ust. 1–2
**Opis:** „Zamawiający nie może wypowiedzieć Umowy przed zakończeniem Wdrożenia" vs „Wykonawca może wypowiedzieć Umowę w każdym czasie i bez podania przyczyny". Dotyczy Zamawiającego (Nova Retail), który jest związany umową bez możliwości wyjścia, podczas gdy Wykonawca może odejść w każdej chwili.
**Skutek:** przy braku terminu wdrożenia (patrz wyżej) Zamawiający może być związany umową bezterminowo bez realnej możliwości wyjścia, a jednocześnie narażony na jednostronne zerwanie przez Wykonawcę w dowolnym momencie.
**Rekomendacja (preferowana):** symetryczne prawo wypowiedzenia dla obu stron, z określonymi przesłankami i okresem wypowiedzenia.
**Fallback (minimum akceptowalne):** prawo Zamawiającego do wypowiedzenia co najmniej w razie istotnego opóźnienia Wykonawcy.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie.md`

#### 5. Prawo obce i sąd zagraniczny dla umowy krajowej — § 8 ust. 1
**Opis:** patrz test pięciopunktowy w bramce ius cogens. Dotyczy Zamawiającego (Nova Retail).
**Skutek:** utrudnione i kosztowne dochodzenie roszczeń.
**Rekomendacja (preferowana):** prawo polskie, sąd polski (siedziba Zamawiającego lub sąd właściwy dla miejsca wykonania).
**Fallback (minimum akceptowalne):** prawo polskie z klauzulą arbitrażową w Polsce (np. SA przy KIG).
**Klauzula z bazy:** `references/baza-klauzul/13-postanowienia-koncowe.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. „Może, ale nie jest zobowiązany" przekazać kod źródłowy — § 4 ust. 2
**Opis:** „Wykonawca może, ale nie jest zobowiązany, przekazać kod źródłowy" — pozorne zobowiązanie. Dotyczy Zamawiającego (Nova Retail), który może nie otrzymać kodu źródłowego mimo nabycia praw autorskich (o ile te w ogóle skutecznie przeszły — patrz ryzyko krytyczne 2).
**Skutek:** brak dostępu do kodu źródłowego ogranicza możliwość samodzielnego utrzymania/rozwoju systemu.
**Rekomendacja (preferowana):** obowiązek przekazania kodu źródłowego wraz z dokumentacją po zapłacie.
**Fallback (minimum akceptowalne):** depozyt kodu źródłowego u zaufanej trzeciej strony (source code escrow) z warunkami wydania.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

#### 2. „Na bieżąco" bez określonej częstotliwości — § 2 ust. 2
**Opis:** „Zamawiający będzie zgłaszał uwagi na bieżąco" — częstotliwość nieoznaczona.
**Skutek:** brak egzekwowalnego harmonogramu akceptacji/uwag, ryzyko sporu o terminowość.
**Rekomendacja (preferowana):** określić interwał (np. w terminie 5 Dni Roboczych od udostępnienia etapu).
**Fallback (minimum akceptowalne):** pozostawić, ale dodać domniemanie akceptacji przy braku uwag w rozsądnym terminie.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 3. „Wdrożenie" jako pojęcie z wielkiej litery bez formalnej definicji — § 1, § 2, § 7
**Opis:** Pojęcie „Wdrożenie" używane z wielkiej litery (§ 1 ust. 2, § 2 ust. 1, § 7 ust. 1) bez odrębnej definicji w słowniczku — antywzorzec definicji-widma.
**Skutek:** niejasny zakres pojęcia przy sporze o to, co dokładnie obejmuje „zakończenie Wdrożenia" (istotne dla § 7 ust. 1).
**Rekomendacja (preferowana):** dodać § Definicje z jasnym określeniem zakresu „Wdrożenia" i kryteriów jego zakończenia (odbiór końcowy).
**Fallback (minimum akceptowalne):** doprecyzować choćby jednym zdaniem w § 1.
**Klauzula z bazy:** `references/baza-klauzul/02-preambuly.md`

### 🟢 RYZYKA NISKIE

#### 1. Brak wskazania umocowania osób podpisujących
**Opis:** brak sekcji reprezentacji/KRS w dostarczonym tekście (dane fikcyjne w nagłówku).
**Skutek:** przy realnym podpisie — ryzyko braku umocowania.
**Rekomendacja (preferowana):** uzupełnić dane rejestrowe i sposób reprezentacji.
**Fallback (minimum akceptowalne):** —
**Klauzula z bazy:** `references/baza-klauzul/01-strony-reprezentacja.md`

### ✓ Obszary bez zastrzeżeń

- **Poufność** — § 6 istnieje, choć lakoniczna (brak okresu po zakończeniu, brak wyłączeń, brak kary) — odnotowane pośrednio jako kontekst dla ryzyka krytycznego 3 (§ 8 ust. 2 sprzeczne z § 6); samodzielnie nie klasyfikowane jako osobne ryzyko z uwagi na priorytet ważniejszych wad
- **Tytuł prawny / przekwalifikowanie** — n/d (umowa wdrożeniowa między dwiema spółkami, nie body leasing ani umowa o dzieło z osobą fizyczną)

---

## OCENA BEZPIECZEŃSTWA: 12/100

Trzy ryzyka 🔴 wynikające z prób obejścia norm bezwzględnie obowiązujących (kara za dług pieniężny, brak pól eksploatacji, przetwarzanie danych bez podstawy) w połączeniu z pięcioma ryzykami 🟠 (brak terminu wdrożenia, ekstremalnie wąska odpowiedzialność Wykonawcy, uznaniowe wsparcie, asymetryczne wypowiedzenie, prawo obce) tworzą dokument, który w praktyce zabezpiecza niemal wyłącznie interes Wykonawcy (Codex Works), przy jednoczesnym ryzyku prawnym nawet dla samego Wykonawcy (nieważne klauzule mogą nie dać oczekiwanej ochrony).

**Werdykt:** NIE PODPISYWAĆ w obecnej formie — wymaga gruntownej przeróbki (nie punktowej negocjacji) przed jakimkolwiek dalszym procedowaniem.

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (kara za dług pieniężny)
→ Zastosuj: `references/baza-klauzul/10-kary-umowne.md`

🔴 RYZYKO 2 (brak pól eksploatacji)
→ Zastosuj: `references/baza-klauzul/08-prawa-autorskie-ip.md`

🔴 RYZYKO 3 (dane do trenowania AI bez podstawy)
→ Zastosuj: `references/checklist-dpa-art28.md`

🟠 RYZYKO 2 (wąska odpowiedzialność Wykonawcy)
→ Zastosuj: `references/baza-klauzul/11-odpowiedzialnosc.md`

🟠 RYZYKO 4 (asymetria wypowiedzenia)
→ Zastosuj: `references/baza-klauzul/12-wypowiedzenie.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
