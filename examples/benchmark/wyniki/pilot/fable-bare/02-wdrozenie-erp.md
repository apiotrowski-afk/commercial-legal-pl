# Audyt: Umowa wdrożeniowa ERP — NOVA RETAIL (Zamawiający) / CODEX WORKS (Wykonawca)

**Charakter audytu:** neutralny — wady flagowane niezależnie od strony, ze wskazaniem, kogo obciążają.
**Punkt odniesienia:** prawo polskie (KC, pr. aut., ustawa o przeciwdziałaniu nadmiernym opóźnieniom, RODO) — z zastrzeżeniem, że umowa wybiera prawo Delaware (pkt 1 poniżej).

Legenda ryzyka: 🟥 krytyczne · 🟧 wysokie · 🟨 średnie · 🟩 niskie/porządkowe

---

## 1. Prawo stanu Delaware i sąd w Wilmington

🟥 **[obciąża: obie strony, praktycznie NOVA RETAIL]** § 8 ust. 1 — dla umowy między dwiema polskimi spółkami, wykonywanej w Polsce, wybór prawa Delaware i sądu w Wilmington jest:
- prawnie wątpliwy co do pełnej skuteczności: przy sytuacji czysto krajowej art. 3 ust. 3 Rzym I nie pozwala wyłączyć bezwzględnie wiążących przepisów prawa polskiego (wybór działa tylko „materialnoprawnie");
- biznesowo zaporowy: dochodzenie roszczeń w USA to koszty i bariera faktyczna — klauzula działa jak **ukryte wyłączenie odpowiedzialności Wykonawcy**, bo Zamawiający realnie nie pozwie;
- ryzykowny także dla Wykonawcy (nieprzewidywalność obcego reżimu, problem uznania/wykonania orzeczenia w PL).

**Rekomendacja:** prawo polskie, sąd polski (neutralnie: siedziba pozwanego albo stałe miejsce, arbitraż krajowy).

## 2. „Dołoży starań w celu wdrożenia" — brak zobowiązania rezultatu

🟥 **[obciąża: NOVA RETAIL]** § 1 ust. 1 — wdrożenie ERP za 480.000 zł ryczałtu skonstruowano jako zobowiązanie **starannego działania**. Zamawiający płaci cenę „za rezultat", ale rezultatu nie może wyegzekwować: brak definicji ukończenia, brak procedury odbiorów (odbiory częściowe/końcowy, testy akceptacyjne, kryteria), brak gwarancji/rękojmi, brak SLA. Załącznik nr 1 jest jedynym nośnikiem zakresu — a nie wiadomo, czy określa kryteria odbioru.

**Rekomendacja:** zobowiązanie rezultatu co do wdrożenia (charakter zbliżony do umowy o dzieło), harmonogram etapowy, procedura odbioru z terminami na uwagi, gwarancja jakości.

## 3. Terminy: „niezwłocznie po podpisaniu" — brak harmonogramu

🟧 **[obciąża: obie strony]** § 2 — „niezwłocznie" to termin rozpoczęcia, nie zakończenia. Brak jakiegokolwiek terminu końcowego, kamieni milowych, konsekwencji opóźnienia Wykonawcy (żadnych kar — por. pkt 6) i procedury zgłaszania uwag (poza „na bieżąco"). Dla Wykonawcy też ryzyko: brak obowiązków współdziałania Zamawiającego (dostępy, dane, decyzje) i skutków ich braku.

## 4. Płatność i prawa autorskie sprzężone w błędne koło

🟧 **[obciąża: NOVA RETAIL]** Konstrukcja § 3–4:
- płatność 480.000 zł jest **jednorazowa i nieuwarunkowana odbiorem** — wymagalna po doręczeniu faktury (60 dni), niezależnie od stanu wdrożenia;
- termin 60 dni między przedsiębiorcami wymaga, by nie był rażąco nieuczciwy wobec wierzyciela (ustawa o przeciwdziałaniu nadmiernym opóźnieniom — domyślny standard 60 dni jest graniczny; tu akurat obciąża Wykonawcę jako wierzyciela) 🟨;
- przeniesienie praw autorskich „z chwilą zapłaty" — pod polskim pr. aut. przeniesienie **wymaga wskazania pól eksploatacji (art. 41 ust. 2, art. 53 pr. aut.)**; „wszelkie prawa bez ograniczeń" jest wadliwe i może okazać się bezskuteczne 🟥 [obciąża NOVA RETAIL — może zapłacić i nie nabyć praw]. Brak też: zezwoleń na wykonywanie praw zależnych, zobowiązania do niewykonywania praw osobistych, licencji przejściowej do czasu zapłaty.

🟥 **Kod źródłowy:** § 4 ust. 2 — „może, ale nie jest zobowiązany" przekazać kod. ERP bez kodu źródłowego (i dokumentacji, i depozytu) = pełny vendor lock-in: Zamawiający formalnie „ma prawa", ale nie ma przedmiotu, na którym mógłby je wykonywać.

**Rekomendacja:** płatności etapami po odbiorach; przeniesienie praw z wyliczonymi polami eksploatacji + prawa zależne + kod źródłowy i dokumentacja jako warunek odbioru (ew. escrow).

## 5. Odpowiedzialność Wykonawcy — praktycznie wyzerowana

🟥 **[obciąża: NOVA RETAIL]** § 5 ust. 1: odpowiedzialność „wyłącznie za szkody wyrządzone umyślnie, **z wyłączeniem winy umyślnej podwykonawców**". Dwie wady:
- pod prawem polskim **nie można wyłączyć odpowiedzialności za szkodę wyrządzoną umyślnie (art. 473 § 2 KC)** — a wyłączenie umyślności podwykonawców obchodzi art. 474 KC (odpowiedzialność za podwykonawców jak za własne działania) i jest co najmniej wątpliwe w świetle art. 473 § 2 i art. 58 KC; pod prawem Delaware analiza byłaby inna — kolejny argument przeciw klauzuli wyboru prawa;
- nawet w ważnym zakresie: brak odpowiedzialności za rażące niedbalstwo i zwykłą winę = Zamawiający ponosi całe ryzyko nieudanego wdrożenia.

## 6. Kary umowne — asymetria i wada konstrukcyjna

🟥 **[obciąża: NOVA RETAIL]** § 5 ust. 2:
- kara 50.000 zł **za każdy dzień** opóźnienia w płatności jest (a) drastycznie rażąco wygórowana (10 dni = kwota przekraczająca całe wynagrodzenie), (b) **nieważna co do zasady**: kara umowna może zabezpieczać wyłącznie zobowiązania **niepieniężne** (art. 483 § 1 KC); kara za opóźnienie w zapłacie jest sprzeczna z ustawą — właściwe są odsetki;
- „Wykonawca nie ponosi kar" — pełna asymetria: żadnej sankcji za opóźnienie/wady wdrożenia.

## 7. Wypowiedzenie — skrajna asymetria

🟥 **[obciąża: NOVA RETAIL]** § 7: Zamawiający nie może wypowiedzieć przed końcem wdrożenia (którego termin nie istnieje — czyli potencjalnie nigdy), a Wykonawca może wypowiedzieć w każdym czasie bez przyczyny — nawet po otrzymaniu zapłaty, przed ukończeniem prac, bez rozliczenia. Uwaga systemowa: jeśli umowę kwalifikować jako umowę o dzieło/zlecenie pod prawem polskim, ustawowych praw Zamawiającego (np. art. 644 KC — odstąpienie za zapłatą wynagrodzenia; art. 746 KC) nie da się w pełni wyłączyć — kolejne tarcie z klauzulą Delaware. Brak też jakiegokolwiek exit-planu (przekazanie prac, zwrot danych).

## 8. Dane Zamawiającego do trenowania AI

🟥 **[obciąża: NOVA RETAIL]** § 8 ust. 2 — „niezależnie od pozostałych postanowień" Wykonawca może wykorzystywać **dane Zamawiającego** do trenowania modeli AI. Dane spółki retail w ERP to: dane osobowe klientów i pracowników (RODO — brak podstawy, brak umowy powierzenia art. 28 RODO; powierzenie nie obejmuje własnych celów procesora → Wykonawca stawałby się administratorem bez podstawy prawnej), tajemnice przedsiębiorstwa (marże, dostawcy, obroty). Klauzula unieważnia w praktyce § 6 (poufność) — „niezależnie od pozostałych postanowień" nadpisuje NDA. Bezterminowa, bez zakresu, bez anonimizacji.

**Rekomendacja:** wykreślić; ewentualnie wąska zgoda na dane zanonimizowane/zagregowane, poza danymi osobowymi, z prawem odwołania.

## 9. Braki porządkowe

🟨 Brak: umowy powierzenia przetwarzania (konieczna przy wdrożeniu ERP), postanowień o podwykonawcach, siły wyższej, zasad zmiany zakresu (change request), okresu poufności (§ 6 bez terminu i wyłączeń), zasad licencji na oprogramowanie standardowe ERP (przenosi się tylko prawa do „stworzonego oprogramowania" — a licencje producenta systemu?).

---

## Werdykt

**🟥 CZERWONY — umowa nie do podpisania przez Zamawiającego; wymaga gruntownej przebudowy.**

To umowa niemal jednostronnie korzystna dla Wykonawcy (CODEX WORKS): staranne działanie zamiast rezultatu, brak terminu i odbiorów, płatność bez warunku, zero odpowiedzialności, kara tylko od Zamawiającego (i to nieważna konstrukcyjnie), wypowiedzenie tylko dla Wykonawcy, prawo Delaware jako bariera egzekucji oraz klauzula AI przełamująca poufność i RODO. Paradoksalnie kilka „przewag" Wykonawcy jest prawnie nieskutecznych pod prawem polskim (kara za opóźnienie płatności, wyłączenie umyślności, przeniesienie praw bez pól eksploatacji) — więc i Wykonawca nie dostaje pewności prawnej, którą pozornie sobie zapisał. Do renegocjacji od fundamentów: rezultat + harmonogram + odbiory + płatności etapowe + symetryczna odpowiedzialność i kary + prawo polskie + wykreślenie klauzuli AI.

*Audyt benchmarkowy na dokumencie fikcyjnym; nie stanowi porady prawnej.*
