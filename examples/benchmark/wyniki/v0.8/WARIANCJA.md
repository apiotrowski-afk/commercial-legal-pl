# Wariancja — sonnet-skill, trzy przebiegi

**Data:** 7.10.2026. **Konfiguracja:** `sonnet-skill`, commit skilla `06a7e59`.
**k = 3** przebiegi po pięć umów, ten sam prompt, różne losowanie.
**Sędziowie:** trzy niezależne oceny Opus, po jednej na przebieg, każda bez
dostępu do pozostałych. Jednostką analizy jest pojedyncza posiana wada.

## Wynik

| Metryka | p1 | p2 | p3 | rozstęp |
|---|---|---|---|---|
| wykrywalność | 30/30 | 30/30 | 30/30 | **0** |
| fałszywe alarmy | 1 | 0 | 0 | 1 |
| trafność flag | 30/30 | 30/30 | 30/30 | 0 |
| zmyślenia | **0** | **0** | **0** | **0** |
| błędy rachunkowe | 0 | 1 | 0 | 1 |
| flagi poza kluczem | 33 | 35 | 25 | 10 |
| FAIL | brak | brak | brak | — |

**Odchylenie standardowe wykrywalności: 0,000 wady. Wad niestabilnych: 0.**
Każda z trzydziestu wad została wykryta w każdym z trzech przebiegów.

Dla kontrastu to, co w tych samych przebiegach się wahało: liczba flag od 6 do
17 w zależności od umowy i przebiegu, ocena punktowa na umowie czystej od 80 do
88, a etykieta werdyktu na tej umowie raz ŻÓŁTA zamiast ZIELONEJ — przy
niezmiennym zerze flag krytycznych i wysokich.

## Trzy wnioski

**1. Metryka jest twarda, opakowanie miękkie.** Wykrywalność, trafność i
zmyślenia nie drgnęły. Werdykt i liczba flag wahają się same z siebie, bez
zmiany czegokolwiek poza losowaniem. Skutek praktyczny: w tekście publicznym
nie wolno pisać „skill ocenił umowę jako zieloną", bo to nieodtwarzalne.
Odtwarzalne jest „nie postawił ani jednej flagi krytycznej ani wysokiej na
umowie bez wad" — trzy razy na trzy.

**2. Rozdzielenie zmyśleń od arytmetyki zdało egzamin na żywych danych.**
W przebiegu p2 wyszedł jeden błąd rachunkowy. Pod regułami v1 liczyłby się
jako zmyślenie, czyli **jeden z trzech przebiegów dostałby FAIL** na metryce
twardego zera — konfiguracja wyglądałaby na niestabilną tam, gdzie stawka jest
najwyższa. Faktycznie niestabilna jest tylko arytmetyka: zmyślenia 0/0/0, błędy
rachunkowe 0/1/0.

**3. Korpus jest wysycony i przestał rozróżniać.** To najważniejszy wniosek i
niewygodny. `fable-skill` ma 30/30, `sonnet-skill` ma 30/30 w każdym z trzech
przebiegów. Przy sufitcie 100% ten korpus **nie potrafi już uszeregować
konfiguracji** — potrafi tylko wykryć regresję, czyli spadek poniżej setki.
Statystyka parowana „ze skillem kontra bez skilla" nie ma tu czego testować:
przy 30/30 wobec 30/30 test McNemara jest bezprzedmiotowy.

Z tego wynika kolejność prac odwrotna do planowanej. Rozbudowa korpusu z pięciu
do piętnastu umów przestaje być „kiedyś" i staje się warunkiem dalszego
mierzenia czegokolwiek poza regresją. Mierzenie delty metody wymaga zadań, na
których którakolwiek konfiguracja się jeszcze myli.

## Co zostaje niezmierzone

Flagi poza kluczem: od 25 do 35 na przebieg, średnio 31 — przy trzydziestu
wadach w kluczu. Ponad połowa objętości raportu dotyczy spraw, których manifest
nie obejmuje, a rozstęp 10 między przebiegami pokazuje, że to też jest
niestabilne. Sędziowie uznali te flagi za trafne, ale dopóki nie wejdą do
klucza, nie mierzymy ani ich przydatności, ani ich nadmiaru.
