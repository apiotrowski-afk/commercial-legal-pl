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

Przeskanuj umowę pod kątem klauzul, które próbują wyłączyć lub obejść poniższe. Trafienie = flaga 🔴 (naruszenie normy bezwzględnej to nie „ryzyko", to nieważność).

| Norma (ius cogens) | Czego NIE MOŻNA | Typowa próba obejścia w umowie |
|---|---|---|
| art. 473 § 2 KC | wyłączyć odpowiedzialności za szkodę wyrządzoną **umyślnie** | „Wykonawca nie ponosi odpowiedzialności za jakiekolwiek szkody" / „odpowiedzialność wyłączona w najszerszym dopuszczalnym zakresie" obejmujące winę umyślną |
| art. 483 § 1 KC | zastrzec kary umownej za zobowiązanie **pieniężne** | kara umowna „za opóźnienie w zapłacie" / „za brak płatności w terminie" (za to należą się odsetki, nie kara) |
| art. 484 § 2 KC | pozbawić dłużnika prawa żądania **miarkowania** rażąco wygórowanej kary | „Strony wyłączają możliwość miarkowania kary umownej" / „kara nie podlega obniżeniu" |
| art. 119 KC | umownie skracać ani wydłużać **terminów przedawnienia** | „roszczenia przedawniają się po 6 miesiącach" (gdy ustawa daje dłużej) / wydłużenie ponad ustawę |
| art. 16 PrAut | zbyć/zrzec się **autorskich praw osobistych** (są niezbywalne) | „Wykonawca przenosi wszelkie prawa autorskie, w tym osobiste" (przenieść można tylko majątkowe; do osobistych — zobowiązanie do niewykonywania) |
| art. 41 ust. 2 PrAut | przenieść praw majątkowych **bez oznaczenia pól eksploatacji** | „przenosi wszelkie prawa bez ograniczeń" (brak katalogu pól = brak skutku rozporządzającego) |
| ustawa o przeciwdziałaniu nadmiernym opóźnieniom (zatory) | dowolnie wydłużać **terminy zapłaty** w B2B ponad granice ustawowe | „termin płatności 120 dni" (co do zasady max 60 dni; dłuższy tylko jeśli nie jest rażąco nieuczciwy wobec wierzyciela) |
| RODO (art. 28) | powierzyć przetwarzania danych osobowych **bez umowy powierzenia** | „Wykonawca może przetwarzać dane w dowolnym celu" / trenowanie AI na danych klienta bez podstawy |
| art. 3531 + 58 § 2 KC | ukształtować stosunku sprzecznie z **zasadami współżycia** / właściwością stosunku | rażąca, jednostronna asymetria bez uzasadnienia gospodarczego |

Uwaga na różnicę B2B vs konsument: **rękojmię** można w B2B umownie ograniczyć lub wyłączyć (art. 558 § 1 KC), ale wobec konsumenta — nie. Zob. też trigger mikroprzedsiębiorcy niżej.

## Trigger mikroprzedsiębiorcy (art. 3855 KC)

Od 2021 r. część ochrony konsumenckiej rozciąga się na **osobę fizyczną prowadzącą jednoosobową działalność gospodarczą**, gdy umowa jest bezpośrednio związana z jej działalnością, ale **nie ma dla niej charakteru zawodowego** (art. 3855 KC). Praktyczny skutek: wobec takiej strony stosuje się m.in. przepisy o klauzulach niedozwolonych (art. 3851–3853 KC).

**Kiedy podnieść:** gdy jedną ze stron B2B jest jednoosobowa firma, a przedmiot umowy leży poza jej zwykłą specjalizacją (np. software house sprzedający usługę IT jednoosobowej kancelarii — dla kancelarii to nie jest umowa „zawodowa"). Wtedy przeskanuj umowę także pod kątem klauzul abuzywnych, tak jak wobec konsumenta.

## Test klauzuli generalnej + efekt kumulatywny

Dla klauzul **granicznych** (nie oczywiste naruszenie, ale podejrzenie abuzywności / nadużycia / sprzeczności z zasadami współżycia) przeprowadź test pięciopunktowy. Podstawy: art. 3851 KC (abuzywność), art. 5 KC (nadużycie prawa), art. 58 § 2 KC (sprzeczność z zasadami współżycia).

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
