---
type: Referencja
title: Normy bezwzględnie obowiązujące (ius cogens) — bramka i test kumulatywny
tags: [ius cogens, normy bezwzględne, nieważność, abuzywność, 353(1) KC, 58 KC, 385(1) KC, 385(5) KC, mikroprzedsiębiorca, test kumulatywny]
contract_types: [wszystkie]
risk_level: krytyczny
mandatory_for: [audyt-ryzyk, pełna-analiza]
requires: [zlote-reguly.md, 11-odpowiedzialnosc.md, 10-kary-umowne.md]
timestamp: 2026-08-01
---

# Normy bezwzględnie obowiązujące (ius cogens) — bramka i test kumulatywny

Swoboda umów (art. 3531 KC) ma trzy granice: **ustawę, właściwość stosunku i zasady współżycia społecznego**. Klauzula, która przekracza granicę *ius cogens*, jest **nieważna** (art. 58 § 1 lub § 3 KC) — niezależnie od tego, co strony podpisały. To inny rodzaj wady niż „ryzyko biznesowe": nie da się jej wynegocjować, bo prawo jej nie dopuszcza.

Ten plik służy dwóm rzeczom:
1. **Bramka ius cogens** — szybki skan, czy jakaś klauzula nie próbuje *obejść normy bezwzględnie obowiązującej* (essentialia mówi „czego brakuje"; ta bramka mówi „czego stronom NIE WOLNO, a próbują").
2. **Test klauzuli generalnej + efekt kumulatywny** — procedura dla klauzul granicznych (abuzywność, nadużycie prawa, sprzeczność z zasadami współżycia).

> **Dyscyplina cytatów (R1):** numery artykułów poniżej to mapa referencyjna. W generowanym raporcie każdy cytat przepisu przepuść przez `verify_article()` lub oznacz `[NIEZWERYFIKOWANE]`. Nie przenoś treści przepisu do outputu „z pamięci".

## Bramka ius cogens — katalog typowych naruszeń

Przeskanuj umowę pod kątem klauzul, które próbują wyłączyć lub obejść poniższe. Trafienie = flaga 🔴 (naruszenie normy bezwzględnej to nie „ryzyko" do negocjacji, to wada, której umowa nie usunie).

**Rozróżniaj sankcje** — bywają mylone, a to różne skutki: (1) **nieważność** postanowienia (art. 58 § 1–2 KC; zwykle tylko w zakresie sprzecznym — art. 58 § 3, nie całej umowy), (2) **brak związania klauzulą** abuzywną (art. 3851 KC — konsument / art. 3855) bez nieważności całej umowy, (3) **bezskuteczność** wobec ustawowego uprawnienia (np. wyłączenie miarkowania nie działa, kara zostaje). Art. 5 KC (nadużycie prawa) **nie unieważnia** klauzuli — odmawia ochrony konkretnemu sposobowi wykonywania prawa.

| Norma (ius cogens) | Czego NIE MOŻNA | Typowa próba obejścia | Skutek |
|---|---|---|---|
| art. 473 § 2 KC | wyłączyć ani ograniczyć odpowiedzialności za szkodę wyrządzoną wierzycielowi **umyślnie** przez dłużnika (w tym organ osoby prawnej) | „Wykonawca nie ponosi odpowiedzialności za jakiekolwiek szkody" / cap „w najszerszym dopuszczalnym zakresie" obejmujący winę umyślną | nieważność **w tym zakresie** (art. 58 § 3); odpowiedzialność za umyślne działania osób z art. 474 KC — odrębna ocena |
| art. 483 § 1 KC | zastrzec kary umownej za zobowiązanie **pieniężne** | kara „za opóźnienie w zapłacie" (należą się odsetki, nie kara) | nieważność; decyduje **funkcja**, nie nazwa — kara zabezpieczająca zobowiązanie niepieniężne może być liczona w pieniądzu |
| art. 484 § 2 KC | **z góry** pozbawić dłużnika żądania miarkowania kary (gdy zobowiązanie w znacznej części wykonane **albo** kara rażąco wygórowana — dwie odrębne przesłanki) | „Strony wyłączają miarkowanie" / „kara nie podlega obniżeniu" | wyłączenie z góry — niedopuszczalne; **odrębnej oceny** wymaga ugoda zawarta już po powstaniu obowiązku zapłaty |
| art. 119 KC (+ art. 117 § 2) | umownie skracać ani wydłużać **terminów przedawnienia**; zrzec się zarzutu przedawnienia **przed** upływem terminu | „roszczenia przedawniają się po 6 miesiącach" / „strona zrzeka się zarzutu przedawnienia" (przed terminem) | nieważność |
| art. 16 PrAut | zbyć lub zrzec się **autorskich praw osobistych** | „przenosi wszelkie prawa, w tym osobiste" | nieważność; **co do zasady** dopuszczalne zobowiązanie do niewykonywania określonych praw osobistych i upoważnienie do czynności — ale nie może być traktowane jak przeniesienie/zrzeczenie; skrajnie szeroka, bezterminowa klauzula → ocena z art. 58/3531 |
| art. 41 ust. 2 PrAut (+ ust. 4, art. 53, art. 67 ust. 5) | przenieść praw / udzielić licencji **bez wyraźnego wskazania pól eksploatacji** (także opisowo, nie muszą to być nazwy ustawowe); objąć pól **nieznanych** w chwili zawarcia; przenieść praw / udzielić licencji wyłącznej **bez formy pisemnej** | „przenosi wszelkie prawa bez ograniczeń" bez identyfikacji pól / umowa ustna lub mailowa | brak skutecznego przeniesienia/licencji w zakładanym zakresie (doktryna: nieważność / bezskuteczność / brak objęcia); brak formy pisemnej — nieważność (art. 53, 67 ust. 5) |
| ustawa o przeciwdziałaniu nadmiernym opóźnieniom — **art. 7 ust. 2, 2a; art. 8 ust. 2** | wydłużać **terminów zapłaty** ponad limity | „termin płatności 120 dni" | B2B: co do zasady 60 dni od doręczenia faktury; dłuższy tylko przy wyraźnym ustaleniu i gdy **nie jest rażąco nieuczciwy** (art. 7 ust. 2); **sztywne 60 dni**, gdy dłużnik = duży przedsiębiorca, wierzyciel = MŚP (ust. 2a); podmiot publiczny: 30 dni, publiczny podmiot leczniczy: 60 (art. 8 ust. 2); zrzeczenie się roszczenia o ustalenie rażącej nieuczciwości — nieważne |
| RODO art. 28 ust. 3 | rozpocząć przetwarzania **bez umowy/instrumentu** spełniającego art. 28 — **jeżeli** relacja faktycznie jest administrator–procesor | „Wykonawca może przetwarzać dane w dowolnym celu" / trenowanie AI na danych klienta bez podstawy | naruszenie RODO (kara art. 83 ust. 4 lit. a). Uwaga: nie każde udostępnienie danych to powierzenie — najpierw kwalifikacja ról (odrębni administratorzy / współadministrowanie / personel z upoważnienia) |
| art. 3531 + art. 58 § 2 KC | ukształtować stosunku sprzecznie z **zasadami współżycia** / właściwością stosunku / ustawą | rażąca, jednostronna asymetria bez uzasadnienia gospodarczego | nieważność (art. 58), zwykle w zakresie sprzecznym |

**Rękojmia — B2B vs ochrona konsumencka:** w klasycznym B2B rękojmię można rozszerzyć, ograniczyć lub wyłączyć (art. 558 § 1 KC), **ale** wyłączenie jest bezskuteczne przy podstępnym zatajeniu wady (art. 558 § 2). Wobec konsumenta reżim zgodności towaru z umową jest dziś w ustawie o prawach konsumenta. Osoba fizyczna-przedsiębiorca zawierająca umowę niezawodową korzysta z części ochrony (art. 3855 — zob. niżej), w tym rękojmi konsumenckiej (art. 5564, 5565 KC).

## Trigger mikroprzedsiębiorcy (art. 3855 KC)

Od 1 stycznia 2021 r. część ochrony konsumenckiej rozciąga się na **osobę fizyczną zawierającą umowę bezpośrednio związaną z jej działalnością gospodarczą**, gdy umowa **nie ma dla niej charakteru zawodowego** (art. 3855 KC). Dotyczy przedsiębiorców będących osobami fizycznymi (działalność indywidualna, wspólnicy spółki cywilnej działający jako przedsiębiorcy) — **nie** spółek kapitałowych ani innych osób prawnych. Skutek: stosuje się m.in. przepisy o klauzulach niedozwolonych (art. 3851–3853 KC) oraz część rękojmi konsumenckiej.

**Kiedy podnieść:** gdy jedną ze stron B2B jest przedsiębiorca-osoba fizyczna, a przedmiot umowy leży poza jej zwykłą specjalizacją (np. software house sprzedający usługę IT jednoosobowej kancelarii — dla kancelarii to nie jest umowa „zawodowa"). Wtedy przeskanuj umowę także pod kątem klauzul abuzywnych, tak jak wobec konsumenta.

## Test klauzuli generalnej + efekt kumulatywny

Dla klauzul **granicznych** (nie oczywiste naruszenie, ale podejrzenie abuzywności / sprzeczności z zasadami współżycia) przeprowadź test pięciopunktowy. Podstawy — o **różnych funkcjach**: art. 3851 KC (abuzywność — konsument i art. 3855; skutek: brak związania klauzulą), art. 58 § 2 KC (nieważność postanowienia sprzecznego z zasadami współżycia), art. 3531 KC (granice kształtowania treści stosunku; przekroczenie → sankcja z art. 58). Art. 5 KC (nadużycie prawa) służy odmowie ochrony konkretnemu **sposobowi wykonywania** prawa, nie stwierdzaniu nieważności klauzuli — powołuj go w tej roli.

1. **Treść obiektywna** — co klauzula realnie znaczy i jaki daje efekt (niezależnie od nazwy)?
2. **Sposób wprowadzenia** — wzorzec narzucony (adhezyjny) czy indywidualnie negocjowany? Klauzule nienegocjowane oceniane surowiej.
3. **Asymetria stron** — czy klauzula rażąco faworyzuje jedną stronę bez uzasadnienia gospodarczego? Uwzględnij pozycję i status stron (trigger art. 3855 KC — mikrofirma).
4. **Praktyka rynkowa** — czy odbiega od standardu rynkowego dla tego typu umowy?
5. **Efekt kumulatywny** — **kluczowy krok, którego nie daje ocena per-klauzula:** nawet jeśli każda klauzula z osobna jest dopuszczalna, czy ich **suma** tworzy niedopuszczalną całość (systemowa asymetria, wydrążenie zobowiązania, obejście ochrony przez rozproszenie po kilku paragrafach)?

**Jak raportować:** przy podejrzeniu efektu kumulatywnego wskaż *zestaw* klauzul, nie pojedynczą, i opisz, jak razem przechylają umowę (np. „§ 5 + § 7 + § 11 łącznie pozbawiają Zamawiającego realnego środka ochrony, mimo że każdy z osobna jest dopuszczalny").

## Jak używać w audycie

1. **Na wejściu** (przed oceną per-kategoria) — przebiegnij katalog bramki ius cogens. Trafienie → 🔴, bo to nieważność, nie ryzyko.
2. Sprawdź **trigger mikroprzedsiębiorcy** — jeśli aktywny, włącz skan klauzul abuzywnych.
3. Klauzule graniczne → **test pięciopunktowy**, ze szczególnym naciskiem na krok 5 (efekt kumulatywny).
4. Werdykt: klauzula nieważna z mocy prawa **zawsze** przesuwa werdykt-triage do 🟥 (reguła dysjunkcji w `workflows/audyt-ryzyk.md`).
