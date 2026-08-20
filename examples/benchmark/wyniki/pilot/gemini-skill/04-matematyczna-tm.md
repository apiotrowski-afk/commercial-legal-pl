## AUDYT RYZYK — UMOWA RAMOWA T&M — ROZWÓJ OPROGRAMOWANIA

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie. Umowa zawiera ryzyka krytyczne, liczne luki i postanowienia, które czynią ją rażąco niekorzystną dla Wykonawcy i niekompletną dla Zamawiającego. Wymaga gruntownej przebudowy.

### 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
| :--- | :--- | :--- | :--- |
| Wartość umowy (szac. 24 msc) | 2 spec. x 160h/msc x 220 zł/h | 70 400 zł/msc × 24 msc | **1 689 600 PLN** |
| Cap nominalny | 12-miesięczne wynagrodzenie | 12 × 70 400 PLN | **844 800 PLN** |
| Kary poza capem (max) | 0,5% / dzień zwłoki + 5 tys. / jakość + 300 tys. / konkurencja | Kara dzienna bez limitu + kary za jakość bez limitu + 300 000 PLN | **Potencjalnie bez limitu** |
| Efektywna ekspozycja | — | Cap + kary poza capem + indemnifikacja IP | **Znacznie wyższa niż cap, potencjalnie nieograniczona** |
| Asymetria (Zamawiający vs Wykonawca) | — | Kary, indemnifikacja, jurysdykcja na korzyść Zamawiającego. Automatyczna podwyżka stawki na korzyść Wykonawcy. | **Rażąco asymetryczna na niekorzyść Wykonawcy** |
| Daty graniczne | Wypowiedzenie przedłużenia | „najpóźniej na 90 dni przed końcem bieżącego okresu” | **Długi, 3-miesięczny okres wypowiedzenia dla klauzuli automatycznego odnowienia.** |

**Wniosek z rachunku:** Nominalny limit odpowiedzialności Wykonawcy jest iluzoryczny. Kary umowne bez sufitu, wyłączone z limitu, oraz nieograniczona klauzula indemnifikacyjna w zakresie IP tworzą potencjalnie nieograniczoną ekspozycję finansową, wielokrotnie przewyższającą wartość umowy.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Nieważny lub skrajnie ryzykowny zakaz konkurencji — § 5
**Opis:** Umowa nakłada na Wykonawcę 24-miesięczny zakaz konkurencji po zakończeniu współpracy, **bez jakiegokolwiek wynagrodzenia**. Takie postanowienie w umowie cywilnoprawnej, mimo większej swobody niż w prawie pracy, jest skrajnie ryzykowne. Może zostać uznane za nieważne jako sprzeczne z zasadami współżycia społecznego (art. 353¹ w zw. z art. 58 § 2 KC [NIEZWERYFIKOWANE]) z powodu rażącej nierównowagi stron i braku ekwiwalentu za istotne ograniczenie swobody działalności gospodarczej.
**Skutek:** Dla **Wykonawcy**: ryzyko zapłaty kary 300 000 zł przy próbie podważenia klauzuli lub paraliż działalności na 2 lata. Dla **Zamawiającego**: ryzyko, że klauzula okaże się całkowicie nieskuteczna i nie będzie chronić jego interesów.
**Rekomendacja (preferowana):** Usunięcie zakazu konkurencji po zakończeniu umowy. Ochronę można zapewnić przez dobrze sformułowaną klauzulę poufności i zakaz podbierania pracowników/klientów (non-solicitation).
**Fallback (minimum akceptowalne):** Wprowadzenie odpłatności za okres zakazu (np. 25-50% wynagrodzenia), skrócenie okresu do 6-12 miesięcy i precyzyjne zdefiniowanie działalności konkurencyjnej.

### 🟠 RYZYKA WYSOKIE

#### 1. Iluzoryczny limit odpowiedzialności i agresywny reżim kar — § 2 ust. 4, § 3 ust. 2
**Opis:** Umowa wprost stanowi, że kary umowne (które nie mają górnego limitu) sumują się i nie wliczają do limitu odpowiedzialności. Dodatkowo, klauzula indemnifikacyjna dotycząca praw IP (§ 3 ust. 2) jest nieograniczona kwotowo. To sprawia, że nominalny cap w wysokości 844 800 zł jest w dużej mierze fikcją.
**Skutek:** Dla **Wykonawcy**: potencjalnie nieograniczona odpowiedzialność finansowa, która może wielokrotnie przekroczyć wartość kontraktu.
**Rekomendacja (preferowana):** Włączenie kar umownych do ogólnego limitu odpowiedzialności. Wprowadzenie limitu kwotowego (cap) również dla klauzuli indemnifikacyjnej (np. do wysokości ogólnego capu lub jego wielokrotności).
**Fallback (minimum akceptowalne):** Ustanowienie osobnego, ale rozsądnego limitu dla sumy kar umownych (np. 20-30% wartości umowy) oraz osobnego limitu dla indemnifikacji IP.

#### 2. Brak klauzuli poufności
**Opis:** Umowa nie zawiera żadnych postanowień dotyczących zachowania poufności. W projekcie dotyczącym rozwoju oprogramowania jest to fundamentalna luka, narażająca obie strony na wyciek tajemnic przedsiębiorstwa, kodu źródłowego i danych biznesowych.
**Skutek:** Dla **obu Stron**: brak umownej podstawy do ochrony informacji poufnych i dochodzenia roszczeń w przypadku ich ujawnienia.
**Rekomendacja (preferowana):** Dodanie rozbudowanej klauzuli poufności, definiującej informacje poufne, okres ochrony (także po zakończeniu umowy), dozwolone ujawnienia i karę umowną za naruszenie.

#### 3. Brak mechanizmu wypowiedzenia umowy
**Opis:** Umowa określa jedynie warunki jej automatycznego przedłużenia, ale nie przewiduje standardowej klauzuli wypowiedzenia za okresem wypowiedzenia (np. 1-3 miesiące). Strony są związane na sztywny okres 24 miesięcy. Choć art. 746 KC [NIEZWERYFIKOWANE] pozwala na wypowiedzenie zlecenia w każdym czasie, może to rodzić roszczenia odszkodowawcze.
**Skutek:** Dla **obu Stron**: brak elastyczności i "uwięzienie" w kontrakcie na 2 lata, nawet jeśli współpraca nie układa się dobrze.
**Rekomendacja (preferowana):** Wprowadzenie prawa do wypowiedzenia umowy dla każdej ze Stron z zachowaniem np. 3-miesięcznego okresu wypowiedzenia, ze skutkiem na koniec miesiąca kalendarzowego.

#### 4. Brak umowy powierzenia przetwarzania danych (RODO)
**Opis:** Umowa milczy na temat przetwarzania danych osobowych. Jest wysoce prawdopodobne, że w trakcie rozwoju oprogramowania Wykonawca będzie miał dostęp do danych osobowych (np. na środowiskach testowych), działając jako podmiot przetwarzający (procesor) dla Zamawiającego (administratora). Brak umowy powierzenia (art. 28 RODO [NIEZWERYFIKOWANE]) jest poważnym naruszeniem przepisów.
**Skutek:** Dla **obu Stron**: ryzyko wysokich kar administracyjnych nakładanych przez Prezesa UODO.
**Rekomendacja (preferowana):** Dołączenie do umowy załącznika w postaci Umowy Powierzenia Przetwarzania Danych Osobowych, spełniającej wymogi art. 28 RODO [NIEZWERYFIKOWANE].

### 🟡 RYZYKA ŚREDNIE

#### 1. Brak przeniesienia praw autorskich
**Opis:** Umowa nie reguluje kwestii przeniesienia praw autorskich do kodu i innych utworów powstałych w jej ramach. Zamawiający płaci za rozwój oprogramowania, ale nie nabywa do niego praw.
**Skutek:** Dla **Zamawiającego**: brak tytułu prawnego do dysponowania oprogramowaniem, za które zapłacił. Dla **Wykonawcy**: potencjalne spory w przyszłości.
**Rekomendacja:** Dodanie klauzuli przenoszącej majątkowe prawa autorskie na Zamawiającego z chwilą zapłaty wynagrodzenia, z wyszczególnieniem pól eksploatacji zgodnie z art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE].

#### 2. Kary umowne bez górnego limitu i nieprecyzyjne
**Opis:** Kara za zwłokę (§ 2 ust. 1) jest naliczana dziennie bez górnego pułapu, co tworzy nieograniczoną ekspozycję. Kara za naruszenie jakości (§ 2 ust. 2) jest nieprecyzyjna ("za każdy przypadek"), co może prowadzić do sporów interpretacyjnych.
**Skutek:** Dla **Wykonawcy**: ryzyko kumulacji kar do nieproporcjonalnie wysokich kwot.
**Rekomendacja:** Wprowadzenie górnego limitu dla sumy kar za zwłokę (np. 20% wynagrodzenia miesięcznego). Doprecyzowanie, co stanowi "przypadek" naruszenia jakości (np. na podstawie raportu z przeglądu kodu).

#### 3. Klauzula automatycznego odnowienia z podwyżką
**Opis:** Umowa automatycznie przedłuża się na kolejne 12 miesięcy z 8% podwyżką stawki, jeśli nie zostanie wypowiedziana z 90-dniowym wyprzedzeniem (§ 4). Długi okres wypowiedzenia zwiększa ryzyko jego przeoczenia.
**Skutek:** Dla **Zamawiającego**: ryzyko związania się na kolejny rok na wyższych warunkach finansowych. Dla **Wykonawcy**: ryzyko utraty klienta, który poczuje się "uwięziony" niekorzystnym mechanizmem.
**Rekomendacja:** Skrócenie okresu wypowiedzenia do 30-60 dni. Uzależnienie podwyżki od negocjacji lub obiektywnego wskaźnika (np. inflacji).

#### 4. Brak definicji i niekompletne dane stron
**Opis:** Umowa używa pojęć pisanych wielką literą ("Specjalista", "Przyrost") bez ich zdefiniowania. Komparycja umowy nie zawiera danych rejestrowych stron (NIP, KRS, adres) ani informacji o sposobie reprezentacji.
**Skutek:** Dla **obu Stron**: ryzyko sporów interpretacyjnych i wątpliwości co do prawidłowego zawarcia umowy.
**Rekomendacja:** Dodanie paragrafu z definicjami. Uzupełnienie pełnych danych stron i informacji o osobach upoważnionych do ich reprezentacji.

### 🟢 RYZYKA NISKIE

#### 1. Jednostronna właściwość sądu — § 6
**Opis:** Umowa wskazuje sąd właściwy dla siedziby Zamawiającego. Jest to standardowa, ale jednostronna klauzula, stawiająca Wykonawcę w nieco mniej komfortowej pozycji w razie sporu.
**Skutek:** Dla **Wykonawcy**: potencjalne niedogodności logistyczne i kosztowe w przypadku procesu sądowego.
**Rekomendacja:** Propozycja zmiany na sąd właściwy dla siedziby pozwanego (klauzula przemienna) lub sąd neutralny.

### ✓ Obszary bez zastrzeżeń

Wszystkie kluczowe obszary analizy wykazały istotne ryzyka lub fundamentalne luki. Żaden z obszarów typowych dla tego rodzaju umowy nie został uregulowany w sposób kompletny i bezpieczny dla obu stron.

---

## OCENA BEZPIECZEŃSTWA: 25/100

**Uzasadnienie:** Ocena jest skrajnie niska z powodu obecności ryzyka krytycznego (nieważny zakaz konkurencji), które może być podstawą do unieważnienia części umowy, oraz licznych ryzyk wysokich, które czynią limit odpowiedzialności iluzorycznym i pozostawiają kluczowe aspekty współpracy (poufność, IP, RODO, zasady wyjścia) całkowicie nieuregulowane. Umowa w obecnej formie jest niebezpieczna dla Wykonawcy i niepełnowartościowa dla Zamawiającego.

**Werdykt:** NIE PODPISYWAĆ

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego lub adwokata prowadzącego sprawę.*