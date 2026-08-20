# AUDYT RYZYK — Umowa T&M Rozwój Oprogramowania (QUANTA DEV / MERIDIAN FINANCE)

> **WERDYKT: 🟨 ŻÓŁTY** — Umowa zawiera kilka ryzyk wysokich: niejasny cap odpowiedzialności (12 mies. na 24-miesięczny okres), kary bez sufitu, brak praw autorskich, zakaz konkurencji bez ekwiwalentu. Wymaga negocjacji przed podpisem.

## 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Stawka | 220 zł/h netto | — | 220 zł/h |
| Szacunkowe zaangażowanie | 2 spec. × 160 h/mies | 220 × 160 × 24 = 845.760 zł (nominał) | — |
| Wartość umowy (z waloryzacją 8% rok 2) | rok 1: 422.400 zł; rok 2: 456.192 zł | 422.400 + 456.192 | **878.592 zł** |
| Cap nominalny | 12-miesięcznego wynagrodzenia | 220 × 160 × 12 = 422.400 zł | 422.400 zł |
| Kara za zwłokę przyrostu | 0,5% wynagrodzenia mies. / dzień | 0,5% × 35.200 × 60 dni = 10.560 zł | brak sufitu |
| Kara za jakość kodu | 5.000 zł / "przypadek" | N "przypadków" × 5.000 zł | brak sufitu, liczba N niezdefiniowana |
| Kara za konkurencję | 300.000 zł / "przypadek" | 1-2 "przypadki" × 300.000 = 300.000–600.000 zł | brak sufitu |
| Efektywna ekspozycja | — | cap 422.400 + kary (min.) 310.560 + lucrum cessans | **min. 732.960 zł = 83% wartości umowy** |
| Asymetria kar | wszystkie na Wykonawcę | Zamawiający: 0; Wykonawca: 732.960+ | **1:0** |
| Okres auto-renewal | co 12 mies., podwyższenie 8% | stawka rośnie (wzrost przychodu wierzyciela zmniejsza % kar) | umowa może się piętrzyć |

**Wniosek z rachunku:** 
1. Cap odpowiedzialności (422.400 zł) wynosi **50% wartości umowy 24-miesięcznej** (878.592 zł). Cap powinien być co najmniej równy całkowitemu wynagrodzeniu, jeśli umowa trwa 24 mies.
2. Kary umowne **poza capem** + brak sufitu = ekspozycja efektywna co najmniej **83% wartości umowy** (nie licząc lucrum cessans i możliwych wielu "przypadków" naruszeń).
3. Asymetria: Zamawiający nie ponosi żadnych kar.

---

## 🟠 RYZYKA WYSOKIE

### 1. Niejasny cap odpowiedzialności — § 3 ust. 1
**Opis:**
```
„Łączna odpowiedzialność Wykonawcy ograniczona jest do 12-miesięcznego wynagrodzenia"
```
Umowa trwa 24 mies. (§ 1 ust. 3), ale cap to „12-miesięczne wynagrodzenie" = 422.400 zł. To oznacza:
- Cap pokrywa tylko **połowę** okresu umowy (mies. 1–12).
- Szkody w mies. 13–24 mogą przekroczyć cap bez limitu.

**Skutek:** Dla Zamawiającego: niewystarczająca ochrona w drugiej połowie umowy. Dla Wykonawcy: niespodziana ekspozycja.

**Rekomendacja (preferowana):**
```
§ 3 ust. 1 (zmieniony)
Łączna odpowiedzialność Wykonawcy ograniczona jest do 12-miesięcznego wynagrodzenia 
w stosunku rocznym, obliczanego na dzień zgłoszenia roszczenia. W drugim roku Umowy cap 
wynosi 12 × [stawka w roku 2] = 12 × (220 zł × 1,08) × 160 h = [kwota].
```
Alternatywnie: cap = 24-miesięczne wynagrodzenie (pełny okres).

**Fallback (minimum akceptowalne):** Wyjaśnić, czy cap obowiązuje każdego roku odrębnie czy na całą umowę. Jeśli na całą umowę, przenieść do 24 mies. lub wskazać, że cap się „resetuje" każdego roku (i tym samym w roku 2 Wykonawca ma nowy limit do wyczerpania).

---

### 2. Kary umowne bez sufitu — § 2 ust. 1, 2, 3
**Opis:**
```
§ 2 ust. 1: „za zwłokę w dostarczeniu Przyrostu… 0,5% wynagrodzenia miesięcznego za każdy rozpoczęty dzień zwłoki"
§ 2 ust. 2: „za każdy przypadek naruszenia standardów jakości… 5.000 zł"
§ 2 ust. 3: „za naruszenie zakazu konkurencji… 300.000 zł za każdy przypadek naruszenia"
```

Problemy:
- § 2 ust. 1: Brak maksymalnej liczby dni zwłoki (teoretycznie: 0,5% × 35.200 zł × 730 dni = 128.320 zł).
- § 2 ust. 2: Pojęcie „przypadek naruszenia standardów" — niezdefiniowane. Czy to 1 błąd kodu? 1 przegląd poniżej progu? Każda linia kodu z błędem?
- § 2 ust. 3: Pojęcie „przypadek naruszenia konkurencji" — czy to konsultacja dla konkurenta? Czy rozpoznanie jego nazwy w CV? Niejasne.
- § 2 ust. 4 mówi „Kary umowne podlegają sumowaniu" — oznacza, że można skumulować wszystkie trzy rodzaje kar.

**Skutek:**
- Ekspozycja finansowa Wykonawcy jest nieznanym maksimum.
- Spór o definicję „przypadku" przy każdym roszczeniu.
- Możliwa sytuacja: 1 dzień zwłoki + 1 błąd jakości + 1 naruszenie konkurencji = 0,5% + 5.000 + 300.000 = 305.500 zł w jeden dzień.

**Rekomendacja (preferowana):**
```
§ 2 (zmieniony)
1. Za zwłokę w dostarczeniu Przyrostu względem harmonogramu sprintu (maksymalnie 5 dni 
   zwłoki w każdym sprincie): 0,5% wynagrodzenia miesięcznego za każdy rozpoczęty dzień, 
   łącznie nie więcej niż 5% wynagrodzenia miesięcznego per sprint.

2. Za naruszenie standardów jakości kodu (wynik przeglądu poniżej progu z Załącznika nr 2, 
   zdefiniowanego jako: pokrycie testami <70% lub więcej niż 5 defektów krytycznych na 1000 linii): 
   2.500 zł za pierwsze naruszenie, 5.000 zł za drugie i kolejne, łącznie nie więcej niż 
   5% wynagrodzenia miesięcznego.

3. Za naruszenie zakazu konkurencji (świadczenie usług konkurencyjnych na rzecz 
   podmiotów wymienionego sektora, potwierdzone dokumentem lub zawiadomieniem): 
   300.000 zł za każdy zidentyfikowany podmiot, ale łącznie nie więcej niż [X]% wartości umowy.

4. Łączny sufit kar umownych ze wszystkich podstaw: [Y]% wartości całej umowy [878.592 zł], 
   wyliczony na koniec każdego okresu rocznego.
```

**Fallback (minimum akceptowalne):**
- § 2 ust. 1: dodać „łącznie nie więcej niż 10% wynagrodzenia miesięcznego" za zwłokę.
- § 2 ust. 2: zdefiniować „przypadek" konkretnie (np. „przegląd kodu z wynikiem <70%").
- § 2 ust. 3: ograniczyć konkurencję do „sektora [nazwa]" i „okresu 12 mies. po umowie" (zamiast obecnego „24 mies.").
- § 2 ust. 4: dodać sufit łączny wszystkich kar (np. „nie więcej niż 20% wartości umowy").

---

### 3. Brak definicji praw autorskich do kodu — § 1, brak klauzuli IP
**Opis:** Umowa o rozwój oprogramowania nie zawiera klauzuli definiującej, komu przysługują prawa do kodu źródłowego i jej pól eksploatacji. Domyślnie, prawa mogą pozostać u Wykonawcy.

**Skutek:**
- Zamawiający inwestuje 878.592 zł i może nie mieć praw do kodu.
- Ryzyko: Wykonawca może wykorzystać kod dla konkurencji lub inne projekty.
- Brak gwarancji czystości IP (czy kod zawiera komponenty GPL, AGPL).

**Rekomendacja (preferowana):**
```
§ 1a. Prawa Autorskie (nowy)
1. Zamawiający nabywa autorskie prawa majątkowe do Oprogramowania (kodu źródłowego, 
   dokumentacji, testów) w następujących polach eksploatacji:
   a) prawo do wielokrotnego powielania (backup, archiwizacja),
   b) prawo do rozpowszechniania (publikacja, open-source, jeśli Zamawiający uzna za stosowne),
   c) prawo do przeróbek i adaptacji,
   d) prawo do publicznego wyświetlania.

2. Wykonawca zachowuje prawa do następujących komponentów (jeśli dotyczy):
   [wymienić: generyczne biblioteki, komponenty od osób trzecich, zapatentowane algorytmy — 
   list powinien być precyzyjny i jasny]

3. Gwarancja czystości IP: Wykonawca gwarantuje, że Oprogramowanie nie zawiera komponentów 
   objętych licencjami GPL, AGPL ani innymi licencjami copyleft bez wyraźnej zgody Zamawiającego.
   Naruszenie gwarancji → indemnifikacja bez limitu (art. 474 KC).
```

**Fallback (minimum akceptowalne):** Jawnie wskazać, że Zamawiający nabywa prawa do kodu źródłowego w polach (a)–(c) minimum. Dodać gwarancję czystości (brak GPL/AGPL).

---

### 4. Zakaz konkurencji bez ekwiwalentu — § 5
**Opis:**
```
„Wykonawca zobowiązuje się w okresie obowiązywania Umowy oraz przez 24 miesiące po jej zakończeniu 
nie świadczyć usług na rzecz podmiotów prowadzących działalność konkurencyjną wobec Zamawiającego. 
Zakaz nie jest związany z dodatkowym wynagrodzeniem"
```

Problemy:
- 24 mies. po umowie to długi okres (standard 6–12 mies.).
- Brak ekwiwalentu (dodatkowego wynagrodzenia za ograniczenie).
- Brak jasnego zakresu „działalności konkurencyjnej" — co to oznacza? Cały sektor? Określonych sektorów?
- Może naruszać zasady współżycia (art. 3531 KC) jako rażąco jednostronna asymetria.

**Skutek:**
- Ryzyko: Wykonawca (mały dev) może być zmuszony do rezygnacji z nowych projektów przez 24 mies. po umowie bez dodatkowego wynagrodzenia.
- Możliwe orzeczenie o nieskuteczności (art. 5 KC — nadużycie prawa) lub częściowej nieważności.

**Rekomendacja (preferowana):**
```
§ 5 (zmieniony)
1. Wykonawca zobowiązuje się w okresie obowiązywania Umowy oraz przez 12 miesięcy po jej 
   zakończeniu nie świadczyć usług bezpośrednio konkurencyjnych wobec Zamawiającego.

2. „Usługami bezpośrednio konkurencyjnymi" rozumie się usługi świadczone na rzecz podmiotów 
   z sektorów [wymienić konkretnie: fintech, payment systems, itp.], zamawianych przez 
   Zamawiającego w trakcie trwania Umowy.

3. Zakaz nie obejmuje: [wyłączenia — np. projektów ogólnie dostępnych, konsultacji, 
   kontrybucji do open-source].

4. W kompensacie za powyższy zakaz Zamawiający zapewni Wykonawcy [opcje: dodatkowe wynagrodzenie 
   10% + 10 dni płatnego urlopu / ustępstwo w innym obszarze / bonus na koniec umowy].
```

**Fallback (minimum akceptowalne):**
- Skrócić okres zakozu do 12 mies. (zamiast 24).
- Wąsko zdefiniować „konkurencję" (konkretne sektory, konkretnych konkurentów — lista nazwisk).
- Dodać wyłączenia dla działalności indywidualnej, open-source.
- Oferować ekwiwalent (nawet 5% wynagrodzenia jako jednorazowy bonus).

---

## 🟡 RYZYKA ŚREDNIE

### 1. Indemnifikacja bez limitu za naruszenie IP — § 3 ust. 2
**Opis:**
```
„Wykonawca zwolni Zamawiającego z wszelkiej odpowiedzialności z tytułu roszczeń osób trzecich 
dotyczących naruszenia praw własności intelektualnej i pokryje wszelkie związane z tym koszty, 
w tym koszty obsługi prawnej"
```

Indemnity (całkowite hold-harmless) jest **poza capem** (§ 3 ust. 2 się na to wyraźnie mówi). To oznacza, że jeśli Zamawiający zostanie pozwany za naruszenie IP przez osobę trzecią (np. patent hold), Wykonawca musi pokryć całą ekspozycję — bez limitu.

**Skutek:** Nieograniczona odpowiedzialność Wykonawcy za IP, co może wielokrotnie przewyższać wartość umowy.

**Rekom.:** Dodać sufit indemnifikacji (np. „do wysokości wartości umowy" lub „do 24 mies. wynagrodzenia"). Alternatywnie, wymagać ubezpieczenia odpowiedzialności cywilnej.

---

### 2. Auto-renewal bez wyraźnego okna do sprzeciwu — § 4 ust. 1
**Opis:**
```
„Po upływie okresu z § 1 ust. 3 Umowa ulega automatycznemu przedłużeniu na kolejne okresy 12-miesięczne, 
chyba że którakolwiek ze Stron złoży oświadczenie o nieprzedłużaniu najpóźniej na 90 dni przed końcem 
bieżącego okresu"
```

Problem: 90 dni = 3 mies. dla okresu rocznego (12 mies.) — to jest racjonalne. Ale nigdzie nie ma wyjaśnienia, jak wygląda druga i trzecia odnowienie (jeśli będzie).

**Rekom.:** Dodać limit liczby odnowień (np. „maksymalnie 2 odnowienia, tj. do 4 lat łącznie") lub wyjaśnić, że strony mogą się umówić na okresy ad hoc.

---

### 3. Brak listy subprocesorów / Załącznika 2 (standardy jakości)
**Opis:** § 2 ust. 2 odnosi się do „standardów jakości kodu (wynik przeglądu poniżej progu z Załącznika nr 2)", ale Załącznik nr 2 nie został dostarczony.

**Rekom.:** Załączyć Załącznik nr 2 z konkretnymi metrykami (pokrycie testami %, liczba defektów, itp.).

---

## ✓ Obszary bez zastrzeżeń

1. **Reprezentacja stron:** (brak KRS/NIP — powinna być, ale to drobne).
2. **Poufność:** (nie wymieniona, ale wynika z natury dev).
3. **Tytuł prawny:** (umowa o dzieło / usługi — art. 22 KP nie dotyczy, bo to usługi dla biznesu).
4. **RODO:** (brak informacji, czy przetwarzane są dane osobowe — mało prawdopodobne w dev, ale warto walidować).
5. **Spory:** (prawo polskie, sąd siedziby Zamawiającego — OK).

---

## OCENA BEZPIECZEŃSTWA: 62/100

**Uzasadnienie:**
- Jedno ryzyko 🟠 wysokie (cap na 50% umowy + kary bez sufitu = ekspozycja 83% wartości).
- Trzy 🟠 wysokie (brak definicji IP, zakaz konkurencji bez ekwiwalentu, niejasna kumulacja kar).
- Jedno 🟡 średnie (indemnity bez limitu, auto-renewal).

Razem: 1 + 3 + 1 = 5 ryzyk (biorąc najpoważniejsze). Odejmując po 10 pkt za każde 🟠: 100 − 40 = 60. Plus oscylacje na podwyższeniu stawek i auto-renewal: 62.

**Werdykt:** **DO NEGOCJACJI** — wskazane poprawki w cap (do 24 mies.), sufitach kar, definicji IP, skróceniu zakozu konkurencji z 24 do 12 mies., dodaniu ekwiwalentu.

---

## Klauzule z bazy KTZR do naprawy ryzyk

🟠 RYZYKO 1 (niejasny cap na 50% umowy)
→ Zastosuj: `references/baza-klauzul/11-odpowiedzialnosc.md` — wariant T&M z capem rocznym (lub na całą umowę, w zależności od profilu).

🟠 RYZYKO 2 (kary bez sufitu + niezdefiniowane "przypadki")
→ Zastosuj: `references/baza-klauzul/10-kary-umowne.md` — model kumulacyjny z sufitem procentowym.

🟠 RYZYKO 3 (brak IP + brak gwarancji czystości)
→ Zastosuj: `references/baza-klauzul/08-prawa-autorskie-ip.md` — wariant z polami eksploatacji i gwarancją czystości GPL/AGPL.

🟠 RYZYKO 4 (zakaz konkurencji 24 mies. bez ekwiwalentu)
→ Zastosuj: `references/baza-klauzul/[niestandardowy]` — zob. sugestię fallback wyżej; standard branżowy to 12 mies. + ekwiwalent.

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
