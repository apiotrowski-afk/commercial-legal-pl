# Audyt: Umowa ramowa T&M — QUANTA DEV (Wykonawca) / MERIDIAN FINANCE (Zamawiający)

**Charakter audytu:** neutralny — wady flagowane niezależnie od strony, ze wskazaniem, kogo obciążają.
**Prawo właściwe:** polskie (§ 6).

Legenda ryzyka: 🟥 krytyczne · 🟧 wysokie · 🟨 średnie · 🟩 niskie/porządkowe

## Parametry liczbowe (baza do oceny proporcji)

- Wynagrodzenie miesięczne (szacunkowe): 2 × 160 h × 220 zł = **70.400 zł netto/mies.**
- Wartość 24 miesięcy: ~**1.689.600 zł netto**
- Limit odpowiedzialności (12 mies.): ~**844.800 zł**
- Kara za zwłokę sprintu: 0,5% × 70.400 = **352 zł/dzień**
- Kara za zakaz konkurencji: **300.000 zł/przypadek** ≈ 4,3 miesiąca przychodu z całego kontraktu — za pojedynczy „przypadek"

---

## 1. Model T&M z karami za rezultat — sprzeczność wewnętrzna

🟧 **[obciąża: QUANTA DEV]** § 1 vs § 2 ust. 1–2: T&M to z natury rozliczenie za czas (staranne działanie), a umowa karze za niedostarczenie „Przyrostu" wg „harmonogramu sprintu" — czyli za rezultat. Przy tym „Przyrost", „harmonogram sprintu" i tryb jego ustalania są **niezdefiniowane** — kara wisi na pojęciach, których treść może jednostronnie kształtować backlog Zamawiającego. Kara jakościowa (5.000 zł za wynik przeglądu poniżej progu z Załącznika nr 2) zależy od tego, kto i jak mierzy — brak wskazania audytora, procedury kontradyktoryjnej i częstotliwości przeglądów: 5.000 zł „za każdy przypadek" przy np. przeglądzie per pull request może eskalować absurdalnie.

**Rekomendacja (QUANTA):** zdefiniować Przyrost/sprint/procedurę pomiaru jakości, wprowadzić próg istotności i wspólny proces review; kary za zwłokę tylko przy harmonogramach uzgodnionych obustronnie.

## 2. Kary poza limitem + odszkodowanie ponad kary — otwarta ekspozycja

🟧 **[obciąża: QUANTA DEV]** § 2 ust. 4: kary sumują się **bez łącznego capu**, są wyłączone z limitu z § 3 i dodatkowo Zamawiający może dochodzić odszkodowania przewyższającego (art. 484 § 1 KC zastrzeżone poprawnie — dla Zamawiającego). Efekt: limit odpowiedzialności z § 3 ust. 1 jest w dużej mierze iluzoryczny. Konstrukcja legalna, ale jednostronna; do negocjacji cap na kary (np. 20–30% wynagrodzenia rocznego).

🟩 Zwrócić uwagę (na korzyść QUANTA): kary za „zwłokę" (wina), nie „opóźnienie" — brak kary przy przyczynach niezależnych; oraz możliwość miarkowania (art. 484 § 2 KC).

## 3. Indemnifikacja IP — bez limitu i bez warunków

🟧 **[obciąża: QUANTA DEV]** § 3 ust. 2: zwolnienie z „wszelkiej odpowiedzialności" + „wszelkie koszty" za roszczenia IP osób trzecich — bez capu (poza/obok limitu z ust. 1 — relacja niejasna 🟨), bez standardowych bezpieczników: obowiązku notyfikacji, kontroli obrony/ugody, wyłączeń (modyfikacje przez Zamawiającego, materiały powierzone, użycie niezgodne z przeznaczeniem, kombinacja z cudzym softem). Dla instytucji finansowej klauzula zrozumiała co do zasady, ale w tej formie nadmiarowa.

## 4. BRAK przeniesienia praw autorskich — luka krytyczna dla Zamawiającego

🟥 **[obciąża: MERIDIAN]** Umowa o **rozwój oprogramowania** nie zawiera żadnego postanowienia o prawach autorskich do wytworzonego kodu. Bez pisemnego przeniesienia z polami eksploatacji (art. 41 ust. 2, art. 53 pr. aut.) prawa pozostają przy Wykonawcy; Zamawiający po zapłacie ~1,7 mln zł może dysponować co najwyżej licencją dorozumianą o spornym zakresie. Paradoks: Wykonawca indemnifikuje za naruszenia IP (§ 3 ust. 2), ale sam nie przenosi IP. Brak też poufności (!), mimo że to sektor finansowy — oraz brak RODO/powierzenia i wymogów bezpieczeństwa (przy MERIDIAN FINANCE, potencjalnie podmiot nadzorowany — outsourcing, DORA — to poważny brak compliance 🟧).

## 5. Zakaz konkurencji — szeroki, długi, bez wynagrodzenia

🟥 **[obciąża: QUANTA DEV]** § 5: zakaz na czas umowy + **24 miesiące po**, wobec „podmiotów prowadzących działalność konkurencyjną wobec Zamawiającego" — bez definicji konkurencji, bez ograniczenia terytorialnego/przedmiotowego, **bez ekwiwalentu**, z karą 300.000 zł za przypadek. Dla software house'u obsługującego rynek finansowy to potencjalne wyłączenie z istotnej części rynku na 2 lata za darmo. W B2B brak ekwiwalentu nie przesądza nieważności (swoboda umów), ale tak szeroki i nieodpłatny zakaz bywa kwestionowany przez pryzmat art. 353¹ i art. 58 § 2 KC (nadmierne ograniczenie wolności działalności gospodarczej); wynik sporu niepewny — czyli ryzyko dla obu stron.

**Rekomendacja:** zawęzić do zakazu pracy nad konkurencyjnymi produktami / dla wskazanych podmiotów, skrócić (6–12 mies.), rozważyć ekwiwalent; alternatywnie zamienić na non-solicitation klientów/personelu.

## 6. Automatyczne przedłużanie + indeksacja 8%

🟨 **[obciąża: MERIDIAN, częściowo obu]** § 4: auto-renewal o 12 mies. z oknem wyjścia 90 dni przed końcem okresu — łatwo przegapić (brak obowiązku przypomnienia); stawka +8% w każdym okresie przedłużenia automatycznie (skumulowane: po 2 przedłużeniach +16,6%). Mechanizm legalny, ale wymaga kalendarzowego pilnowania.

🟧 **Brak wypowiedzenia w trakcie okresu** [obciąża: obu, bardziej MERIDIAN]: umowa na 24 miesiące bez klauzuli wypowiedzenia, bez wypowiedzenia z ważnych powodów, bez rozwiązania za naruszenie. Przy T&M o charakterze zlecenia art. 746 KC (wypowiedzenie z ważnych powodów — niewyłączalne) daje wentyl, ale spór o kwalifikację i skutki jest przedprogramowany.

## 7. Braki i niejasności pozostałe

- 🟨 „Szacowane zaangażowanie" bez mechanizmu zmiany wolumenu: czy Zamawiający gwarantuje 320 h/mies.? Czy może zejść do zera (dla QUANTA ryzyko przychodu przy jednoczesnym 24-mies. zakazie konkurencji — szczególnie toksyczna kombinacja: zero zleceń + zakaz pracy dla konkurencji Zamawiającego)?
- 🟨 § 3 ust. 1: limit „12-miesięcznego wynagrodzenia" — przy T&M niejednoznaczny (szacunkowego? faktycznie zapłaconego za ostatnie 12 mies.?).
- 🟨 Brak: procedury raportowania i akceptacji timesheetów, terminu płatności, zasad zastępowalności Specjalistów, siły wyższej, poufności, exit-planu (przekazanie kodu/wiedzy).
- 🟩 Sąd siedziby Zamawiającego — standardowa przewaga strony silniejszej.

---

## Werdykt

**🟧 POMARAŃCZOWY — do podpisania wyłącznie po istotnych zmianach; dziś umowa niekorzystna dla obu stron w różnych punktach.**

Dla **QUANTA DEV** głównym zagrożeniem jest triada: kary bez capu poza limitem + nielimitowana indemnifikacja IP + 24-miesięczny nieodpłatny zakaz konkurencji z karą 300.000 zł (przy przychodzie 70.400 zł/mies. i braku gwarancji wolumenu). Dla **MERIDIAN** — brak przeniesienia praw autorskich do zamawianego oprogramowania, brak poufności i brak wymogów regulacyjnych (outsourcing/DORA/RODO) to luki krytyczne. Umowa wygląda na „ostrą dla wykonawcy", a jednocześnie nie zabezpiecza podstawowego interesu zamawiającego (IP). Wymaga dopisania warstwy IP/poufność/compliance i zbalansowania sankcji.

*Audyt benchmarkowy na dokumencie fikcyjnym; nie stanowi porady prawnej.*
