# Workflow: Audyt ryzyk (standalone)

Standalone audyt ryzyk prawnych i biznesowych w umowie. Mniejszy zakres niż pełna analiza — skupiony **wyłącznie na ryzykach**, bez essentialii, checklisty kompletności i logiki wewnętrznej.

Używaj tego workflowu, gdy użytkownik mówi: "sprawdź ryzyka", "audyt", "co tu jest niebezpieczne", "co mi grozi", "sprawdź pułapki".

---

## Krok 1: Identyfikacja ryzyk

Przeczytaj umowę z uwagą na typowe obszary ryzyka. Otwórz `references/zlote-reguly.md` jako filtr, przez który patrzysz na tekst umowy.

### Typowe obszary ryzyka do sprawdzenia

**Odpowiedzialność i kary:**
- Brak limitu odpowiedzialności (cap)
- Nieograniczone lucrum cessans (utracone korzyści)
- Próba wyłączenia winy umyślnej (nieważne — art. 473 § 2 KC)
- Kary umowne niewspółmierne do naruszenia
- Brak ekwiwalentu zakazu konkurencji (przy braku — klauzula może być nieskuteczna lub naruszać dobre obyczaje)

**Prawa autorskie (przy umowach IT):**
- Brak wymienienia pól eksploatacji (bez tego — brak skutku rozporządzającego, art. 41 ust. 2 PrAut)
- Brak klauzuli anty-copyleft (ryzyko nabycia oprogramowania z GPL/AGPL)
- Brak gwarancji czystości IP od Zbywcy
- Niejasny moment przejścia praw

**Definicje i logika:**
- Pojęcia używane bez definicji
- Definicje wewnętrznie sprzeczne
- Definicje używane niespójnie z treścią

**Reprezentacja:**
- Brak wskazania umocowania osoby podpisującej (KRS / pełnomocnictwo)
- Niekompletne dane stron (brak KRS/NIP)

**Wypowiedzenie i exit:**
- Brak okresu wypowiedzenia (umowa na czas nieokreślony zawsze rozwiązywalna z 1-mies. okresem — art. 746 KC dla zlecenia)
- Brak procedury exit (zwrot materiałów, danych, rozliczenie WIP)
- Asymetria wypowiedzenia (tylko jedna strona może wypowiedzieć)

**RODO:**
- Powierzenie przetwarzania bez umowy art. 28 RODO
- Brak listy subprocesorów
- Brak procedury zwrotu/usunięcia danych

**Tytuł prawny i przekwalifikowanie:**
- W body leasing — brak wyraźnego wyłączenia art. 22 § 1 KP, brak autonomii Specjalisty (ryzyko przekwalifikowania na stosunek pracy)
- W umowie o dzieło — brak rezultatu (ryzyko przekwalifikowania na zlecenie z konsekwencjami ZUS)

**Poufność:**
- Brak okresu po zakończeniu umowy
- Brak wyłączeń (informacje publiczne, niezależnie opracowane)
- Brak kary umownej (trudna egzekucja)

**Spory:**
- Sąd niewygodny (jurysdykcja zagraniczna bez uzasadnienia)
- Prawo obce (jeśli umowa polska — niepotrzebna komplikacja)
- Klauzula arbitrażowa bez sprecyzowania sądu

---

## Krok 2: Klasyfikacja ryzyk

Dla każdego zidentyfikowanego ryzyka przypisz poziom:

| Poziom | Kryteria |
|---|---|
| 🔴 **KRYTYCZNY** | Może prowadzić do: nieważności umowy lub jej części; nieograniczonej odpowiedzialności; utraty praw autorskich; egzekucji wobec klienta na nieoczekiwanej skali; sankcji administracyjnych |
| 🟠 **WYSOKI** | Istotne ryzyko finansowe (>10% wartości umowy) lub operacyjne; trudne do naprawy po zawarciu; wymaga natychmiastowej negocjacji |
| 🟡 **ŚREDNI** | Warto poprawić; potencjalne kłopoty interpretacyjne; nieskuteczność konkretnych klauzul |
| 🟢 **NISKI** | Drobne nieścisłości; sugestie stylistyczne; usprawnienia |

---

## Krok 3: Format wyjścia

```
## AUDYT RYZYK — [Nazwa umowy/projektu]

### 🔴 RYZYKA KRYTYCZNE

#### 1. [Krótki tytuł ryzyka] — § X ust. Y
**Opis:** [konkretnie co jest źle, dlaczego ryzykowne]
**Skutek:** [co może się stać — egzekucja, nieważność, kara, utrata praw]
**Rekomendacja:** [konkretna naprawa]
**Klauzula z bazy:** `references/baza-klauzul/XX-yyy.md`

#### 2. [...]

### 🟠 RYZYKA WYSOKIE

#### 1. [...]

### 🟡 RYZYKA ŚREDNIE

#### 1. [...]

### 🟢 RYZYKA NISKIE

#### 1. [...]

---

## OCENA BEZPIECZEŃSTWA: XX/100

[2-3 zdania uzasadnienia — co wpłynęło na ocenę]

**Werdykt:** [DO PODPISANIA / DO NEGOCJACJI / DO GRUNTOWNEJ PRZERÓBKI / NIE PODPISYWAĆ]

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
```

---

## Skala oceny bezpieczeństwa

| Punkty | Opis | Werdykt |
|---|---|---|
| 85–100 | Bardzo dobra; drobne ulepszenia | DO PODPISANIA z drobnymi poprawkami |
| 70–84 | Dobra; pojedyncze obszary do negocjacji | DO NEGOCJACJI (1–3 ryzyka 🟠) |
| 50–69 | Mieszana; istotne ryzyka | DO NEGOCJACJI (kilka 🟠 lub 1 🔴) |
| 30–49 | Słaba; gruntowna przeróbka konieczna | DO GRUNTOWNEJ PRZERÓBKI |
| 0–29 | Niebezpieczna; nie podpisywać w obecnej formie | NIE PODPISYWAĆ |

Każde 🔴 odejmuje ok. 15–20 pkt, każde 🟠 ok. 5–10 pkt, 🟡 ok. 1–3 pkt, 🟢 ok. 0,5 pkt.

---

## Wybór klauzul z bazy do naprawy ryzyk

Po audycie zaproponuj **konkretne klauzule z bazy** do naprawy najpoważniejszych ryzyk. Format:

```
### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 (nieograniczona odpowiedzialność)
→ Zastosuj: `references/baza-klauzul/11-odpowiedzialnosc.md` — wariant z capem 12 mies. wynagrodzenia

🔴 RYZYKO 2 (brak klauzuli anty-copyleft)
→ Zastosuj: `references/baza-klauzul/08-prawa-autorskie-ip.md` (wariant z gwarancjami czystości IP)

🟠 RYZYKO 3 (brak okresu poufności po umowie)
→ Zastosuj: `references/baza-klauzul/09-poufnosc.md` — model warstwowy okresów poufności (10 lat / bezterminowo dla tajemnicy przedsiębiorstwa)
```

Nie wkleja się tu pełnej treści klauzul (chyba że użytkownik prosi) — pokazujesz, **gdzie ich szukać**.
