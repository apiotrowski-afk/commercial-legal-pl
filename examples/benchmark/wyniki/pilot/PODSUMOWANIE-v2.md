# Przesądzenie pilotu sędzią z innej linii — wynik

**Data:** 6.10.2026. **Materiał:** te same 30 audytów z sierpnia 2026, bez
ponownego uruchamiania modeli. **Sędzia:** sześciu niezależnych agentów Opus,
każdy bez dostępu do poprzedniej karty oceny. **Instrukcja:**
`manifesty/instrukcja-sedziego-v2.md` (zmyślenie rozdzielone od błędu
rachunkowego).

W pilocie sędziami było sześciu agentów Fable, a najwyższy wynik dostała
konfiguracja `fable-skill`. Pytanie brzmiało: ile z tego 100% to metoda, a ile
rozpoznanie własnego stylu.

## Zestawienie

| Konfiguracja | Wykrywalność v1 → v2 | Fałszywe alarmy | Trafność flag | Zmyślenia v1 → v2 | Błędy rachunkowe (nowa metryka) | FAIL v1 → v2 |
|---|---|---|---|---|---|---|
| fable-skill | 30/30 → **30/30** | 0 → 0 | 30/30 → 30/30 | 0 → 0 | 0 | brak → brak |
| fable-bare | 29/30 → **29/30** | 0 → 0 | 28/29 → 28/29 | 0 → 0 | 0 | brak → brak |
| sonnet-skill | 28/30 → **28/30** | 1 → 2 | 27/28 → 27/28 | 0 → 0 | **2** | brak → brak |
| gemini-skill | 28/30 → **28/30** | 1 → 1 | 27/28 → 27/28 | 0 → 0 | 0 | brak → brak |
| haiku-skill | 27/30 → **26/30** | 1 → 1 | 25/27 → 24/26 | 3 → **2** | **8** | umowa 04 → **umowy 02 i 05** |
| gemini-bare | 26/30 → **27/30** | 3 → 3 | 25/26 → 26/27 | 0 → 0 | 0 | brak → brak |

## Co z tego wynika

**1. Hipoteza o samopreferencji się nie potwierdziła.** `fable-skill` utrzymał
30/30, zero fałszywych alarmów i zero zmyśleń u sędziego z innej linii, który
sprawdził każde powołanie przepisu osobno. Wynik nie był artefaktem sędziego.

**2. Zgodność sędziów na wykrywalności jest wysoka.** Cztery konfiguracje na
sześć bez zmiany, dwie o jedną wadę (Haiku −1, gemini-bare +1). Różnice między
konfiguracjami są większe niż rozjazd sędziów, więc ranking nie jest szumem —
z zastrzeżeniem, że na dole tabeli Haiku i gemini-bare zamieniły się miejscami,
czyli tam, gdzie różnica wynosi jedną wadę, kolejność jest nierozstrzygnięta.

**3. Rozdzielenie metryk zmieniło powód FAIL-a Haiku, nie jego istnienie — i
nowy powód jest poważniejszy.** Sierpniowy FAIL na umowie 04 upadł: audyt
odczytał z umowy właściwe liczby i dopiero w rachunku zgubił mnożnik dwóch
specjalistów, co naprawia kalkulator. Za to wyszło coś, czego stara metryka nie
widziała, bo tonęło w jednym worku: **dwa razy przypisał art. 83 ust. 4 RODO
karę 20 mln EUR albo 4% przychodu**. Sprawdzone u źródła przez legal-cite-pl
na tekście z CELLAR: ust. 4 przewiduje 10 mln EUR i 2%, a 20 mln i 4% jest w
ust. 5. To jest zmyślenie przepisu, nie pomyłka w mnożeniu. FAIL przeniósł się
z umowy 04 na umowy 02 i 05.

**4. Błędy rachunkowe były niewidoczne, bo nikt ich osobno nie liczył.** Nowa
metryka pokazuje 8 u Haiku (jedna przyczyna źródłowa: pominięty mnożnik
dwóch specjalistów, plus trzy samoistne pomyłki) i **2 u Sonneta**, których
sierpniowy sędzia nie zgłosił w ogóle. Pod regułami v1 Sonnet dostałby za to
FAIL, bo manifest umowy 04 kazał traktować arytmetykę jak zmyślenie.

**5. Wniosek produktowy z pilotu zostaje, ale z innym uzasadnieniem.** „Minimum
Sonnet do audytu produkcyjnego" broni się nadal — tyle że nie dlatego, że Haiku
źle mnoży, bo to naprawia deterministyczny kalkulator pod R12, tylko dlatego,
że Haiku przypisuje przepisom treść, której w nich nie ma. Tego kalkulator nie
naprawi.

**6. Zero zmyśleń utrzymało się w pięciu konfiguracjach na sześć**, przy
sędzim, który weryfikował cytaty i przepisy pojedynczo u źródła. To najmocniejsza
liczba w tym zestawieniu.

## Czego ten pomiar nie rozstrzyga

- **Opus i Fable to różne linie, ale ten sam dostawca.** Wykluczyliśmy
  samopreferencję w obrębie linii, nie wspólne ślepe plamy obu. Sędzia spoza
  dostawcy wymaga klucza API albo zalogowanej sesji.
- **Jeden przebieg na konfigurację.** Wariancja nadal nieznana; różnice
  jednej wady są poniżej rozdzielczości tego pomiaru.
- **Fałszywe alarmy mierzone na czterech miejscach** (trzy czyste obszary w
  manifestach plus umowa 03) wobec trzydziestu miejsc pomiaru wykrywalności.
  „Zero fałszywych alarmów" znaczy mniej, niż brzmi.
