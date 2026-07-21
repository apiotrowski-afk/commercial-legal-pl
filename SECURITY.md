# Polityka bezpieczeństwa / Security Policy

> 🇵🇱 Wersja polska poniżej · 🇬🇧 English version below

---

## 🇵🇱 Zgłaszanie podatności

Dziękujemy za pomoc w utrzymaniu bezpieczeństwa tego projektu. Prosimy o **prywatne** zgłaszanie podatności — nie otwieraj publicznego zgłoszenia (Issue) ani Pull Requesta z opisem luki.

**Kanał zgłoszeń:** `a.piotrowski@ktzr.pl` (temat: `SECURITY: commercial-legal-pl`).

W zgłoszeniu opisz:
- na czym polega podatność i jak ją odtworzyć (kroki, wersja/commit),
- potencjalny wpływ,
- opcjonalnie: propozycję poprawki.

**Czego się spodziewać:**
- potwierdzenie odbioru w ciągu **7 dni**,
- wstępną ocenę i plan działania w ciągu **30 dni**,
- **coordinated disclosure** — publiczne ujawnienie dopiero po udostępnieniu poprawki.

Projekt jest utrzymywany bez programu nagród (bug bounty) — zgłoszenia przyjmujemy z wdzięcznością, ale nie oferujemy wynagrodzenia.

### Zakres

**W zakresie** (kod):
- `tools/legal-cite/` — serwer MCP (Python) pobierający treść przepisów,
- `scripts/` — skrypty pomocnicze (m.in. pre-commit sanitizer).

**Poza zakresem:**
- **Treść prawna** (`references/`, `workflows/`, `examples/`) — to wzory i wiedza doktrynalna, nie oprogramowanie. Uwagi merytoryczno-prawne zgłaszaj przez [Issues](../../issues) lub szablony w `.github/ISSUE_TEMPLATE/`, nie tym kanałem.
- Dane w `examples/testowe-akta/` są **fikcyjne** (zmyślone podmioty, NIP-y o celowo błędnej sumie kontrolnej) — to nie jest wyciek danych.
- Podatności w Claude Code, serwerach MCP osób trzecich lub innych zależnościach — zgłaszaj do ich autorów.

> ⚠️ Ten projekt nie stanowi porady prawnej ani usługi bezpieczeństwa. Treści są udostępniane „tak jak są", na licencji Apache 2.0.

---

## 🇬🇧 Reporting a Vulnerability

Thank you for helping keep this project secure. Please report vulnerabilities **privately** — do not open a public Issue or a Pull Request describing the flaw.

**Reporting channel:** `a.piotrowski@ktzr.pl` (subject: `SECURITY: commercial-legal-pl`).

Please include:
- a description and reproduction steps (version/commit),
- potential impact,
- optionally, a suggested fix.

**What to expect:**
- acknowledgement within **7 days**,
- initial assessment and plan within **30 days**,
- **coordinated disclosure** — public disclosure only after a fix is available.

This project has no bug-bounty program — reports are welcome and appreciated, but not financially rewarded.

### Scope

**In scope** (code):
- `tools/legal-cite/` — Python MCP server that fetches statutory text,
- `scripts/` — helper scripts (incl. the pre-commit sanitizer).

**Out of scope:**
- **Legal content** (`references/`, `workflows/`, `examples/`) — these are templates and doctrinal knowledge, not software. Report substantive legal concerns via [Issues](../../issues) or the `.github/ISSUE_TEMPLATE/` forms, not this channel.
- Data in `examples/testowe-akta/` is **fictitious** (invented entities, NIP numbers with deliberately invalid checksums) — not a data leak.
- Vulnerabilities in Claude Code, third-party MCP servers, or other dependencies — report those to their maintainers.

> ⚠️ This project is not legal advice nor a security service. Content is provided "as is" under the Apache 2.0 license.
