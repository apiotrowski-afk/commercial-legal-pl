---
type: Referencja
title: Antywzorce językowe — pułapki po brzmieniu
tags: [antywzorce, red-flags, wykrywanie, brzmienie, klauzule ryzykowne, due diligence]
contract_types: [wszystkie]
risk_level: informacyjny
mandatory_for: [audyt-ryzyk, pełna-analiza]
requires: [zlote-reguly.md, 11-odpowiedzialnosc.md]
timestamp: 2026-08-01
---

# Antywzorce językowe — pułapki po brzmieniu

Baza klauzul mówi *czego szukać po kategorii*. Ten plik działa **prostopadle** — łapie ryzyko **po konkretnym sformułowaniu**, niezależnie od tego, w którym paragrafie się pojawi. Otwórz przy audycie ryzyk i pełnej analizie i przeskanuj tekst umowy pod kątem tych fraz.

Zasada: wykrycie frazy to **sygnał do sprawdzenia**, nie automatyczny werdykt. Kontekst decyduje — ta sama fraza bywa neutralna albo groźna. Kolumna „Dlaczego" mówi, co zweryfikować.

## Zobowiązania rozmyte (obietnica bez treści)

| Fraza w umowie | Typ pułapki | Dlaczego groźne / co sprawdzić |
|---|---|---|
| „dołoży starań", „dołoży należytych starań" | staranne działanie zamiast rezultatu | Przy obowiązku, który miał być rezultatem (wdrożenie, dostawa, termin) — degraduje go do zobowiązania starannego działania. Trudniej dochodzić niewykonania. Sprawdź, czy strona chce rezultatu — jeśli tak, żądaj „zobowiązuje się". |
| „w miarę możliwości", „o ile to możliwe", „w rozsądnym terminie" | brak twardego progu | Obowiązek bez mierzalnej granicy. Kto ocenia „możliwości" i „rozsądek"? Zamień na konkretny termin/warunek. |
| „niezwłocznie" (bez liczby dni) | termin nieoznaczony | Źródło sporu — „niezwłocznie" znaczy co innego dla każdej strony. Żądaj liczby dni (np. „w terminie 3 Dni Roboczych"). |
| „na bieżąco", „okresowo", „regularnie" | częstotliwość nieoznaczona | Brak egzekwowalnego harmonogramu. Doprecyzuj interwał. |

## Jednostronna władza (uznaniowość bez kryteriów)

| Fraza w umowie | Typ pułapki | Dlaczego groźne / co sprawdzić |
|---|---|---|
| „według wyłącznego uznania", „wedle własnego uznania", „w każdym czasie i bez podania przyczyny" | uznaniowość bez standardu | Jedna strona decyduje bez kryteriów i kontroli. Przy blokadzie usługi, zmianie warunków, akceptacji odbioru — rażąca asymetria. Żądaj obiektywnych przesłanek. |
| „może, ale nie jest zobowiązany" | pozorne zobowiązanie | Uprawnienie udające obowiązek — druga strona nie może na nim polegać. Sprawdź, czy miało być obowiązkiem. |
| „zastrzega sobie prawo do…" | jednostronna zmiana | Często ukrywa prawo do jednostronnej zmiany istotnych warunków. Sama klauzula powinna określać **przesłanki i zakres** zmiany. Przy wzorcu w stosunku ciągłym — art. 384¹ KC wiąże nowym wzorcem tylko przy prawidłowym doręczeniu/udostępnieniu (art. 384) **i** realnej możliwości wypowiedzenia w najbliższym terminie; przepis nie legalizuje każdej klauzuli zmiany, a wobec konsumenta podlega ona kontroli abuzywności. |
| „z przyczyn leżących po stronie…" (bez katalogu) | przerzucenie ryzyka | Otwarta formuła obciążająca jedną stronę nieokreślonym zbiorem zdarzeń. Żądaj zamkniętego katalogu. |

## Rozdmuchanie / zawężenie zakresu

| Fraza w umowie | Typ pułapki | Dlaczego groźne / co sprawdzić |
|---|---|---|
| „w tym w szczególności", „między innymi" po stronie **obowiązków klienta** | zakres otwarty w górę | Lista przykładowa obowiązków = obowiązki nieograniczone. Przy obowiązkach naszego klienta domagaj się katalogu zamkniętego. |
| „wszelkie", „jakiekolwiek", „nieograniczone" przy odpowiedzialności/licencji/danych | zakres maksymalny | „nieograniczona odpowiedzialność", „licencja na wszelkich polach", „prawo do wszelkich danych" — sprawdź, czy to nie obejście capu / minimalizacji danych (RODO). Przy IP: sama formuła „wszelkie pola" **nie zastępuje** wyraźnego wskazania pól (art. 41 ust. 2 PrAut) — wadliwa jest ogólna formuła **zamiast** identyfikacji; jeśli po niej następuje kompletne, jednoznaczne wyliczenie, wymóg może być spełniony. Umowa nie obejmie pól nieznanych w chwili zawarcia (art. 41 ust. 4); licencja wyłączna wymaga formy pisemnej (art. 67 ust. 5). |
| „niezależnie od pozostałych postanowień", „bez względu na inne zapisy" | nadpisanie umowy | Klauzula wyłączająca inne postanowienia — może cicho ubezskutecznić cap, karę, wyłączenia. Sprawdź, co realnie nadpisuje (cross-check z resztą umowy). |
| „trwałe", „nieodwołalne", „bezterminowe" przy licencji/zgodzie/zobowiązaniu | brak wyjścia | Zobowiązanie bez końca i bez możliwości cofnięcia. Sprawdź, czy adekwatne do ekwiwalentu i czy w ogóle dopuszczalne. |

## Przerzucenie ryzyka i kosztów

| Fraza w umowie | Typ pułapki | Dlaczego groźne / co sprawdzić |
|---|---|---|
| „na własny koszt i ryzyko" | cichy transfer kosztów | Sprawdź, czy koszt/ryzyko nie powinno leżeć po drugiej stronie lub być dzielone. |
| „zwolni z wszelkiej odpowiedzialności", „zabezpieczy przed wszelkimi roszczeniami" (indemnity otwarta) | indemnifikacja bez limitu | Otwarte hold-harmless potrafi obejść cap odpowiedzialności. Sprawdź limit, wyłączenia i wzajemność. |
| „odpowiada jak za własne działania" (bez ograniczeń) | odpowiedzialność za podwykonawców | Art. 474 KC to reguła ustawowa (za osoby, którymi dłużnik się posługuje) — w obrocie profesjonalnym modyfikowalna w granicach art. 473, 3531 i 58 KC. Sprawdź, czy współmierne i czy nie obejmuje operatorów chmury poza kontrolą strony. |
| „kara umowna nie wyłącza dochodzenia odszkodowania przewyższającego" (jednostronnie) | kumulacja sankcji | Sprawdź symetrię i czy nie prowadzi do rażąco wygórowanej sankcji (art. 484 §2 KC — miarkowanie). |

## Pozorna wzajemność i definicje-wytrychy

| Fraza w umowie | Typ pułapki | Dlaczego groźne / co sprawdzić |
|---|---|---|
| „Strony wzajemnie…" + sankcje/obowiązki tylko na jedną stronę | fałszywa symetria | Deklarowana wzajemność, realna asymetria. Cross-check: czy kary/obowiązki obciążają obie strony, czy tylko jedną. |
| pojęcie pisane Wielką Literą, ale **bez definicji** | definicja-widmo | Termin traktowany jak zdefiniowany, którego nie zdefiniowano. Sprawdź słowniczek. |
| ta sama rzecz nazwana różnie („Specjalista" / „Konsultant" / „Wykonawca") | dryf terminologiczny | Niespójne nazewnictwo rodzi spór interpretacyjny. Ujednolić. |
| „zgodnie z obowiązującymi przepisami" (jako całość obowiązku) | obowiązek pusty | Odesłanie do „przepisów" bez wskazania których = brak konkretnej treści. Sprawdź, czy nie zastępuje realnego zobowiązania. |

---

## Jak używać w audycie

1. Po identyfikacji ryzyk po kategoriach (Krok 1 audytu) — **przeskanuj tekst pod kątem powyższych fraz**.
2. Każde trafienie zważ w kontekście: fraza to sygnał, nie wyrok. Neutralna w jednym miejscu, groźna w innym.
3. Trafienie istotne → dołącz do raportu jako ryzyko z odpowiednią flagą 🔴/🟠/🟡, z rekomendacją i **fallbackiem** (minimum akceptowalne brzmienie kierunkowo).
4. Lista jest **otwarta** — brak frazy na liście nie znaczy, że zapis jest bezpieczny.
