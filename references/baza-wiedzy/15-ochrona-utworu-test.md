# Czy wytwór IT jest utworem — test ochrony prawnoautorskiej

**Źródło:** opracowanie KTZR — Kancelaria Radców Prawnych Żurawska Piotrowski i Wspólnicy, Gdańsk (ktzr.pl).
**Powiązania:** `baza-klauzul/08-prawa-autorskie-ip.md`, `baza-wiedzy/02-przeniesienie-praw-oprogramowanie.md`, `baza-klauzul/21-polityka-ai.md`.
**Status:** zatwierdzone do bazy wiedzy KTZR.

## TL;DR — co Claude musi wiedzieć

1. Klauzula IP przenosi prawa **do utworu**. Jeśli wytwór **nie jest utworem**, przeniesienie praw autorskich jest **bezprzedmiotowe** — nie ma czego przenieść. To luka, którą łatwo przeoczyć: umowa mówi „przenosi prawa do wszystkich rezultatów", a część rezultatów w ogóle nie podlega ochronie.
2. **Zanim** ocenisz pola eksploatacji i moment przejścia — sprawdź, czy wytwór spełnia przesłanki utworu (art. 1 ust. 1 PrAut).
3. **Sam nakład pracy nie tworzy utworu** („sweat of the brow" nie wystarcza — zgodnie z prawem UE i polskim). Liczy się twórczy, indywidualny wybór człowieka.
4. **Wytwór wygenerowany w całości przez AI, bez twórczego wkładu człowieka, nie jest utworem** — nie ma czego przenosić ani licencjonować jako prawo autorskie.

> **Dyscyplina cytatów (R1):** numery artykułów i sygnatury (art. 1, 74 PrAut; orzecznictwo TSUE) to mapa referencyjna. W raporcie każdy cytat przepisu przepuść przez `verify_article()` lub oznacz `[NIEZWERYFIKOWANE]`; sygnatur TSUE nie podawaj z pamięci.

## Test dwustopniowy — czy to utwór (art. 1 ust. 1 PrAut)

Utwór to **przejaw działalności twórczej o indywidualnym charakterze, ustalony w jakiejkolwiek postaci**. Rozłóż to na dwa kroki:

**Krok 1 — Określony, identyfikowalny sposób wyrażenia + ustalenie.** Czy istnieje dostatecznie określony i obiektywnie identyfikowalny sposób wyrażenia (nie sama idea, wrażenie, ogólna koncepcja), który został ustalony w jakiejkolwiek postaci? Unijny wymóg „wyrażenia z wystarczającą precyzją i obiektywnością" (Levola Hengelo C-310/17) jest funkcjonalnie zbliżony do polskiego „ustalenia", ale to **nie te same pojęcia** — mapowanie jest prounijną wykładnią doktrynalną, nie literalnym brzmieniem ustawy.

**Krok 2 — Oryginalność: swobodne, twórcze wybory człowieka.** Czy wytwór jest rezultatem **swobodnych, twórczych wyborów** odzwierciedlających osobowość autora — a nie rezultatem z góry zdeterminowanym? Odpowiada „własnej twórczości intelektualnej" z linii Infopaq C-5/08, Painer C-145/10, Cofemel C-683/17 (dwa elementy: oryginalny przedmiot + jego wyrażenie), którą w prawie polskim odczytuje się przez przesłanki „działalności twórczej" i „indywidualnego charakteru".

Obie przesłanki muszą być spełnione łącznie. Brak którejkolwiek → **nie utwór**.

**Formy i granice, o których łatwo zapomnieć:** przeniesienie autorskich praw majątkowych wymaga **formy pisemnej pod rygorem nieważności** (art. 53 PrAut), tak samo licencja wyłączna (art. 67 ust. 5); umowa może dotyczyć tylko pól eksploatacji **znanych** w chwili jej zawarcia (art. 41 ust. 4). Program stworzony przez **pracownika** w ramach obowiązków — prawa majątkowe przysługują pracodawcy (art. 74 ust. 3), ale reguła ta **nie stosuje się automatycznie do kontraktorów B2B** — tu potrzebne jest przeniesienie w umowie.

## Cztery podstawy wyłączenia ochrony

Wytwór **nie jest utworem** (lub ochrona jest wyłączona), gdy zachodzi którakolwiek:

| Podstawa | Na czym polega | Podstawa prawna |
|---|---|---|
| **Determinacja funkcją/techniką** | Kształt podyktowany wyłącznie funkcją techniczną — brak pola na twórczy wybór | art. 1 ust. 2¹ PrAut (ochrona tylko sposobu wyrażenia, nie idei/procedur/metod) |
| **Determinacja regułą/standardem** | Wytwór narzucony przez normę, standard, wymóg interoperacyjności, składnię języka | art. 74 ust. 2 PrAut (idee i zasady, w tym interfejsów, poza ochroną) |
| **Sam nakład pracy (sweat of the brow)** | Sam nakład pracy, umiejętności lub środków nie przesądza o utworze, jeżeli rezultat nie wyraża swobodnych i twórczych wyborów (np. mechaniczne zestawienie danych) | art. 1 ust. 1 — brak oryginalności rozumianej jako własna twórczość intelektualna |
| **Idea, a nie wyrażenie** | Chroniony jest sposób wyrażenia, nie sama koncepcja, algorytm, funkcjonalność | art. 1 ust. 2¹ PrAut |

## Decyzyjnik dla typowych wytworów IT

| Wytwór | Utwór? | Uwaga |
|---|---|---|
| **Kod źródłowy** (autorski, nieszablonowy) | zwykle TAK | program komputerowy chroniony jak utwór literacki (art. 74 ust. 1 PrAut); ochrona obejmuje formy wyrażenia, **nie** idee i zasady będące podstawą elementów programu, w tym „łączy" — interfejsów (art. 74 ust. 2; por. SAS Institute C-406/10, BSA C-393/09) |
| **Kod generyczny / boilerplate / wygenerowany z szablonu** | często NIE | brak twórczego wyboru — kod zdeterminowany frameworkiem/standardem |
| **GUI / układ interfejsu** | zależnie | GUI **nie jest formą wyrażenia programu**, ale może być **odrębnym utworem**, jeśli jego konkretny sposób wyrażenia jest oryginalny (BSA C-393/09); sama funkcjonalność, logika działania, język programowania, formaty danych — nie (SAS C-406/10) |
| **Baza danych** | możliwa **kumulacja** | twórczy dobór/układ/zestawienie → utwór (art. 3 PrAut); niezależnie od tego baza wymagająca istotnego nakładu na **sporządzenie, weryfikację lub prezentację zawartości** → ochrona **sui generis** (ustawa o ochronie baz danych). Oba reżimy **mogą występować łącznie**; inwestycja w samo wytworzenie danych nie wystarcza |
| **Dokumentacja techniczna** | zwykle TAK | jeśli ma indywidualny charakter; czysto techniczne, szablonowe zestawienia — wątpliwe |
| **Konfiguracja / pliki ustawień** | zwykle NIE | zdeterminowane technicznie, brak twórczego wyboru |
| **Wytwór w całości wygenerowany przez AI** | co do zasady NIE | wg dominującego stanowiska brak twórcy-człowieka i twórczych wyborów w końcowym wyrażeniu (zob. niżej); obszar w rozwoju, bez rozstrzygającego orzecznictwa PL/UE |

## Wytwór AI a ochrona — konsekwencje dla klauzuli IP

To gorący punkt w umowach IT. Reguły:

1. **Output wygenerowany autonomicznie przez AI** (prompt → wynik, bez twórczych wyborów człowieka w końcowym sposobie wyrażenia) — zgodnie z **dominującym stanowiskiem** nie stanowi utworu w rozumieniu PrAut (antropocentryczna konstrukcja ustawy). W tym zakresie nie powstają autorskie prawa majątkowe, które można by przenieść. **Zastrzeżenie:** brak rozstrzygającego orzecznictwa polskiego i unijnego; próg i charakter wkładu człowieka pozostają w doktrynie sporne. **Nie pisz szeroko „nie ma czego przenieść"** — odrębnie oceń prawa do wkładów ludzkich, materiałów wejściowych, twórczej selekcji/kompozycji/modyfikacji wyniku, bazy danych i innych komponentów rezultatu.
2. **Wytwór AI-assisted** — ochrona zależy od **zakresu twórczego wkładu człowieka**: jeśli końcowy sposób wyrażenia odzwierciedla dostatecznie konkretne, swobodne wybory człowieka (dobór, selekcja, kompozycja, istotna modyfikacja), rezultat może być utworem w części odzwierciedlającej ten wkład. **Samo wydanie ogólnego polecenia (promptu) nie przesądza o autorstwie.**
3. **Konsekwencja dla umowy:** przy wytworach z udziałem AI klauzula IP nie może opierać się wyłącznie na przeniesieniu praw autorskich. Rozważ:
   - **dokumentowanie wkładu twórczego** człowieka (historia zmian, decyzje projektowe) — zob. `baza-klauzul/21-polityka-ai.md` § 5,
   - **alternatywne tytuły** do wytworu nie-utworu — z kwalifikatorami: **tajemnica przedsiębiorstwa** tylko po spełnieniu przesłanek art. 11 ust. 2 u.z.n.k. (w tym podjęcie z należytą starannością działań poufnościowych); **zobowiązania umowne** (poufność, wyłączność, niekorzystanie) mają skutek **względny** między stronami, nie tworzą prawa wyłącznego wobec wszystkich i podlegają art. 3531/58 KC oraz prawu konkurencji; przeniesienie **własności egzemplarza/nośnika** samo w sobie nie przenosi praw autorskich,
   - **oświadczenie o wkładzie** i zapewnienie co do praw osób trzecich — wynik AI **nie powinien być domyślnie traktowany** jako wolny od praw osób trzecich: może zawierać chronione elementy cudzych utworów lub kodu; przy kodzie open source mogą powstać obowiązki licencyjne wymagające odrębnej analizy (nie każde podobieństwo = naruszenie). Gwarancje umowne nie powinny bezwarunkowo zapewniać „pełnego autorstwa" — opisz poziom wkładu człowieka, źródła komponentów i proces kontroli.

## Jak używać w umowie

1. **Przed klauzulą IP** (audyt lub generowanie) — dla każdej kategorii rezultatu przejdź decyzyjnik: utwór / nie-utwór / sui generis / AI-output.
2. **Rezultat nie-utwór** → nie opieraj się na przeniesieniu praw autorskich; sięgnij po alternatywny tytuł (tajemnica przedsiębiorstwa, zobowiązanie umowne, licencja/egzemplarz).
3. **Rezultat AI-assisted** → dodaj obowiązek dokumentowania wkładu + oświadczenie o czystości prawnej wyniku.
4. Wpięcie w audyt: brak rozróżnienia utwór/nie-utwór przy szerokiej klauzuli „przenosi prawa do wszystkich rezultatów" → flaga 🟠 (klauzula częściowo bezprzedmiotowa, ryzyko sporu o zakres nabytych praw).
