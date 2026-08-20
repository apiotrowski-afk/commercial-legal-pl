**RAPORT Z AUDYTU UMOWY RAMOWEJ T&M — ROZWÓJ OPROGRAMOWANIA**

**Data audytu:** 24.05.2024 r.
**Przedmiot audytu:** Projekt Umowy Ramowej T&M pomiędzy QUANTA DEV sp. z o.o. a MERIDIAN FINANCE S.A.
**Cel audytu:** Identyfikacja ryzyk prawnych i biznesowych dla obu Stron w oparciu o przepisy prawa polskiego.

---

### **I. OGÓLNA OCENA I WERDYKT**

Przedstawiony projekt Umowy jest dokumentem szczątkowym, obarczonym **krytycznymi wadami prawnymi i logicznymi**. W obecnej formie Umowa jest **skrajnie niekorzystna dla Wykonawcy** i generuje **bardzo wysokie ryzyko sporów** ze względu na wewnętrzne sprzeczności oraz brak kluczowych postanowień standardowych dla umów IT.

**Werdykt:** Umowa w obecnym kształcie **nie nadaje się do zawarcia**. Wymaga fundamentalnej przebudowy i uzupełnienia. Jej podpisanie przez Wykonawcę bez istotnych zmian byłoby nieracjonalne biznesowo i prawnie. Zamawiający również ponosi ryzyko, gdyż wiele postanowień może okazać się w praktyce niewykonalnych lub nieważnych, co podważa jego poczucie bezpieczeństwa.

---

### **II. ANALIZA SZCZEGÓŁOWA RYZYK**

#### **1. Niespójność modelu współpracy (T&M vs. Fixed Price)**

*   **Zidentyfikowane Ryzyko:** Umowa deklaruje model Time & Material (§ 1 ust. 1), który polega na rozliczaniu za poświęcony czas i staranne działanie. Jednocześnie wprowadza kary umowne za "zwłokę w dostarczeniu Przyrostu względem harmonogramu sprintu" (§ 2 ust. 1), co jest cechą umów rezultatu (np. Fixed Price, umowa o dzieło). Powstaje fundamentalna sprzeczność: czy Wykonawca ma dostarczać czas pracy, czy konkretny, terminowy rezultat?
*   **Poziom Ryzyka:** **KRYTYCZNE**
*   **Strona Obciążona Ryzykiem:** Obie Strony.
    *   **Wykonawca:** Może być karany za opóźnienia, na które nie miał wpływu (np. zmiana wymagań przez Zamawiającego, błędy w specyfikacji, brak dostępności zasobów po stronie Zamawiającego), co jest sprzeczne z duchem T&M.
    *   **Zamawiający:** Ma fałszywe poczucie kontroli nad terminowością, podczas gdy model T&M z natury nie gwarantuje dostarczenia określonego zakresu w sztywnym terminie i budżecie.
*   **Rekomendacja:**
    1.  **Wariant 1 (Utrzymanie T&M):** Usunąć § 2 ust. 1. Zamiast kar, wprowadzić mechanizmy monitorowania efektywności i eskalacji problemów. Zobowiązanie Wykonawcy powinno dotyczyć świadczenia usług z należytą starannością przez określoną liczbę godzin.
    2.  **Wariant 2 (Model Hybrydowy):** Precyzyjnie zdefiniować, czym jest "Przyrost", "harmonogram sprintu" oraz określić procedurę akceptacji. Należy jasno wskazać, że harmonogram jest estymacją, a jego niedotrzymanie może skutkować karą tylko w przypadku zawinionej przez Wykonawcę zwłoki, przy jednoczesnym braku przeszkód po stronie Zamawiającego. Jest to rozwiązanie skomplikowane i wymagające bardzo precyzyjnych zapisów.

#### **2. Kary umowne – konstrukcja i wysokość**

*   **Zidentyfikowane Ryzyko:** Postanowienia o karach umownych (§ 2) są jednostronne, nieprecyzyjne i potencjalnie nieważne lub podlegające miarkowaniu przez sąd.
    *   **§ 2 ust. 1 (Zwłoka):** Podstawa naliczenia kary ("wynagrodzenie miesięczne") jest niejasna. Czy chodzi o szacunkowe wynagrodzenie (70 400 zł netto), czy faktycznie zafakturowane?
    *   **§ 2 ust. 2 (Jakość kodu):** Klauzula jest niewykonalna z powodu braku Załącznika nr 2. Nawet gdyby istniał, kara w stałej kwocie 5 000 zł za "każdy przypadek" jest nieproporcjonalna i może być łatwo nadużywana.
    *   **§ 2 ust. 4 (Sumowanie i odszkodowanie):** Zapis o sumowaniu kar, wyłączeniu ich z limitu odpowiedzialności oraz możliwości dochodzenia odszkodowania przewyższającego jest **skrajnie niekorzystny**. W praktyce unieważnia on limit odpowiedzialności z § 3, tworząc dla Wykonawcy nieograniczone ryzyko finansowe.
*   **Poziom Ryzyka:** **KRYTYCZNE**
*   **Strona Obciążona Ryzykiem:** Wykonawca.
*   **Rekomendacja:**
    1.  Usunąć lub gruntownie przeredagować § 2 ust. 1 i 2.
    2.  W § 2 ust. 4 **bezwzględnie** usunąć zapis o wyłączeniu kar z limitu odpowiedzialności.
    3.  Wprowadzić zapis, że kary umowne stanowią wyłączny środek prawny Zamawiającego z tytułu danego naruszenia (wyczerpują roszczenia).
    4.  Ograniczyć możliwość dochodzenia odszkodowania przewyższającego kary umowne tylko do przypadków winy umyślnej Wykonawcy.
    5.  Wprowadzić łączny, maksymalny pułap wszystkich kar umownych w danym okresie rozliczeniowym (np. 15% wynagrodzenia za dany miesiąc) oraz w całej umowie.

#### **3. Zakaz konkurencji**

*   **Zidentyfikowane Ryzyko:** Zakaz konkurencji (§ 5) jest sformułowany w sposób wadliwy i restrykcyjny. Jest nieprecyzyjny ("działalność konkurencyjna" nie jest zdefiniowana), ma bardzo długi okres obowiązywania po zakończeniu umowy (24 miesiące) i nie przewiduje żadnego ekwiwalentu pieniężnego. W sporze sądowym istnieje wysokie prawdopodobieństwo uznania go za nieważny jako sprzeczny z zasadami współżycia społecznego (art. 58 w zw. z art. 353¹ Kodeksu cywilnego) lub rażąco naruszający interesy Wykonawcy.
*   **Poziom Ryzyka:** **KRYTYCZNE**
*   **Strona Obciążona Ryzykiem:** Wykonawca (ryzyko paraliżu działalności), Zamawiający (ryzyko nieważności klauzuli).
*   **Rekomendacja:**
    1.  **Najlepsza opcja:** Usunąć całkowicie zakaz konkurencji i zastąpić go precyzyjną klauzulą o zakazie podbierania pracowników (non-solicitation) i klientów Zamawiającego, z którymi Wykonawca miał bezpośredni kontakt w ramach realizacji Umowy.
    2.  **Opcja alternatywna:** Drastycznie ograniczyć zakres zakazu:
        *   Precyzyjnie zdefiniować działalność konkurencyjną (np. poprzez wskazanie konkretnych produktów, usług lub wymienienie z nazwy kluczowych konkurentów).
        *   Skrócić okres obowiązywania po zakończeniu umowy do maksymalnie 6-12 miesięcy.
        *   Wprowadzić odpłatność za okres obowiązywania zakazu po ustaniu umowy, co znacząco zwiększa jego szanse na utrzymanie się w mocy.

#### **4. Odpowiedzialność i gwarancje**

*   **Zidentyfikowane Ryzyko:** Klauzula indemnifikacyjna dotycząca praw własności intelektualnej (§ 3 ust. 2) jest nieograniczona. Zwalnia Zamawiającego z "wszelkiej odpowiedzialności" i nakazuje pokrycie "wszelkich kosztów", co tworzy nielimitowane i nieprzewidywalne ryzyko dla Wykonawcy, wykraczające poza ogólny limit odpowiedzialności z § 3 ust. 1.
*   **Poziom Ryzyka:** **KRYTYCZNE**
*   **Strona Obciążona Ryzykiem:** Wykonawca.
*   **Rekomendacja:**
    1.  Należy jednoznacznie podporządkować odpowiedzialność z tytułu naruszeń IP ogólnemu limitowi odpowiedzialności z § 3 ust. 1.
    2.  Dodać obowiązki Zamawiającego: niezwłoczne poinformowanie o roszczeniu, przekazanie Wykonawcy kontroli nad obroną w sporze i współpraca w tym zakresie.
    3.  Ograniczyć odpowiedzialność Wykonawcy do oprogramowania dostarczonego wyłącznie przez niego (z wyłączeniem komponentów open source użytych zgodnie z licencją, materiałów dostarczonych przez Zamawiającego itp.).

#### **5. Okres obowiązywania i waloryzacja**

*   **Zidentyfikowane Ryzyko:** Automatyczne przedłużenie umowy na 12 miesięcy z długim, 90-dniowym terminem na złożenie oświadczenia o nieprzedłużaniu (§ 4 ust. 1) może być pułapką dla Strony, która zapomni o terminie. Jednocześnie automatyczna waloryzacja stawki o 8% (§ 4 ust. 2) jest korzystna dla Wykonawcy, ale może być nieakceptowalna dla Zamawiającego.
*   **Poziom Ryzyka:** **ŚREDNIE**
*   **Strona Obciążona Ryzykiem:** Obie Strony (ryzyko niechcianego przedłużenia), Zamawiający (ryzyko automatycznej podwyżki).
*   **Rekomendacja:**
    *   Skrócić termin na złożenie oświadczenia o nieprzedłużaniu do 30 lub 60 dni.
    *   Zamawiający powinien negocjować mechanizm waloryzacji, np. uzależniając go od wskaźnika inflacji GUS lub poddając go corocznym negocjacjom.

---

### **III. BRAKUJĄCE KLAUZULE O KLUCZOWYM ZNACZENIU**

Umowa pomija szereg postanowień niezbędnych dla prawidłowego i bezpiecznego wykonania kontraktu IT. Ich brak jest samodzielnym, **krytycznym ryzykiem**.

1.  **Prawa Własności Intelektualnej (IPR):** Brak jakichkolwiek zapisów o tym, kto jest właścicielem wytworzonego oprogramowania i na jakich warunkach następuje przeniesienie autorskich praw majątkowych lub udzielenie licencji. **To fundamentalny błąd.**
2.  **Poufność (NDA):** Brak klauzuli o zachowaniu poufności, która jest standardem w każdej umowie biznesowej, a zwłaszcza w sektorze IT i finansów.
3.  **Procedury Odbioru i Testów:** Brak opisu, w jaki sposób Zamawiający ma weryfikować i akceptować wykonane prace. Generuje to ogromne pole do sporów.
4.  **Obowiązki Zamawiającego:** Brak sprecyzowania, co Zamawiający musi zapewnić, aby Wykonawca mógł świadczyć usługi (np. dostęp do systemów, dokumentacji, dedykowana osoba do kontaktu/Product Owner).
5.  **Warunki Płatności:** Brak terminu płatności faktur i konsekwencji jego niedotrzymania (np. odsetki za opóźnienie w transakcjach handlowych).
6.  **Zasady Zmiany i Wymiany Personelu:** Brak procedur dotyczących kluczowych specjalistów, ich ewentualnej wymiany i okresu wdrożenia nowych osób.
7.  **Rozwiązanie Umowy:** Brak możliwości wypowiedzenia umowy za porozumieniem stron, z zachowaniem okresu wypowiedzenia (np. 1-3 miesiące) oraz w trybie natychmiastowym z powodu rażącego naruszenia postanowień.
8.  **Przetwarzanie Danych Osobowych (RODO/GDPR):** Jeśli w ramach prac Wykonawca będzie miał dostęp do danych osobowych, umowa musi zawierać lub odsyłać do odrębnej Umowy Powierzenia Przetwarzania Danych, której brak jest naruszeniem prawa.
9.  **Definicje:** Brak słowniczka kluczowych pojęć (np. "Przyrost", "Sprint", "Dzień Roboczy"), co prowadzi do niejasności interpretacyjnych.