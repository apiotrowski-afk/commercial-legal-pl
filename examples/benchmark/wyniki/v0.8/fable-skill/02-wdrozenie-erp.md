```
konfiguracja: fable-skill
commit skilla: fa26dc0
przebieg: 1 z 1
data: 2026-10-07
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"
```

## AUDYT RYZYK — Umowa wdrożeniowa ERP (NOVA RETAIL sp. z o.o. / CODEX WORKS sp. z o.o.)

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie. Trzy postanowienia są nieważne z mocy prawa (§ 4 ust. 1 w zakresie skutku rozporządzającego, § 5 ust. 1 zd. 2, § 5 ust. 2 zd. 1), a § 8 ust. 2 otwiera Zamawiającemu ekspozycję na sankcje RODO. Umowę trzeba przebudować, a nie poprawiać.

**Parametry przebiegu:** tryb express (bez STOP-ów) · audyt neutralny (przy każdej fladze wskazana strona dotknięta) · tryb PRAWNIK · brak `practice-profile.md` → progi domyślne KTZR · brak MCP `legal-cite` → każdy przepis oznaczony `[NIEZWERYFIKOWANE]` · pamięć kancelarii nie odpytywana (warunek: tylko treść umowy) · trigger mikroprzedsiębiorcy (art. 385⁵ KC [NIEZWERYFIKOWANE]) — **nieaktywny**, obie strony to sp. z o.o.

**Założenie przekrojowe (prawo właściwe).** Umowa wybiera prawo stanu Delaware (§ 8 ust. 1). Obie strony to polskie spółki z o.o., a wdrożenie odbywa się „w infrastrukturze Zamawiającego". Jeżeli wszystkie istotne elementy stanu faktycznego są zlokalizowane w Polsce (lokalizacji infrastruktury umowa nie podaje — `[BRAK DANYCH]`), wybór prawa obcego nie uchyla polskich przepisów bezwzględnie obowiązujących (art. 3 ust. 3 rozporządzenia Rzym I [NIEZWERYFIKOWANE]). Na tym założeniu opiera się ocena ius cogens poniżej. Bez niego ocena się nie zmienia kierunkowo, ale spór zaczyna się od pytania o prawo właściwe.

---

### 🧮 Rachunek ekspozycji

**Liczby wyciągnięte z umowy:** wynagrodzenie ryczałtowe 480.000 zł netto (§ 3 ust. 1) · termin płatności 60 dni od doręczenia faktury (§ 3 ust. 2) · kara 50.000 zł za każdy dzień opóźnienia w płatności, bez sufitu (§ 5 ust. 2) · kary Wykonawcy: 0 (§ 5 ust. 2 zd. 2) · cap kwotowy: brak · termin wdrożenia: „niezwłocznie" (§ 2 ust. 1) · okres wypowiedzenia: brak (§ 7) · okres poufności: brak (§ 6).

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy | 480.000 zł netto (§ 3 ust. 1) | VAT — `[BRAK DANYCH]` w umowie | **480.000 zł netto** |
| Cap Wykonawcy — wina nieumyślna | „wyłącznie za szkody wyrządzone umyślnie" (§ 5 ust. 1) | odpowiedzialność za niedbalstwo wyłączona w całości | **0 zł** |
| Cap Wykonawcy — wina umyślna własna | brak capu; art. 473 § 2 KC [NIEZWERYFIKOWANE] | ustawowo bez limitu | **nieograniczona** |
| Odpowiedzialność Wykonawcy za umyślne działania podwykonawców | wyłączona (§ 5 ust. 1 zd. 2) | wyłączenie nieważne (flaga 🔴 2) → wraca reguła ustawowa | **nieograniczona** po nieważności; 0 zł wg literalnego brzmienia |
| Kary obciążające Wykonawcę | „Wykonawca nie ponosi kar" (§ 5 ust. 2) | — | **0 zł** |
| Kary obciążające Zamawiającego — stawka | 50.000 zł / dzień opóźnienia w płatności | 50.000 / 480.000 | **10,42% wartości umowy dziennie** |
| — próg przekroczenia wartości umowy | — | 480.000 / 50.000 = 9,6 dnia | **10. dzień opóźnienia** (10 × 50.000 = 500.000 zł = 104,2%) |
| — 30 dni opóźnienia | — | 30 × 50.000 | **1.500.000 zł = 312,5% wartości** |
| — 60 dni opóźnienia | — | 60 × 50.000 | **3.000.000 zł = 625% wartości** |
| — 90 dni opóźnienia | — | 90 × 50.000 | **4.500.000 zł = 937,5% wartości** |
| — sufit kary | brak | ekspozycja otwarta; 365 dni = 18.250.000 zł | **3802% wartości rocznie** |
| Kara przy zobowiązaniu pieniężnym — stan prawny | art. 483 § 1 KC [NIEZWERYFIKOWANE] | kara nieważna (flaga 🔴 1) | realna ekspozycja Zamawiającego za opóźnienie = odsetki ustawowe za opóźnienie w transakcjach handlowych + rekompensata za koszty odzyskania (ustawa o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych [NIEZWERYFIKOWANE]); stopa — `[BRAK DANYCH]` w umowie |
| Efektywna ekspozycja Zamawiającego (wg literalnego brzmienia) | 480.000 zł + kary bez sufitu + odpowiedzialność bez capu | np. przy 30 dniach opóźnienia: 480.000 + 1.500.000 | **1.980.000 zł = 4,1× wartości umowy**; bez górnej granicy |
| Efektywna ochrona Zamawiającego przy niewykonaniu wdrożenia | brak kar + odpowiedzialność tylko za winę umyślną + „dołoży starań" | 0 + 0 + (rezultat niewymagalny) | **0 zł** poza przypadkiem udowodnionej winy umyślnej |
| Asymetria kar (Zamawiający : Wykonawca) | 50.000 zł/dzień : 0 zł | iloraz do zera | **∞** (sankcja tylko po jednej stronie) |
| Asymetria wyjścia | Zamawiający: brak prawa wypowiedzenia przed końcem Wdrożenia; Wykonawca: „w każdym czasie" | okres wypowiedzenia Wykonawcy: 0 dni; Zamawiający: brak prawa | **0 dni vs brak prawa** |
| Daty graniczne — termin wdrożenia | „niezwłocznie po podpisaniu" (§ 2 ust. 1) | nie da się policzyć | `[BRAK DANYCH]` — antywzorzec „niezwłocznie" |
| Daty graniczne — płatność | 60 dni od doręczenia faktury (§ 3 ust. 2) | D (doręczenie faktury) + 60 = wymagalność; kara od D+61; przekroczenie wartości umowy w D+70 | 60 dni = **górna granica ustawowa** dla B2B (art. 7 ust. 2 ustawy o przeciwdziałaniu nadmiernym opóźnieniom [NIEZWERYFIKOWANE]) — zgodne, bez zapasu; moment wystawienia faktury `[BRAK DANYCH]` |
| Daty graniczne — przejście praw autorskich | „Z chwilą zapłaty" (§ 4 ust. 1) | najwcześniej D + 0, najpóźniej D + 60 (przy terminowej zapłacie) | między oddaniem systemu a zapłatą Zamawiający korzysta z oprogramowania **bez tytułu** — luka licencyjna do 60 dni (i dłużej przy sporze) |
| Okres poufności | brak (§ 6) | — | bezterminowo / `[BRAK DANYCH]` — ryzyko wypowiedzenia zobowiązania bezterminowego (flaga 🟡 1) |

**Wniosek z rachunku:** umowa przenosi całe ryzyko finansowe na Zamawiającego — dziesięć dni opóźnienia w płatności kosztuje więcej niż cały projekt, a niewykonanie wdrożenia przez Wykonawcę nie kosztuje Wykonawcy nic. Ta konstrukcja nie przetrwa jednak w sądzie w całości: kara z § 5 ust. 2 jest nieważna (art. 483 § 1 KC [NIEZWERYFIKOWANE]), a zestaw wyłączeń po stronie Wykonawcy grozi nieważnością z art. 353¹ w zw. z art. 58 KC [NIEZWERYFIKOWANE]. Każda ze stron, licząc na literalne brzmienie, liczy na coś, czego nie dostanie.

---

### ⛔ Bramka ius cogens (R10) — wynik

| Norma | Postanowienie | Wynik |
|---|---|---|
| art. 483 § 1 KC [NIEZWERYFIKOWANE] — kara tylko za zobowiązanie niepieniężne | § 5 ust. 2 zd. 1 — kara za opóźnienie w płatności | **TRAFIENIE** → nieważność (🔴 1) |
| art. 473 § 2 KC w zw. z art. 474 KC [NIEZWERYFIKOWANE] — wina umyślna | § 5 ust. 1 zd. 2 — wyłączenie winy umyślnej podwykonawców | **TRAFIENIE** (wg linii bazy KTZR; w doktrynie spór — zob. 🔴 2) |
| art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE] — pola eksploatacji | § 4 ust. 1 — „wszelkie prawa autorskie … bez ograniczeń" bez pól | **TRAFIENIE** → brak skutku rozporządzającego (🔴 3) |
| art. 16 PrAut [NIEZWERYFIKOWANE] — prawa osobiste | § 4 ust. 1 — „wszelkie prawa autorskie" | **TRAFIENIE częściowe** — w zakresie praw osobistych nieobjętych art. 77 PrAut [NIEZWERYFIKOWANE] (🔴 3) |
| art. 746 § 3 KC w zw. z art. 750 KC [NIEZWERYFIKOWANE] — wypowiedzenie z ważnych powodów | § 7 ust. 1 | **TRAFIENIE warunkowe** — przy kwalifikacji jako umowa o świadczenie usług (🔴 6) |
| RODO art. 5, 6, 28 [NIEZWERYFIKOWANE] | § 8 ust. 2 — trenowanie AI na danych Zamawiającego; brak umowy powierzenia | **TRAFIENIE** (🔴 4, 🟠 8) |
| art. 353¹ w zw. z art. 58 § 2 KC [NIEZWERYFIKOWANE] — test pięciopunktowy, efekt kumulatywny | § 1 ust. 1 + § 2 ust. 1 + § 5 ust. 1 zd. 1 + § 5 ust. 2 zd. 2 + § 5 ust. 3 + § 7 ust. 2 | **TRAFIENIE** — wydrążenie zobowiązania Wykonawcy (🔴 5) |
| ustawa o przeciwdziałaniu nadmiernym opóźnieniom — termin zapłaty | § 3 ust. 2 — 60 dni od doręczenia faktury | ✓ w granicy ustawowej |
| art. 119 KC, art. 484 § 2 KC [NIEZWERYFIKOWANE] | — | ✓ brak prób modyfikacji przedawnienia ani wyłączenia miarkowania |

---

### 🔴 RYZYKA KRYTYCZNE

#### 1. Kara umowna za opóźnienie w zapłacie — § 5 ust. 2 zd. 1
**Strona dotknięta:** obie — Wykonawca (zabezpieczenie, na które liczy, nie istnieje) i Zamawiający (narażony na żądanie kar i spór, a przy literalnym odczycie na ekspozycję wielokrotności wartości umowy).
**Opis:** „Zamawiający zapłaci karę umowną 50.000 zł za każdy dzień opóźnienia w płatności". Kara umowna może zabezpieczać wyłącznie zobowiązanie niepieniężne (art. 483 § 1 KC [NIEZWERYFIKOWANE]); obowiązek zapłaty wynagrodzenia jest pieniężny. Decyduje funkcja, nie nazwa — tu funkcja jest jednoznaczna. Dodatkowo kara liczona za „opóźnienia", czyli niezależnie od winy Zamawiającego (np. przy wadliwej fakturze).
**Skutek:** postanowienie nieważne (art. 58 § 1 KC [NIEZWERYFIKOWANE]). Wykonawcy pozostają odsetki ustawowe za opóźnienie w transakcjach handlowych i rekompensata za koszty odzyskania należności. Gdyby sąd z jakiegoś powodu kwalifikował świadczenie inaczej — kara 10,42% wartości umowy dziennie i 312,5% po 30 dniach byłaby rażąco wygórowana (art. 484 § 2 KC [NIEZWERYFIKOWANE]); miarkowanie to uprawnienie sądu, nie automat.
**Rekomendacja (preferowana):** wykreślić karę; zabezpieczyć interes Wykonawcy odsetkami ustawowymi, prawem wstrzymania dalszych prac po wezwaniu oraz uzależnieniem przejścia praw od zapłaty (już jest w § 4 ust. 1).
**Fallback (minimum akceptowalne):** jeżeli Wykonawca potrzebuje dodatkowej dyscypliny płatniczej — prawo odstąpienia lub wstrzymania prac po bezskutecznym upływie dodatkowego terminu (np. 14 dni) zamiast kary; żadnej kary za zobowiązanie pieniężne.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md` (kary za zobowiązania niepieniężne, z sufitem), `references/baza-klauzul/06-wynagrodzenie.md`

#### 2. Wyłączenie odpowiedzialności za winę umyślną podwykonawców — § 5 ust. 1 zd. 2
**Strona dotknięta:** Zamawiający.
**Opis:** „…z wyłączeniem winy umyślnej podwykonawców". Dłużnik odpowiada za osoby, którymi się posługuje, jak za własne działania (art. 474 KC [NIEZWERYFIKOWANE]). Odpowiedzialność za te osoby można umownie ograniczać, ale linia przyjęta w bazie wiedzy KTZR (`baza-wiedzy/06`, `05`) stawia granicę na winie umyślnej (art. 473 § 2 KC [NIEZWERYFIKOWANE]); orzeczenie SN z 2023 r. dopuszczające zawężenie odpowiedzialności za osoby trzecie z zastrzeżeniem art. 473 § 2 KC [SYGNATURA NIEZWERYFIKOWANA]. W doktrynie występuje pogląd, że art. 473 § 2 KC chroni wyłącznie przed winą umyślną samego dłużnika (i jego organów), a umyślność pomocników wymaga odrębnej oceny — dlatego skutek nie jest przesądzony, ale ryzyko nieważności jest realne. Umowa nie reguluje przy tym w ogóle dopuszczalności podwykonawstwa, więc Wykonawca może całość prac powierzyć osobom trzecim, za których umyślne działania (np. sabotaż, kradzież danych) nie odpowiada.
**Skutek:** wg linii KTZR — nieważność w tym zakresie i powrót do pełnej odpowiedzialności z art. 474 KC; wg literalnego brzmienia — Zamawiający bez ochrony przy najcięższych naruszeniach w łańcuchu dostaw.
**Rekomendacja (preferowana):** wykreślić zd. 2; wprowadzić zasadę „Wykonawca odpowiada za podwykonawców jak za działania własne" oraz wymóg uprzedniej zgody Zamawiającego na podwykonawców.
**Fallback (minimum akceptowalne):** ograniczenie odpowiedzialności wyłącznie za podwykonawców **wskazanych przez Zamawiającego**, z zachowaniem wyjątku winy umyślnej i z cesją roszczeń Wykonawcy wobec tych podwykonawców na Zamawiającego.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (Umowa współpracy operacyjnej — odpowiedzialność za osoby trzecie jak za własne), `references/baza-wiedzy/06-sila-wyzsza-i-podwykonawcy.md` (cesja roszczeń)

#### 3. Przeniesienie praw autorskich bez pól eksploatacji — § 4 ust. 1
**Strona dotknięta:** Zamawiający (płaci 480.000 zł i nie nabywa praw); pośrednio Wykonawca (niepewność, kto i na jakiej podstawie korzysta z oprogramowania, spór o wynagrodzenie).
**Opis:** „Z chwilą zapłaty Wykonawca przenosi na Zamawiającego wszelkie prawa autorskie do stworzonego oprogramowania bez ograniczeń." Umowa obejmuje tylko pola eksploatacji w niej wyraźnie wymienione (art. 41 ust. 2 PrAut [NIEZWERYFIKOWANE]) — formuła „wszelkie … bez ograniczeń" nie zastępuje ich wskazania. Wymóg dotyczy także licencji, więc nie da się „uratować" postanowienia jako dorozumianej licencji w zakładanym zakresie. Dalej: (a) „wszelkie prawa autorskie" obejmuje literalnie prawa osobiste, które są niezbywalne (art. 16 PrAut [NIEZWERYFIKOWANE]; przy programach część z nich wyłącza art. 77 PrAut [NIEZWERYFIKOWANE]), a prawa osobiste przysługują osobom fizycznym — twórcom, nie Wykonawcy; (b) brak przeniesienia prawa do wykonywania praw zależnych i do dokumentacji; (c) „Z chwilą zapłaty" — nie wiadomo, czy chodzi o zapłatę całości, a do zapłaty Zamawiający korzysta z systemu bez żadnego tytułu (luka do 60 dni, zob. rachunek); (d) brak potwierdzenia formy pisemnej (art. 53 PrAut [NIEZWERYFIKOWANE]) — dokument nie zawiera podpisów; (e) przy wdrożeniu ERP znaczna część rezultatu to konfiguracja i parametryzacja cudzego systemu — może nie być utworem (`baza-wiedzy/15-ochrona-utworu-test.md`), więc zbiór „stworzonego oprogramowania" bywa bardzo wąski.
**Skutek:** brak skutku rozporządzającego; prawa majątkowe zostają przy Wykonawcy (lub jego twórcach), Zamawiający nie może legalnie modyfikować, rozwijać ani zlecać utrzymania osobie trzeciej. W zakresie praw osobistych — nieważność.
**Rekomendacja (preferowana):** pełny, wyczerpujący katalog pól eksploatacji dla programu, dokumentacji i opracowań (Zasada KTZR nr 1), przeniesienie prawa do wykonywania praw zależnych, zobowiązanie do przeniesienia praw na nowych polach na wezwanie bez dodatkowego wynagrodzenia (Zasada KTZR nr 2, art. 45 PrAut [NIEZWERYFIKOWANE]), zobowiązanie twórców do niewykonywania praw osobistych, przejście praw z chwilą zapłaty **każdej części** wynagrodzenia za dany etap + licencja przejściowa od dnia wydania do przejścia praw.
**Fallback (minimum akceptowalne):** wyłączna licencja w formie pisemnej (art. 67 ust. 5 PrAut [NIEZWERYFIKOWANE]) na wymienionych polach, bezterminowa, z prawem modyfikacji przez osoby trzecie i opcją nabycia praw.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md` (dwie zasady KTZR przy przenoszeniu praw; klauzula nowych pól eksploatacji)

#### 4. Prawo Wykonawcy do trenowania modeli AI na danych Zamawiającego — § 8 ust. 2
**Strona dotknięta:** Zamawiający (administrator danych, właściciel tajemnicy przedsiębiorstwa); także Wykonawca (przetwarzanie we własnym celu bez podstawy prawnej).
**Opis:** „Niezależnie od pozostałych postanowień Umowy, Wykonawca zachowuje prawo do wykorzystania danych Zamawiającego do trenowania modeli AI." Trzy warstwy problemu:
- **RODO.** System ERP z natury przetwarza dane osobowe (pracownicy, klienci, kontrahenci — założenie, bo Załącznik nr 1 nie został dołączony). Trenowanie modeli to **własny cel** Wykonawcy — Wykonawca przestaje być procesorem i staje się odrębnym administratorem, bez podstawy z art. 6 ust. 1 RODO [NIEZWERYFIKOWANE] i z naruszeniem zasady ograniczenia celu (art. 5 ust. 1 lit. b RODO [NIEZWERYFIKOWANE]). Zamawiający, udostępniając dane na ten cel, sam narusza RODO. Brak podstawy przetwarzania to naruszenie zagrożone karą do 20 mln EUR lub 4% obrotu (art. 83 ust. 5 RODO [NIEZWERYFIKOWANE]).
- **Poufność.** Klauzula „Niezależnie od pozostałych postanowień Umowy" nadpisuje § 6 — dane Zamawiającego (ceny, marże, kontrahenci, wolumeny) mogą trafić do modelu, z którego korzystają inni klienci Wykonawcy. Zgoda na takie użycie podważa przesłankę podjęcia przez uprawnionego działań w celu utrzymania informacji w poufności, konieczną do ochrony tajemnicy przedsiębiorstwa (art. 11 ust. 2 u.z.n.k. [NIEZWERYFIKOWANE]).
- **Zakres.** „Dane Zamawiającego" — bez definicji, bez limitu czasowego, bez anonimizacji, bez zakazu ponownej identyfikacji, bez prawa sprzeciwu; „zachowuje prawo" sugeruje uprawnienie istniejące, którego umowa nigdzie nie ustanawia.
**Skutek:** sankcje administracyjne i roszczenia osób, których dane dotyczą (art. 82 RODO [NIEZWERYFIKOWANE]); utrata ochrony tajemnicy przedsiębiorstwa; nieodwracalność — danych wprowadzonych do treningu modelu praktycznie nie da się wycofać.
**Rekomendacja (preferowana):** wykreślić § 8 ust. 2; wprowadzić wprost zakaz trenowania, dostrajania i ewaluacji modeli na danych Zamawiającego, z rozciągnięciem na podwykonawców.
**Fallback (minimum akceptowalne):** wyłącznie dane nieosobowe, trwale zanonimizowane, z zakazem ponownej identyfikacji, po odrębnej pisemnej zgodzie Zamawiającego na konkretny zbiór i cel, z prawem jej cofnięcia; nigdy „niezależnie od pozostałych postanowień".
**Klauzula z bazy:** `references/checklist-dpa-art28.md` (A1 — zakaz trenowania z flow-down; A2 — anonimizacja), `references/baza-klauzul/09-poufnosc.md` (klauzula o narzędziach AI i zakazie trenowania), `references/baza-klauzul/14-rodo.md`

#### 5. Efekt kumulatywny — wydrążenie zobowiązania Wykonawcy — § 1 ust. 1 + § 2 ust. 1 + § 5 ust. 1 zd. 1 + § 5 ust. 2 zd. 2 + § 5 ust. 3 + § 7 ust. 2
**Strona dotknięta:** Zamawiający; także Wykonawca (ryzyko, że sąd uzna cały zestaw wyłączeń za nieważny i przywróci odpowiedzialność na zasadach ogólnych — bez żadnego limitu).
**Opis (test pięciopunktowy, krok 5):** każde z tych postanowień z osobna dałoby się bronić, ale razem dają umowę, w której Wykonawca otrzymuje 480.000 zł i nie ma egzekwowalnego obowiązku:
- „dołoży starań w celu wdrożenia" (§ 1 ust. 1) — zamiast rezultatu staranne działanie;
- „niezwłocznie po podpisaniu Umowy" (§ 2 ust. 1) — brak terminu, więc brak momentu zwłoki;
- „odpowiedzialność wyłącznie za szkody wyrządzone umyślnie" (§ 5 ust. 1) — niedbalstwo, w tym rażące, wolne od odpowiedzialności;
- „Wykonawca nie ponosi kar" (§ 5 ust. 2) — brak sankcji umownych;
- wsparcie powdrożeniowe „według wyłącznego uznania" (§ 5 ust. 3) — brak obowiązków po wdrożeniu;
- wypowiedzenie „w każdym czasie i bez podania przyczyny" (§ 7 ust. 2) — Wykonawca może odejść w trakcie bez skutków.
Treść obiektywna: zobowiązanie iluzoryczne. Asymetria: rażąca, bez uzasadnienia gospodarczego (Zamawiający jednocześnie obciążony karą 50.000 zł/dzień). Praktyka rynkowa: standard dla wdrożeń to cap 100–150% wynagrodzenia z wyłączeniami, a nie wyłączenie odpowiedzialności za niedbalstwo.
**Skutek:** ryzyko nieważności zestawu jako sprzecznego z naturą stosunku zobowiązaniowego i zasadami współżycia społecznego (art. 353¹ w zw. z art. 58 § 2 i § 3 KC [NIEZWERYFIKOWANE]). Dla Zamawiającego — do czasu rozstrzygnięcia sądowego brak realnego środka ochrony; dla Wykonawcy — w razie nieważności powrót do art. 471 KC [NIEZWERYFIKOWANE] bez capu, z utraconymi korzyściami.
**Rekomendacja (preferowana):** przebudować § 1, § 2 i § 5: obowiązek rezultatu („zobowiązuje się wdrożyć"), harmonogram z datami, cap łączny 100–150% wynagrodzenia z wyłączeniami (wina umyślna, IP, poufność, dane osobowe), kary za zwłokę w kamieniach milowych z sufitem, symetryczne zasady wyjścia.
**Fallback (minimum akceptowalne):** cap na poziomie 100% wynagrodzenia + odpowiedzialność za winę umyślną i rażące niedbalstwo poza capem + kary za zwłokę z sufitem 10–20% wynagrodzenia.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (klauzula wzorcowa z capem 12 mies. i wyłączeniami), `references/baza-wiedzy/05-cap-lucrum-wina-umyslna.md` (elementy A–C), `references/baza-klauzul/10-kary-umowne.md`

#### 6. Asymetria wyjścia i wyłączenie wypowiedzenia z ważnych powodów — § 7 ust. 1 i 2
**Strona dotknięta:** Zamawiający (zablokowany w umowie); także Wykonawca (brak zasad rozliczenia prac wykonanych przed wypowiedzeniem).
**Opis:** „Zamawiający nie może wypowiedzieć Umowy przed zakończeniem Wdrożenia." / „Wykonawca może wypowiedzieć Umowę w każdym czasie i bez podania przyczyny." Kwalifikacja decyduje o skutku:
- jeżeli umowa to umowa o świadczenie usług (za tym przemawia „dołoży starań" w § 1 ust. 1) — nie można z góry zrzec się prawa wypowiedzenia z ważnych powodów (art. 746 § 3 w zw. z art. 750 KC [NIEZWERYFIKOWANE]); § 7 ust. 1 jest w tym zakresie nieważny;
- jeżeli to umowa o dzieło — § 7 ust. 1 wyłącza dyspozytywne prawo odstąpienia z art. 644 KC [NIEZWERYFIKOWANE]; ustawowe prawa odstąpienia (art. 635, art. 636, art. 491 KC [NIEZWERYFIKOWANE]) pozostają, bo § 7 posługuje się tylko pojęciem „wypowiedzieć" — ale Zamawiający musi je wywodzić w sporze, w którym nie ma terminu wykonania (§ 2 ust. 1), od którego liczy się zwłokę.
Po stronie Wykonawcy: wypowiedzenie ze skutkiem natychmiastowym (0 dni), bez obowiązku wydania wyników prac, kodu, dokumentacji i bez rozliczenia wynagrodzenia ryczałtowego.
**Skutek:** Zamawiający może zostać z niedokończonym wdrożeniem ERP, bez praw (przejście praw dopiero „Z chwilą zapłaty") i bez kodu (§ 4 ust. 2), a Wykonawca — bez jasnej podstawy do żądania wynagrodzenia za część wykonaną. Ryzyko nieważności § 7 ust. 1 w części.
**Rekomendacja (preferowana):** symetryczne prawo wypowiedzenia z okresem (np. 30 dni) + rozwiązanie natychmiastowe z katalogu (istotne naruszenie nieusunięte w terminie, upadłość) + rozliczenie pro rata według kamieni milowych + exit plan (wydanie kodu, dokumentacji, danych, wsparcie migracyjne).
**Fallback (minimum akceptowalne):** usunięcie prawa Wykonawcy do wypowiedzenia bez przyczyny; Zamawiający z prawem odstąpienia za zapłatą wynagrodzenia za prace wykonane; obowiązek wydania wyników prac przy każdym zakończeniu umowy.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md` (klauzula wzorcowa IT; kompleksowy exit plan)

---

### 🟠 RYZYKA WYSOKIE

#### 1. Nieokreślony przedmiot i niespójna kwalifikacja umowy — § 1 ust. 1, Załącznik nr 1
**Strona dotknięta:** obie — Zamawiający (nie wie, co kupuje) i Wykonawca (ryczałt bez zakresu).
**Opis:** przedmiot opisuje Załącznik nr 1, którego nie dołączono (Złota Reguła nr 4 — załącznik osierocony). Bez niego „wdrożenia systemu ERP" nie wskazuje ani systemu, ani modułów, ani zakresu migracji danych. Do tego umowa sama sobie przeczy co do typu: „dołoży starań" (§ 1 ust. 1 — usługa, staranne działanie) vs „wykona Wdrożenie" i „Wynagrodzenie ryczałtowe" (§ 2 ust. 1, § 3 ust. 1 — dzieło, rezultat).
**Skutek:** spór o to, czy umowa w ogóle doszła do skutku co do istotnego przedmiotu; spór o kwalifikację przesądza o rękojmi (art. 638 KC [NIEZWERYFIKOWANE]), zasadach wyjścia (art. 644 vs art. 746 KC [NIEZWERYFIKOWANE]) i przedawnieniu (art. 646 KC [NIEZWERYFIKOWANE]). Dla Wykonawcy: przy ryczałcie nie może żądać podwyższenia wynagrodzenia, choćby zakres okazał się większy (art. 632 § 1 KC [NIEZWERYFIKOWANE]) — nieokreślony zakres przy ryczałcie to otwarte ryzyko scope creep.
**Rekomendacja (preferowana):** dołączyć szczegółową specyfikację (SOW) jako Załącznik nr 1; § 1 jako mapa umowy (Złota Reguła nr 12); „zobowiązuje się wykonać" zamiast „dołoży starań"; oświadczenie o kwalifikacji (dzieło z elementami usług).
**Fallback (minimum akceptowalne):** minimalna specyfikacja (system, moduły, zakres migracji, liczba użytkowników, środowiska) w treści umowy + procedura zmiany zakresu (change request) z wyceną.
**Klauzula z bazy:** `references/baza-klauzul/04-przedmiot-umowy.md`, `references/essentialia-mapowanie.md` (umowa wdrożeniowa IT — fixed price)

#### 2. Brak terminu wykonania i harmonogramu — § 2 ust. 1
**Strona dotknięta:** Zamawiający przede wszystkim; także Wykonawca (brak pewności, kiedy popada w opóźnienie).
**Opis:** „Wykonawca wykona Wdrożenie niezwłocznie po podpisaniu Umowy." — antywzorzec „niezwłocznie" bez liczby dni; brak kamieni milowych i daty końcowej.
**Skutek:** nie da się ustalić zwłoki, więc nie działają ustawowe prawa odstąpienia ani roszczenia z tytułu opóźnienia; projekt ERP bez harmonogramu może trwać dowolnie długo.
**Rekomendacja (preferowana):** harmonogram jako załącznik, kamienie milowe z datami, przesunięcie terminów o czas opóźnień leżących po stronie Zamawiającego.
**Fallback (minimum akceptowalne):** jedna data końcowa wdrożenia + prawo odstąpienia po bezskutecznym upływie dodatkowego terminu.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`

#### 3. Brak procedury odbioru i nieokreślona wymagalność wynagrodzenia — § 2 ust. 2, § 3 ust. 2
**Strona dotknięta:** obie.
**Opis:** „Zamawiający będzie zgłaszał uwagi na bieżąco." — brak testów akceptacyjnych, terminów, kategorii wad, protokołu. § 3 ust. 2 wiąże termin płatności z doręczeniem faktury, ale nie mówi, kiedy wolno ją wystawić (po podpisaniu? po odbiorze?).
**Skutek:** dla Zamawiającego — ryzyko faktury na 480.000 zł przed jakimkolwiek rezultatem, a w połączeniu z § 5 ust. 2 presja zapłaty pod groźbą kary; dla Wykonawcy — brak momentu, od którego zamyka się projekt i należy się wynagrodzenie (przy dziele co do zasady w chwili oddania — art. 642 § 1 KC [NIEZWERYFIKOWANE]), brak fikcji odbioru przy bierności Zamawiającego; przejście praw autorskich („Z chwilą zapłaty") zawieszone w próżni.
**Rekomendacja (preferowana):** procedura odbioru (UAT w 10 dni roboczych, kategorie wad, odbiór milczący), faktura po protokole odbioru, płatności za kamienie milowe.
**Fallback (minimum akceptowalne):** faktura końcowa po protokole odbioru końcowego; odbiór milczący po upływie terminu na zgłoszenie wad krytycznych.
**Klauzula z bazy:** `references/baza-klauzul/07-terminy-kamienie-milowe.md`, `references/baza-klauzul/06-wynagrodzenie.md`

#### 4. Kod źródłowy jako uprawnienie, nie obowiązek — § 4 ust. 2
**Strona dotknięta:** Zamawiający.
**Opis:** „Wykonawca może, ale nie jest zobowiązany, przekazać kod źródłowy." — antywzorzec pozornego zobowiązania.
**Skutek:** nawet po skutecznym przeniesieniu praw Zamawiający nie może z nich korzystać (modyfikacje, utrzymanie przez innego dostawcę) — vendor lock-in; w połączeniu z § 5 ust. 3 i § 7 ust. 2 Zamawiający zależy od uznania Wykonawcy przez cały cykl życia systemu.
**Rekomendacja (preferowana):** obowiązek wydania pełnego kodu źródłowego z historią zmian, dokumentacją i skryptami budowania przy każdym odbiorze oraz przy zakończeniu umowy, do repozytorium Zamawiającego.
**Fallback (minimum akceptowalne):** depozyt kodu (escrow) z wydaniem w razie zakończenia umowy, upadłości Wykonawcy lub zaprzestania wsparcia.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md` (kompleksowy exit plan — przekazanie kodu z commit history)

#### 5. Brak gwarancji czystości IP, zasad licencjonowania systemu bazowego i komponentów open source — § 4 (luka)
**Strona dotknięta:** Zamawiający.
**Opis:** umowa nie mówi, czyj jest system ERP (własny Wykonawcy czy producenta trzeciego), kto dostarcza licencje i na jakich warunkach; brak oświadczenia Wykonawcy o łańcuchu praw od twórców (pracowników i kontraktorów B2B), brak zakazu komponentów copyleft i brak indemnifikacji za roszczenia osób trzecich.
**Skutek:** Zamawiający odpowiada wobec producenta ERP lub autorów za korzystanie bez licencji; ryzyko obowiązku ujawnienia kodu przy komponentach GPL/AGPL; brak regresu do Wykonawcy poza zasadami ogólnymi — a te § 5 ust. 1 ogranicza do winy umyślnej.
**Rekomendacja (preferowana):** oświadczenie o pełni praw + indemnifikacja IP poza capem z procedurą obrony + zakaz copyleft + wskazanie licencji na system bazowy (licencjodawca, zakres, koszt — w ryczałcie czy poza nim).
**Fallback (minimum akceptowalne):** oświadczenie o pełni praw i wykaz komponentów stron trzecich z licencjami jako załącznik.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md` (gwarancja czystości IP — umowa wdrożeniowa; zakaz komponentów copyleft), `references/baza-wiedzy/07-indemnifikacja-kary-umowne.md`

#### 6. Wsparcie powdrożeniowe według wyłącznego uznania — § 5 ust. 3
**Strona dotknięta:** Zamawiający.
**Opis:** „Zakres wsparcia powdrożeniowego Wykonawca ustala według wyłącznego uznania." — uznaniowość bez kryteriów; brak gwarancji, SLA, czasów reakcji i napraw; rękojmia nieuregulowana, a przy kwalifikacji jako usługa w ogóle jej nie ma. Nie wiadomo też, czy wsparcie mieści się w ryczałcie.
**Skutek:** po wdrożeniu Zamawiający nie ma roszczenia o usunięcie wad poza ustawowym minimum (i to tylko przy kwalifikacji jako dzieło); system ERP jest krytyczny dla działalności — przestój nie ma umownego remedium.
**Rekomendacja (preferowana):** gwarancja (np. 12 miesięcy) z kategoriami wad i czasami reakcji/naprawy, odrębna umowa maintenance z SLA.
**Fallback (minimum akceptowalne):** minimalny okres usuwania wad krytycznych w ramach ryczałtu + stawka godzinowa za wsparcie ponad limit.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md` (SLA — dostępność i czasy reakcji), `references/baza-klauzul/06-wynagrodzenie.md` (kwantyfikacja wsparcia), `references/baza-wiedzy/01-maintenance-art750-kc.md`

#### 7. Prawo stanu Delaware i sąd w Wilmington — § 8 ust. 1
**Strona dotknięta:** obie (każda, która będzie dochodzić roszczeń — w praktyce częściej Zamawiający, bo to on ma roszczenia o wykonanie).
**Opis:** „Prawem właściwym jest prawo stanu Delaware (USA); sądem właściwym jest sąd w Wilmington." Dwie polskie spółki, wdrożenie w infrastrukturze Zamawiającego, wynagrodzenie w złotych — żadnego łącznika z USA. Umowa posługuje się konstrukcjami prawa polskiego (kara umowna, ryczałt, prawa autorskie na polach eksploatacji), które w prawie obcym nie mają prostych odpowiedników.
**Skutek:** koszt i czas sporu nieproporcjonalny do wartości 480.000 zł; wyrok sądu amerykańskiego wymaga uznania i stwierdzenia wykonalności w Polsce (art. 1145 i n. KPC [NIEZWERYFIKOWANE]); spór wstępny o skuteczność derogacji jurysdykcji polskiej (art. 1105 KPC [NIEZWERYFIKOWANE]) i o prawo właściwe (art. 3 ust. 3 Rzym I [NIEZWERYFIKOWANE] — polskie przepisy bezwzględnie obowiązujące i tak zastosowane). Dla procesora danych spoza prawa UE/PCz — dodatkowy problem RODO (`baza-wiedzy/08`).
**Rekomendacja (preferowana):** prawo polskie; sąd powszechny właściwy dla siedziby jednej ze stron albo sąd polubowny z jasno wskazaną instytucją i regulaminem.
**Fallback (minimum akceptowalne):** prawo polskie + arbitraż w Polsce (wskazana instytucja, język polski).
**Klauzula z bazy:** `references/baza-klauzul/17-postanowienia-koncowe.md`

#### 8. Brak umowy powierzenia przetwarzania danych — luka (§ 6, § 8)
**Strona dotknięta:** Zamawiający (administrator, rozliczalność); Wykonawca (przetwarza bez instrumentu z art. 28 RODO).
**Opis:** wdrożenie ERP z migracją danych w infrastrukturze Zamawiającego oznacza dostęp Wykonawcy do danych osobowych (założenie — brak Załącznika nr 1). Umowa nie zawiera ani klauzul powierzenia, ani DPA jako załącznika: brak przedmiotu, czasu, celu, kategorii danych i osób, subprocesorów, procedury zgłaszania naruszeń, zwrotu lub usunięcia danych.
**Skutek:** przetwarzanie bez instrumentu z art. 28 ust. 3 RODO [NIEZWERYFIKOWANE] — naruszenie zagrożone karą z art. 83 ust. 4 lit. a RODO [NIEZWERYFIKOWANE]; administrator pozostaje odpowiedzialny za zgodność, nawet gdy angażuje procesora (art. 5 ust. 2 RODO [NIEZWERYFIKOWANE]). W połączeniu z § 8 ust. 1 (prawo obce) i § 8 ust. 2 (własny cel Wykonawcy) — ryzyko kwalifikacji Wykonawcy jako odrębnego administratora.
**Rekomendacja (preferowana):** DPA jako załącznik, kompletny wg siatki art. 28 + warstwa AI (zakaz trenowania).
**Fallback (minimum akceptowalne):** klauzula powierzenia w treści umowy z pięcioma elementami art. 28 ust. 3 RODO i obowiązkiem zawarcia pełnej DPA przed dostępem do danych produkcyjnych.
**Klauzula z bazy:** `references/baza-klauzul/14-rodo.md`, `references/checklist-dpa-art28.md`, `references/baza-wiedzy/08-rodo-powierzenie-konstrukcja.md`

---

### 🟡 RYZYKA ŚREDNIE

#### 1. Szczątkowa klauzula poufności — § 6 ust. 1
**Strona dotknięta:** obie (wzajemna), w praktyce głównie Zamawiający — to jego dane trafiają do Wykonawcy.
**Opis:** „Strony zachowają poufność informacji przekazanych w związku z Umową." — brak definicji informacji poufnych, wyłączeń (informacje publiczne, uzyskane niezależnie, ujawnienie na żądanie organu), okresu po zakończeniu umowy, kary umownej, zasad zwrotu materiałów. § 8 ust. 2 i tak ją nadpisuje.
**Skutek:** spór o zakres; zobowiązanie bezterminowe może zostać wypowiedziane (art. 365¹ KC [NIEZWERYFIKOWANE]); bez kary umownej — konieczność wykazania szkody.
**Rekomendacja (preferowana):** pełna klauzula: definicja, wyłączenia, okres (np. 5 lat po zakończeniu, tajemnica przedsiębiorstwa bezterminowo), kara z odszkodowaniem uzupełniającym, zasady korzystania z narzędzi AI.
**Fallback (minimum akceptowalne):** definicja + wyłączenia + okres po zakończeniu umowy.
**Klauzula z bazy:** `references/baza-klauzul/09-poufnosc.md`, `references/baza-klauzul/18-zwrot-materialow.md`

#### 2. Nieokreślone obowiązki współdziałania Zamawiającego — § 1 ust. 2, § 2 ust. 2
**Strona dotknięta:** Wykonawca.
**Opis:** „Strony wzajemnie zobowiązują się do współpracy przy realizacji Wdrożenia." — wzajemność deklarowana, bez treści: brak obowiązków Zamawiającego (dostęp do infrastruktury, dane do migracji, kluczowi użytkownicy, terminy decyzji); uwagi zgłaszane „na bieżąco".
**Skutek:** przy ryczałcie i obowiązku rezultatu Wykonawca nie ma umownego mechanizmu przesunięcia terminu i rozliczenia kosztów za opóźnienia po stronie Zamawiającego; zostaje mu procedura ustawowa (art. 640 KC [NIEZWERYFIKOWANE] — przy dziele).
**Rekomendacja (preferowana):** katalog obowiązków Zamawiającego z terminami; przesunięcie harmonogramu o czas opóźnienia Zamawiającego; zasady rozliczenia przestoju.
**Fallback (minimum akceptowalne):** zasada, że opóźnienie Zamawiającego przesuwa terminy Wykonawcy o ten sam czas.
**Klauzula z bazy:** `references/baza-klauzul/05-obowiazki-stron.md`

#### 3. Asymetria odpowiedzialności Zamawiającego — § 5 (luka)
**Strona dotknięta:** Zamawiający.
**Opis:** § 5 ogranicza tylko odpowiedzialność Wykonawcy. Odpowiedzialność Zamawiającego (np. za niewykonanie obowiązków współdziałania, za szkody w mieniu Wykonawcy) pozostaje nieograniczona, z utraconymi korzyściami (art. 361 § 2, art. 471 KC [NIEZWERYFIKOWANE]); do tego kara z § 5 ust. 2 (nieważna, ale wywołująca spór).
**Skutek:** ekspozycja Zamawiającego otwarta przy jednoczesnym 0 zł po stronie Wykonawcy za niedbalstwo (zob. rachunek).
**Rekomendacja (preferowana):** cap wzajemny i symetryczny.
**Fallback (minimum akceptowalne):** wzajemne wyłączenie utraconych korzyści z wyjątkami (wina umyślna, IP, poufność, dane osobowe).
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 4. Oznaczenie stron, reprezentacja, data, miejsce i forma — komparycja, brak części końcowej
**Strona dotknięta:** obie.
**Opis:** brak KRS, NIP, adresów, osób reprezentujących i podstawy umocowania, daty i miejsca zawarcia, bloku podpisów (Złota Reguła nr 8). Dane oznaczono jako fikcyjne — w realnej umowie to luka do uzupełnienia, nie wada konstrukcyjna. Brak podpisów ma jednak znaczenie materialne: przeniesienie praw autorskich wymaga formy pisemnej pod rygorem nieważności (art. 53 PrAut [NIEZWERYFIKOWANE]); brak też adresów do doręczeń, a od doręczenia faktury biegnie termin płatności (§ 3 ust. 2).
**Skutek:** spór o umocowanie i o datę zawarcia (od niej liczy się „niezwłocznie" z § 2 ust. 1); ryzyko nieważności przeniesienia praw przy zawarciu w formie innej niż pisemna.
**Rekomendacja (preferowana):** pełna komparycja z KRS/NIP i umocowaniem, data i miejsce, adresy do doręczeń z rygorem, podpisy (własnoręczne lub kwalifikowane elektroniczne).
**Fallback (minimum akceptowalne):** KRS + osoby reprezentujące + podpisy kwalifikowane.
**Klauzula z bazy:** `references/baza-klauzul/01-oznaczenie-stron.md`, `references/baza-klauzul/17-postanowienia-koncowe.md` (doręczenia z rygorem skuteczności)

---

### 🟢 RYZYKA NISKIE

#### 1. Definicje i terminologia — cała umowa
**Strona dotknięta:** obie.
**Opis:** pojęcia pisane wielką literą bez definicji — „Wdrożenie", „Umowa", „Załącznik nr 1" (Złota Reguła nr 1); brak § Definicje; „systemu ERP" pisany małą literą, choć to centralny przedmiot. Mini-weryfikacja odesłań: jedyne odesłanie wewnętrzne (§ 1 ust. 1 → Załącznik nr 1) prowadzi do dokumentu, którego nie ma (ujęte w 🟠 1); odesłań między paragrafami brak; klauzula „Niezależnie od pozostałych postanowień Umowy" (§ 8 ust. 2) nadpisuje co najmniej § 6 (ujęte w 🔴 4).
**Skutek:** drobne kłopoty interpretacyjne, poza zakresem już opisanym przy flagach wyższych.
**Rekomendacja (preferowana):** § Definicje: Umowa, Wdrożenie, System, Oprogramowanie, Dokumentacja, Kod Źródłowy, Dane Zamawiającego, Odbiór.
**Fallback (minimum akceptowalne):** definicje „Wdrożenia" i „Systemu" w § 1.
**Klauzula z bazy:** `references/baza-klauzul/03-definicje.md`

---

### ✓ Bramka kompletności (R9) — zamknięcie obszarów

| Obszar | Status |
|---|---|
| Odpowiedzialność i kary | 🔴 1, 🔴 2, 🔴 5, 🟠 6, 🟡 3 |
| Prawa autorskie | 🔴 3, 🟠 4, 🟠 5 |
| Definicje i logika | 🟠 1, 🟢 1 |
| Reprezentacja | 🟡 4 |
| Wypowiedzenie i exit | 🔴 6 |
| RODO | 🔴 4, 🟠 8 |
| Tytuł prawny i przekwalifikowanie | dzieło vs usługa — 🟠 1; przekwalifikowanie na stosunek pracy — n/d (strony to spółki kapitałowe) |
| Poufność | 🟡 1 |
| Spory | 🟠 7 |

**Obszary bez zastrzeżeń:** termin płatności 60 dni (§ 3 ust. 2) mieści się w granicy ustawowej; brak prób modyfikacji przedawnienia i wyłączenia miarkowania kar; trigger mikroprzedsiębiorcy nieaktywny.

---

## OCENA BEZPIECZEŃSTWA: 5/100

Sześć ryzyk krytycznych, w tym trzy nieważności z mocy prawa (kara za zobowiązanie pieniężne, przeniesienie praw bez pól eksploatacji, wyłączenie winy umyślnej podwykonawców), klauzula AI nadpisująca poufność i RODO oraz zestaw wyłączeń, który w sumie wydrąża zobowiązanie Wykonawcy. Umowa jest zła dla obu stron: Zamawiający płaci 480.000 zł za obietnicę starań, a Wykonawca opiera swoje zabezpieczenie na karze, której nie wyegzekwuje.

**Werdykt:** NIE PODPISYWAĆ

---

### Klauzule z bazy KTZR do uzupełnienia

🔴 1 (kara za zobowiązanie pieniężne) → `references/baza-klauzul/10-kary-umowne.md` — kary wyłącznie za zobowiązania niepieniężne, z sufitem; po stronie płatności odsetki ustawowe
🔴 2 (podwykonawcy) → `references/baza-klauzul/11-odpowiedzialnosc.md` — odpowiedzialność za osoby trzecie jak za własne; `baza-wiedzy/06` — cesja roszczeń przy wyjątkach
🔴 3 (prawa autorskie) → `references/baza-klauzul/08-prawa-autorskie-ip.md` — pełny katalog pól + klauzula nowych pól eksploatacji (dwie zasady KTZR)
🔴 4 (trenowanie AI) → `references/checklist-dpa-art28.md` (A1, A2) + `references/baza-klauzul/09-poufnosc.md` (klauzula o narzędziach AI)
🔴 5 (efekt kumulatywny) → `references/baza-klauzul/11-odpowiedzialnosc.md` — cap 12 mies. z wyłączeniami; `baza-wiedzy/05` — elementy A–C
🔴 6 (wyjście) → `references/baza-klauzul/12-wypowiedzenie-exit.md` — klauzula wzorcowa IT + kompleksowy exit plan
🟠 1–3 (przedmiot, terminy, odbiór) → `references/baza-klauzul/04-przedmiot-umowy.md`, `07-terminy-kamienie-milowe.md`, `06-wynagrodzenie.md`
🟠 4 (kod źródłowy) → `references/baza-klauzul/12-wypowiedzenie-exit.md` — przekazanie kodu z commit history
🟠 5 (czystość IP) → `references/baza-klauzul/08-prawa-autorskie-ip.md` — gwarancja czystości IP (umowa wdrożeniowa), zakaz copyleft
🟠 6 (wsparcie) → `references/baza-klauzul/11-odpowiedzialnosc.md` — SLA
🟠 7 (prawo i sąd) → `references/baza-klauzul/17-postanowienia-koncowe.md`
🟠 8 (DPA) → `references/baza-klauzul/14-rodo.md` + `references/checklist-dpa-art28.md`

### Miejsca, w których w trybie standardowym zatrzymałbym się na decyzję (R6)

1. **Kogo reprezentujemy?** Audyt jest neutralny. Po wyborze strony zmienia się kierunek rekomendacji przy 🔴 5, 🔴 6, 🟡 2 i 🟡 3 (pozycja wyjściowa vs fallback).
2. **Kwalifikacja umowy (dzieło czy usługa)** — przesądza o skutku § 7 ust. 1 (🔴 6) i o rękojmi (🟠 6); potrzebna decyzja, którą konstrukcję przyjmujemy przy przebudowie.
3. **Jaki system ERP i czyje licencje** — bez Załącznika nr 1 nie da się ocenić, co mieści się w pojęciu „stworzonego oprogramowania" (🔴 3, 🟠 5).
4. **Czy Wykonawca będzie miał dostęp do danych osobowych** — założyłem, że tak (🔴 4, 🟠 8); do potwierdzenia.
5. **Lokalizacja infrastruktury** — przesądza o zastosowaniu art. 3 ust. 3 Rzym I [NIEZWERYFIKOWANE] i o tym, czy cała ocena ius cogens działa mimo wyboru prawa Delaware.
6. **Konfiguracja kancelarii** — brak `practice-profile.md`; progi domyślne KTZR. Do rozważenia: `workflows/konfiguracja-kancelarii.md`.

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
