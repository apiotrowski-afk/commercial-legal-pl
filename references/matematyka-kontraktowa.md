---
type: Referencja
title: Matematyka kontraktowa — policz zanim ocenisz
tags: [matematyka, ekspozycja, cap, kary umowne, kumulacja, terminy, daty, wypowiedzenie, SLA, arytmetyka, weryfikacja liczbowa]
contract_types: [wszystkie]
risk_level: informacyjny
mandatory_for: [audyt-ryzyk, pełna-analiza, ocena-2-strony]
requires: [11-odpowiedzialnosc.md, 10-kary-umowne.md, 07-terminy-kamienie-milowe.md]
timestamp: 2026-08-07
---

# Matematyka kontraktowa — policz zanim ocenisz

Modele językowe dobrze czytają klauzule, ale **źle liczą** — mylą się w kumulacji kar, sumowaniu okresów, porównaniu capu z realną ekspozycją. A ryzyko w umowie prawie zawsze ma **kwotę i termin**. Dlatego przed werdyktem liczysz — jawnie, krok po kroku, na liczbach **z tekstu umowy** (zamknięte wejście; brak liczby w umowie = nie zgaduj, oznacz `[BRAK DANYCH]`).

Zasada: **pokaż działanie, nie tylko wynik.** Czytelnik ma móc sprawdzić rachunek. Nominalna deklaracja w umowie („cap 12 miesięcy") ≠ efektywna ekspozycja — liczysz drugie.

## 1. Efektywna ekspozycja odpowiedzialności

Cap to nie koniec rachunku. Sprawdź, **co przechodzi obok capu**:

```
Cap nominalny            = [wg umowy, np. 12 × wynagrodzenie miesięczne = X zł]
+ kary umowne poza capem = [suma maksymalnych kar, jeśli umowa nie liczy ich do capu]
+ indemnifikacja bez limitu = [otwarte hold-harmless — potencjalnie bez granicy]
+ wyłączenia z capu      = [wina umyślna samego dłużnika, w tym organu osoby prawnej (ustawowo poza capem — art. 473 § 2 KC; umyślne działania osób z art. 474 KC — odrębna ocena), poufność, IP, RODO, roszczenia osób trzecich — jeśli wyłączone z limitu]
= EFEKTYWNA EKSPOZYCJA   ≥ cap nominalny
```

Pytania kontrolne: czy kary umowne **wliczają się** w cap, czy są obok? Czy odszkodowanie uzupełniające ponad karę jest dopuszczone (art. 484 § 1 KC)? Czy indemnity ma sufit? Jeśli ekspozycja efektywna wielokrotnie przewyższa cap — cap jest **iluzoryczny** → flaga 🟠/🔴 mimo „ładnej" klauzuli limitu.

## 2. Kumulacja kar umownych

Kara „za dzień" ma ogon. Policz maksimum:

```
Kara dzienna × maksymalna liczba dni (do sufitu, jeśli jest; jeśli nie — do końca umowy / rozsądnego horyzontu)
np. 0,5% wartości / dzień × 60 dni = 30% wartości umowy
    50.000 zł / dzień × 30 dni = 1.500.000 zł (przy umowie 480.000 zł → 312% wartości)
```

Kontrola: czy jest **sufit kary** (np. 20% wartości)? Brak sufitu przy karze dziennej = ekspozycja otwarta. Czy kary z różnych podstaw **sumują się** (za zwłokę + za jakość + za poufność)? Kara wielokrotnie przewyższająca wartość umowy → argument o **rażącym wygórowaniu** (miarkowanie, art. 484 § 2 KC). Miarkowanie to **uprawnienie sądu** (ius moderandi), nie automat — sąd waży m.in. interes wierzyciela, zakres wykonania, rozmiar naruszenia, wysokość szkody (jej brak nie wyłącza kary), funkcję kompensacyjną i dyscyplinującą; wielokrotność wartości umowy to tylko jeden z argumentów. Skill **flaguje ryzyko** uznania kary za rażąco wygórowaną, nie przesądza, że zostanie zmiarkowana.

## 3. Asymetria — porównaj obie strony liczbowo

Nie „asymetryczne", tylko **o ile**:

```
Strona A: cap [X] · kary max [Y] · okres wypowiedzenia [n dni]
Strona B: cap [X'] · kary max [Y'] · okres wypowiedzenia [n' dni]
Stosunek: kary A/B = ..., ekspozycja A/B = ...
```

Symetria deklarowana („Strony wzajemnie…") vs policzona to częsty rozjazd (por. antywzorzec „pozorna wzajemność").

## 4. Daty, terminy, okresy — policz kalendarzowo

- **Okres wypowiedzenia:** od jakiego zdarzenia biegnie (doręczenie? koniec miesiąca?) i kiedy realnie kończy umowę → podaj datę graniczną, jeśli daty w umowie na to pozwalają.
- **Auto-renewal:** okno na sprzeciw (np. „90 dni przed końcem") → policz **ostatni dzień skutecznego wypowiedzenia**; przegapienie = kolejny okres (kwota = wartość okresu).
- **Terminy płatności:** czy > 60 dni w B2B (granica ustawy o zatorach płatniczych; dłuższy tylko, gdy nie rażąco nieuczciwy) → oznacz.
- **Kamienie milowe:** suma okresów etapów vs termin końcowy — czy się domykają? Luka/nakładka → niespójność.
- **Okresy gwarancji/rękojmi/poufności:** od jakiego momentu, do kiedy; „bezterminowo" oznacz jawnie.
- **Naruszenie RODO:** okno procesor→administrator (np. 48h) + 72h administratora → czy łańcuch mieści się w 72h od stwierdzenia? (zob. `baza-wiedzy/09`).

Zasada: „niezwłocznie"/„w rozsądnym terminie" **nie da się policzyć** → to sygnał do flagowania (antywzorzec), nie do zgadywania liczby.

## 5. Wynagrodzenie i ryzyko kursowe/waloryzacja

- Ryczałt vs T&M: przy T&M policz **realistyczny koszt** (stawka × szacowana pracochłonność), nie tylko stawkę.
- Waloryzacja/indeksacja: od jakiego wskaźnika, jak często, czy dwustronna.
- Waluta obca: kto ponosi ryzyko kursu; brak klauzuli = ryzyko po stronie płacącego w PLN.
- SLA credits: policz **maksymalny kredyt** (sufit) vs realny koszt przestoju — czy kredyt jest jedynym środkiem („sole remedy")?

## Jak używać w audycie

1. **Wyciągnij wszystkie liczby i daty** z umowy (kwoty, procenty, dni, okresy, sufity) — lista, zanim zaczniesz oceniać.
2. **Policz** ekspozycję efektywną, kumulację kar, asymetrię, daty graniczne — pokazując działanie.
3. Liczba nieobecna w umowie → `[BRAK DANYCH]`, nie szacunek. Wynik zależny od założenia → oznacz założenie jawnie.
4. **Werdykt i flagi kalibruj do policzonych kwot**, nie do etykiet w umowie: „cap 12 mies." przy karach poza capem 3× wartości to 🔴, nie 🟢.
5. Wynik wpisz do raportu w sekcji **„Rachunek ekspozycji"** (audyt) — kwoty i terminy przed oceną słowną, zgodnie z zasadą: ryzyko przez kwotę i termin, czytelnik sam wyciąga wniosek.
