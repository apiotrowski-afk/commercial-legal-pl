---
type: Klauzula
title: Prawa autorskie / Własność intelektualna
tags: [prawa-autorskie, IP, pola-eksploatacji, prawa-zależne, open-source, copyleft, licencja, AI-generowane, wizerunek, white-label]
contract_types: [B2B-IT, body-leasing, wdrożenie, licencyjna, NDA, maintenance]
risk_level: krytyczny
mandatory_for: [B2B-IT, body-leasing, wdrożenie]
requires: [03-definicje.md, 06-wynagrodzenie.md]
timestamp: 2026-06-27
---

# Prawa autorskie / Własność intelektualna

## Kiedy stosować i na co uważać

Kto jest właścicielem rezultatów pracy, na jakich polach eksploatacji, kiedy następuje przeniesienie. To najczęściej niedostatecznie uregulowany obszar w umowach IT — a jednocześnie najdroższy w skutkach.

### ⚠️ Red flags

Brak wskazania pól eksploatacji (przeniesienie nieskuteczne — art. 41 ust. 2 PrAut). Brak uregulowania praw do komponentów open-source / third-party. Moment przeniesienia nieokreślony. Brak przeniesienia prawa do wykonywania praw zależnych. Klauzula licencyjna zamiast przeniesienia bez uzasadnienia biznesowego. Szeroka klauzula „przenosi prawa do wszystkich rezultatów" bez rozróżnienia utwór / nie-utwór — przy wytworach zdeterminowanych technicznie lub wygenerowanych przez AI przeniesienie bywa **bezprzedmiotowe** (nie ma czego przenieść).

> **Zanim ocenisz pola eksploatacji** — sprawdź, czy wytwór w ogóle jest utworem: `references/baza-wiedzy/15-ochrona-utworu-test.md` (test dwustopniowy, decyzyjnik dla kodu/GUI/baz danych/wytworu AI). Rezultat nie-utwór wymaga alternatywnego tytułu (tajemnica przedsiębiorstwa, zobowiązanie umowne), nie przeniesienia praw autorskich.

## ⭐ Dwie zasady KTZR przy przenoszeniu praw

Obowiązują **zawsze**, gdy reprezentujemy stronę **nabywającą** prawa. Przy stronie zbywającej odwracamy je świadomie (zawężamy katalog, wyceniamy nowe pola odrębnie).

### Zasada 1 — pola eksploatacji wymieniaj maksymalnie szeroko

Umowa obejmuje **wyłącznie pola wyraźnie w niej wymienione** (art. 41 ust. 2 PrAut). Pole pominięte zostaje przy twórcy — i nie da się go „dorozumieć" z celu umowy. Dlatego katalog budujemy **wyczerpująco, nie przykładowo**, z opisem sposobu korzystania (nie tylko nazwą ustawową) i z odniesieniem do nośników oraz technik nieznanych z nazwy.

Nie wystarcza lista czterech haseł („utrwalanie, zwielokrotnianie, modyfikowanie, rozpowszechnianie") — pełny katalog niżej.

### Zasada 2 — klauzula nowych pól eksploatacji

Umowa **nie może** obejmować pól nieznanych w chwili jej zawarcia (art. 41 ust. 4 PrAut) — takie postanowienie jest w tym zakresie bezskuteczne. Rozwiązanie: nie przenosimy praw na przyszłe pola, tylko **zobowiązujemy zbywcę do ich przeniesienia na wezwanie** (konstrukcja zobowiązaniowa, nie rozporządzająca), z terminem i bez dodatkowego wynagrodzenia.

Dlaczego „bez dodatkowego wynagrodzenia" trzeba napisać **wprost**: twórcy przysługuje odrębne wynagrodzenie za korzystanie na każdym odrębnym polu, **chyba że umowa stanowi inaczej** (art. 45 PrAut). Milczenie umowy = ryzyko roszczenia o dopłatę za każde pole.

> **Klauzula wzorcowa — nowe pola eksploatacji**
>
> Gdyby w przyszłości powstały pola eksploatacji inne niż wymienione w ust. [2], [Zbywca] **zobowiązuje się** przenieść na [Nabywcę] autorskie prawa majątkowe w zakresie tych pól **bez dodatkowego wynagrodzenia**. Zobowiązanie podlega wykonaniu na pisemne wezwanie, w ciągu [7] dni od jego doręczenia.

Przy audycie: brak tej klauzuli w umowie nabywcy praw → flaga 🟡 (za 5 lat nowy kanał dystrybucji wymaga renegocjacji z twórcą, często z pozycji słabszej). Klauzula skonstruowana jako **przeniesienie** na przyszłe pola (nie zobowiązanie) → 🟠, bo w tym zakresie bezskuteczna.

### Klauzula wzorcowa (generyczny IT)

> Wykonawca przenosi na Zamawiającego autorskie prawa majątkowe do wszystkich Utworów powstałych w wykonaniu Umowy, z chwilą zapłaty wynagrodzenia za dany okres rozliczeniowy, na następujących polach eksploatacji: (a) utrwalanie i zwielokrotnianie; (b) wprowadzanie do pamięci komputera i sieci; (c) modyfikowanie i opracowywanie; (d) rozpowszechnianie. Przeniesienie obejmuje również prawo do wykonywania praw zależnych. Wynagrodzenie za przeniesienie praw jest wliczone w stawkę.

## Klauzule z umów KTZR

### Body Leasing IT (KTZR)

> Z chwilą zaakceptowania Timesheetu Usługodawca przenosi na Usługobiorcę całość autorskich praw majątkowych do Utworów, bez ograniczeń czasowych i terytorialnych, na polach eksploatacji: (a) utrwalanie i zwielokrotnianie; (b) wprowadzanie do pamięci komputera oraz sieci; (c) modyfikowanie, tłumaczenie, opracowywanie; (d) rozpowszechnianie; (e) obrót oryginałem i egzemplarzami.

> Usługodawca przenosi na Usługobiorcę prawo do wykonywania i zezwalania osobom trzecim na wykonywanie zależnych praw autorskich do Utworów.

> Usługodawca oświadcza, że zawarł ze Specjalistami umowy zapewniające przeniesienie autorskich praw majątkowych w zakresie niezbędnym do wykonania ust. 1 i 2, a Specjaliści nie zachowują żadnych praw wyłącznych do Utworów.

> Usługodawca gwarantuje, że Utwory są oryginalne, wolne od wad prawnych i roszczeń osób trzecich.

### Umowa licencyjno-doradcza

> Licencjodawca udziela Licencjobiorcy odpłatnej, niewyłącznej, niezbywalnej i nieprzenoszalnej licencji, bez prawa do udzielania sublicencji, na korzystanie z Know-how.

> Udzielenie Licencji nie przenosi na Licencjobiorcę żadnych praw własności intelektualnej do Know-how. Licencjobiorca nie jest uprawniona do modyfikowania, adaptowania, dekompilowania, odtwarzania kodu źródłowego ani tworzenia opracowań bez uprzedniej pisemnej zgody Licencjodawcy.

⚠️ W zakresie, w jakim Know-how obejmuje programy komputerowe: bezwzględny zakaz dekompilacji jest nieważny co do dekompilacji dla interoperacyjności — art. 75 ust. 3 PrAut jest semiimperatywny (art. 58 § 1 KC). Dla Know-how niebędącego programem komputerowym pełny zakaz modyfikacji może być skuteczny.

### NDA IT (KTZR)

> Niniejsza Umowa nie przenosi na Stronę Otrzymującą żadnych praw własności intelektualnej, licencji, patentów, znaków towarowych ani innych uprawnień. Udostępnienie Informacji Poufnych nie stanowi udzielenia licencji.

### Zgoda na wizerunek (umowa o pracę)

> Dobrowolnie wyrażam zgodę na nieodpłatne wykorzystanie i rozpowszechnianie mojego wizerunku dla celów marketingowych Spółki [...] bez ograniczeń terytorialnych oraz czasowych, pod warunkiem że po zakończeniu stosunku zatrudnienia obejmuje ona wyłącznie materiały opublikowane przed dniem ustania stosunku pracy.

### Gwarancja czystości IP i zakaz odtwarzania kodu (umowa wdrożeniowa / maintenance IT)

> Wykonawca oświadcza i gwarantuje, że: (a) przysługuje mu pełnia autorskich praw majątkowych do Utworów i jest uprawniony do ich przeniesienia bez ograniczeń; (b) Utwory są oryginalne i wolne od wad prawnych oraz roszczeń osób trzecich; (c) W przypadku gdy Wykonawca korzystał z pomocy osób trzecich, zawarł z nimi skuteczne umowy przenoszące na niego prawa do wyników ich pracy; (d) w przypadku gdy Utwory zostały wytworzone z zastosowaniem systemów sztucznej inteligencji, udział twórczy człowieka w wykonaniu Utworu jest wystarczający do uznania efektów za utwór w rozumieniu ustawy o prawie autorskim i prawach pokrewnych.

> Wykonawca zobowiązuje się do bezwzględnego powstrzymania się od jakiegokolwiek wykorzystywania, kopiowania, odtwarzania (w tym inżynierii wstecznej), dekompilacji, modyfikowania lub tworzenia utworów zależnych na bazie Oprogramowania, jego kodów źródłowych, logiki działania lub architektury — na rzecz własną lub osób trzecich. Zakaz ma charakter bezterminowy i dotyczy całości, jak i jakiejkolwiek części Oprogramowania.

### Zakaz komponentów copyleft (umowy IT — ochrona kodu produkcyjnego)

> Komponenty Open Source mogą być wykorzystywane wyłącznie na licencjach permisywnych niewymagających ujawnienia kodu pochodnego (w szczególności MIT, BSD, Apache 2.0). Zakazane jest stosowanie komponentów na licencjach copyleft nakładających obowiązek udostępnienia kodu źródłowego dzieł pochodnych (w szczególności GPL, LGPL, AGPL). Naruszenie zobowiązuje Wykonawcę do naprawienia szkody Zamawiającego w pełnej wysokości, w tym kosztów zastąpienia wadliwych komponentów i obsługi prawnej.

### Pełne przeniesienie praw z zachowaniem pól eksploatacji i praw zależnych (maintenance IT)

> Z chwilą odbioru Utworu oraz zapłaty wynagrodzenia na Zamawiającego przechodzą wszelkie autorskie prawa majątkowe do Utworu. Przeniesienie obejmuje wszystkie znane w chwili przeniesienia pola eksploatacji, w tym: (a) utrwalanie i zwielokrotnianie techniką cyfrową; (b) wprowadzanie do pamięci komputera i sieci; (c) modyfikowanie, adaptowanie, tłumaczenie; (d) rozpowszechnianie, w tym w modelu SaaS i chmurowym; (e) publiczne udostępnianie w sieciach; (f) wdrażanie w systemach AI i uczeniu maszynowym. Przeniesienie następuje bez ograniczeń terytorialnych i czasowych.

> Wraz z przeniesieniem autorskich praw majątkowych Wykonawca przenosi prawo do wykonywania i zezwalania na wykonywanie zależnych praw autorskich, w tym modyfikacji, lokalizacji, kompilacji i opracowań udostępnianych pod marką Zamawiającego bez wskazywania Wykonawcy jako twórcy (model white-label). Dla Utworów stanowiących program komputerowy zastosowanie znajduje art. 77 PrAut, wyłączający sprzeciw wobec modyfikacji i nadzór autorski.

> Na pisemne wezwanie Zamawiającego Wykonawca zobowiązuje się zawrzeć umowę przenoszącą autorskie prawa majątkowe do Utworów na każde nowe pole eksploatacji, które stanie się znane po dacie zawarcia Umowy — bez prawa do dodatkowego wynagrodzenia, w terminie 14 dni od wezwania.

⚠️ Zobowiązanie do zawarcia umowy na **przyszłe pola eksploatacji** może być kwestionowane na podstawie art. 41 ust. 4 PrAut — umowa może obejmować wyłącznie pola znane w chwili zawarcia; nieważność klauzuli grozi z art. 58 § 1 KC. Bezpieczniejsza alternatywa: zostawić warunki (cenę i zakres) do negocjacji na moment, gdy nowe pole stanie się znane.

### ⭐ Pełna klauzula IP z wyczerpującym katalogiem pól (umowa zlecenia / ramowa)

Wzorzec do stosowania po stronie **nabywcy praw**. Realizuje obie zasady KTZR: wyczerpujący katalog pól + zobowiązanie do przeniesienia na nowe pola.

> **§ [X]. Materiały i prawa autorskie**
>
> 1. Gdy rezultatem danego zlecenia ma być utwór w rozumieniu ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych, w propozycji wskazuje się: a) rodzaj materiału objętego zamówieniem; b) zakres, w jakim Zleceniodawca będzie z niego korzystał; c) zasady nabycia praw inne niż przewidziane w ust. 2, o ile Strony tak postanowią.
>
> 2. Zleceniobiorca przenosi na Zleceniodawcę — z chwilą wydania materiału oraz uiszczenia wynagrodzenia — autorskie prawa majątkowe do utworów powstałych przy realizacji przyjętego zlecenia, **bez ograniczeń czasowych i terytorialnych**, w zakresie następujących pól eksploatacji:
>    a) **utrwalanie i zwielokrotnianie** utworu każdą techniką oraz w każdym formacie — w szczególności drukarską, reprograficzną, cyfrową, a także zapisem magnetycznym i optycznym — bez względu na system, standard i rodzaj nośnika, w tym wytwarzanie egzemplarzy utworu;
>    b) **wprowadzanie do pamięci komputera** oraz pozostałych urządzeń, a także przechowywanie, również przy użyciu usług przetwarzania w chmurze, i umieszczanie utworu w sieciach teleinformatycznych;
>    c) **publiczne udostępnianie** utworu w sposób pozwalający każdemu uzyskać do niego dostęp w wybranym przez siebie miejscu i czasie, w szczególności w serwisach społecznościowych, w serwisach służących publikacji wideo, na stronach internetowych i w aplikacjach mobilnych, a także w komunikacji elektronicznej;
>    d) **publiczne wykonanie i wystawienie, wyświetlenie oraz odtworzenie, a także nadawanie i reemitowanie** — również drogą satelitarną, w sieciach kablowych oraz w sieciach teleinformatycznych;
>    e) **wprowadzanie do obrotu, użyczenie i najem** egzemplarzy utworu albo jego oryginału;
>    f) **wykorzystanie całości utworu oraz dowolnych jego fragmentów**, zarówno odrębnie, jak i w zestawieniu z innymi utworami, w szczególności w materiałach audiowizualnych i multimedialnych;
>    g) **wykorzystanie na potrzeby informacyjne, promocyjne, reklamowe i marketingowe** Zleceniodawcy, także w materiałach opracowywanych przez podmioty działające na jego rzecz.
>
> 3. Jeżeli w przyszłości pojawią się **nowe pola eksploatacji** inne niż wskazane w ust. 2, Zleceniobiorca zobowiązuje się przenieść na Zleceniodawcę — na jego pisemne żądanie i **bez dodatkowego wynagrodzenia** — autorskie prawa majątkowe do utworów na tych polach, w ciągu [7] dni od doręczenia żądania.
>
> 4. Kwota przewidziana w [załączniku cenowym] dla właściwej kategorii usługi zawiera w sobie zapłatę z tytułu przeniesienia autorskich praw majątkowych **na wszystkich polach eksploatacji wymienionych w ust. 2 i 3**.
>
> 5. Z chwilą przeniesienia praw Zleceniodawca uzyskuje od Zleceniobiorcy **zezwolenie na wykonywanie zależnego prawa autorskiego**, obejmujące sporządzanie opracowań, skrótów, modyfikacji i adaptacji utworu oraz korzystanie z nich i rozporządzanie nimi; Zleceniobiorca **przenosi również własność nośników**, na których materiał został wydany.
>
> 6. Zleceniobiorca przyjmuje na siebie obowiązek **powstrzymania się od wykonywania wobec Zleceniodawcy autorskich praw osobistych** do utworów, o których mowa w ust. 2, w zakresie, w jakim utrudniałoby to korzystanie z nich w sposób przewidziany Umową — dotyczy to zwłaszcza prawa nadzoru nad sposobem korzystania z utworu — oraz **upoważnia Zleceniodawcę do rozpowszechniania tych utworów bez wskazywania autorstwa**.
>
> 7. W razie wydania Zleceniodawcy materiału, do którego nie stosuje się ust. 2, Zleceniodawcy przysługuje licencja **niewyłączna**, nieograniczona terytorialnie, upoważniająca do korzystania z materiału w zakresie niezbędnym do osiągnięcia celu, w jakim materiał ten powstał. Zapłata należna **Zleceniobiorcy** z tytułu udzielenia tej licencji mieści się w wynagrodzeniu przewidzianym w [załączniku cenowym].
>
> 8. W materiałach o charakterze promocyjnym **wizerunek lub głos** Zleceniobiorcy mogą być rozpowszechniane wyłącznie na podstawie osobnej, dobrowolnej zgody, wskazującej zakres i sposób takiego wykorzystania.

**Trzy elementy, które ratują tę klauzulę w praktyce:**

- **ust. 5** — samo przeniesienie praw majątkowych **nie daje** prawa do modyfikacji: prawa zależne wymagają odrębnego zezwolenia (art. 2 PrAut). Bez tego nabywca nie może legalnie zrobić skrótu ani adaptacji. Dochodzi przeniesienie własności nośnika — odrębne od praw (art. 52 PrAut).
- **ust. 6** — praw osobistych **nie da się przenieść ani zrzec** (art. 16 PrAut), więc konstruujemy: zobowiązanie do niewykonywania + upoważnienie do rozpowszechniania bez oznaczania autorstwa. Formuła „przenosi prawa osobiste" byłaby nieważna.
- **ust. 1 lit. c + ust. 7** — rozdzielenie: materiał **zamówiony** (przeniesienie z ust. 2) vs materiał **przekazany przy okazji** (licencja niewyłączna). Bez tego rozdziału albo nabywca nie ma nic do materiałów pobocznych, albo klauzula obejmuje wszystko i staje się nadmierna.

**Formalności, o których nie wolno zapomnieć:** przeniesienie praw i licencja wyłączna wymagają **formy pisemnej pod rygorem nieważności** (art. 53 i art. 67 ust. 5 PrAut) — mail nie wystarcza. Zob. `baza-wiedzy/15-ochrona-utworu-test.md`.

> **Uwaga redakcyjna:** w wersji roboczej tej klauzuli ust. 4 odsyłał do „zdania poprzedzającego" (rozjazd — chodzi o ust. 2 i 3), a ust. 7 przyznawał wynagrodzenie za licencję Zleceniodawcy zamiast Zleceniobiorcy. Oba poprawione powyżej. Typowy przykład błędów, które łapie `workflows/weryfikacja-spojnosci-odeslan.md` (odesłania) i R11 (nazwy stron).
