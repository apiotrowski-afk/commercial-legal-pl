# Metoda pomiaru — v2 (dla v0.8)

Pilot z sierpnia 2026 (`wyniki/pilot/PODSUMOWANIE.md`) dał liczby, ale miał
cztery dziury, które same w sobie przesądzają o tym, ile te liczby znaczą. Ten
dokument je zamyka. Opisuje stan docelowy; przy każdym punkcie stoi, co jest
już zrobione, a co czeka.

## 1. Sędzia z innej rodziny modeli niż audytowany

**Dziura:** w pilocie sędziami było sześciu agentów Fable, a najwyższy wynik
(100% wykrywalności, zero wszystkiego) dostała konfiguracja `fable-skill`.
Sędzia oceniał model z własnej rodziny. To jest podręcznikowa stronniczość
samopreferencji i bez kontroli nie da się powiedzieć, czy te 100% to wynik
metody, czy rozpoznanie własnego stylu wypowiedzi.

**Zasada:** każdy audyt ocenia sędzia z rodziny innej niż audytowana. Wynik
raportujemy z nazwą rodziny sędziego. Gdy rodziny się pokrywają — osobna
adnotacja przy liczbie.

**Zgodność sędziów:** te same audyty przechodzą przez dwóch sędziów z różnych
rodzin. Raportujemy zgodność per metryka: ile wad obaj uznali za wykryte, ile
tylko jeden, i gdzie się rozjechali. Rozjazd większy niż różnice między
konfiguracjami oznacza, że ranking konfiguracji jest szumem sędziego.

**Granica tej kontroli — zamknięta 7.10.2026.** Opus i Fable to różne linie
modeli, ale ten sam dostawca, więc przesądzenie samo w sobie nie wykluczało
wspólnych ślepych plam. Kontrolę domknął **Gemini 2.5 Pro przez Vertex AI**
(projekt ktzr-asystent, lokalizacja `global`, temperatura 0), uruchamiany
skryptem na poświadczeniach gcloud — bez przeglądarki i bez osobnego klucza.
Na pomiarze v0.8 zgodność z sędzią Opus jest pełna na każdej punktowanej
metryce. Od tej pory pomiar bez sędziego spoza dostawcy opisujemy jako
niepełny.

*Stan: przesądzenie pilotu sędzią Opus — zrobione, wyniki w `wyniki/pilot/oceny-v2/`.*

## 2. Powtórzenia i statystyka parowana

**Dziura:** pilot to jeden przebieg na konfigurację. Przy jednym przebiegu
różnica 100% kontra 96,7% to jedna wada, czyli dokładnie tyle, ile potrafi
zmienić losowość próbkowania. Wariancja była nieznana, a mimo to liczby
porównywano między konfiguracjami.

**Zasada:** k = 3 przebiegi na parę (konfiguracja × umowa), ta sama umowa, ten
sam prompt, różne losowanie. Jednostką analizy jest pojedyncza posiana wada,
nie umowa — daje to 30 obserwacji na przebieg zamiast pięciu.

**Test:** porównania „ze skillem kontra bez skilla" robimy **na tym samym
modelu**, więc są parowane. Dla wyniku binarnego (wada wykryta albo nie) na
tych samych 30 wadach właściwy jest test McNemara. Przy k > 1 najpierw liczymy
odsetek wykryć na wadę, potem porównujemy parowanym testem rangowym Wilcoxona.

**Czego ten test nie da:** przy 30 wadach różnice poniżej około 10 punktów
procentowych i tak zostaną w przedziale ufności. Benchmark ma wykrywać
regresje i duże delty metody, nie rozstrzygać, czy model A jest o dwa punkty
lepszy od B. To ograniczenie zostaje w raporcie, nie w przypisie.

*Stan: do uruchomienia.*

## 3. Zmyślenie to nie to samo co błąd rachunkowy

**Dziura:** pilot wrzucał do jednej metryki „twardego zera" trzy różne rzeczy:
zmyślony cytat, błędnie powołany przepis i źle wykonane mnożenie. Haiku dostał
przez to FAIL za arytmetykę, mimo że liczby wziął z umowy prawidłowo.

**Zasada:** dwie osobne metryki.
- **Zmyślenie** — treść, której w źródle nie ma: cytat nieobecny w umowie,
  liczba przypisana umowie wbrew jej tekstowi, przepis, który nie reguluje
  tego, co audyt mu przypisuje. Twarde zero, jedno zmyślenie to FAIL.
- **Błąd rachunkowy** — liczby wzięte z umowy prawidłowo, działanie wykonane
  źle. Raportowany osobno, **nie jest FAIL**.

Rozstrzyga pochodzenie liczb, nie wielkość błędu. Skutek praktyczny jest różny:
zmyślenia nie naprawia nic poza zmianą modelu, błąd rachunkowy naprawia
deterministyczny kalkulator podpięty pod R12.

*Stan: zrobione, `manifesty/instrukcja-sedziego-v2.md`.*

## 4. Próby negatywne

**Dziura:** fałszywe alarmy liczono właściwie tylko na umowie 03, bo tylko ona
jest w całości czysta. Mianownik był więc jedną umową na pięć.

**Zasada:** mianownikiem są wszystkie obszary z pól `czyste_obszary` we
wszystkich pięciu manifestach plus cała umowa 03. Fałszywy alarm to flaga
KRYTYCZNE albo WYSOKIE postawiona na takim obszarze. Uwaga ŚREDNIA lub NISKA
nią nie jest — to kalibracja, nie błąd.

**Policzone 6.10.2026: mianownik to trzy obszary.** Po jednym w umowach 01, 02
i 04; umowy 03 i 05 nie mają wypełnionego pola w ogóle. Razem z umową 03 jako
całością daje to cztery miejsca, w których fałszywy alarm da się w ogóle
zauważyć, wobec 30 miejsc, w których mierzymy wykrywalność. Zdanie „zero
fałszywych alarmów" znaczy więc dziś znacznie mniej, niż brzmi.

Wniosek, wbrew temu, co zakładałem przed policzeniem: **tego punktu nie da się
domknąć samą zmianą metody.** Trzeba dopisać czyste obszary do istniejących
pięciu umów — każdy taki wpis to twierdzenie prawne, że dana klauzula jest
świadomie w porządku, więc wymaga przejścia prawnika po tekście, nie
automatu. Nowe umowy nie są potrzebne, ale praca merytoryczna tak.

*Stan: wymaga przeglądu pięciu umów pod kątem obszarów świadomie czystych.*

## 5. Holdout z zatrzymanym kluczem

**Dziura:** cały manifest leży w repozytorium. Każda kolejna wersja skilla jest
rozwijana z dostępem do pełnego klucza, więc wzrost wyniku może być
dopasowaniem do testu, a nie poprawą metody.

**Zasada bez powiększania korpusu:** część posianych wad zostaje wyjęta z
jawnego manifestu do pliku zatrzymanego. W repozytorium zostaje **suma
kontrolna SHA-256** tego pliku wraz z datą — dzięki temu da się później
udowodnić, że klucz nie zmienił się po pomiarze. Zatrzymane wady ujawniamy
dopiero w raporcie z pomiaru, razem z wynikiem.

Wynik raportujemy wtedy w dwóch liczbach: na części jawnej i na zatrzymanej.
Rozjazd między nimi jest miarą dopasowania do testu.

*Stan: do ustalenia z Adamem, które wady idą do zatrzymanych i gdzie leży plik.*

## Co zostaje poza zakresem tej wersji

Rozbudowa korpusu z pięciu do piętnastu umów to osobne zadanie. Ten dokument
celowo nie wymaga ani jednej nowej umowy — chodzi o to, żeby najpierw wiedzieć,
ile znaczą liczby z korpusu, który już jest.
