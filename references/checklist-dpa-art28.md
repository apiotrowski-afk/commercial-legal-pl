---
type: Referencja
title: Siatka audytu umowy powierzenia (DPA — art. 28 RODO)
tags: [RODO, DPA, umowa powierzenia, art. 28, procesor, subprocesor, audyt, checklist, powierzenie]
contract_types: [DPA, umowa powierzenia, SaaS, hosting, body-leasing, wdrożenie]
risk_level: krytyczny
mandatory_for: [DPA, powierzenie danych osobowych]
requires: [14-rodo.md, normy-bezwzglednie.md]
timestamp: 2026-08-02
---

# Siatka audytu umowy powierzenia (DPA — art. 28 RODO)

Dedykowany checklist do **przeglądu i konstrukcji umowy powierzenia** (DPA). Uzupełnia `baza-wiedzy/08-rodo-powierzenie-konstrukcja.md` (dlaczego) o siatkę operacyjną (co sprawdzić punkt po punkcie, z flagą i remediacją). Otwórz przy audycie/generowaniu DPA albo gdy umowa główna zawiera przetwarzanie danych osobowych.

Działa na **zamkniętym wejściu** — wgranej/analizowanej umowie. Przy cytowaniu klauzul stosuj R11 (cytat musi być dosłownie w tekście).

> **Dyscyplina cytatów (R1):** numery artykułów i sygnatury decyzji UODO / wyroków TSUE poniżej to mapa referencyjna z LEX. W raporcie klienckim cytat przepisu → `verify_article()` lub `[NIEZWERYFIKOWANE]`; sygnatur decyzji/wyroków nie podawaj z pamięci — oznacz `[SYGNATURA NIEZWERYFIKOWANA]`, jeśli nie masz pewności.

## ⚠️ Red flags (natychmiast 🔴)

Brak pisemnej umowy powierzenia mimo faktycznego przetwarzania (naruszenie art. 28 ust. 3 i 9 — kara z art. 83 ust. 4 lit. a). Opis przedmiotu/celu ograniczony do ogólnika („świadczenie usług IT") bez katalogu operacji, danych i kategorii osób. Brak którejkolwiek z klauzul lit. a–h. „Milcząca" zgoda ogólna na subprocesorów bez realnej możliwości sprzeciwu. Wyjątek od usunięcia danych oparty na „kopiach technicznych", nie na obowiązku prawnym. Prawo audytu iluzoryczne (wyłączone lub nierealne do wykonania). Kwalifikacja jako powierzenie tam, gdzie faktycznie jest współadministrowanie (art. 26) lub odrębne administrowanie.

## Siatka — elementy obligatoryjne (art. 28 ust. 3)

Każdy element zamknij flagą: 🟢 obecny i adekwatny · 🟡 obecny, ale ogólnikowy/niekompletny · 🔴 brak lub sprzeczny z RODO · `— n/d`. Suma = liczba pozycji (bramka kompletności R9).

### Elementy ramowe (nagłówek art. 28 ust. 3)

| # | Element | Co sprawdzić | Kryterium 🔴 | Remediacja (kierunek) |
|---|---|---|---|---|
| R1 | Przedmiot i czas przetwarzania | konkretny opis, nie „usługi IT" | brak lub czysty ogólnik | dopisać zakres operacji + okres = czas umowy głównej |
| R2 | Charakter i cel przetwarzania | po co i jak (systemy, konteksty) | brak | opis celu powiązany z usługą |
| R3 | Rodzaj danych osobowych | katalog kategorii danych | brak | wymienić kategorie (dane zwykłe / szczególne art. 9) |
| R4 | Kategorie osób, których dane dotyczą | pracownicy / klienci / kontrahenci itd. | brak | wymienić kategorie osób |
| R5 | Obowiązki i prawa administratora | rola administratora (instrukcje, dostarczanie danych) | brak | opisać uprawnienia i obowiązki administratora |

### Klauzule lit. a–h (art. 28 ust. 3)

| # | Lit. | Obowiązek procesora | Kryterium 🔴 | Remediacja (kierunek) |
|---|---|---|---|---|
| a | a | przetwarza **wyłącznie na udokumentowane polecenie** administratora (też przy transferach), **chyba że** wymaga tego prawo UE/państwa członkowskiego — wtedy informuje administratora **przed** rozpoczęciem, o ile prawo nie zabrania z ważnych względów interesu publicznego | brak klauzuli poleceń albo swoboda procesora | dodać: przetwarzanie tylko wg udokumentowanych poleceń + wyjątek prawny z obowiązkiem uprzedniej informacji |
| b | b | osoby upoważnione **zobowiązane do poufności** (umownie lub ustawowo) | brak | klauzula zobowiązania do tajemnicy osób upoważnionych |
| c | c | wdraża środki **bezpieczeństwa art. 32** | brak lub puste odesłanie | katalog TOMs lub odesłanie do załącznika/polityki (nie może być pusty) |
| d | d | przestrzega warunków **subprocesora** (art. 28 ust. 2 i 4) | brak | zob. sekcja „Subprocesor" niżej |
| e | e | **pomaga w realizacji praw osób** (rozdz. III, art. 12–22) środkami techn./organ. | brak | klauzula wsparcia przy żądaniach osób (podział ról, terminy — zob. Moduł 6) |
| f | f | **pomaga w obowiązkach art. 32–36** (bezpieczeństwo, naruszenia, DPIA, konsultacje) | brak | klauzula współpracy przy naruszeniach i DPIA |
| g | g | po zakończeniu **usuwa lub zwraca** dane + kopie, chyba że prawo nakazuje przechowanie | brak lub wyjątek „kopie techniczne" | zob. sekcja „Zwrot/usunięcie" niżej |
| h | h | **udostępnia informacje + umożliwia audyt**; **niezwłocznie** informuje, gdy jego zdaniem polecenie narusza RODO | brak lub audyt iluzoryczny | zob. sekcja „Audyt" niżej |

**Skutek braków:** brak pisemnego/elektronicznego instrumentu lub brak elementów art. 28 ust. 3 stanowi **naruszenie RODO** (za wytycznymi EROD 07/2020; kara z art. 83 ust. 4 lit. a) — **jeżeli faktycznie zachodzi relacja administrator–procesor** (ustalana funkcjonalnie, niezależnie od nazwy). Brak instrumentu nie zmienia procesora automatycznie w administratora. Umowa ma **wyjaśniać sposób wdrożenia** obowiązków, nie tylko powtarzać przepis. Praktyka Prezesa UODO potwierdza tę linię w szeregu decyzji dotyczących art. 28 ust. 1, 3 i 9 — **sygnatur nie podawaj z pamięci**; do raportu klienckiego wyszukaj decyzję w rejestrze UODO i zacytuj ze źródła.

## Forma (art. 28 ust. 9)

Umowa (lub inny akt prawny) — **forma pisemna, w tym elektroniczna** (art. 28 ust. 9; nie musi to być kwalifikowana forma pisemna w rozumieniu KC). Brak formy przy faktycznym przetwarzaniu = naruszenie art. 28 ust. 3 i 9. Odpowiedzialność administratora i procesora ocenia się **odrębnie**, według obowiązków ciążących na każdej stronie — administrator nie uwolni się przez przyjęcie narzuconych, niezgodnych warunków, ale procesor ma też własne, bezpośrednie obowiązki. Flaga 🔴, jeśli DPA istnieje tylko jako ustalenie ustne / w korespondencji bez podpisu.

## Subprocesor (art. 28 ust. 2 i 4)

- **Zgoda** administratora: szczegółowa (konkretny podmiot) **lub** ogólna (kategorie + obowiązek notyfikacji zmian i **realna możliwość sprzeciwu**). „Milcząca" zgoda bez sprzeciwu → 🟡/🔴.
- **Flow-down (ust. 4):** umowa z subprocesorem nakłada **te same obowiązki** ochrony danych (adekwatnie do zakresu podpowierzenia) — gwarancje art. 32, klauzule lit. a–h, naruszenia, zwrot/usunięcie, audyt.
- **Odpowiedzialność:** za niewywiązanie się subprocesora **pełną odpowiedzialność wobec administratora ponosi procesor pierwotny** (art. 28 ust. 4) — nie wyłącza to ewentualnej bezpośredniej odpowiedzialności subprocesora z RODO lub umowy.
- Remediacja: forma zgody + tryb notyfikacji + termin sprzeciwu + obowiązek odwzorowania DPA w umowie z subprocesorem + przejęcie odpowiedzialności.

## Zwrot / usunięcie po zakończeniu (art. 28 ust. 3 lit. g)

- Zasada: **zwrot albo usunięcie** danych + usunięcie kopii.
- Ustawowy wyjątek **wyłącznie** gdy konkretny przepis prawa UE/PL nakazuje przechowanie (np. podatkowy, księgowy) — samo istnienie kopii zapasowych **nie tworzy** wyjątku pozwalającego zachować dane bezterminowo.
- **Backupy — ujęcie praktyczne:** nie oznacza to konieczności natychmiastowego nadpisania każdego nośnika. Umowa może określić **techniczny cykl usunięcia danych z kopii zapasowych**, pod warunkiem: izolacji kopii od zwykłego użycia, zakazu dalszego aktywnego przetwarzania, użycia wyłącznie do odtworzenia systemu (z ponownym wykonaniem usunięcia) i usunięcia najpóźniej z końcem uzasadnionego cyklu retencji.
- Klauzula powinna: wskazać wybór (zwrot/usunięcie) po stronie administratora; wymagać podania **podstawy prawnej i okresu** dalszego przechowania; ograniczyć przetwarzanie przechowywanych danych **tylko do celu tego obowiązku**.

## Audyt i inspekcja (art. 28 ust. 3 lit. h)

- Minimum: procesor **udostępnia informacje** na wykazanie zgodności + **umożliwia audyt/inspekcję** administratora lub upoważnionego audytora i przyczynia się do nich.
- Dopuszczalne **rozsądne** ograniczenia (nie czyniące prawa iluzorycznym): częstotliwość (np. raz/rok + ad hoc po incydencie), oparcie o raporty/certyfikaty (ISO 27001) jako podstawowy środek z prawem własnej inspekcji przy wątpliwościach, podział kosztów (rutyna vs audyt po naruszeniu), wcześniejsze zawiadomienie z możliwością audytu ad hoc przy incydencie.
- 🔴, jeśli audyt wyłączony lub warunki czynią go niewykonalnym.

## Powiązania

- Kwalifikacja ról (administrator/współadministrator/procesor) i skutki błędu → `baza-wiedzy/08-rodo-powierzenie-konstrukcja.md`.
- Bezpieczeństwo i naruszenia (okno kontraktowe) → `baza-wiedzy/09-rodo-bezpieczenstwo-i-naruszenia.md`.
- art. 28 RODO w katalogu norm bezwzględnie obowiązujących → `references/normy-bezwzglednie.md` (R10).
- Klauzule wzorcowe → `baza-klauzul/14-rodo.md`.
