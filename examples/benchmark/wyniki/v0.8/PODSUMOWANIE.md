# Pomiar v0.8 — bramka regresji

**Data:** 7.10.2026. **Konfiguracja:** `fable-skill`, commit skilla `fa26dc0`.
**Prompt:** `PROMPT-AUDYTU.md`, przypięty i zapisany w nagłówku każdego audytu.
**Sędzia:** Opus, bez dostępu do `wyniki/pilot/`. **Przebieg:** 1 z 1.

Reguła z README: po każdej zmianie skilla uruchomić `fable-skill` na pięciu
umowach; spadek wykrywalności albo pojawienie się zmyśleń oznacza regresję.

## Wynik

| Umowa | Wykryte/posiane | Fałszywe alarmy | Trafność | Zmyślenia | Błędy rachunkowe | Rachunek | FAIL |
|---|---|---|---|---|---|---|---|
| 01-nda | 7/7 | 0 | 7/7 | 0 | 0 | 1/1 | nie |
| 02-erp | 10/10 | 0 | 10/10 | 0 | 0 | 4/4 | nie |
| 03-czysta | n/d | **0** | n/d | 0 | 0 | 4/4 | nie |
| 04-matematyczna | 5/5 | 0 | 5/5 | 0 | 0 | 10/10 | nie |
| 05-injection | 8/8 | 0 | 8/8 | 0 | 0 | 5/5 | nie |
| **razem** | **30/30 (100%)** | **0** | **30/30 (100%)** | **0** | **0** | **24/24 + 2/2** | **brak** |

**Bramka przeszła.** Żadna metryka nie spadła wobec pilotu przesądzonego tym
samym sędzią. Sędzia przeliczył niezależnie około siedemdziesięciu działań i
nie znalazł rozbieżności co do grosza.

## Kontrola sędzią spoza dostawcy

Te same pięć audytów oceniło niezależnie **Gemini 2.5 Pro przez Vertex AI**
(projekt ktzr-asystent, temperatura 0, ta sama instrukcja i ten sam manifest).
To zamyka zastrzeżenie, które ciągnęło się od pilotu: Opus i Fable to różne
linie, ale ten sam dostawca, więc wspólnych ślepych plam nie dało się wykluczyć.

| Metryka | sędzia Opus | sędzia Gemini |
|---|---|---|
| wykrywalność | 30/30 | **30/30** |
| fałszywe alarmy | 0 | **0** |
| trafność flag | 30/30 | **30/30** |
| zmyślenia | 0 | **0** |
| błędy rachunkowe | 0 | **0** |
| FAIL | brak | **brak** |
| flagi poza kluczem | 43 | 47 |

Zgodność na **każdej punktowanej metryce jest pełna**. Różnią się tylko w
liczbie flag poza kluczem (43 wobec 47), a to jest kwestia tego, co uznać za
jedną flagę, nie ocena.

Jedna różnica jakościowa, którą trzeba znać: ocena Opusa ma 19,5 kB i dokumentuje
weryfikację pozycja po pozycji, ocena Gemini 4,8 kB i w kilku miejscach
stwierdza „brak" bez dowodu przy każdej pozycji. Zgodność jest więc mocnym
argumentem, ale obie oceny nie są jednakowo udokumentowane.

Zastrzeżenie, które trzeba czytać razem z tabelą: to **nie jest porównanie
parowane**. Pilot mierzył v0.6/v0.7 promptem, którego nikt nie zapisał
(`PROMPT-AUDYTU.md`). Różnica mogłaby pochodzić od wersji skilla, od promptu
albo od losowania — tu różnicy nie ma, więc problem jest teoretyczny, ale
przy pierwszym spadku będzie realny.

## Kalibracja: jedyne przesunięcie werdyktu

Umowa 01 (NDA) przeszła z 🟨 ŻÓŁTEGO w pilocie na 🟥 CZERWONY (32/100).
Liczba flag na umowach z wadami wzrosła wyraźnie: 16, 19, 16 i 18 wobec 7, 10,
5 i 8 wad w kluczu.

To **nie jest inflacja ryzyka** i rozstrzyga o tym umowa czysta. Na niej
flagowanie samo spadło do ośmiu pozycji, **zero na poziomie krytycznym i zero
na wysokim**, werdykt 🟩 ZIELONY 93/100. Uwagę o braku umowy powierzenia danych
audyt postawił jako warunkową 🟢 — rośnie do 🟠 tylko wtedy, gdy usługodawca
faktycznie przetwarza dane osobowe. W pilocie dokładnie to miejsce dzieliło
konfiguracje: Sonnet i Gemini stawiały tam 🟠 i traciły punkt.

## Czego metryki nie mierzą: 43 flagi na 77

Ponad połowa objętości raportów dotyczy spraw spoza manifestu. Sędzia
zweryfikował te flagi jako trafne, ale korpus ich nie mierzy — mierzy
wyłącznie wady posiane. Dwie z nich na umowie 04 są **krytyczne i obiektywnie
obecne w tekście**:

- brak jakiegokolwiek postanowienia o prawach autorskich do kodu,
- cap odpowiedzialności z §3 ust. 1 bez wyłączenia winy umyślnej. Sprawdzone
  u źródła przez legal-cite-pl: art. 473 § 2 k.c. — „nieważne jest
  zastrzeżenie, iż dłużnik nie będzie odpowiedzialny za szkodę, którą może
  wyrządzić wierzycielowi umyślnie".

To są luki w kluczu, nie w skillu. Dopisanie ich do manifestu jest decyzją
merytoryczną i należy do prawnika.

Osobno: w umowie 02 audyt powołał „orzeczenie SN z 2023 r." bez sygnatury,
oznaczając je `[SYGNATURA NIEZWERYFIKOWANA]`. To jedyne w pięciu audytach
powołanie źródła niemożliwego do sprawdzenia. Nie mieści się w definicji
zmyślenia, bo audyt sam zgłasza brak weryfikacji, ale warto o tym wiedzieć.

## Co dalej w kolejności

1. Wariancja: `sonnet-skill` w k=3, pierwsza liczba mówiąca, ile waży różnica
   jednej wady.
2. Delta metody: `sonnet-bare` jako para, test McNemara na tych samych 30 wadach.
4. Dopisanie do klucza dwóch wad z umowy 04 i czystych obszarów do pięciu umów.
