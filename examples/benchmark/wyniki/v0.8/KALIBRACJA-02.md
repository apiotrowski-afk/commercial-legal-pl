# Kalibracja kryteriów atomowych — umowa 02

**Data:** 8.10.2026. **Materiał:** cztery istniejące audyty umowy 02 — `fable-skill`
i trzy przebiegi `sonnet-skill`, wszystkie powstałe przed napisaniem kryteriów.
**Rubryka:** `manifesty/kryteria/02-wdrozenie-erp.yaml`, 35 kryteriów z dziesięciu
wad e1–e10. **Sędzia:** Gemini 2.5 Pro przez Vertex, temperatura 0, jedno zapytanie
na kryterium (`sedzia_kryteria.py`).

## Najpierw skrypt

`sedzia_kryteria.py` przyjmuje teraz umowę jako argument, przerywa bez zapisu, gdy
wczyta mniej kryteriów, niż rubryka deklaruje, liczy błąd zapytania osobno od
niezaliczenia i ponawia tylko pary z błędem (`--dopytaj`). Pierwsza próba
parametryzacji (7.10) wczytała zero kryteriów i zapisała pustą listę.

Kontrola na umowie 04 z zapisem poza repo: **120 na 120 werdyktów identycznych**
z pilotem z 7.10. Skrypt mierzy to samo co wcześniej.

## Wynik

| Konfiguracja | rubryka v1 | rubryka v2 |
|---|---|---|
| fable-skill | 34/35 (0,0) | **35/35 (1,0)** |
| sonnet-skill p1 | 35/35 (1,0) | **35/35 (1,0)** |
| sonnet-skill p2 | 35/35 (1,0) | **35/35 (1,0)** |
| sonnet-skill p3 | 34/35 (0,0) | **35/35 (1,0)** |

Zero błędów zapytań w obu przebiegach.

## Jedna wada rubryki

Oba niezaliczenia w v1 to **K02-034** — próba negatywna na konstrukcji ryczałtu.
Sędzia uznał za atak na ryczałt dwie flagi o niedołączonym Załączniku nr 1:
„nieokreślony zakres przy ryczałcie” (Fable) i „ryczałt 480.000 zł bez zakresu”
(Sonnet p3). Żaden audyt nie twierdzi, że ryczałt albo kwota są wadliwe — oba
wskazują, że umowa odsyła po zakres do załącznika, którego nie ma.

Kryterium zwalniało flagi o braku waloryzacji, etapów, powiązania z odbiorem i
zabezpieczenia płatności, ale nie wymieniało braku zakresu. Ten sam błąd co
K04-029 w pilocie umowy 04. W v2 lista zwolnień obejmuje też nieokreślony zakres
świadczenia.

## Powtarzalność sędziego

136 par, których poprawka nie dotyczyła, dało w drugim przebiegu **identyczne
werdykty**. Razem z kontrolą na umowie 04: 256 na 256 powtórzonych werdyktów bez
zmiany. Przy temperaturze 0 rozrzut sędziego na tym materiale jest zerowy, więc
różnica między audytami pochodzi z audytów albo z rubryki.

## Co z tego wynika

**Umowa 02 przy kryteriach atomowych nadal nie rozróżnia konfiguracji.** Na
umowie 04 ziarnistość przywróciła rozdzielczość (all-pass 1,0 wobec 1/3), na 02
wszystkie cztery audyty przechodzą wszystko. Wniosek z pilotu 04 — że wysycenie
bierze się z grubości kryteriów, nie z liczby umów — był prawdziwy dla jednej
umowy, nie dla korpusu. Różnica jest w materiale: 04 to arytmetyka i szczegół
(9 kryteriów liczbowych), 02 to rażące wady konstrukcyjne (1 kryterium
liczbowe), które każda z tych konfiguracji widzi.

**Zastrzeżenie metodyczne.** Kalibracja i pomiar odbyły się na tych samych
czterech audytach, a jedyna poprawka rubryki podniosła wynik. Wynik v2 jest
więc wynikiem kalibracji, nie pomiaru. Pomiarem będzie dopiero przebieg tej
rubryki na audytach powstałych po niej — kolejnej wersji skilla albo
konfiguracji `sonnet-bare`.

**Poza kluczem:** niedołączony Załącznik nr 1 (zakres przedmiotu umowy) obie
konfiguracje zgłosiły jako 🟠, a manifest tej wady nie zawiera. Kandydat do
dopisania, obok dwóch wad z umowy 04 — decyzja prawnika.

## Co dalej

1. Rubryki dla 01, 03 i 05. Umowa 05 (injection, rozbieżność kwot) i 01 (NDA,
   wada n5 gubiona w pilocie przez trzy konfiguracje) mają większą szansę
   rozróżniać niż 02.
2. `sonnet-bare` na umowach 02 i 04 — pierwszy pomiar rubryki na audytach, na
   których nie była kalibrowana, i pierwsza delta „ze skillem kontra bez”.
