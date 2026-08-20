# AUDYT RYZYK — NDA Wzajemne (HELIX SOFT / BALTIC CAPITAL)

> **WERDYKT: 🟥 CZERWONY** — Umowa zawiera rażące naruszenia norm bezwzględnych (pozorna wzajemność przy karach) i otwarte ekspozycje finansowe. Wymaga gruntownej negocjacji przed podpisem.

## 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | brak (NDA ramowa) | — | [BRAK DANYCH] |
| Kara za naruszenie | 200.000 zł / naruszenie | brak sufitu, pojęcie "naruszenie" niezdefiniowane | [OTWARTA] |
| Liczba możliwych kar | brak limitu | każde "naruszenie" = 1 kara | potencjalnie wielokrotne |
| Efektywna ekspozycja | — | min. 200.000 zł za 1 ujawnienie, bez sufitu | **[NIEOGRANICZONA]** |
| Asymetria kar | art. § 3 ust. 2 | Strona A: 200k zł · Strona B: 0 zł | **1:0 (rażąca)** |
| Okres poufności | brak danych | poufność tylko "podczas negocjacji" | [BRAK DANYCH] — potencjalnie 0 dni po umowie |

**Wniosek z rachunku:** Brak sufitu kary przy nieokreślonej definicji "naruszenia" stwarza ekspozycję finansową nieznaną i potencjalnie otwartą. Asymetria kar (tylko strona otrzymująca płaci) może być uznana za sprzeczną z zasadami współżycia (art. 3531 KC).

---

## 🔴 RYZYKA KRYTYCZNE

### 1. Pozorna wzajemność + asymetryczne kary — § 1, § 3
**Opis:** § 1 ust. 1 deklaruje „Strony wzajemnie zobowiązują się", lecz § 3 ust. 2 wyłącza Stronę Ujawniającą z kar umownych całkowicie. Rzeczywiste zobowiązania i sankcje obciążają wyłącznie Stronę Otrzymującą. To narusza zasadę symetrii umowy B2B.

**Skutek:** 
- Klauzula może być uznana za sprzeczną z zasadami współżycia społecznego (art. 3531 KC).
- Strona Otrzymująca (Baltic Capital) ponosi całe ryzyko finansowe, Strona Ujawniająca (Helix Soft) żadne.
- W praktyce: jeśli Helix ujawni tajemnice Baltic Capital, Baltic nie ma regresu.

**Rekomendacja (preferowana):** Obie Strony powinny ponosić karę umowną za naruszenie poufności — symetryczne kwoty lub przynajmniej wymienić powody asymetrii.

**Fallback (minimum akceptowalne):** Jeśli strony zaakceptują asymetrię, zastrzec wyraźnie (np. „Strona Ujawniająca ponosi karę X zł, Strona Otrzymująca karę 200.000 zł") zamiast milczącej asymetrii.

---

### 2. Nieokreślona definicja „naruszenia" + brak sufitu kary — § 3 ust. 1
**Opis:** Kara 200.000 zł przysługuje za „każde naruszenie obowiązku poufności", lecz:
- Pojęcie „naruszenie" nie jest definiowane (pojedyncze ujawnienie? wiele ujawnień? każda osoba, której przekazano tajemnicę?).
- Brak maksymalnej liczby kar ani sufitu łącznej wysokości.
- Logika: 1 pracownik zarabia 220 zł/h (wg umowy 04), a pojedyncze „naruszenie" kosztuje 200.000 zł — dysproporcja.

**Skutek:**
- Ekspozycja finansowa Strony Otrzymującej potencjalnie wielokrotnie przewyższa wartość transakcji.
- Brak precyzji „naruszenia" rodzi spór interpretacyjny (sąd będzie musiał decydować, co zalicza się do naruszenia).
- Potencjalna nieważność kary jako rażąco wygórowanej (art. 484 § 2 KC — miarkowanie).

**Rekomendacja (preferowana):** 
```
„Kara umowna wynosi 200.000 zł za każde ujawnienie Informacji Poufnych osobie trzeciej bez uprzedniej zgody Strony Ujawniającej, łącznie nie więcej niż 10% szacowanej wartości negocjacji [XYZ zł]. Dla uniknięcia wątpliwości, każdorazowe ujawnienie temu samemu podmiotowi liczy się oddzielnie, lecz kara od tego samego naruszenia obliczana jest raz."
```

**Fallback (minimum akceptowalne):** Określić, co liczy się za „naruszenie" (np. „każde ujawnienie niezauthentycznym osobom" lub „każdy dzień braku ochrony ponad 48 godzin") + ustalić sufit kary (np. 600.000 zł = 3 × kara bazowa).

---

### 3. Brak warunków zakończenia umowy i okresu poufności — § 4, § 2 ust. 4
**Opis:** § 4 mówi „Umowa obowiązuje przez okres prowadzenia Negocjacji", ale:
- Negocjacje mogą trwać miesiące lub latami — brak konkretnej daty.
- Brak wyraźnego warunku zakończenia („podpisanie umowy", „brak zgody po X dniach", itp.).
- Brak okresu poufności PO zakończeniu negocjacji — teoretycznie Informacje Poufne mogą być ujawnione dzień po zakończeniu umowy.
- § 2 ust. 4 odnosi się do „Materiałów Roboczych" bez definicji i bez okresu zwrotu/niszczenia.

**Skutek:**
- Informacje mogą przestać być chronione w momencie podpisania, brak ochrony po negocjacjach.
- Niejasna procedura wznowienia / wstrzymania obowiązków.
- Brak pewności, czy zwrócone materiały zostały całkowicie usunięte.

**Rekomendacja (preferowana):**
```
§ 4a. Okres poufności
1. Umowa obowiązuje przez okres prowadzenia Negocjacji, jednak nie mniej niż [6 miesięcy od podpisania].
2. Obowiązek zachowania poufności Informacji Poufnych trwa:
   - 3 lata od daty ujawnienia dla informacji handlowych i technicznych;
   - bezterminowo dla tajemnic przedsiębiorstwa (wg art. 11 USTAT).

§ 2 ust. 4a (Materiały Robocze)
Definiujemy Materiały Robocze jako [wskaż konkretnie: notes, druki, prototypy, kod...].
Na żądanie Strony Ujawniającej, Strona Otrzymująca niezwłocznie (w ciągu 5 Dni Roboczych) zwróci 
lub zniszczy Materiały Robocze i poświadczy pisemnie dokonanie zniszczenia.
```

**Fallback (minimum akceptowalne):** Ustalić okresy: 
- minimum 90 dni wykonywania umowy; 
- poufność 1 rok po zakończeniu dla informacji ogólnych; 
- poufność bezterminowa dla tajemnic przedsiębiorstwa.

---

## 🟠 RYZYKA WYSOKIE

### 1. Asymetryczne forum sądowe — § 5 ust. 2
**Opis:** „Sądem właściwym jest sąd siedziby Strony Ujawniającej" = zawsze sąd siedziby Helix Soft (Gdynia). Baltic Capital zawsze będzie pozwaną na terenie Gdyni, niezależnie czy jest pozwaną czy powodą.

**Skutek:** 
- Rażąca asymetria: Helix Soft zawsze sądzi w domu, Baltic Capital zawsze musi przyjechać.
- Wyższa ekspozycja kosztowa dla Baltic Capital.
- Ryzyko: sąd lokalny może być mniej familiarny z przynależną Zamawiającemu praktyką biznesu.

**Rekomendacja (preferowana):** 
```
Sądem właściwym jest sąd siedziby Strony pozwanej (ius defensionis), 
alternatywnie: mediacja [przed sądem], sąd Warszawy jako kompromis.
```

**Fallback (minimum akceptowalne):** Sąd siedziby drugiej strony przy jej pozwie; sąd siedziby Helix tylko gdy Helix będzie powodą (symetryczne).

---

### 2. „Dołoży starań" zamiast obowiązku rezultatu — § 2 ust. 2
**Opis:** Strona Otrzymująca „dołoży starań, aby zabezpieczyć Informacje Poufne" — to zobowiązanie do starannego działania, nie do wyniku. Oznacza, że:
- Strona Otrzymująca nie odpowiada za faktyczne ujawnienie, jeśli „starała się" (np. miała hasło, ale pracownik je noty wpisał).
- Trudniej dochodzić niewykonania.

**Skutek:** Ograniczona praktyczna ochrona tajemnic (odpowiedzialność na zasadzie „czy starał się", nie „czy chronił").

**Rekomendacja (preferowana):**
```
„zobowiązuje się utrzymywać Informacje Poufne pod kluczem, z dostępem ograniczonym do personelu 
mającego uzasadnioną potrzebę dostępu i zaznajomionego z niniejszą Umową"
```
(Zobowiązanie rezultatu + konkretne środki).

**Fallback (minimum akceptowalne):** Rozszerzyć na „dołoży należytych starań, w tym [wdrożenie szyfrowania / kontrola dostępu / umowy NDA z pracownikami]".

---

### 3. Brak wyłączeń z poufności — § 1 ust. 2
**Opis:** Definicja Informacji Poufnych = „wszelkie informacje przekazane" — brak wyłączeń dla:
- Informacji publicznych z powszechnie dostępnych źródeł.
- Informacji już posiadanych przez Stronę Otrzymującą przed ujawnieniem.
- Informacji niezależnie opracowanych bez użycia tajemnic.
- Informacji wymaganych do ujawnienia przez prawo (np. CEIDG, UOKIK).

**Skutek:** Nawet informacja, która stała się publiczna lub była wcześniej znana, pozostaje chroniona bez uzasadnienia.

**Rekomendacja (preferowana):**
```
Informacje Poufne nie obejmują informacji:
a) publicznych ze źródeł niezależnych od Strony Otrzymującej,
b) posiadane przez Stronę Otrzymującą przed ujawnieniem (z dokumentacją),
c) opracowane niezależnie bez użycia Informacji Poufnych,
d) których ujawnienia wymaga prawo (z powiadomieniem Strony Ujawniającej).
```

**Fallback (minimum akceptowalne):** Wymienić przynajmniej kategorię (a) i (d).

---

## 🟡 RYZYKA ŚREDNIE

### 1. Termin „niezwłocznie" bez precyzji — § 2 ust. 3
**Opis:** „Strona Otrzymująca niezwłocznie poinformuje Stronę Ujawniającą o każdym przypadku ujawnienia" — brak liczby dni.

**Skutek:** Spór, czy 24 godziny, 48 godzin czy 5 dni to „niezwłocznie".

**Rekomendacja:** Określić „w terminie 24 godzin" lub „niezwłocznie, jednak nie później niż 24 godziny od stwierdzenia ujawnienia".

---

### 2. Nieokreślona definicja „Materiałów Roboczych" — § 2 ust. 4
**Opis:** Klauzula odnosi się do zwrotu „Materiałów Roboczych" bez ich zdefiniowania wcześniej.

**Skutek:** Spór, co zalicza się do materiałów (notatki elektroniczne? wersje robocze? backup?).

**Rekomendacja:** Dodać do § 1 „Definicje": „Materiały Robocze — wszelkie dokumenty, notatki, prototypy i kopie zawierające lub odzwierciedlające Informacje Poufne, w formie papierowej, elektronicznej lub innej."

---

### 3. Krótki okres działania umowy
**Opis:** Umowa obowiązuje tylko „przez okres prowadzenia Negocjacji", co może być kilka tygodni. Po jej zakończeniu — brak ochrony poufności.

**Skutek:** Niska praktyczna wartość jako umowa długoterminowa.

**Rekomendacja:** Określić minimalny okres (np. 6 miesięcy lub do momentu podpisania umowy głównej).

---

## 🟢 RYZYKA NISKIE

### 1. Brak identyfikacji stron — NIP / KRS
**Opis:** Umowa nie zawiera numerów KRS ani NIP obydwu podmiotów, co utrudnia weryfikację uprawnienia podpisujących.

**Rekom.:** Dodać do preambułu: „…o NIP: [XX-XXX-XXX-XXX], reprezentowana przez…" i wskaźnik KRS dla każdej spółki.

---

## ✓ Obszary bez zastrzeżeń

- **Prawa autorskie:** N/A (NDA, brak przetwarzania praw)
- **RODO:** N/A (brak ujęcia przetwarzania danych; umowa nie powierrza danych jako procesor)
- **Tytuł prawny / przekwalifikowanie:** N/A (usługi niematerialne, brak ryzyka prekaryzacji)

---

## OCENA BEZPIECZEŃSTWA: 28/100

**Uzasadnienie:** Umowa zawiera jedno naruszenie normy bezwzględnej (pozorna wzajemność przy karach, potencjalnie sprzeczne z art. 3531 KC), trzy ryzyka krytyczne (nieokreślona ekspozycja na kary, asymetryczne forum, brak okresu po umowie) i trzy wysokie. Brak sufitu kar + otwarta definicja „naruszenia" stwarzają ekspozycję finansową nieznaną. Umowa wymaga gruntownej przeróbki przed podpisem.

**Werdykt:** **NIE PODPISYWAĆ** — wymaga negocjacji punktów krytycznych (symetryzacja kar, sufit kary, określenie „naruszenia", okres poufności po umowie, forum).

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
