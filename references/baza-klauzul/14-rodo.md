---
type: Klauzula
title: Dane osobowe / RODO
tags: [RODO, DPA, administrator, procesor, art-28-RODO, EOG, data-breach, wizerunek, zgoda, art-6-RODO]
contract_types: [B2B-IT, body-leasing, platforma, hosting, SaaS]
risk_level: krytyczny
mandatory_for: [B2B-IT, SaaS, platforma]
requires: [03-definicje.md]
timestamp: 2026-06-27
---

# Dane osobowe / RODO

## Kiedy stosować i na co uważać

Określenie ról stron (administrator vs procesor), zasad przetwarzania i bezpieczeństwa danych. Od 2018 r. obowiązkowe w każdej umowie IT, gdzie dochodzi do przetwarzania danych osobowych.

### ⚠️ Red flags

Brak jakiegokolwiek uregulowania RODO. Brak DPA jako załącznika. Nieokreślone role stron. Brak zakazu transferu poza EOG. Brak procedury data breach notification. Podpowierzenie bez zgody.

### Klauzula wzorcowa (generyczny IT)

> W zakresie, w jakim Wykonawca przetwarza dane osobowe w imieniu Zamawiającego, Wykonawca działa jako Podmiot Przetwarzający w rozumieniu art. 28 RODO. Szczegółowe zasady przetwarzania określa Umowa Powierzenia Przetwarzania Danych Osobowych stanowiąca Załącznik nr [X]. Podpowierzenie wymaga uprzedniej pisemnej zgody Zamawiającego. Wykonawca nie przekazuje danych poza Europejski Obszar Gospodarczy bez zgody Zamawiającego.

## Klauzule z umów KTZR

### Body Leasing IT (KTZR)

> W zakresie, w jakim Specjalista uzyskuje dostęp do danych osobowych przetwarzanych przez Usługobiorcę, Strony zawierają odrębną umowę powierzenia przetwarzania danych osobowych zgodnie z art. 28 RODO, stanowiącą Załącznik nr 3.

### Zgoda na wizerunek

> Podstawą prawną przetwarzania danych osobowych jest art. 6 ust. 1 lit. a RODO (zgoda osoby, której dane dotyczą). Czas przechowywania danych: do czasu wycofania zgody lub ustania celu przetwarzania.

⚠️ Podstawę przetwarzania wizerunku należy wskazać jako **jedną** z liter art. 6 ust. 1 RODO — lit. a (zgoda) i lit. f (uzasadniony interes) wykluczają się wzajemnie dla tej samej czynności. Powołanie obu jednocześnie sprawia, że wycofanie zgody staje się bezskuteczne (administrator nadal może powoływać lit. f), co narusza art. 7 ust. 3 RODO. Dla wizerunku pracownika w celach promocyjnych właściwa jest wyłącznie **lit. a**. Jeśli przetwarzanie może być oparte na lit. f — nie pobieraj zgody.

> W dowolnym momencie może Pani/Pan wycofać zgodę poprzez zgłoszenie faktu Administratorowi. Wycofanie zgody nie wpływa na zgodność z prawem przetwarzania mającego miejsce przed jej cofnięciem.

## Klauzula informacyjna (art. 13 / 14 RODO) — nagrywanie i analiza AI

Baza dotąd pokrywała umowy między stronami; to jest dokument kierowany **do osoby, której dane dotyczą**. Wymagany zawsze przy nagrywaniu rozmów, a przy analizie AI — z dodatkowymi elementami.

**Rozdziel dwie sytuacje:** dane zbierane **od osoby** (art. 13 — rozmówca, pracownik) i dane otrzymane **od kogoś innego** (art. 14 — np. dane osoby trzeciej wspomnianej w rozmowie). Przy nagrywaniu rozmów zwykle występują obie naraz.

### Komunikat przed rozmową (wersja krótka)

> Administratorem Pani/Pana danych osobowych jest [•]. Niniejsza rozmowa jest rejestrowana, a jej zapis może podlegać automatycznej transkrypcji oraz analizie z wykorzystaniem systemów sztucznej inteligencji. Szerszą informację zamieszczono pod adresem: [•].

Komunikat musi paść **przed merytoryczną częścią** rozmowy. Samo „rozmowa może być nagrywana" nie wystarcza, gdy w grę wchodzi analiza AI — to odrębna operacja i odrębna informacja.

### Elementy klauzuli pełnej

| Blok | Treść |
|---|---|
| Administrator | oznaczenie administratora i sposób kontaktu z nim (art. 13 ust. 1 lit. a); inspektor ochrony danych, o ile został powołany (lit. b) |
| Cele i podstawy | **każdy cel opisany osobno**: utrwalenie przebiegu rozmowy oraz poczynionych ustaleń · rozpatrywanie reklamacji, a także ustalenie/dochodzenie/obrona roszczeń · badanie jakości i cele szkoleniowe · realizacja obowiązków prawnych. Do każdego z nich — wskazana podstawa z art. 6 (oraz art. 9, jeżeli ma zastosowanie) |
| Udział AI | **bez niedomówień**: zapis rozmowy jest transkrybowany, a następnie poddawany analizie językowej przez system AI; jaki jest zakres tej analizy; że rezultat pełni rolę pomocniczą i **nie stanowi jedynej przesłanki** rozstrzygnięcia |
| Czego AI nie robi | system nie rozpoznaje emocji ani nie prowadzi identyfikacji i kategoryzacji biometrycznej (o ile odpowiada to stanowi faktycznemu — a powinno) |
| Odbiorcy | podmioty świadczące usługi i przetwarzające dane na polecenie administratora (transkrypcja, hosting, model), wraz ze wskazaniem kategorii odbiorców |
| Transfery | przekazanie poza EOG — ze wskazaniem mechanizmu z rozdz. V, gdy do takiego przekazania dochodzi |
| Okresy przechowywania | **osobno dla każdej kategorii**: nagrania / transkrypcje / wyniki analiz (okresy bywają odmienne — zob. `22-monitoring-pracownikow.md`) |
| Prawa | prawo dostępu, sprostowania, usunięcia, ograniczenia przetwarzania, sprzeciwu oraz przenoszenia danych; a także wniesienie skargi do PUODO |
| Dobrowolność | informacja, czy przekazanie danych stanowi wymóg ustawowy/umowny, oraz skutki odmowy ich podania |
| Zautomatyzowane decyzje | art. 22 — czy w ogóle mają miejsce; przy odpowiedzi przeczącej należy to jasno zakomunikować |

### ⚠️ Red flags klauzuli informacyjnej

Jedna podstawa prawna „na wszystko" zamiast przypisania podstawy do celu. Brak wzmianki o AI przy rozmowie faktycznie analizowanej modelem. Jeden okres retencji dla nagrań i wyników analiz. Brak informacji dla **rozmówcy** (skupienie tylko na pracowniku). Pominięcie art. 14 przy danych osób trzecich padających w rozmowie. Klauzula wręczana po rozmowie zamiast przed.

### Powiązanie z warstwą kontraktową

Klauzula informacyjna to **obowiązek administratora**, nie procesora. Procesor (dostawca AI) zwykle zastrzega w umowie, że **nie ocenia zgodności z prawem procesu** stosowanego przez administratora i nie odpowiada za brak podstawy prawnej ani niespełnienie obowiązku informacyjnego — zob. `references/checklist-dpa-art28.md` oraz `baza-klauzul/11-odpowiedzialnosc.md` (indemnifikacja odwrócona).
