# AUDYT RYZYK — Umowa Wdrożeniowa ERP (NOVA RETAIL / CODEX WORKS)

> **WERDYKT: 🟥 CZERWONY** — Umowa zawiera co najmniej cztery naruszenia norm bezwzględnie obowiązujących (ius cogens) oraz rażące asymetrie uprawnień. Nie podpisywać bez gruntownej przeróbki.

## 🧮 Rachunek ekspozycji

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł | — | 480.000 zł |
| Cap nominalny | brak | — | [BRAK CAPU] |
| Kary za opóźnienie płatności | 50.000 zł / dzień | 50k × 30 dni = 1.500.000 zł | **312% wartości umowy** |
| Maksymalna kara umowna | brak sufitu | potencjalnie nieograniczona | [OTWARTA] |
| Efektywna ekspozycja | — | brak capu + kary otwarte + brak gwarancji rezultatu | **[NIEOGRANICZONA]** |
| Asymetria kar | § 3 ust. 2 + § 5 ust. 2 | Zamawiający: 50k/dzień · Wykonawca: 0 zł | **1:0** |
| Termin płatności | 60 dni od faktury | zakres ustawy o zatorach (B2B limit 60 dni) | 60 dni OK, ale za karę naruszenie |

**Wniosek z rachunku:** Brak capu odpowiedzialności + brak sufitu kar = ekspozycja otwarta. Kara za opóźnienie płatności (50k/dzień) wielokrotnie przewyższa normalny koszt wdrożenia i narusza normę ius cogens (art. 483 § 1 KC). Asymetria kar = 1:0.

---

## 🔴 RYZYKA KRYTYCZNE

### 1. Kara umowna za opóźnienie w zapłacie narusza art. 483 § 1 KC — § 3 ust. 2
**Opis:** 
```
„Zamawiający zapłaci karę umowną 50.000 zł za każdy dzień opóźnienia w płatności"
```
Art. 483 § 1 KC zabrania kary umownej za zobowiązanie **pieniężne** (czytaj: zapłatę kwoty). Za zobowiązanie pieniężne należą się **odsetki ustawowe** (art. 359 KC i dalsze), nie kara umowna. Ponieważ zobowiązanie do zapłaty faktury to zobowiązanie pieniężne, kara za jego opóźnienie jest **nieważna z mocy prawa**.

**Skutek:**
- Klauzula karą jest **nieważna** (art. 58 § 1 KC) — Zamawiający nie jest związany tą karą.
- Jednak Wykonawca może dochodzić odsetek ustawowych zamiast kary (art. 359 KC i inne).
- Umowa zawiera niezawinioną przez strony nieważność postanowienia.

**Rekomendacja (preferowana):** Usunąć. Odsetek ustawowe obowiązują z mocy prawa.

**Fallback (minimum akceptowalne):** Jeśli strony chcą „kary", to nie za sam fakt opóźnienia płatności, a za **niedotrzymanie terminu płatności rozliczenia końcowego** (rozróżnić: rata za etap ≠ rozliczenie końcowe). Wtedy może być „kara za niedotrzymanie sprawozdania" lub „za zwłokę w przesłaniu dokumentów do rozliczenia", ale nie za sam fakt opóźnienia zapłaty.

---

### 2. Przeniesienie praw autorskich bez pól eksploatacji — art. 41 ust. 2 PrAut — § 4 ust. 1
**Opis:**
```
„Z chwilą zapłaty Wykonawca przenosi na Zamawiającego wszelkie prawa autorskie 
do stworzonego oprogramowania bez ograniczeń"
```
Art. 41 ust. 2 PrAut wymaga, aby przeniesienie praw był wyraźnie wskazane **pola eksploatacji** (np. publikacja, rozpowszechnianie, przeróbki, prawo do wynajęcia, prawo do wyświetlania publicznego). Zapis „bez ograniczeń" **nie zastępuje** wymogów wskazania pól — to jest pominięcie wymogów ustawowych. Art. 41 ust. 4 PrAut zakazuje przeniesienia pól nieznanych w chwili zawarcia.

**Skutek:**
- Przeniesienie praw w obrębie pól **nieznanych w chwili zawarcia** jest **nieważne**.
- Zamawiający ma niepewność, czy rzeczywiście nabywa prawo do używania kodu.
- Ryzyko: Wykonawca później może twierdzić, że prawo do „SaaS" czy „wynajmu na chmurze" nie zostały przesłane (bo były nieznane).

**Rekomendacja (preferowana):**
```
§ 4 ust. 1 (zmieniony)
Wykonawca przenosi na Zamawiającego następujące pola eksploatacji autorskich 
praw majątkowych do Oprogramowania:
a) prawo do wielokrotnego powielania (w tym backup, archiwizacja),
b) prawo do rozpowszechniania (w tym instalacja, hostowanie na serwerach Zamawiającego),
c) prawo do publicznego wyświetlania i użytku publicznego,
d) prawo do przeróbek i adaptacji,
e) prawo do wydzierżawiania / wynajęcia [jeśli dotyczy].

Przeniesienie jest bezterminowe i obejmuje prawo do wykonywania pól przez podwykonawców 
i pracowników Zamawiającego.

Zamawiający nie nabywa prawa do: [jeśli dotyczy — wyłączenia Wykonawcy, np. generyczne 
komponenty, licencje open-source z tymi samymi warunkami dla trzecich].
```

**Fallback (minimum akceptowalne):** Wymienić conajmniej pola (a) i (b) jawnie; dodać: „rozumie się, że pola eksploatacji są rozumieniami na dzień zawarcia i obejmują użytki znane w branży IT".

---

### 3. Naruszenie RODO art. 28 — prawo do trenowania AI na danych Zamawiającego — § 8
**Opis:**
```
„Niezależnie od pozostałych postanowień Umowy, Wykonawca zachowuje prawo 
do wykorzystania danych Zamawiającego do trenowania modeli AI"
```
Jeśli dane Zamawiającego zawierają dane osobowe (np. dane klientów, pracowników, kontrahentów), to rozpoczęcie przetwarzania bez umowy art. 28 RODO (jeśli relacja to administrator-procesor) lub bez wyraźnej zgody administratora (jeśli odrębni administratorzy) narusza RODO. Klauzula narzuca zgodę pomimo woli Zamawiającego, co jest niedopuszczalne.

**Skutek:**
- Naruszenie art. 28 RODO (brak umowy o powierzeniu przetwarzania z wymaganymi gwarancjami).
- Naruszenie art. 6 RODO (brak podstawy prawnej do przetwarzania).
- Sankcja: kara do 20 mln EUR lub 4% światowego przychodu (art. 83 ust. 4 RODO).
- Roszczenie osób, których dane są przetwarzane.

**Rekomendacja (preferowana):** Usunąć całkowicie. Jeśli Wykonawca chce trenować modele, to na **anonimizowanych** danych (nie zawierających danych osobowych) lub na oddzielnych, nieidentyfikowalnych zbiorach.

**Fallback (minimum akceptowalne):** Jeśli dane to dane biznesowe (nie zawierają danych osobowych), to wymienić jawnie: „danymi Zamawiającego rozumie się wyłącznie dane niebędące danymi osobowymi w rozumieniu RODO, takie jak [wymienić konkretnie]". Dodać: „Wykonawca nie trenuje modeli na danych osobowych bez wyraźnej zgody każdej osoby, której dane dotyczą".

---

### 4. Asymetryczne prawo do wypowiedzenia — § 7 ust. 1 i 2
**Opis:**
```
§ 7 ust. 1: Zamawiający nie może wypowiedzieć Umowy przed zakończeniem Wdrożenia
§ 7 ust. 2: Wykonawca może wypowiedzieć Umowę w każdym czasie i bez podania przyczyny
```
Asymetria jest rażąca: Zamawiający uwięziony do końca wdrożenia (ryzyka: przeterminowanie, brak rezultatów, koszt skaluje się), Wykonawca ma drzwi wyjściowe otwarte 24/7.

**Skutek:**
- Ryzyko: Wykonawca opuszcza projekt w połowie realizacji — Zamawiający musi szukać nowego Wykonawcy, a Umowa nie pozwala się wycofać.
- Brak procedury exit (zwrot źródeł, dokumentacji, danych).
- Asymetria może być uznana za sprzeczną z zasadami współżycia (art. 3531 KC).

**Rekomendacja (preferowana):**
```
§ 7 (zmieniony)
1. Każda ze Stron może wypowiedzieć Umowę z zachowaniem 30 dni okresu wypowiedzenia, 
   ze skutkiem na koniec miesiąca kalendarzowego.
2. W przypadku wypowiedzenia Wykonawca zobowiązany jest do:
   a) zwrotu lub dostarczenia całości kodu źródłowego, dokumentacji i danych,
   b) wsparcia przejścia na nowego dostawcę (30 godzin konsultacji),
   c) rozliczenia proporcjonalnego za wykonane prace.
```

**Fallback (minimum akceptowalne):** Zamawiający może wypowiedzieć z 60-dniowym okresem wypowiedzenia; Wykonawca tylko za naruszenie Umowy (brak zobowiązania do zwrotu źródeł bezpłatnie, ale co najmniej dostępu do nich).

---

### 5. Zobowiązanie działania zamiast rezultatu + brak Załącznika — § 1 ust. 1
**Opis:**
```
„Wykonawca dołoży starań w celu wdrożenia systemu ERP"
```
To zobowiązanie **starannego działania**, nie **rezultatu**. A wdrożenie to zobowiązanie, które powinno być rezultatem (system ma być zainstalowany i działać). Dodatkowo, brak Załącznika nr 1, który miał określać szczegóły wdrożenia.

**Skutek:**
- Zamawiający płaci 480k zł za „starania", niekoniecznie za działający system.
- Spór: co obejmuje „starania"? Ile pracy to „dość"?
- Brak kryteriów odbioru, testowania, walidacji.

**Rekomendacja (preferowana):**
```
§ 1 ust. 1 (zmieniony)
Wykonawca zobowiązuje się do wdrożenia Systemu ERP w infrastrukturze Zamawiającego 
zgodnie z Załącznikiem nr 1 (Specyfikacja Techniczna), z spełnieniem następujących 
warunków rezultatu:
- Wdrożenie obejmuje zainstalowanie oprogramowania, konfigurację, migrację danych, testy UAT,
- System musi być dostępny i funkcjonalny przez minimum 7 dni przed formą odbioru,
- Zamawiający ma prawo do maksymalnie 5 dyniów popraw w ciągu 30 dni od odbioru.

Załącznik nr 1 (OBOWIĄZKOWE)
[pełna specyfikacja, kamienie milowe, kryteria zdania]
```

**Fallback (minimum akceptowalne):** Zachować „dołoży starań", ale dodać kryteria minimalnego zakresu (np. „obejmując przynajmniej [wymienić poszczególne moduły, raporty, interfejsy]") i okresu gwarancji (np. „przez 6 miesięcy od wdrożenia").

---

## 🟠 RYZYKA WYSOKIE

### 1. Prawo Delaware i sąd w Wilmington (USA) — § 8 ust. 1
**Opis:** Umowa polska, strony polskie, ale prawo Delaware i sąd USA. To niepotrzebna komplikacja.

**Skutek:** Wyższa ekspozycja kosztowa, adwokatem w USA, opóźnienia, niepewność interpretacji.

**Rekom.:** Prawo polskie, sąd Warszawy (lub Gdańska, jeśli siedziba tam).

---

### 2. Brak kodu źródłowego — § 4 ust. 2
**Opis:**
```
„Wykonawca może, ale nie jest zobowiązany, przekazać kod źródłowy"
```
Zamawiający nie nabywa kodu, co oznacza lock-in: jeśli Wykonawca upadnie lub się wyprowadzi, Zamawiający zostaje z zamkniętą aplikacją.

**Rekom.:** Wymienić kod źródłowy jako **obowiązkowe**, albo escrow kodu (depozyt u trzeciej strony, dostępny w razie upadku Wykonawcy).

---

### 3. Brak terminu realizacji + „niezwłocznie" i „na bieżąco" — § 2
**Opis:** § 2 ust. 1 „niezwłocznie", § 2 ust. 2 „na bieżąco" — brak liczby dni, harmonogramu, kamieni milowych.

**Rekom.:** Określić: „W terminie 60 dni od podpisania Umowy", poszczególne fazy w Załączniku.

---

### 4. Brak poufności po umowie — § 6
**Opis:** § 6 mówi o poufności, ale brak okresu po zakończeniu.

**Rekom.:** „Obowiązek zachowania poufności trwa 3 lata po zakończeniu Umowy, bezterminowo dla tajemnic przedsiębiorstwa".

---

## 🟡 RYZYKA ŚREDNIE

### 1. Brak szczegółów warunków wspólpracy — § 2 ust. 2
„Zamawiający będzie zgłaszał uwagi na bieżąco" — brak kanału komunikacji, czasu odpowiedzi, procedury akceptacji uwag.

---

### 2. Brak danych stron (KRS / NIP)
Brak numerów KRS obydwu podmiotów.

---

## ✓ Obszary bez zastrzeżeń

- Reprezentacja stron: [powinno się pojawić, ale nie ma]
- Przeniesienie całościowe problematyczne w czterech punktach powyżej

---

## OCENA BEZPIECZEŃSTWA: 12/100

**Uzasadnienie:** Umowa zawiera cztery naruszenia norm bezwzględnie obowiązujących:
1. Kara za opóźnienie płatności narusza art. 483 § 1 KC (nieważna).
2. Przeniesienie praw bez pól narusza art. 41 ust. 2 PrAut (brak skutecznego przeniesienia).
3. Trenowanie AI na danych narusza art. 28 RODO (brak umowy, brak zgody).
4. Asymetryczne prawo do wypowiedzenia może naruszać art. 3531 KC (zasady współżycia).

Dodatkowo: zobowiązanie działania zamiast rezultatu, brak Załącznika, brak terminu, prawo Delaware.

**Werdykt:** **NIE PODPISYWAĆ** — wymaga wymiany czterech klauzul naruszających ius cogens i zdefiniowania zakresu prac.

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
