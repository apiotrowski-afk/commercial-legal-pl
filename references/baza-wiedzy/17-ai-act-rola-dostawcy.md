---
type: Baza wiedzy
title: AI Act — rola dostawcy i pułapka art. 25
tags: [AI Act, dostawca, provider, deployer, art. 25, art. 6, art. 13, art. 14, załącznik III, załącznik IV, klasyfikacja, instrukcja obsługi, white-label]
contract_types: [umowa wdrożeniowa AI, SaaS AI, licencja oprogramowania, umowa o dzieło IT]
risk_level: wysoki
mandatory_for: [umowy dotyczące systemów AI, white-label, istotna modyfikacja systemu]
requires: [14-polityka-ai-wdrozenie.md]
timestamp: 2026-09-22
---

# AI Act — rola dostawcy i pułapka art. 25

## TL;DR — co trzeba wiedzieć

Obowiązki z AI Act rozkładają się nierówno: **dostawca** dźwiga dokumentację techniczną, instrukcję obsługi, nadzór człowieka, rejestry i rejestrację, **podmiot stosujący** (deployer) — znacznie mniej. Dlatego pierwsze pytanie przy umowie brzmi nie „czy to system wysokiego ryzyka", lecz **„kto jest tu dostawcą"**. Odpowiedź bywa inna, niż strony zakładają, bo rola przenosi się z mocy art. 25 także wtedy, gdy nikt tego nie chciał.

`baza-wiedzy/14-polityka-ai-wdrozenie.md` opisuje obowiązki od strony **deployera**. Ten plik patrzy z drugiej strony.

## Pułapka art. 25 — rola dostawcy przenosi się sama

Dystrybutor, importer, deployer albo inna strona trzecia **staje się dostawcą** systemu wysokiego ryzyka w trzech przypadkach:

1. umieszcza **własną nazwę lub znak towarowy** na systemie już wprowadzonym do obrotu,
2. dokonuje **istotnej modyfikacji** systemu,
3. **zmienia przeznaczenie** systemu tak, że staje się on systemem wysokiego ryzyka.

To najczęściej pomijane ryzyko kontraktowe w umowach IT z AI. Klient kupujący rozwiązanie w modelu white-label albo dostosowujący je pod siebie przejmuje wtedy **pełen reżim dostawcy** — z dokumentacją techniczną, systemem zarządzania jakością i odpowiedzialnością włącznie.

Umowa powinna to przesądzać z góry: określać **przeznaczenie** systemu wprost, wyłączać zastosowania z załącznika III, uzależniać istotne modyfikacje i oznaczanie własną marką od zgody, a na wypadek przejścia roli — dzielić obowiązki między strony. Brak takiego zapisu nie oznacza, że rola nie przejdzie; oznacza, że przejdzie bez uzgodnienia, kto za co odpowiada.

## Klasyfikacja — kolejność kroków ma znaczenie

Klasyfikację przeprowadza się **odrębnie dla każdego zastosowania**, nie raz dla produktu. Kolejność nie jest dowolna, bo wcześniejszy krok potrafi zamknąć dalsze:

| Krok | Pytanie | Skutek |
|---|---|---|
| 1 | System AI w rozumieniu art. 3 pkt 1? | jeśli nie — AI Act nie ma zastosowania |
| 2 | Praktyka zakazana (art. 5)? | jeśli tak — zastosowanie **zablokowane**, dalsze kroki bezprzedmiotowe |
| 3 | Wysokie ryzyko (art. 6)? | zał. I (produkty regulowane) albo zał. III (samodzielne systemy) |
| 4 | Odstępstwo z art. 6 ust. 3? | tylko przy zał. III, przesłanki lit. a–d |
| 5 | Model GPAI (art. 53)? | odrębna warstwa obowiązków |
| 6 | Przejrzystość (art. 50)? | interakcja z AI, treści syntetyczne, deepfake |

**Najczęstszy błąd siedzi w kroku 4.** Odstępstwo z art. 6 ust. 3 nie działa, gdy system prowadzi **profilowanie osób fizycznych** — bez względu na to, jak niewielką rolę odgrywa w decyzji. Profilowanie wyłącza odstępstwo automatycznie.

Drugi błąd: potraktowanie odstępstwa jako zwolnienia z formalności. Dostawca, który uznaje system z obszaru zał. III za niebędący systemem wysokiego ryzyka, musi to **udokumentować przed wprowadzeniem do obrotu** i zarejestrować (art. 6 ust. 4 w zw. z art. 49 ust. 2).

## Co ciąży na dostawcy

Dokumentacja techniczna z **załącznika IV** (art. 11) obejmuje m.in. opis systemu i jego przeznaczenia, dane i zbiory treningowe, architekturę i decyzje projektowe, metryki dokładności, znane ograniczenia i przewidywalne niewłaściwe wykorzystanie, środki nadzoru człowieka, testy i walidację oraz system zarządzania ryzykiem. Poza załącznikiem IV: rejestry zdarzeń (art. 12), system zarządzania jakością (art. 17), rejestracja w bazie UE (art. 49) i oznakowanie zgodności.

Dla MŚP przewidziano uproszczoną formę dokumentacji — nie zwolnienie z niej.

## Instrukcja obsługi — trzy reguły, które decydują o jej jakości

Art. 13 ust. 3 wylicza, co instrukcja ma zawierać. O jej wartości decyduje jednak coś innego:

**Adresat.** Instrukcja jest dla *podmiotu stosującego*, nie dla prawnika ani inżyniera. Poziom szczegółu dobiera się do wiedzy odbiorcy, a nie do kompletności opisu.

**Spójność z dowodami.** Instrukcja **nie może przedstawiać systemu korzystniej, niż wynika to z testów**. Ograniczenia i przewidywalne niewłaściwe wykorzystanie nazywa się wprost. Rozjazd między instrukcją a wynikami walidacji jest samodzielnym naruszeniem.

**Wykonalność obowiązków odbiorcy.** Instrukcja musi *umożliwiać* deployerowi wykonanie art. 26: zapewnienie nadzoru kompetentnych osób, kontrolę danych wejściowych, monitorowanie działania, prowadzenie rejestrów oraz poinformowanie pracowników i osób objętych decyzją. Instrukcja, z której nie da się tego wyczytać, przenosi na klienta obowiązek bez narzędzi do jego wykonania — i wraca do dostawcy jako spór.

## Nadzór człowieka (art. 14)

Nadzór ma być **rzeczywisty**, nie formalny. Osoba nadzorująca musi rozumieć możliwości i ograniczenia systemu, mieć realną możliwość odrzucenia albo skorygowania wyniku oraz zatrzymania systemu. Zapis w umowie, że „klient zapewnia nadzór człowieka", bez wskazania kompetencji i uprawnień tej osoby, nie spełnia tego wymogu.

## Terminy

Stan prawny po rozporządzeniu **2026/1744 (Digital Omnibus)** — terminy uległy przesunięciu i mogą się jeszcze zmienić, zob. tabelę w `baza-wiedzy/14-polityka-ai-wdrozenie.md`. Kluczowe dla roli dostawcy: załącznik III — **2 grudnia 2027 r.**, załącznik I — **2 sierpnia 2028 r.**

## Powiązania

- `baza-wiedzy/14-polityka-ai-wdrozenie.md` — te same przepisy od strony deployera
- `baza-klauzul/21-polityka-ai.md` — polityka korzystania z AI w organizacji
- `baza-klauzul/22-monitoring-pracownikow.md` — zał. III pkt 4 lit. b w praktyce
- `baza-klauzul/20-regulamin-usdde-aup.md` — art. 50, oznaczanie treści
