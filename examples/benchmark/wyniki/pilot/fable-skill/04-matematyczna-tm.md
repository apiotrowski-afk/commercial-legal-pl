# AUDYT RYZYK — Umowa ramowa T&M QUANTA DEV / MERIDIAN FINANCE (benchmark, tryb express)

> **WERDYKT: 🟥 CZERWONY** — Nie podpisywać w obecnej formie: cap odpowiedzialności jest iluzoryczny (kary bez sufitów poza capem + indemnity bez limitu), umowa nie przenosi praw do tworzonego oprogramowania, a zakaz konkurencji bez ekwiwalentu z karą 300.000 zł jest graniczny.

Audyt neutralny — wady flagowane niezależnie od tego, którą stronę krzywdzą. Tryb express: bez STOPów, bez pamięci MCP. Brak MCP `legal-cite` → wszystkie cytaty przepisów `[NIEZWERYFIKOWANE]`.

### 🧮 Rachunek ekspozycji

Założenie jawne: wynagrodzenie miesięczne liczone z szacunku z § 1 ust. 2 (umowa nie definiuje „wynagrodzenia miesięcznego" inaczej): 220 zł × 2 Specjalistów × 160 h = **70.400 zł netto/mies.**

| Pozycja | Wg umowy | Rachunek | Wynik |
|---|---|---|---|
| Wartość umowy (24 mies.) | T&M, szacunek § 1 ust. 2 | 70.400 × 24 | ≈ 1.689.600 zł netto |
| Cap nominalny | „12-miesięczne wynagrodzenie" (§ 3 ust. 1) | 12 × 70.400 | ≈ 844.800 zł |
| Kara za zwłokę w Przyroście | 0,5% wynagrodzenia miesięcznego/dzień (§ 2 ust. 1), **bez sufitu** | 352 zł/dzień; np. 90 dni zwłoki = 31.680 zł; horyzont nieograniczony | ekspozycja otwarta `[BRAK DANYCH — sufit]` |
| Kara za jakość kodu | 5.000 zł „za każdy przypadek" (§ 2 ust. 2), **bez sufitu** | np. 2 przypadki/mies. × 24 mies. = 240.000 zł (ilustracja) | ekspozycja otwarta `[BRAK DANYCH — sufit]` |
| Kara za zakaz konkurencji | 300.000 zł „za każdy przypadek" (§ 2 ust. 3), **bez sufitu** | 3 przypadki = 900.000 zł | ekspozycja otwarta |
| Kary a cap | „Kary umowne podlegają sumowaniu i nie są wliczane do limitu odpowiedzialności z § 3" (§ 2 ust. 4) + odszkodowanie przewyższające kary | cap + kary + odszkodowanie | kary w całości **obok capu** |
| Indemnity IP | „zwolni Zamawiającego z wszelkiej odpowiedzialności" + „wszelkie… koszty" (§ 3 ust. 2), **bez limitu** | — | bez granicy |
| **Efektywna ekspozycja Wykonawcy** | — | 844.800 (cap) + kary bez sufitów + indemnity bez limitu | **nieograniczona — cap iluzoryczny** |
| Asymetria | wszystkie kary i indemnity na Wykonawcę | Wykonawca: bez granicy vs Zamawiający: 0 zł kar, brak capu na zasadach ogólnych | kary: ∞ vs 0 |
| Auto-renewal | przedłużenie o 12 mies., sprzeciw ≥ 90 dni przed końcem (§ 4 ust. 1), stawka +8% (§ 4 ust. 2) | ostatni dzień skutecznego oświadczenia = dzień 640. z 730 dni okresu (daty kalendarzowej brak — `[BRAK DANYCH]` daty zawarcia); wartość przegapienia: 70.400 × 1,08 × 12 | **≈ 912.384 zł** związania za przegapione okno; stawka 220 → 237,60 → 256,61 zł/h w kolejnych okresach |
| Zakaz konkurencji | 24 mies. po zakończeniu, bez wynagrodzenia (§ 5) | przy przedłużeniach: 24/36/48 mies. umowy + 24 mies. zakazu | do 6 lat związania bez ekwiwalentu |
| Wypowiedzenie | brak jakiejkolwiek klauzuli | — | `[BRAK DANYCH]` — związanie 24 mies. bez umownego wyjścia |

Wniosek z rachunku: nominalny cap 844.800 zł to etykieta — § 2 ust. 4 wyprowadza poza cap trzy kary bez sufitów i odszkodowanie uzupełniające, a § 3 ust. 2 dokłada indemnity bez granicy. Efektywna ekspozycja Wykonawcy jest nieograniczona, przy zerowej ekspozycji karnej Zamawiającego. To kalibruje flagę na 🔴 mimo „ładnej" klauzuli limitu (R12).

### Bramka ius cogens (R10)

Skan `normy-bezwzglednie.md`: kary zabezpieczają zobowiązania niepieniężne (art. 483 § 1 KC `[NIEZWERYFIKOWANE]` — formalnie OK); brak wyłączenia miarkowania; brak manipulacji przedawnieniem. **Klauzule graniczne** (test pięciopunktowy z efektem kumulatywnym): zakaz konkurencji 24 mies. bez ekwiwalentu z karą 300.000 zł oraz architektura § 2 ust. 4 + § 3 ust. 2 — ocena w 🔴 nr 1 i 🟠 nr 2. Trigger mikroprzedsiębiorcy (art. 385⁵ KC `[NIEZWERYFIKOWANE]`): nieaktywny — obie strony to spółki. Brak trafień wprost w katalog nieważności; werdykt 🟥 wynika z ryzyk 🔴 poniżej.

### 🔴 RYZYKA KRYTYCZNE

#### 1. Cap iluzoryczny — kary bez sufitów poza capem + odszkodowanie uzupełniające — § 2 ust. 4 w zw. z § 2 ust. 1–3 i § 3 ust. 1 *(krzywdzi: QUANTA DEV)*
**Opis:** trzy kary „za każdy przypadek/dzień" bez żadnego sufitu, wprost wyjęte z limitu („nie są wliczane do limitu odpowiedzialności z § 3"), z dopuszczonym odszkodowaniem przewyższającym. Rachunek wyżej: ekspozycja efektywna nieograniczona przy capie nominalnym 844.800 zł.
**Skutek:** odpowiedzialność Wykonawcy realnie bez granic — dokładnie ten stan, któremu cap miał zapobiec; przy karach wielokrotnie przewyższających szkodę — spór o miarkowanie (art. 484 § 2 KC `[NIEZWERYFIKOWANE]`), czyli lata procesu zamiast przewidywalności dla obu stron.
**Rekomendacja (preferowana):** sufit łączny kar (np. 20–30% wynagrodzenia rocznego), kary wliczane do capu, odszkodowanie uzupełniające do wysokości capu.
**Fallback (minimum akceptowalne):** sufity per podstawa kary (zwłoka ≤ 15% wynagrodzenia miesięcznego/sprint, jakość ≤ X/rok) + łączny limit odpowiedzialności z karami 150% capu.
**Klauzula z bazy:** `references/baza-klauzul/10-kary-umowne.md`, `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Brak przeniesienia praw autorskich do tworzonego oprogramowania — cała umowa *(krzywdzi: MERIDIAN FINANCE)*
**Opis:** umowa ramowa „rozwoju oprogramowania" nie zawiera żadnej klauzuli IP — ani przeniesienia praw, ani licencji, ani pól eksploatacji (art. 41 ust. 2 PrAut `[NIEZWERYFIKOWANE]`). Paradoks: § 3 ust. 2 każe Wykonawcy zwalniać Zamawiającego z roszczeń IP osób trzecich, ale sam Zamawiający nie nabywa praw do kodu, za który płaci ~70.400 zł miesięcznie.
**Skutek:** prawa majątkowe zostają przy Wykonawcy; Zamawiający (instytucja finansowa!) korzysta z systemu bez tytułu — ryzyko blokady rozwoju, audytów regulacyjnych i sporu przy wyjściu.
**Rekomendacja:** klauzula przeniesienia praw z katalogiem pól eksploatacji, prawami zależnymi i wydawaniem kodu per sprint.
**Fallback:** licencja wyłączna, bezterminowa, z prawem sublicencji i depozytem kodu.
**Klauzula z bazy:** `references/baza-klauzul/08-prawa-autorskie-ip.md`

### 🟠 RYZYKA WYSOKIE

#### 1. Indemnifikacja IP bez limitu i bez procedury — § 3 ust. 2 *(krzywdzi: QUANTA DEV)*
**Opis:** otwarte hold-harmless („z wszelkiej odpowiedzialności…, wszelkie związane z tym koszty") — bez sufitu, bez obowiązku notyfikacji roszczenia, bez prawa Wykonawcy do prowadzenia obrony, bez wyłączeń (np. modyfikacje dokonane przez Zamawiającego). Element rachunku ekspozycji nieograniczonej.
**Rekomendacja:** limit indemnity (np. 200% capu), procedura defense & control, wyłączenia. **Fallback:** sam limit kwotowy + notyfikacja.
**Klauzula z bazy:** `references/baza-klauzul/11-odpowiedzialnosc.md`

#### 2. Zakaz konkurencji 24 mies. po umowie bez ekwiwalentu, z karą 300.000 zł — § 5 w zw. z § 2 ust. 3 *(krzywdzi: QUANTA DEV)*
**Opis:** zakaz obejmuje „podmioty prowadzące działalność konkurencyjną wobec Zamawiającego" — bez definicji konkurencji, bez terytorium, bez katalogu podmiotów; Zamawiający to instytucja finansowa, więc dla software house'u to potencjalnie cały sektor finansowy przez 2 lata po umowie. „Zakaz nie jest związany z dodatkowym wynagrodzeniem." Test pięciopunktowy: treść obiektywna — eliminacja z rynku; asymetria bez ekwiwalentu; odbiega od praktyki (w B2B zakaz poumowny zwykle płatny lub wąski); efekt kumulatywny z karą 300.000 zł/przypadek bez sufitu — ryzyko uznania za sprzeczny z zasadami współżycia (art. 353¹, art. 58 § 2 KC `[NIEZWERYFIKOWANE]`).
**Skutek:** dla Wykonawcy — ekspozycja 300.000 zł × n i zamrożenie działalności; dla Zamawiającego — ryzyko, że klauzula w sporze upadnie w całości i nie ochroni niczego.
**Rekomendacja:** zawęzić (katalog konkurentów lub zakres projektowy), skrócić do 6–12 mies., dodać ekwiwalent; sufit kary. **Fallback:** zakaz ograniczony do zespołu pracującego dla Zamawiającego i wiedzy projektowej (de facto non-solicitation + poufność).
**Klauzula z bazy:** `references/baza-klauzul/13-non-solicitation.md`

#### 3. Auto-renewal z podwyżką 8% i oknem 90 dni — § 4 *(krzywdzi: obie strony, głównie MERIDIAN)*
**Opis:** przegapienie okna sprzeciwu (ostatni dzień = 90 dni przed końcem okresu; daty kalendarzowej brak — umowa bez daty zawarcia) wiąże na kolejne 12 mies. za ≈ 912.384 zł, każdorazowo drożej o 8% (mechanizm bez powiązania z jakimkolwiek wskaźnikiem i bez symetrii — indeksacja tylko w górę).
**Rekomendacja:** przedłużenie za zgodnym oświadczeniem (opt-in) albo okno 30 dni z obowiązkiem przypomnienia; waloryzacja wskaźnikiem (np. średnioroczny CPI), obustronna. **Fallback:** zachować opt-out, skrócić okno do 30 dni i ograniczyć podwyżkę do min(8%, CPI).
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md`

#### 4. Brak klauzuli wypowiedzenia i procedury exit — cała umowa *(obie strony)*
**Opis:** 24 miesiące związania bez umownego prawa wypowiedzenia, bez exit planu (przekazanie kodu, wiedzy, WIP, okres przejściowy). Przy umowie o świadczenie usług wchodzi reżim ustawowy (art. 750 w zw. z art. 746 KC `[NIEZWERYFIKOWANE]`) — wypowiedzenie możliwe, ale z ryzykiem odpowiedzialności odszkodowawczej i chaosu na wyjściu.
**Rekomendacja:** wypowiedzenie symetryczne (np. 3 mies.), wypowiedzenie natychmiastowe z ważnych przyczyn (katalog), exit plan z obowiązkiem transferu wiedzy. **Fallback:** minimum wypowiedzenie z ważnych przyczyn + zwrot artefaktów.
**Klauzula z bazy:** `references/baza-klauzul/12-wypowiedzenie-exit.md`, `references/baza-klauzul/18-zwrot-materialow.md`

### 🟡 RYZYKA ŚREDNIE

#### 1. Definicje-widma i załączniki — § 1–2 *(obie strony)*
„Przyrost", „Specjalista", „harmonogram sprintu" — pojęcia kluczowe dla kar, bez definicji (Złota Reguła 1); kara jakościowa odsyła do „progu z Załącznika nr 2", którego istnienia i treści nie potwierdzono w dostarczonym tekście, a Załącznika nr 1 w ogóle brak (ryzyko osieroconych załączników). Kara oparta o niezdefiniowany próg = spór gwarantowany.

#### 2. Brak poufności *(obie strony)*
Rozwój oprogramowania dla instytucji finansowej bez żadnej klauzuli poufności — dane, architektura, luki bezpieczeństwa bez ochrony kontraktowej. → `references/baza-klauzul/09-poufnosc.md`.

#### 3. Brak RODO / powierzenia *(obie strony)*
Zespół Wykonawcy będzie niemal na pewno miał dostęp do środowisk z danymi osobowymi klientów instytucji finansowej — brak DPA art. 28 RODO `[NIEZWERYFIKOWANE]`. → `references/baza-klauzul/14-rodo.md`.

#### 4. Braki formalne komparycji *(obie strony)*
Brak daty i miejsca zawarcia (przez co nie da się policzyć dat granicznych auto-renewalu!), siedzib, KRS/NIP, reprezentacji (Złota Reguła 8).

### 🟢 RYZYKA NISKIE

#### 1. „Sąd właściwy dla siedziby Zamawiającego" — § 6 ust. 1 *(krzywdzi: QUANTA DEV)*
Standardowa przewaga forum; drobna, ale spójna z resztą jednostronnej architektury. Sugestia: sąd pozwanego.

### ✓ Obszary bez zastrzeżeń (bramka kompletności R9 — 9 obszarów)

- **Odpowiedzialność i kary** — 🔴 nr 1, 🟠 nr 1–2
- **Prawa autorskie** — 🔴 nr 2
- **Definicje i logika** — 🟡 nr 1
- **Reprezentacja** — 🟡 nr 4
- **Wypowiedzenie i exit** — 🟠 nr 3–4
- **RODO** — 🟡 nr 3
- **Tytuł prawny i przekwalifikowanie** — ✓ sprawdzone, brak zastrzeżeń (B2B między spółkami; model T&M z „Specjalistami" bez zapisów o podporządkowaniu — ryzyka KP nie widać w dostarczonym tekście)
- **Poufność** — 🟡 nr 2
- **Spory** — 🟢 nr 1 (prawo polskie — bez zastrzeżeń)

---

## OCENA BEZPIECZEŃSTWA: 34/100

Dwa ryzyka krytyczne: cap istniejący tylko na papierze (kary bez sufitów i indemnity bez limitu obok capu) oraz brak jakiegokolwiek nabycia praw do oprogramowania, które jest przedmiotem umowy. Do tego graniczny zakaz konkurencji bez ekwiwalentu, auto-renewal z jednostronną indeksacją i brak wyjścia z 24-miesięcznego związania. Umowa krzywdzi obie strony: Wykonawcę ekspozycją bez granic, Zamawiającego brakiem IP.

**Werdykt:** DO GRUNTOWNEJ PRZERÓBKI

### Klauzule z bazy KTZR do uzupełnienia

🔴 RYZYKO 1 → `references/baza-klauzul/10-kary-umowne.md` (sufity) + `references/baza-klauzul/11-odpowiedzialnosc.md` (cap obejmujący kary)
🔴 RYZYKO 2 → `references/baza-klauzul/08-prawa-autorskie-ip.md` (przeniesienie z polami eksploatacji per sprint)
🟠 RYZYKO 2 → `references/baza-klauzul/13-non-solicitation.md` (zamiast szerokiego zakazu konkurencji)
🟠 RYZYKO 3–4 → `references/baza-klauzul/12-wypowiedzenie-exit.md`

---

*Analiza ma charakter pomocniczy i nie zastępuje oceny radcy prawnego prowadzącego sprawę.*
