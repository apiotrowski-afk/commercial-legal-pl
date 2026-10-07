# Pilot kryteriów atomowych — umowa 04

**Data:** 7.10.2026. **Materiał:** cztery audyty umowy 04, które powstały
**przed** napisaniem tych kryteriów — `fable-skill` i trzy przebiegi
`sonnet-skill`. **Rubryka:** `manifesty/kryteria/04-matematyczna-tm.yaml`,
30 kryteriów rozpisanych z pięciu grubych wad m1–m5. **Sędzia:** Gemini 2.5 Pro
przez Vertex, temperatura 0, **jedno zapytanie na kryterium**.

## Wynik

| Konfiguracja | zaliczone | odsetek | all-pass |
|---|---|---|---|
| fable-skill | 30/30 | 100% | **1,0** |
| sonnet-skill p1 | 29/30 | 97% | 0,0 |
| sonnet-skill p2 | 29/30 | 97% | 0,0 |
| sonnet-skill p3 | 30/30 | 100% | **1,0** |

**Ziarnistość przywróciła rozdzielczość.** Przy grubych kryteriach wszystkie
cztery audyty miały 5/5 wad i były nierozróżnialne. Teraz all-pass wynosi 1,0
dla Fable'a i 1/3 dla Sonneta, a wariancja Sonneta ma konkretny adres.

Jedyne realne niezaliczenie: **K04-016** w przebiegach p1 i p2 — audyt omawia
indemnifikację z § 3 ust. 2, ale pomija to, że obejmuje ona również koszty
obsługi prawnej. Przebieg p3 to złapał. Jedna pozycja, nazwana, sprawdzalna.

## Trzy wady rubryki wyłapane przez pilot

Pierwszy przebieg dał pięć niezaliczeń. Po ręcznym sprawdzeniu **trzy z nich
były wadą kryteriów, nie audytów**:

1. **K04-031 — fałszywy dodatni przy najcięższym zarzucie.** Sędzia uznał za
   zmyślenie frazę „Działalność konkurencyjna wobec Zamawiającego", bo § 5
   ust. 1 ma „działalność konkurencyjną" w bierniku. To odmiana, nie wymyślona
   treść — audyt nazywał pojęcie w mianowniku, żeby wskazać, że jest
   niezdefiniowane.
2. **K04-029 — warunek wyłączający przywiązany do poziomu flagi.** Przez to
   uwaga o braku procedury akceptacji godzin liczyła się jako atak na model
   T&M, jeśli dostała poziom wysoki. Obszarem czystym jest konstrukcja modelu i
   stawka, a nie brak zabezpieczeń wokół nich.
3. **K04-031, 032 i 033 nie były kryteriami atomowymi.** Kazały przejrzeć
   wszystkie cytaty, liczby i przepisy w całym audycie, czyli były całą metryką
   przebraną za kryterium. Wszystkie dziewięć zapytań, które nie zmieściły się
   w limicie czasu, pochodziło z tych trzech pozycji. Wycofane z rubryki;
   integralność zostaje osobnym przebiegiem z dowodem ze źródła.

**Wniosek metodyczny: rubryka atomowa wymaga własnego przebiegu kalibracyjnego,
zanim posłuży do pomiaru.** U Harveya rolę tę pełni recenzja drugiego prawnika.
U nas pełni ją pilot na audytach, które już istnieją — i wyłapał trzy wady na
trzydzieści trzy pozycje, w tym jedną, która fałszywie oskarżała o zmyślenie.

## Co to zmienia w kolejności prac

Wczorajszy wniosek z wariancji brzmiał: korpus jest wysycony, więc rozbudowa z
pięciu do piętnastu umów staje się warunkiem dalszego mierzenia. **Ten pilot to
koryguje.** Wysycenie brało się z grubości kryteriów, nie z liczby umów —
trzydzieści pozycji na jedną umowę wystarczyło, żeby odróżnić cztery audyty,
które wcześniej były identyczne. Rozbudowa korpusu wraca na swoje miejsce:
przydatna, ale nie pierwsza.

Pierwsze jest rozpisanie kryteriów dla pozostałych czterech umów.
