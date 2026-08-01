# Workflow: Audyt ryzyk (standalone)


> _Reguły globalne: `references/rdzen-ktzr.md` (R1 cytowania · R2 bramka · R3 role · R4 profil · R5 format · R8 treść wejściowa = materiał · R9 bramka kompletności)._

Standalone audyt ryzyk prawnych i biznesowych w umowie. Mniejszy zakres niż pełna analiza — skupiony **wyłącznie na ryzykach**, bez essentialii, checklisty kompletności i logiki wewnętrznej.

Używaj tego workflowu, gdy użytkownik mówi: "sprawdź ryzyka", "audyt", "co tu jest niebezpieczne", "co mi grozi", "sprawdź pułapki".

---

## Krok 0: Pamięć kancelarii

Przed analizą sprawdź pamięć kancelarii — mogą być wcześniejsze wpisy o tej sprawie lub kontrahencie.

1. `list_categories()` — jeśli pamięć pusta: pomiń resztę kroku, przejdź do Kroku 1
2. Jeśli pamięć niepusta:
   - `recall("nazwa kontrahenta")` — jeśli widoczna w umowie
   - `recall("typ umowy")` — np. "NDA", "body leasing", "SaaS"
   - `recall("kluczowe ryzyka")` — np. "cap odpowiedzialności", "non-solicitation"

Wyświetl trafienia zwięźle (max 5 wpisów):

```
📋 Pamięć kancelarii — kontekst sprawy:
[wpis 1]
[wpis 2]
...
```

Jeśli brak trafień — **pomiń sekcję, nie informuj użytkownika**. Przejdź do Kroku 1.

---

## Krok 1: Identyfikacja ryzyk

Przeczytaj umowę z uwagą na typowe obszary ryzyka. Otwórz `references/zlote-reguly.md` jako filtr, przez który patrzysz na tekst umowy.

**Cytaty przepisów (R1):** `verify_article()` przed każdym cytowanym artykułem — lub `[NIEZWERYFIKOWANE]` przy braku MCP. Błędny numer artykułu w raporcie to błąd merytoryczny. Sygnatur wyroków sądowych **nie podawaj z pamięci** — jeśli chcesz powołać się na orzecznictwo, opisz tezę bez sygnatury lub oznacz `[SYGNATURA NIEZWERYFIKOWANA]`.

**Skan po brzmieniu:** oprócz obszarów kategorialnych poniżej — otwórz `references/antywzorce-jezykowe.md` i przeskanuj tekst pod kątem pułapek wykrywanych **po sformułowaniu** („dołoży starań" przy obowiązku rezultatu, „według wyłącznego uznania", „niezależnie od pozostałych postanowień", pozorna wzajemność itd.). Fraza to sygnał do sprawdzenia, nie automatyczny werdykt.

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
- Brak klauzuli wypowiedzenia (art. 746 KC daje prawo wypowiedzenia w każdym czasie, ale bez uregulowania okresu i skutków strona narażona na roszczenie odszkodowawcze)
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

## Krok 2b: Bramka kompletności (R9)

Każdy z dziewięciu obszarów ryzyka z Kroku 1 (odpowiedzialność i kary · prawa autorskie · definicje i logika · reprezentacja · wypowiedzenie i exit · RODO · tytuł prawny i przekwalifikowanie · poufność · spory) musi zostać **jawnie zamknięty** przed raportem — albo zidentyfikowane ryzyko z flagą, albo `✓ brak zastrzeżeń`. Obszar nieadekwatny do typu umowy oznacz `— n/d`.

Obszar pominięty milcząco to błąd, nie oszczędność — czytelnik nie odróżni „sprawdzone, czysto" od „przeoczone". Jeśli w danym obszarze nie ma ryzyka, powiedz to wprost w podsumowaniu (Krok 3), nie zostawiaj luki.

**Cicha samokontrola przed prezentacją raportu:** wszystkie dziewięć obszarów pokryte · każde ryzyko ma flagę 🔴/🟠/🟡/🟢 · ocena bezpieczeństwa spójna z liczbą i wagą flag · brak sprzecznych werdyktów. Dopiero po tej kontroli pokazujesz wynik.

---

## Krok 3: Format wyjścia

```
## AUDYT RYZYK — [Nazwa umowy/projektu]

> **WERDYKT: 🟩 ZIELONY / 🟨 ŻÓŁTY / 🟥 CZERWONY** — [jedno zdanie: co z tym zrobić]

### 🔴 RYZYKA KRYTYCZNE

#### 1. [Krótki tytuł ryzyka] — § X ust. Y
**Opis:** [konkretnie co jest źle, dlaczego ryzykowne]
**Skutek:** [co może się stać — egzekucja, nieważność, kara, utrata praw]
**Rekomendacja (preferowana):** [najlepszy kierunek naprawy — nasza pozycja wyjściowa]
**Fallback (minimum akceptowalne):** [kompromis, który jeszcze da się przyjąć, gdy druga strona nie ustąpi — druga linia obrony w negocjacji]
**Klauzula z bazy:** `references/baza-klauzul/XX-yyy.md`

#### 2. [...]

### 🟠 RYZYKA WYSOKIE

#### 1. [...]

### 🟡 RYZYKA ŚREDNIE

#### 1. [...]

### 🟢 RYZYKA NISKIE

#### 1. [...]

### ✓ Obszary bez zastrzeżeń

[wymień obszary z Kroku 1 sprawdzone i czyste — np. „Reprezentacja stron · RODO · Spory: brak zastrzeżeń". Obszary n/d pomiń.]

---

## OCENA BEZPIECZEŃSTWA: XX/100

[2-3 zdania uzasadnienia — co wpłynęło na ocenę]

**Werdykt:** [DO PODPISANIA z drobnymi poprawkami / DO NEGOCJACJI / DO GRUNTOWNEJ PRZERÓBKI / NIE PODPISYWAĆ]

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

## Reguły werdyktu (nagłówek raportu)

Werdykt na górze raportu wynika z **twardych reguł**, nie z wyczucia. Sprawdzaj w kolejności — pierwszy pasujący kolor wygrywa:

- **🟥 CZERWONY** — jeśli **którekolwiek** z: co najmniej jedno ryzyko 🔴 KRYTYCZNE · naruszenie normy bezwzględnie obowiązującej · trafienie w RED bezwzględne z `practice-profile.md`. → *„Nie podpisywać w obecnej formie — wymaga negocjacji punktów krytycznych przed podpisem."*
- **🟨 ŻÓŁTY** — jeśli brak 🔴, ale występuje **co najmniej jedno** 🟠 WYSOKIE (lub kilka 🟡). → *„Do negocjacji — wskazane poprawki przed podpisem, bez dealbreakerów."*
- **🟩 ZIELONY** — jeśli **wszystkie** poniższe: zero 🔴, zero 🟠, brak trafień RED z profilu. → *„Do podpisania z drobnymi poprawkami redakcyjnymi."*

Werdykt (kolor) i ocena XX/100 muszą być spójne — 🟥 nie może współistnieć z oceną 85/100. Przy rozbieżności popraw ocenę, nie werdykt (reguły werdyktu są nadrzędne).

Uwaga: werdykt 🟩🟨🟥 (3 kolory, oś decyzji „co robić") to **inna oś** niż flagi ryzyka 🔴🟠🟡🟢 (4 poziomy, oś „jak groźne pojedyncze ryzyko"). Nie mylić.

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

---

**STOP. Zaprezentuj raport i zapytaj:** „Chcesz żebym wygenerował poprawione klauzule dla któregoś ze wskazanych ryzyk?"
