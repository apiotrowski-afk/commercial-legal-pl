---
type: Klauzula
title: Poufność
tags: [poufność, NDA, informacje-poufne, tajemnica-przedsiębiorstwa, breach-notification, wykluczenia, 72h]
contract_types: [NDA, body-leasing, licencyjna, ramowa, B2B-IT]
risk_level: wysoki
mandatory_for: [NDA]
requires: [03-definicje.md, 18-zwrot-materialow.md]
timestamp: 2026-06-27
---

# Poufność

## Kiedy stosować i na co uważać

Ochrona informacji poufnych obu stron. W IT obejmuje kod źródłowy, architekturę systemów, dane klientów, know-how technologiczny. Może być w umowie głównej lub jako osobne NDA.

### ⚠️ Red flags

Brak definicji informacji poufnych. Brak okresu obowiązywania po zakończeniu umowy. Obowiązek poufności tylko jednostronny. Brak wyłączeń (informacje publiczne, uzyskane niezależnie, wymagane prawem). Brak kary umownej — trudna egzekucja.

### Klauzula wzorcowa (generyczny IT)

> Strona Otrzymująca zobowiązuje się do: (a) zachowania Informacji Poufnych w ścisłej tajemnicy; (b) wykorzystywania ich wyłącznie w celu realizacji Umowy; (c) ujawniania ich wyłącznie osobom, których udział jest niezbędny, pod warunkiem zobowiązania ich do poufności. Obowiązek poufności obowiązuje przez okres trwania Umowy oraz 3 lata po jej wygaśnięciu. Kara umowna za naruszenie: [kwota] PLN za każdy przypadek.

## Klauzule z umów KTZR

### NDA IT (KTZR)

> Strona Otrzymująca zobowiązuje się do: zachowania Informacji Poufnych w ścisłej tajemnicy; wykorzystywania ich wyłącznie w celu realizacji Projektu; zastosowania co najmniej takiej samej staranności przy ochronie, z jaką chroni własne informacje poufne — jednak nie mniejszej niż należyta staranność wymagana od profesjonalisty.

> Zobowiązanie do zachowania poufności obowiązuje przez 5 (pięć) lat od dnia zakończenia Projektu lub rozmów między Stronami — niezależnie od przyczyny zakończenia współpracy.

> Za Informacje Poufne nie uznaje się informacji, które: (a) są publicznie dostępne w sposób inny niż w wyniku naruszenia Umowy; (b) były w posiadaniu Strony Otrzymującej przed ich ujawnieniem; (c) zostały niezależnie opracowane; (d) uzyskane od osoby trzeciej bez obowiązku poufności; (e) muszą być ujawnione na podstawie przepisów prawa. Ciężar dowodu wyłączeń spoczywa na Stronie Otrzymującej.

> Niezwłoczne — nie później niż w ciągu 72 godzin — pisemne powiadomienie Strony Ujawniającej o każdym przypadku nieuprawnionego ujawnienia, utraty, kradzieży lub uzasadnionym podejrzeniu naruszenia poufności.

> ⚠️ **Przy łączeniu z klauzulą Poufność techniczna** (sekcja poniżej): stosuj termin 24-godzinny jako lex specialis — usuń termin 72-godzinny z wersji końcowej, aby uniknąć sprzeczności.

### Body Leasing IT (KTZR)

> Usługodawca zobowiązuje się do zawarcia ze Specjalistami odrębnych umów o zachowaniu poufności (NDA) w zakresie co najmniej równoważnym z niniejszym paragrafem, przed przystąpieniem Specjalisty do świadczenia Usług.

### Umowa ramowa współpracy prowizyjnej

> Wszelkie informacje przekazane przez Zleceniodawcę w jakiejkolwiek formie, niezależnie od opatrzenia ich klauzulą „Informacje poufne”, stanowią informacje poufne i nie będą (również po okresie obowiązywania Umowy) użyte przez Partnera do innego celu niż należyta realizacja Umowy.

### Umowa licencyjno-doradcza

> Licencjobiorca zobowiązuje się do zachowania w ścisłej tajemnicy wszelkich Informacji Poufnych zarówno w trakcie trwania Umowy, jak i bezterminowo po jej zakończeniu.

### Poufność techniczna (IT — kod źródłowy, dane dostępowe, infrastruktura)

> Informacje Poufne obejmują w szczególności: (a) dane techniczne — kod źródłowy, architekturę systemów, loginy, hasła, certyfikaty SSL, klucze API, parametry środowiskowe; (b) dane operacyjne — bazy danych, warunki handlowe, know-how procesowe; (c) dane finansowe — obroty, marże, koszty operacyjne; (d) plany biznesowe — projekty nowych modułów, strategie rozwoju. W razie wątpliwości co do charakteru danej informacji domniemywa się, że stanowi Informację Poufną.

> Strona Otrzymująca nie jest uprawniona do kopiowania, eksportowania, pobierania ani przechowywania poza infrastrukturą Strony Ujawniającej żadnych danych, kodu źródłowego ani innych Informacji Poufnych. Zakaz obejmuje wszelkie formy i nośniki, w tym pliki lokalne, nośniki zewnętrzne, usługi chmurowe i prywatne repozytoria. Dozwolone są wyłącznie zatwierdzone kopie zapasowe.

> W przypadku powzięcia podejrzenia o nieuprawnionym dostępie do Informacji Poufnych, ich utraty lub ujawnienia, Strona Otrzymująca zobowiązuje się powiadomić Stronę Ujawniającą w formie dokumentowej nie później niż w ciągu 24 godzin od powzięcia informacji. Brak terminowego poinformowania traktowany jest jako odrębne naruszenie poufności.

> Strona Ujawniająca ma prawo do bieżącego monitorowania aktywności Strony Otrzymującej w zakresie korzystania z udostępnionych zasobów, w tym przeglądania logów i przeprowadzania audytów bezpieczeństwa.

> Obowiązki z niniejszego paragrafu wiążą przez cały okres obowiązywania Umowy oraz przez 10 lat od daty jej zakończenia, niezależnie od przyczyny. Dla informacji stanowiących tajemnicę przedsiębiorstwa w rozumieniu art. 11 ust. 2 u.z.n.k. obowiązek poufności jest bezterminowy.

## Zobowiązanie jednostronne (NDA składane, nie zawierane)

Odmiana używana, gdy poufność ma chronić **tylko jedną stronę** i nie ma potrzeby negocjowania dwustronnej umowy: usługodawca (kancelaria, doradca, wykonawca) **składa oświadczenie** adresatowi na etapie rozmów wstępnych. Szybsze niż NDA wzajemne, bo nie wymaga negocjacji — i psychologicznie łatwiejsze przy pozyskiwaniu klienta.

Cechy konstrukcyjne, które trzeba zachować:

> **Retroaktywność.** Ochroną objęte są Informacje Poufne ujawnione po dniu złożenia zobowiązania, **a także te udostępnione wcześniej**, w szczególności w korespondencji prowadzonej przed tym dniem.

> **Brak zobowiązania do kontraktowania.** Żadna ze Stron nie jest wskutek złożenia zobowiązania zobligowana do zawarcia umowy ani do prowadzenia dalszych rozmów. Zobowiązanie **nie skutkuje przejściem jakichkolwiek praw do przedsięwzięcia, z którym wiążą się Informacje Poufne, ani nie oznacza udzielenia licencji.**

> **Nieodwołalność.** Składającemu **nie przysługuje prawo jednostronnego odwołania ani zawężenia** niniejszego zobowiązania.

> **Skuteczność wobec następcy.** Zobowiązanie wiąże także następcę prawnego Adresata — w tym spółkę powstałą w wyniku przekształcenia, jak również podmiot powołany przez Adresata do prowadzenia przedsięwzięcia, z którym wiążą się Informacje Poufne — ze skutkiem od dnia zawiadomienia [kanał].

> **Rola przy danych osobowych.** Jeżeli Informacje Poufne zawierają dane osobowe, Składający przetwarza takie dane **jako odrębny administrator** i czyni to wyłącznie dla celu wskazanego w pkt [•]. Poza tym celem Składający nie korzysta z nich na własne potrzeby.

Ostatnia klauzula jest ważna: doradca analizujący cudzy projekt zwykle **nie jest procesorem** — jest odrębnym administratorem. Wpisanie tego wprost oszczędza sporu o umowę powierzenia (zob. `references/checklist-dpa-art28.md` — kwalifikacja ról).

### Zakres Informacji Poufnych przy projekcie IT/AI

Katalog wart skopiowania, bo pokrywa to, co strony zwykle pomijają:

> architektura rozwiązania, kod źródłowy, specyfikacje oraz dokumentacja techniczna, **w tym sposób wdrożenia i ustawienia integracji** z systemami zewnętrznymi · wykorzystywane modele wraz z parametrami ich działania, **w tym treść poleceń kierowanych do modeli (promptów)**, logika przetwarzania oraz reguły analityczne · dane powierzone przez kontrahentów · **dane identyfikujące klientów i kontrahentów**, ustalone warunki handlowe, stawki oraz model rozliczeń · plany produktowe, model biznesowy i informacje finansowe · rezultaty prac badawczo-rozwojowych, prototypy oraz wyniki testów · **sam fakt prowadzenia rozmów, jak również ich treść**.

Dwa elementy rzadko spotykane, a cenne: **prompty jako informacja poufna** (przy produktach AI to realne know-how) oraz **sam fakt rozmów** (chroni przed wyciekiem informacji o negocjacjach).

### ⚠️ Klauzula AI w NDA — zakaz karmienia modeli

Klauzula, której brak w większości NDA sprzed 2025 r., a która dziś jest niezbędna:

> Strona Otrzymująca może wprowadzać Informacje Poufne do narzędzi opartych na sztucznej inteligencji **tylko w takim przypadku, gdy dostawca danego narzędzia wyłączył wykorzystywanie przekazywanych mu danych do trenowania modeli**. Strona Otrzymująca **nie trenuje na Informacjach Poufnych modeli własnych**.

Bez tego zapisu wklejenie cudzej dokumentacji do publicznego chatbota nie narusza NDA wprost — a faktycznie wynosi informację poza kontrolę stron. Konstrukcja jest dwuczłonowa: (1) narzędzia cudze — tylko z wyłączonym treningiem, (2) modele własne — zakaz bezwarunkowy. Odpowiednik po stronie umowy powierzenia → `references/checklist-dpa-art28.md`, klauzula A1.

### Tajemnica zawodowa (gdy składającym jest radca prawny / adwokat)

> Wszystko, czego Składający dowiedział się w związku z udzielaniem pomocy prawnej, pozostaje objęte **tajemnicą zawodową radcy prawnego**, o której mowa w art. 3 ust. 3–5 ustawy o radcach prawnych. Tajemnica ta **nie jest ograniczona terminem, a radca prawny nie może być z niej zwolniony**. Niniejsze zobowiązanie w żaden sposób nie zawęża ochrony płynącej z tajemnicy zawodowej.

Relacja jest jednokierunkowa: NDA **dokłada** ochronę, nigdy jej nie zawęża. Wyjątki od poufności muszą wprost obejmować ujawnienia wymagane prawem (w tym AML), obronę przed roszczeniami klienta i postępowanie dyscyplinarne — z powiadomieniem przed ujawnieniem, o ile nie jest zakazane.

Zwrot materiałów **nie obejmuje** dokumentacji zachowywanej na podstawie przepisów lub zasad wykonywania zawodu (akta sprawy, dokumentacja rozliczeniowa, dokumentacja do obrony przed roszczeniami) — ta pozostaje objęta poufnością.
