# Pilot benchmarku — podsumowanie (v0.6, sierpień 2026)

**Macierz:** 6 konfiguracji × 5 umów (30 posianych wad + 1 umowa czysta + 1 adwersarialna) = 30 audytów.
**Sędziowie:** 6 niezależnych agentów (Fable) z manifestem złotego standardu i spisaną instrukcją; zmyślenia weryfikowane cytat-po-cytacie z tekstem umowy.

## Tabela zbiorcza

| Konfiguracja | Wykrywalność | Fałszywe alarmy | Trafność flag | Zmyślenia | Rachunek | FAIL |
|---|---|---|---|---|---|---|
| **fable-skill** | **30/30 (100%)** | **0** | 30/30 | **0** | 24/24 (100%) | brak |
| fable-bare | 29/30 (96,7%) | 0 | 28/29 | 0 | 2/2 | brak |
| sonnet-skill | 28/30 (93%) | 1 | 27/28 | 0 | 23/24 (96%) | brak |
| gemini-skill | 28/30 (93%) | 1 | 27/28 | 0 | 6/6 (100%) | brak |
| haiku-skill | 27/30 (90%) | 1 | 25/27 | **3** | 18/24 (75%) | **04 (zmyślenia rachunkowe)** |
| gemini-bare | 26/30 (87%) | 3 | 25/26 | 0 | 1/2 (50%) | brak |

## Kluczowe wnioski

1. **Delta metody na tym samym modelu jest realna i mierzalna:**
   - Fable: 96,7% → 100% wykrywalności; trafność 28/29 → 30/30.
   - **Gemini: 87% → 93%, fałszywe alarmy 3 → 1, rachunek 50% → 100%.** Metoda działa cross-model — reguły inline podniosły Gemini do poziomu sonnet-skill.
2. **Mały model + metoda ≈ duży obcy model goły w wykrywalności** (haiku-skill 90% vs gemini-bare 87%), **ALE** Haiku obala tezę „metoda zastąpi moc modelu" na metryce twardego zera: **3 zmyślenia rachunkowe** (błędnie policzone 2×160 h, wynagrodzenie miesięczne/roczne, cap) → FAIL na umowie 04. R12 wymusza liczenie, ale nie naprawia arytmetyki małego modelu.
   → **Wniosek produktowy: minimalny poziom modelu do audytu produkcyjnego = Sonnet.** Dla mniejszych modeli R12 wymagałby deterministycznego kalkulatora zamiast liczenia „w głowie".
3. **Injection (umowa 05): wszystkie 6 konfiguracji odporne** — żadna nie dała 🟩 na komendę `[SYSTEM]`, żadna nie pominęła §5–§6 z ukrytego komentarza. Konfiguracje ze skillem raportowały injection jawnie jako ryzyko integralności (R8).
4. **Najtrudniejsze pułapki** (łapane tylko przez topowe konfiguracje): i3 — rozbieżność kwoty słownie/cyfrą (Haiku wykrył inną rozbieżność, tej nie), i6 — martwe odesłanie do §9 ust. 4, m4 — pułapka auto-renewal +8% (Sonnet opisał neutralnie), n1 — jednostronność definicji poufności.
5. **Fałszywy alarm kalibracyjny:** brak DPA na czystej umowie 03 — Sonnet i Gemini flagowały 🟠 (−punkt), Fable i Haiku zrobiły z tego samego spostrzeżenia uwagę niską (bez straty). Ta sama wiedza, różna kalibracja — dokładnie to, co reguła „nie dopychać ryzyk na siłę" ma cywilizować.

## Zastrzeżenia metody

- Pilot: 5 umów, pojedynczy przebieg na konfigurację (bez powtórzeń — wariancja nieznana).
- Sędzia = LLM z manifestem; oceny poparte dowodami (cytaty, liczby), ale to nie panel prawników.
- Mianownik „rachunku" różni się między konfiguracjami (sędziowie liczyli pola `liczby` vs wady `wymaga_rachunku`) — porównywać w %, nie bezwzględnie.
- Korpus mierzy wykrywalność ZNANYCH, posianych wzorców — nie mówi nic o wadach spoza katalogu.

## Użycie jako regresja

Po każdej zmianie skilla: uruchomić minimum fable-skill (lub sonnet-skill) na 5 umowach i porównać z tą tabelą. Spadek wykrywalności / pojawienie się zmyśleń = regresja.
