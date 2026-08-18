# Podstawy przetwarzania danych osobowych (art. 6 / 7 / 9 RODO)

**Źródło:** opracowanie KTZR na podstawie RODO, Kodeksu pracy oraz doktryny i decyzji UODO (wsad z LEX).
**Powiązania:** `baza-klauzul/14-rodo.md`, `references/checklist-dpa-art28.md`, `baza-wiedzy/08-rodo-powierzenie-konstrukcja.md`.
**Status:** zatwierdzone do bazy wiedzy KTZR.

## TL;DR — co Claude musi wiedzieć

1. Każde przetwarzanie musi mieć **co najmniej jedną podstawę z art. 6 ust. 1** (a dla danych szczególnych — dodatkowo przesłankę z art. 9 ust. 2). Brak podstawy = ciężkie naruszenie (art. 83 ust. 5 lit. a, do 20 mln € / 4% obrotu).
2. Przy umowach IT/HR najczęstsze podstawy: **wykonanie umowy** (lit. b), **obowiązek prawny** (lit. c), **prawnie uzasadniony interes** (lit. f). Zgoda (lit. a) — ostrożnie, zwłaszcza w relacji pracowniczej.
3. **Uzasadniony interes (lit. f) wymaga udokumentowanego testu trójstopniowego** — nie wystarcza samo powołanie się na przepis.

> **Dyscyplina cytatów (R1):** artykuły i sygnatury (UODO/TSUE) to referencja z LEX; w outputcie weryfikuj przez `verify_article()` lub oznacz `[NIEZWERYFIKOWANE]` / `[SYGNATURA NIEZWERYFIKOWANA]`.

## Test prawnie uzasadnionego interesu (art. 6 ust. 1 lit. f)

Trójstopniowy — wszystkie kroki muszą wypaść pozytywnie:

1. **Identyfikacja interesu** — konkretny, rzeczywisty, zgodny z prawem cel administratora lub strony trzeciej (nie hipotetyczny).
2. **Niezbędność** — czy celu nie da się osiągnąć w sposób mniej ingerujący w prywatność (minimalizacja).
3. **Test równowagi** — czy interesy lub podstawowe prawa i wolności osoby **nie przeważają** nad interesem administratora. Uwzględnij: rodzaj danych, skalę i kontekst, wpływ na osobę, środki zabezpieczające i **„rozsądne oczekiwania"** osoby w danej relacji. Szczególna ostrożność, gdy dane dotyczą dzieci.

**Typowe zastosowania a lit. f:**
- **Bezpieczeństwo IT** (ochrona systemów, wykrywanie nadużyć) — zwykle mieści się jako uzasadniony interes, przy udokumentowanym teście.
- **Marketing bezpośredni** — motyw 47 RODO wskazuje go jako możliwy uzasadniony interes; **bezwzględne prawo sprzeciwu** (art. 21 ust. 2–3). **Zastrzeżenie sektorowe:** podstawa z RODO **nie wystarcza** do użycia określonych kanałów — art. 398 Prawa komunikacji elektronicznej wymaga co do zasady **uprzedniej zgody** na używanie automatycznych systemów wywołujących / telekomunikacyjnych urządzeń końcowych do przesyłania informacji handlowej (marketing e-mail/SMS/telefon). Sprawdź oba reżimy.
- **Monitoring** (wizyjny, pracowniczy, użytkowników) — możliwy jako uzasadniony interes, ale z naciskiem na oczekiwania osób i przepisy szczególne (monitoring pracowniczy — art. 22² k.p.).

**Zasada rozliczalności:** administrator powinien przeprowadzić test **przed** rozpoczęciem przetwarzania i **być w stanie wykazać** jego wynik (art. 5 ust. 2) — w praktyce oznacza to utrwalenie analizy w dokumentacji (art. 5 ust. 2 nie wymaga literalnie dokumentu „LIA", ale bez utrwalenia trudno wykazać zgodność). Dla danych szczególnych lit. f **nie wystarcza** — potrzebna dodatkowo przesłanka z art. 9 ust. 2. Odrębny reżim mają dane o wyrokach skazujących (art. 10 RODO).

## Zmiana podstawy przetwarzania — stanowisko EROD jest restrykcyjne

Czy można zmienić podstawę już rozpoczętego przetwarzania (np. ze zgody na uzasadniony interes)? **Co do tego samego celu — nie.**

**Stanowisko EROD** (wytyczne 05/2020 ws. zgody; zasady rzetelności i przejrzystości z art. 5 ust. 1 lit. a, motyw 42):
- podstawę należy **wybrać przed rozpoczęciem** przetwarzania;
- administrator **nie może** po wycofaniu lub zakwestionowaniu zgody „przełączyć się" retrospektywnie na uzasadniony interes dla **tego samego celu** — ani użyć innej podstawy jako awaryjnego uzasadnienia wcześniejszego przetwarzania;
- **dopuszczalne** jest natomiast równoległe przetwarzanie dla **innego, samodzielnego celu** na innej, uprzednio ustalonej podstawie (np. zachowanie części danych dla wykonania obowiązku prawnego lub obrony roszczeń), z zachowaniem obowiązków informacyjnych i zasad art. 5.

W doktrynie spotyka się zastrzeżenia wobec absolutnego charakteru zakazu, ale **operacyjne stanowisko organów jest restrykcyjne** i tak należy je prezentować.

**Jak stosować:** klauzula umożliwiająca „zmianę podstawy" po fakcie dla tego samego celu → **🔴** (naruszenie zasad rzetelności/przejrzystości). Odrębny cel z odrębną, uprzednio określoną podstawą → OK, sprawdź obowiązek informacyjny.

## Zgoda (art. 7) — pracownicy i B2B

**Relacja pracownicza — nierównowaga stron:**
- Zgoda pracownika / kandydata może być podstawą przetwarzania **innych** danych niż z art. 22¹ k.p. (art. 22¹ᵃ k.p.), z wyjątkiem danych o wyrokach skazujących (art. 10 RODO).
- **Brak zgody lub jej cofnięcie nie mogą być podstawą niekorzystnego traktowania** (odmowa zatrudnienia, wypowiedzenie) — art. 22¹ᵃ k.p.
- Dane szczególne (art. 9 ust. 1) na podstawie zgody kandydata/pracownika — **tylko gdy przekazanie następuje z jego inicjatywy** (art. 22¹ᵇ k.p.). Dane **biometryczne** bez zgody — wyłącznie gdy niezbędne do kontroli dostępu do **szczególnie ważnych informacji**, których ujawnienie mogłoby narazić pracodawcę na szkodę, lub do **pomieszczeń wymagających szczególnej ochrony**; ogólna wygoda / usprawnienie ewidencji **nie wystarcza**.
- Wniosek: ze względu na nierównowagę stron oparcie przetwarzania na zgodzie w stosunku pracy ma charakter **wyjątkowy** — zgoda musi spełniać też wymogi RODO (art. 7); weryfikuj dobrowolność, preferuj inne podstawy tam, gdzie to możliwe.

**B2B:** brak szczególnej regulacji krajowej — stosuj standard RODO: zgoda dobrowolna, konkretna, świadoma, jednoznaczna, z prawem cofnięcia bez negatywnych konsekwencji (art. 7).

## Dane szczególnych kategorii (art. 9) w umowach IT/HR

Przetwarzanie danych z art. 9 ust. 1 wymaga **dodatkowej przesłanki z art. 9 ust. 2**. Typowe w IT/HR:
- **zgoda** (lit. a) — przy zachowaniu warunków art. 7 i regulacji krajowych (art. 22¹ᵇ k.p.);
- **obowiązki z zakresu prawa pracy i zabezpieczenia społecznego** (lit. b) — w zakresie wynikającym z ustaw (np. ustawa o rehabilitacji — dane o stanie zdrowia pracowników, z zabezpieczeniami i ograniczeniem czasu przechowywania);
- **dane biometryczne pracownika** — kontrola dostępu do szczególnie chronionych pomieszczeń/informacji (art. 22¹ᵇ k.p.).

## Jak używać w audycie/generowaniu

1. Dla każdego procesu opisanego w umowie ustal **podstawę z art. 6** (i art. 9, jeśli dane szczególne). Brak podstawy → 🔴.
2. Podstawa = uzasadniony interes → sprawdź, czy jest **udokumentowany test trójstopniowy**; brak → 🟠.
3. Zgoda w stosunku pracy → zweryfikuj dobrowolność i zakres (art. 22¹ᵃ/ᵇ k.p.); zgoda jako jedyna podstawa relacji zależnej → 🟠.
4. Klauzula umożliwiająca retroaktywną zmianę podstawy dla tego samego celu → 🔴 (stanowisko EROD restrykcyjne); odrębny cel z uprzednio określoną podstawą → sprawdź obowiązek informacyjny.
5. Marketing e-mail/SMS/telefon → obok podstawy z RODO sprawdź zgodę z art. 398 PKE.
