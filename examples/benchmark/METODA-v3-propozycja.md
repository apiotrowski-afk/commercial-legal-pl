# Metoda v3 — co bierzemy z Harvey LAB, a co zostaje nasze

Przegląd z 7.10.2026. Źródłem jest **metoda**, nie dane: zadania Harveya to
prawo amerykańskie po angielsku, a kod ich harnessu jest na MIT. Sposób
oceniania nie jest przedmiotem prawa autorskiego, więc rozmowa jest o tym, co
jest lepsze, nie o tym, co wolno.

## Ich metoda w pięciu punktach

1. **Ocena „all-pass".** Zadanie dostaje 1,0 tylko wtedy, gdy przeszło KAŻDE
   kryterium; w przeciwnym razie 0,0. Uzasadnienie podają wprost: memo z due
   diligence, które łapie 95% problemów i gubi jeden istotny, nie jest użyteczne
   w 95% — jest błędne. Odsetek przeszłych kryteriów zostaje jako metryka
   **diagnostyczna**, nie wchodzi do wyniku zadania.
2. **Kryterium jest atomowe i samo jest wzorcem.** Pola: `id`, `title`,
   `match_criteria`, `deliverables`, opcjonalnie `sources`. Nie ma osobnego
   pliku złotego standardu — `match_criteria` opisuje dokładnie to, co sędzia ma
   sprawdzić, i to wystarcza.
3. **Sędzia ocenia po jednym kryterium naraz**, żeby kryteria nie wpływały na
   siebie. Dopasowanie wyłącznie semantyczne, bez regexów. Każde kryterium widzi
   tylko te pliki wyjściowe, które zadeklarowało.
4. **Dwóch sędziów z dwóch dostawców**, temperatura 0. Przy rozbieżności wynik
   zadania to 0,0, 0,5 albo 1,0, a raport pokazuje **osobno** średnią i wariant
   „obaj sędziowie zgodni".
5. **Zakaz watowania rubryki.** Kryteria mają zawierać to, co sprawdziłby
   nadzorujący prawnik przed wysłaniem pracy do klienta — i nic ponad to.

## Co bierzemy

**(a) All-pass jako nagłówek, odsetek kryteriów jako diagnostyka.** To wprost
naprawia wysycenie, które wyszło dziś przy wariancji. Przy grubych kryteriach
Fable i Sonnet mają po 30/30 i korpus przestał rozróżniać. Przy kryteriach
atomowych i regule all-pass wynik zadania spada do zera na pierwszym potknięciu,
więc znowu jest co mierzyć. Mamy już tę logikę dla zmyśleń — jedno zmyślenie to
FAIL. Rozszerzamy ją na całość.

**(b) Kryterium jako jedyny wzorzec.** Dziś mamy manifest ORAZ instrukcję
sędziego i te dwa dokumenty już się raz rozjechały: manifest umowy 04 kazał
liczyć błąd rachunkowy jako zmyślenie, co było reliktem v1 i wyprodukowało
nieprawdziwy FAIL konfiguracji Haiku w sierpniu. Jeden dokument, jedno miejsce
prawdy.

**(c) Ocena po jednym kryterium naraz.** Nasi sędziowie czytają pięć audytów i
trzydzieści wad w jednym przebiegu — to jest dokładnie ta sytuacja, w której
kryteria wpływają na siebie i w której rozbieżność między sędziami nie da się
przypisać do konkretnego miejsca. Rozbicie na kryteria daje też zrównoleglenie.

**(d) „Obaj sędziowie zgodni" jako liczba raportowana osobno.** Dziś mamy pełną
zgodność Opusa i Gemini na v0.8, ale podaliśmy to opisowo. To ma być kolumna.

**(e) Zakaz watowania.** Daje podstawę do rozstrzygnięcia sprawy 43 flag na 77
poza kluczem: kryterium wchodzi do rubryki wtedy, gdy nadzorujący radca
sprawdziłby to przed wysłaniem pisma klientowi.

## Co zostaje nasze, bo jest mocniejsze

**Dowód przy każdym zarzucie.** Ich prompt sędziego ma cztery zmienne i żąda
JSON-a z werdyktem i krótkim uzasadnieniem — i tyle. Nasza instrukcja v2 wymaga
przy zmyśleniu i przy błędzie rachunkowym **dosłownego cytatu z audytu plus
dowodu ze źródła**, bez dowodu nie wolno zgłosić. Przy narzędziu, którego celem
jest odcinanie halucynacji, to nie jest ozdoba: dzisiejszy zarzut wobec Haiku
(art. 83 ust. 4 RODO) dał się potwierdzić u źródła właśnie dlatego.

**Rozdzielenie zmyślenia od błędu rachunkowego.** U nich jedno i drugie to po
prostu niezaliczone kryterium. U nas to dwie metryki o różnym skutku, bo
arytmetykę naprawia kalkulator, a zmyślenia nie naprawia nic poza zmianą modelu.
Wariancja z dzisiaj pokazała, że to działa na żywych danych: zmyślenia 0/0/0,
błędy rachunkowe 0/1/0.

**Próba negatywna.** Umowa bez wad i mierzenie fałszywych alarmów na obszarach
świadomie czystych. All-pass sam z siebie nie karze nadmiarowego flagowania —
zadanie przechodzi albo nie, a dopychanie ryzyk nie obniża wyniku, dopóki nie
złamie żadnego kryterium.

## Czego nie bierzemy

**Skali.** 984 zadania, z czego 498 umownych, przy 75 tysiącach kryteriów pisanych
przez prawników. To zespół na etacie. Nasza przewaga jest w jednym: prawo polskie.

**Samego all-pass bez diagnostyki.** Przy pięciu umowach all-pass dałby 0/5 i
żadnego gradientu do pracy. Dlatego bierzemy ich układ w całości: all-pass jako
liczba nagłówkowa, odsetek kryteriów jako liczba robocza.

## Droga wdrożenia bez ani jednej nowej umowy

1. Rozpisać 30 wad na kryteria atomowe z liczbą w treści. Materiał już jest —
   nasze umowy mają kwoty, stawki i terminy, a manifest ma pola `liczby`.
   Szacunek po ich ziarnistości: 40–60 kryteriów na umowę.
2. Przenieść `match_criteria` do manifestu i wyrzucić z instrukcji sędziego
   wszystko, co powtarza wzorzec.
3. Sędzia per kryterium, dwóch dostawców, temperatura 0, raport z kolumną
   „obaj zgodni".
4. Zachować nasze trzy metryki, których u nich nie ma: zmyślenia jako twarde
   zero z dowodem, błędy rachunkowe osobno, fałszywe alarmy na obszarach czystych.
5. Dopiero potem rozbudowa korpusu — bo po punkcie 1 wiadomo, czy pięć umów
   jeszcze rozróżnia.
