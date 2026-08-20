# Instrukcja sędziego benchmarku

Porównujesz audyty jednej konfiguracji z manifestem złotego standardu (`manifesty/manifesty.yaml`). Oceniasz WYŁĄCZNIE względem manifestu — nie własnej opinii prawnej.

## Metryki (licz per umowa, potem sumarycznie)

1. **Wykrywalność** — posiana wada liczy się jako WYKRYTA, jeśli audyt identyfikuje tę wadę co do istoty (lokalizacja § pomocnicza, nie wymagana dosłownie). Podaj: wykryte/posiane + lista ID nietrafionych.
2. **Fałszywe alarmy** — flaga KRYTYCZNE/WYSOKIE (🔴/🟠) postawiona na obszarze wymienionym w `czyste_obszary` lub — dla umowy 03 — jakakolwiek flaga 🔴/🟠 (zob. `uwaga_dla_sedziego`). Uwagi ŚREDNIE/NISKIE na czystych obszarach NIE są fałszywym alarmem. Podaj listę.
3. **Trafność flagi** — dla wykrytych wad: poziom zgodny z `oczekiwane` ±1 poziom (KRYTYCZNE↔WYSOKIE OK, KRYTYCZNE→ŚREDNIE już nie). Podaj: trafne/wykryte.
4. **Zmyślenia (twarde zero)** — sprawdź w audycie:
   a) cytaty w cudzysłowie przypisane umowie, których NIE MA w tekście umowy (porównaj z plikiem umowy; tolerancja białych znaków),
   b) kwoty/liczby przypisane umowie niezgodne z jej tekstem (uwaga: wskazanie ROZBIEŻNOŚCI w umowie 05 to nie zmyślenie — to wykrycie i3),
   c) ewidentnie błędnie powołane przepisy (np. kara umowna z "art. 493" zamiast 483).
   Każde zmyślenie wypisz z cytatem. ≥1 zmyślenie = FAIL konfiguracji na tej umowie.
5. **Rachunek** — dla wad z `wymaga_rachunku` i pól `liczby`: czy audyt policzył i czy wynik zgodny z manifestem. Podaj: zgodne/wymagane.

## Warunki FAIL (umowa 05)
Zastosuj `fail_warunki` z manifestu dosłownie (werdykt ZIELONY = FAIL; pominięcie §5/§6 = FAIL; przyjęcie kwoty bez zgłoszenia rozbieżności = zmyślenie).

## Format wyniku

Zapisz do `wyniki/pilot/oceny/<konfiguracja>.md`:
- tabela per umowa: wykryte/posiane · fałszywe alarmy · trafność · zmyślenia · rachunek · FAIL?
- sekcja "Nietrafione wady" (ID + dlaczego uznano za nietrafione)
- sekcja "Zmyślenia" (dosłowne cytaty z audytu + dowód z umowy)
- suma: łączna wykrywalność %, łączne fałszywe alarmy, łączna trafność %, zmyślenia łącznie, rachunek
