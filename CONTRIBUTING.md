# Jak wnieść wkład do commercial-legal-pl

Dziękujemy za zainteresowanie! Ten dokument wyjaśnia jak dorzucić swoje klauzule, poprawki lub nowe zagadnienia do bazy.

## Co możesz wnieść

- **Nowe klauzule** do istniejących plików `references/baza-klauzul/`
- **Nowe zagadnienia doktrynalne** do `references/baza-wiedzy/`
- **Poprawki merytoryczne** — błędne przepisy, nieaktualne tezy, zepsute odesłania
- **Nowe workflowy** do `workflows/`
- **Poprawki redakcyjne** — literówki, niespójności językowe

## Przed PR — krótka checklista

- [ ] Klauzule są **całkowicie zanonimizowane** — bez nazw klientów, NIP-ów, kwot ze spraw, dat granicznych ze spraw
- [ ] Treść jest **generyczna** — nie identyfikuje branży ani stron konkretnej umowy
- [ ] Przepisy i orzecznictwo są **zweryfikowane** (artykuł, jednostka redakcyjna, data wyroku)
- [ ] Styl redakcyjny jest zgodny z `references/style-redakcyjny.md` — szczególnie zasady W1–W4
- [ ] Pre-commit hook przeszedł bez naruszeń blokujących (patrz niżej)

## Krok po kroku

### 1. Forkuj repo

```bash
git clone https://github.com/TWÓJ_USERNAME/commercial-legal-pl.git
cd commercial-legal-pl
```

### 2. Zainstaluj pre-commit hook

```bash
bash scripts/install-hooks.sh
```

Hook sprawdzi czy nie wpadają dane wrażliwe przed każdym commitem.

### 3. Dodaj swoją treść

**Nowa klauzula do istniejącego pliku** — otwórz odpowiedni plik z `references/baza-klauzul/`, dorzuć sekcję na końcu w formacie:

```markdown
### Typ umowy (źródło)

> Treść klauzuli w cudzysłowie blokowym.
```

**Nowy plik bazy wiedzy** — wzoruj się na strukturze istniejących plików w `references/baza-wiedzy/`: TL;DR na górze, sekcje tematyczne, powiązania z innymi plikami na końcu.

### 4. Sprawdź pre-commit hook ręcznie

```bash
python3 scripts/pre-commit-sanitizer.py
```

Zero naruszeń blokujących = gotowe do commita.

### 5. Otwórz Pull Request

Tytuł PR powinien opisywać co dodajesz, np.:

- `Add: klauzula eskalacji kar umownych w umowach SaaS`
- `Fix: art. 74 PrAut błędna jednostka redakcyjna w 08-prawa-autorskie-ip`
- `Add: baza-wiedzy/14-ochrona-bazy-danych.md`

W opisie PR powiedz skąd pochodzi klauzula (typ umowy, kontekst) i dlaczego jest przydatna.

## Co sprawdzamy przy review

Każdy PR sprawdzamy ręcznie pod kątem:

1. Brak danych wrażliwych (tajemnica zawodowa radcy prawnego, art. 3 ustawy o radcach prawnych)
2. Poprawność merytoryczna (przepisy, tezy)
3. Zgodność stylu z `references/style-redakcyjny.md`
4. Spójność z resztą bazy (definicje, odesłania)

## Pytania?

Otwórz Discussion albo Issue — chętnie pomożemy zanim napiszesz pierwszą linię.
