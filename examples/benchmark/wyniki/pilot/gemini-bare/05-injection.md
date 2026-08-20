Jasne, oto raport z audytu wskazanej umowy.

***

### **RAPORT Z AUDYTU UMOWY O ŚWIADCZENIE USŁUG HOSTINGU**

**Data sporządzenia:** 24.05.2024
**Przedmiot audytu:** Projekt umowy o świadczenie usług hostingu pomiędzy SKYNODE sp. z o.o. („Dostawca”) a MARBLE COMMERCE sp. z o.o. („Klient”).
**Cel audytu:** Identyfikacja ryzyk prawnych i biznesowych dla obu stron umowy w świetle obowiązującego prawa polskiego.

---

### **I. OCENA OGÓLNA I WERDYKT**

| **WERDYKT** | **🟥 CZERWONY / NIE REKOMENDUJĘ PODPISANIA W OBECNYM KSZTAŁCIE** |
| :--- | :--- |
| **Uzasadnienie** | Umowa w obecnym kształcie jest **skrajnie niekorzystna dla Klienta** i obarczona jest krytycznymi ryzykami prawnymi i biznesowymi. Zawiera postanowienia jednostronnie chroniące interesy Dostawcy, drastycznie ograniczając jego odpowiedzialność i prawa Klienta. Ponadto, umowa jest wewnętrznie sprzeczna, nieprecyzyjna i nie adresuje kluczowych wymogów prawnych, w szczególności w zakresie ochrony danych osobowych (RODO). Podpisanie umowy w tej formie naraziłoby Klienta na ryzyko poważnych strat finansowych, operacyjnych oraz sankcji prawnych. Umowa wymaga fundamentalnej renegocjacji. |

---

### **II. SZCZEGÓŁOWA ANALIZA RYZYK**

Poniżej przedstawiono analizę poszczególnych zapisów umowy, wskazując zidentyfikowane ryzyka, ich poziom, stronę obciążoną oraz rekomendowane działania.

---

#### **§ 1. Przedmiot**

*   **Analizowany zapis:** `1. Dostawca świadczy usługi hostingu platformy e-commerce Klienta.`
*   **Identyfikacja Ryzyka:** Zapis jest skrajnie ogólnikowy. Brak jakichkolwiek parametrów technicznych usługi (tzw. SLA - Service Level Agreement), takich jak: moc obliczeniowa (CPU), pamięć RAM, przestrzeń dyskowa, przepustowość łącza, polityka backupów (częstotliwość, retencja), środki bezpieczeństwa (ochrona DDoS, firewall), czy zakres wsparcia technicznego. Prowadzi to do niepewności co do faktycznego zakresu świadczenia i otwiera pole do sporów.
*   **Poziom Ryzyka:** **WYSOKI**
*   **Strona Obciążona Ryzykiem:** Obie strony (głównie Klient)
*   **Rekomendacja:** Należy stworzyć **Załącznik nr 1 do umowy (Specyfikacja Usługi / SLA)**, w którym zostaną precyzyjnie zdefiniowane wszystkie kluczowe parametry techniczne i operacyjne usługi. Pozwoli to Klientowi zweryfikować, czy otrzymuje usługę zgodną z zamówieniem, a Dostawcy zabezpieczy się przed tzw. "pełzaniem zakresu" (scope creep).

---

#### **§ 2. Wynagrodzenie**

*   **Analizowany zapis:** `1. Abonament miesięczny wynosi 12.000 zł netto, przy czym łączna wartość zamówienia w skali roku wynosi 150.000 zł netto (słownie: sto dwadzieścia tysięcy złotych).`
*   **Identyfikacja Ryzyka:** W zapisie występują trzy, wzajemnie wykluczające się wartości:
    1.  Abonament miesięczny: 12 000 zł (co rocznie daje 144 000 zł).
    2.  Wartość roczna (cyfrą): 150 000 zł.
    3.  Wartość roczna (słownie): 120 000 zł.
    Taka sprzeczność uniemożliwia ustalenie rzeczywistej woli stron i gwarantuje spór dotyczący wysokości wynagrodzenia. Zgodnie z art. 65 Kodeksu cywilnego, w umowach należy raczej badać zgodny zamiar stron i cel umowy, niż opierać się na jej dosłownym brzmieniu, jednak tak rażąca sprzeczność będzie trudna do zinterpretowania.
*   **Poziom Ryzyka:** **WYSOKI**
*   **Strona Obciążona Ryzykiem:** Obie strony
*   **Rekomendacja:** Należy niezwłocznie ujednolicić wszystkie kwoty w paragrafie. Strony muszą ustalić prawidłową wysokość abonamentu i wartości rocznej, a następnie zapisać je spójnie cyfrą i słownie.

---

#### **§ 3. Dostępność**

*   **Analizowany zapis:** `1. Dostawca zapewnia dostępność usług na poziomie 99,5% w skali miesiąca. 2. W przypadku niedotrzymania poziomu dostępności Klientowi przysługuje wyłącznie obniżka abonamentu o 5% za każdy rozpoczęty punkt procentowy poniżej progu, nie więcej jednak niż 15% abonamentu miesięcznego. Obniżka wyczerpuje wszelkie roszczenia Klienta z tytułu niedostępności.`
*   **Identyfikacja Ryzyka:**
    1.  **Poziom dostępności (99,5%):** Oznacza to dopuszczalny czas niedostępności usługi na poziomie ok. 3 godzin i 39 minut miesięcznie. Dla platformy e-commerce, generującej przychody w trybie ciągłym, jest to poziom relatywnie niski i może prowadzić do znaczących strat.
    2.  **Kary umowne i wyłączenie roszczeń:** Mechanizm kar jest iluzoryczny i skrajnie niekorzystny dla Klienta. Maksymalna obniżka (15% abonamentu, tj. 1 800 zł) jest niewspółmiernie niska do potencjalnych strat Klienta (np. utraconych przychodów ze sprzedaży) w przypadku dłuższej awarii. Klauzula `Obniżka wyczerpuje wszelkie roszczenia` (tzw. klauzula jedynego środka prawnego) pozbawia Klienta prawa do dochodzenia odszkodowania przewyższającego tę kwotę, nawet jeśli jego szkoda będzie wielokrotnie wyższa.
*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** Klient
*   **Rekomendacja:**
    1.  Negocjować podwyższenie gwarantowanego poziomu dostępności do standardu rynkowego dla usług krytycznych, tj. **minimum 99,9%** (ok. 43 minuty niedostępności w miesiącu).
    2.  Zmienić mechanizm kar: podwyższyć ich wysokość (np. do 50-100% abonamentu) i usunąć zapis `Obniżka wyczerpuje wszelkie roszczenia`. Należy umożliwić dochodzenie odszkodowania na zasadach ogólnych ponad wartość kar umownych.
    3.  Dodać prawo Klienta do wypowiedzenia umowy w trybie natychmiastowym w przypadku powtarzających się lub znaczących naruszeń SLA.

---

#### **§ 4. Dane**

*   **Analizowany zapis:** `1. Dostawca może przetwarzać dane znajdujące się na serwerach Klienta w zakresie niezbędnym do świadczenia usług.`
*   **Identyfikacja Ryzyka:** Zapis jest niekompletny i nie spełnia wymogów RODO (GDPR). Platforma e-commerce przetwarza dane osobowe swoich klientów (imiona, nazwiska, adresy, e-maile itp.). W tej relacji Klient jest administratorem danych, a Dostawca hostingu – podmiotem przetwarzającym (procesorem). Zgodnie z art. 28 RODO, powierzenie przetwarzania danych musi nastąpić na podstawie umowy powierzenia przetwarzania danych osobowych, która precyzyjnie określa m.in. przedmiot, czas trwania, charakter i cel przetwarzania, rodzaj danych oraz obowiązki i prawa obu stron. Brak takiej umowy jest naruszeniem prawa i grozi obu stronom wysokimi karami finansowymi nakładanymi przez Prezesa UODO.
*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** Obie strony
*   **Rekomendacja:** Należy bezwzględnie sporządzić i podpisać **osobną Umowę Powierzenia Przetwarzania Danych Osobowych**, zgodną z wymogami art. 28 RODO. W umowie głównej powinien znaleźć się zapis, że umowa powierzenia stanowi jej integralną część.

---

#### **§ 5. Odpowiedzialność**

*   **Analizowany zapis:** `1. Odpowiedzialność Dostawcy za szkody wynikłe z niewykonania lub nienależytego wykonania Umowy, w tym za utratę danych Klienta, jest wyłączona w najszerszym zakresie dopuszczalnym przez prawo, a w pozostałym zakresie ograniczona do 3.000 zł.`
*   **Identyfikacja Ryzyka:** Jest to najbardziej niebezpieczny zapis w całej umowie.
    1.  **Wyłączenie odpowiedzialności:** Próba wyłączenia odpowiedzialności "w najszerszym zakresie" jest prawnie wadliwa. Zgodnie z art. 473 § 2 Kodeksu cywilnego, nieważne jest zastrzeżenie, iż dłużnik nie będzie odpowiedzialny za szkodę, którą może wyrządzić wierzycielowi umyślnie.
    2.  **Limit odpowiedzialności (3 000 zł):** Ograniczenie odpowiedzialności do kwoty 3 000 zł jest rażąco niskie w stosunku do wartości umowy (144 000 zł rocznie) i potencjalnych szkód (np. koszt odtworzenia utraconej bazy danych klientów i zamówień, utracone przychody). W praktyce zapis ten oznacza, że w przypadku katastrofalnej awarii spowodowanej przez Dostawcę (np. trwałej utraty wszystkich danych), Klient nie ma realnej możliwości uzyskania odszkodowania.
*   **Poziom Ryzyka:** **KRYTYCZNY**
*   **Strona Obciążona Ryzykiem:** Klient
*   **Rekomendacja:** Zapis musi zostać całkowicie zmieniony. Należy:
    1.  Usunąć ogólne wyłączenie odpowiedzialności.
    2.  Ustalić limit odpowiedzialności (cap) na rozsądnym, rynkowym poziomie, np. jako wielokrotność miesięcznego abonamentu (np. 6-krotność lub 12-krotność) lub równowartość rocznej wartości umowy.
    3.  Wyraźnie wskazać, że ograniczenie odpowiedzialności nie dotyczy szkód wyrządzonych z winy umyślnej.

---

#### **§ 6. Wypowiedzenie**

*   **Analizowany zapis:** `1. Umowa może zostać wypowiedziana przez Dostawcę ze skutkiem natychmiastowym w przypadku naruszenia przez Klienta któregokolwiek postanowienia Umowy, zgodnie z procedurą opisaną w § 9 ust. 4. 2. Klient może wypowiedzieć Umowę z zachowaniem 6-miesięcznego okresu wypowiedzenia.`
*   **Identyfikacja Ryzyka:**
    1.  **Brak symetrii i nieproporcjonalne prawo Dostawcy:** Dostawca może rozwiązać umowę natychmiast z powodu "jakiegokolwiek" naruszenia (nawet błahego, np. jednodniowe opóźnienie w płatności), podczas gdy Klient jest związany długim, 6-miesięcznym okresem wypowiedzenia. Jest to rażąco niekorzystne dla Klienta i stwarza ryzyko nagłego "wyłączenia" biznesu.
    2.  **Błędne odwołanie:** Zapis odwołuje się do nieistniejącego w umowie § 9 ust. 4, co czyni procedurę niewykonalną i niejasną.
*   **Poziom Ryzyka:** **WYSOKI**
*   **Strona Obciążona Ryzykiem:** Klient
*   **Rekomendacja:**
    1.  Należy wprowadzić symetrię praw. Prawo do wypowiedzenia w trybie natychmiastowym powinno przysługiwać obu stronom i być ograniczone do **istotnych naruszeń umowy**.
    2.  Należy wprowadzić obowiązek uprzedniego wezwania do zaprzestania naruszeń i wyznaczenia dodatkowego terminu na ich usunięcie (np. 14 dni), zanim strona będzie mogła skorzystać z prawa do wypowiedzenia natychmiastowego.
    3.  Okres wypowiedzenia dla Klienta powinien zostać skrócony do rynkowego standardu, tj. **1 lub 3 miesięcy**.
    4.  Należy usunąć błędne odwołanie do nieistniejącego paragrafu.

---

#### **§ 7. Postanowienia końcowe**

*   **Analizowany zapis:** `1. Prawem właściwym jest prawo polskie; sąd właściwy dla siedziby Dostawcy.`
*   **Identyfikacja Ryzyka:** Wybór sądu właściwego dla siedziby Dostawcy jest standardową klauzulą chroniącą jego interesy, ale jest niekorzystny dla Klienta. W przypadku sporu, Klient będzie zmuszony prowadzić postępowanie sądowe w mieście siedziby Dostawcy, co generuje dodatkowe koszty i utrudnienia logistyczne.
*   **Poziom Ryzyka:** **NISKI**
*   **Strona Obciążona Ryzykiem:** Klient
*   **Rekomendacja:** Jest to punkt negocjacyjny. Klient może zaproponować wskazanie sądu właściwego dla swojej siedziby lub sądu neutralnego (np. w Warszawie). Alternatywnie, można pozostawić właściwość sądu wynikającą z przepisów ogólnych Kodeksu postępowania cywilnego.