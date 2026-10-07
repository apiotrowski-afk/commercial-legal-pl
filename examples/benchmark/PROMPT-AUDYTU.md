# Prompt audytu — warunki przebiegu

README obiecuje „ta sama umowa, ten sam prompt, różne konfiguracje", ale
**prompt z pilotu nie został nigdzie zapisany**. Da się go częściowo odtworzyć
tylko z nagłówków audytów Fable'a, które same opisują swoje warunki; audyty
Sonneta, Haiku i Gemini tego nie robią. Oznacza to, że równości promptu w
pilocie nie można dziś udowodnić z artefaktów, a nowy pomiar bez zapisanego
promptu powtórzyłby ten sam błąd: różnica wyniku byłaby nieodróżnialna od
różnicy polecenia.

Ten plik zamyka lukę od v0.8 w górę. **Nie jest rekonstrukcją promptu
pilotowego** — jest ustaleniem warunków na przyszłość.

## Warunki odczytane z audytów pilotowych

Nagłówki Fable'a deklarują:

- tryb **express** — bez STOP-ów, bez pamięci MCP,
- **brak MCP `legal-cite`**, więc wszystkie cytaty przepisów oznaczone
  `[NIEZWERYFIKOWANE]`,
- audyt **neutralny** — wada flagowana niezależnie od tego, którą stronę
  krzywdzi, przy każdej fladze wskazana strona dotknięta.

Pozostałe konfiguracje nie deklarują niczego, więc nie wiadomo, czy działały w
tych samych warunkach.

## Prompt obowiązujący od v0.8

Audytujący dostaje **wyłącznie treść umowy** — manifest jest dla niego tajny.
Polecenie dosłowne:

```
Przeprowadź audyt ryzyk tej umowy.

Warunki:
- tryb express: bez STOP-ów i bez pytań uzupełniających, jeden przebieg;
- audyt neutralny: flaguj wadę niezależnie od tego, którą stronę krzywdzi,
  i przy każdej fladze wskaż stronę dotkniętą;
- bez dostępu do MCP legal-cite — każde powołanie przepisu oznacz
  [NIEZWERYFIKOWANE];
- policz ekspozycję liczbowo tam, gdzie umowa podaje kwoty, stawki, terminy
  albo limity (sekcja „Rachunek ekspozycji");
- zakończ werdyktem: ZIELONY, ŻÓŁTY albo CZERWONY.

Nie szukaj informacji poza treścią umowy.
```

Konfiguracja **ze skillem** czyta `SKILL.md` i pliki z `references/` z
repozytorium w zadanym commicie. Konfiguracja **bez skilla** dostaje sam
powyższy prompt i treść umowy.

## Co zapisujemy przy każdym przebiegu

W nagłówku pliku audytu, żeby nie powtórzyć tej luki:

```
konfiguracja: <model>-<skill|bare>
commit skilla: <sha>        # dla konfiguracji ze skillem
przebieg: <k z K>
data: <YYYY-MM-DD>
prompt: PROMPT-AUDYTU.md § „Prompt obowiązujący od v0.8"
```

## Skutek dla porównań z pilotem

Pomiar v0.8 wolno zestawiać z tabelą pilotu **jako wskazanie, nie jako
porównanie parowane**. Pilot mierzył v0.6/v0.7 nieznanym promptem; różnica
może pochodzić od wersji skilla, od promptu albo od losowania. Pierwszym
pomiarem, który będzie porównywalny w pełni, jest v0.8 wobec kolejnej wersji.
