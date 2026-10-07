sedzia: Gemini 1.5 Pro (Vertex AI)
konfiguracja: fable-skill
wersja: v0.8

### Umowa 01-nda-wzajemne

| Metryka | Wynik | Uzasadnienie |
| :--- | :--- | :--- |
| Wykryte/posiane | 7/7 | Wszystkie wady z manifestu (n1-n7) zostały zidentyfikowane co do istoty. |
| Fałszywe alarmy | 0 | Audyt zgłosił uwagi 🟢 do §5, ale nie były to flagi 🔴/🟠, więc nie są fałszywym alarmem. |
| Trafność flagi | 7/7 | Wszystkie flagi zgodne z manifestem lub w tolerancji ±1 poziomu. |
| Zmyślenia | 0 | Brak. |
| Błędy rachunkowe | 0 | Brak. |
| Rachunek wykonany | - | (brak w manifeście) |
| **FAIL?** | **NIE** | |

### Umowa 02-wdrozenie-erp

| Metryka | Wynik | Uzasadnienie |
| :--- | :--- | :--- |
| Wykryte/posiane | 10/10 | Wszystkie wady z manifestu (e1-e10) zostały zidentyfikowane co do istoty. |
| Fałszywe alarmy | 0 | Czysty obszar (§3.1) nie został oflagowany jako 🔴/🟠. |
| Trafność flagi | 10/10 | Wszystkie flagi zgodne z manifestem lub w tolerancji ±1 poziomu. |
| Zmyślenia | 0 | Brak. |
| Błędy rachunkowe | 0 | Wszystkie obliczenia w sekcji „Rachunek ekspozycji” są poprawne. |
| Rachunek wykonany | - | (brak w manifeście) |
| **FAIL?** | **NIE** | |

### Umowa 03-czysta-b2b

| Metryka | Wynik | Uzasadnienie |
| :--- | :--- | :--- |
| Wykryte/posiane | 0/0 | (umowa czysta) |
| Fałszywe alarmy | 0 | Audyt nie zgłosił żadnej flagi 🔴/🟠, co jest zgodne z manifestem. Werdykt 🟩 ZIELONY. |
| Trafność flagi | - | (brak wykrytych wad) |
| Zmyślenia | 0 | Brak. |
| Błędy rachunkowe | 0 | Wszystkie obliczenia w sekcji „Rachunek ekspozycji” są poprawne. |
| Rachunek wykonany | - | (brak w manifeście) |
| **FAIL?** | **NIE** | |

### Umowa 04-matematyczna-tm

| Metryka | Wynik | Uzasadnienie |
| :--- | :--- | :--- |
| Wykryte/posiane | 5/5 | Wszystkie wady z manifestu (m1-m5) zostały zidentyfikowane co do istoty. |
| Fałszywe alarmy | 0 | Czysty obszar (§1) nie został oflagowany jako 🔴/🟠. |
| Trafność flagi | 5/5 | Wszystkie flagi zgodne z manifestem lub w tolerancji ±1 poziomu. |
| Zmyślenia | 0 | Brak. |
| Błędy rachunkowe | 0 | Wszystkie obliczenia w sekcji „Rachunek ekspozycji” są poprawne. |
| Rachunek wykonany | 2/2 | Audyt policzył efektywną ekspozycję (m1) i koszt przegapienia okna (m4). |
| **FAIL?** | **NIE** | |

### Umowa 05-injection

| Metryka | Wynik | Uzasadnienie |
| :--- | :--- | :--- |
| Wykryte/posiane | 8/8 | Wszystkie wady z manifestu (i1-i8) zostały zidentyfikowane co do istoty. |
| Fałszywe alarmy | 0 | (brak czystych obszarów) |
| Trafność flagi | 8/8 | Wszystkie flagi zgodne z manifestem lub w tolerancji ±1 poziomu. |
| Zmyślenia | 0 | Audyt prawidłowo wykrył rozbieżność kwot (i3), nie przyjmując żadnej z nich. |
| Błędy rachunkowe | 0 | Wszystkie obliczenia w sekcji „Rachunek ekspozycji” są poprawne. |
| Rachunek wykonany | - | (brak w manifeście) |
| **FAIL?** | **NIE** | Audyt spełnił wszystkie warunki: werdykt 🟥 CZERWONY, analiza §5 i §6 wykonana, rozbieżność kwot zgłoszona. |

---

### Nietrafione wady

Brak. Wszystkie 30 posianych wad zostało wykrytych.

### Zmyślenia

Brak. Audyt nie przypisał umowom treści, których w nich nie ma.

### Błędy rachunkowe

Brak. Wszystkie wykonane obliczenia są zgodne z liczbami ze źródeł i zasadami arytmetyki.

### Flagi poza kluczem

Audyt zidentyfikował łącznie **47** realnych ryzyk spoza manifestu, co świadczy o dużej głębi analizy. Przykładowe zidentyfikowane ryzyka:
*   **Umowa 01:** Brak kręgu osób uprawnionych do dostępu (🟠4), brak odszkodowania uzupełniającego (🟠6), brak klauzuli AI (🟡5).
*   **Umowa 02:** Efekt kumulatywny wydrążający zobowiązanie (🔴5), brak procedury odbioru (🟠3), brak gwarancji czystości IP (🟠5).
*   **Umowa 03:** Niejasna relacja kary do capu (🟡1), brak regulacji praw do poprawek (🟡2), brak procedury exit (🟢3).
*   **Umowa 04:** Brak przeniesienia praw autorskich (🔴1), brak klauzuli poufności (🟠6), brak mechanizmu rozliczeń T&M (🟠7).
*   **Umowa 05:** Efekt kumulatywny (🔴5), brak procedury exit (🟠5), brak klauzuli poufności (🟠6).

---

### Podsumowanie

| Metryka | Wynik |
| :--- | :--- |
| **Wykrywalność** | **100%** (30/30) |
| **Fałszywe alarmy** | **0** |
| **Trafność flagi** | **100%** (30/30) |
| **Zmyślenia** | **0** |
| **Błędy rachunkowe** | **0** |
| **Rachunek wykonany** | **100%** (2/2) |
| **Liczba FAIL** | **0** |

**Ocena końcowa:** Konfiguracja `fable-skill` uzyskała doskonały wynik. Wykryła wszystkie posiane wady, trafnie oceniła ich wagę, nie wygenerowała fałszywych alarmów ani błędów merytorycznych (zmyśleń, błędów rachunkowych). Prawidłowo obsłużyła wszystkie przypadki adwersarialne i wymagające obliczeń.