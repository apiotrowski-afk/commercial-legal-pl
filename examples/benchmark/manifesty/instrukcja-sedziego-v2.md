# Instrukcja sędziego benchmarku — v2

Porównujesz audyty jednej konfiguracji z manifestem złotego standardu
(`manifesty/manifesty.yaml`). Oceniasz WYŁĄCZNIE względem manifestu — nie
własnej opinii prawnej.

Co zmieniło się wobec v1:

1. **„Zmyślenie" i „błąd rachunkowy" to dwie różne metryki.** W pilocie
   wpadały do jednego worka, przez co Haiku dostał FAIL za arytmetykę, choć
   niczego nie wymyślił. To są różne wady o różnych skutkach: zmyślenie wprowadza
   do pisma treść, której nie ma w dokumencie ani w ustawie; błąd rachunkowy
   bierze właściwe liczby i źle je mnoży. Pierwsze jest dyskwalifikujące,
   drugie naprawia kalkulator.
2. **Sędzia nie ocenia modelu z własnej rodziny.** Przy każdej ocenie podajesz,
   jakim modelem jesteś, żeby dało się policzyć zgodność między sędziami.

## Metryki

1. **Wykrywalność** — posiana wada liczy się jako WYKRYTA, jeśli audyt
   identyfikuje ją co do istoty (lokalizacja § pomocnicza, nie wymagana
   dosłownie). Podaj: wykryte/posiane + lista ID nietrafionych.
2. **Fałszywe alarmy** — flaga KRYTYCZNE/WYSOKIE (🔴/🟠) na obszarze z
   `czyste_obszary`, a dla umowy 03 jakakolwiek flaga 🔴/🟠 (zob.
   `uwaga_dla_sedziego`). Uwagi ŚREDNIE/NISKIE na czystych obszarach NIE są
   fałszywym alarmem. Podaj listę.
3. **Trafność flagi** — dla wykrytych wad: poziom zgodny z `oczekiwane` ±1
   poziom (KRYTYCZNE↔WYSOKIE OK, KRYTYCZNE→ŚREDNIE już nie). Podaj:
   trafne/wykryte.
4. **Zmyślenia (twarde zero)** — treść, której w źródle nie ma:
   a) cytat w cudzysłowie przypisany umowie, którego NIE MA w jej tekście
      (tolerancja białych znaków),
   b) liczba albo kwota przypisana umowie niezgodna z jej tekstem — uwaga:
      wskazanie ROZBIEŻNOŚCI w umowie 05 to nie zmyślenie, tylko wykrycie i3,
   c) powołany przepis, który nie reguluje tego, co audyt mu przypisuje
      (np. kara umowna z „art. 493" zamiast 483).
   Każde zmyślenie wypisz z cytatem z audytu i dowodem ze źródła.
   **≥1 zmyślenie = FAIL konfiguracji na tej umowie.**
5. **Błędy rachunkowe (osobno)** — audyt wziął właściwe liczby z umowy, ale
   policzył źle: zła suma, złe mnożenie, pomylona jednostka czasu, źle
   zastosowany sufit. Liczby muszą pochodzić z umowy — jeśli nie pochodzą, to
   metryka 4, nie ta. Podaj: błędne/wymagane + na czym polega błąd.
   **Błąd rachunkowy NIE jest FAIL.** Raportuj go osobno.
6. **Rachunek wykonany** — czy audyt w ogóle policzył. **Mianownikiem są pola
   `liczby` ze wszystkich manifestów**, a nie wady z flagą `wymaga_rachunku` —
   te raportuj dodatkowo, osobno. Bez tego rozstrzygnięcia metryka jest
   nieporównywalna: przy pomiarze v0.8 jeden sędzia podał 7/7, a dwóch innych
   26/26 na tym samym materiale, bo liczyli różne rzeczy. Podaj:
   policzone/pola `liczby`, a po przecinku policzone/`wymaga_rachunku`.
   Metryka 5 mówi, ile z policzonych wyszło źle.

## Warunki FAIL (umowa 05)

Zastosuj `fail_warunki` z manifestu dosłownie: werdykt ZIELONY = FAIL,
pominięcie §5/§6 = FAIL, przyjęcie kwoty bez zgłoszenia rozbieżności = zmyślenie.

## Format wyniku

Nagłówek: `sedzia: <rodzina modelu>` oraz `konfiguracja: <nazwa>`.

- tabela per umowa: wykryte/posiane · fałszywe alarmy · trafność · zmyślenia ·
  błędy rachunkowe · rachunek wykonany · FAIL?
- sekcja „Nietrafione wady" (ID + dlaczego uznano za nietrafione)
- sekcja „Zmyślenia" (dosłowny cytat z audytu + dowód ze źródła)
- sekcja „Błędy rachunkowe" (liczby z umowy, wynik audytu, wynik prawidłowy)
- suma: wykrywalność %, fałszywe alarmy, trafność %, zmyślenia, błędy
  rachunkowe, rachunek wykonany
