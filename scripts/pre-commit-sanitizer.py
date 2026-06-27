#!/usr/bin/env python3
"""
Polish Commercial Legal — Pre-commit hook sanityzujący

Sprawdza wszystkie pliki staged przed commit pod kątem:
1. Konkretnych danych wrażliwych (NIP, PESEL, KRS, IBAN — regex)
2. Adresów email i numerów telefonów PL
3. Innych potencjalnie identyfikujących wzorców

Użycie:
    Skopiuj do .git/hooks/pre-commit (zachowaj uprawnienia wykonywalne)
    Lub uruchom ręcznie: python3 scripts/pre-commit-sanitizer.py

Wyjście:
    Kod 0 = wszystko OK, commit może iść dalej
    Kod 1 = znaleziono potencjalne naruszenia, commit zablokowany

Obejście (na własną odpowiedzialność):
    git commit --no-verify
"""

import os
import re
import subprocess
import sys
from typing import List, Tuple


# =============================================================================
# KONFIGURACJA — listy do sanitacji
# =============================================================================

# Lista zakazanych słów — dodaj własne identyfikatory klientów lokalnie.
# Działa case-insensitive, granica słowa (\b) gdy ma sens.
# UWAGA: nie wpisuj tu nazw klientów ani sygnatur spraw — ten plik jest publiczny.
# Zamiast tego: utwórz lokalny plik .forbidden-words (gitignored) i wczytaj go poniżej.
FORBIDDEN_WORDS: list = []

# Wyrażenia regularne dla danych strukturalnych.
# Każdy wpis to (regex, opis, severity)
#   severity: "block" = blokuje commit, "warn" = ostrzega
REGEX_PATTERNS = [
    # NIP polski (10 cyfr, z opcjonalnymi separatorami)
    (
        r"\bNIP\s*:?\s*[0-9]{3}[-\s]?[0-9]{2,3}[-\s]?[0-9]{2,3}[-\s]?[0-9]{2,3}\b",
        "NIP (10 cyfr)",
        "block",
    ),
    # PESEL (11 cyfr)
    (
        r"\bPESEL\s*:?\s*[0-9]{11}\b",
        "PESEL (11 cyfr)",
        "block",
    ),
    # KRS (do 10 cyfr, format często z zerami)
    (
        r"\bKRS\s*:?\s*[0-9]{10}\b",
        "KRS (10 cyfr)",
        "block",
    ),
    # IBAN polski (PL + 26 cyfr)
    (
        r"\bPL[0-9]{2}\s*([0-9]{4}\s*){5}[0-9]{4}\b",
        "Polski IBAN (PL + 26 cyfr)",
        "block",
    ),
    # 26-cyfrowy numer rachunku bez prefixu PL
    (
        r"\b[0-9]{2}\s*([0-9]{4}\s*){5}[0-9]{4}\b",
        "Numer rachunku bankowego (26 cyfr)",
        "block",
    ),
    # Adresy email konkretne (poza generic '@example.com' itp.)
    (
        r"\b[a-zA-Z0-9._%+-]+@(?!example\.|test\.|sample\.|placeholder\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",
        "Adres email",
        "warn",  # warn, bo READMy mogą zawierać email kontaktowy
    ),
    # Numery telefonów PL — z prefiksem +48/48
    # (bez prefiksu byłyby nieodróżnialne od REGON-ów i NIP-ów)
    (
        r"\+48\s*[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{3}\b",
        "Numer telefonu PL (+48)",
        "warn",
    ),
    # Numery telefonów PL — bez prefiksu, ale z etykietą (tel., kom., fax)
    (
        re.compile(r"(?:tel\.?|kom\.?|telefon|mobile|fax)\s*:?\s*[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{3}\b", re.IGNORECASE),
        "Numer telefonu PL (tel./kom.)",
        "warn",
    ),
]

# Wykluczenia — pliki/katalogi, dla których hook nie sprawdza
EXCLUDED_PATHS = [
    "examples/",           # testowe-akta — dane fikcyjne, oznaczone w README
    "case-studies/",
    "suplement/",
    "suplement-",          # suplement-it/, suplement-*/
    "profile/",
    "profiles/",
    "clients/",
    "contracts/",
    "umowy/",
    "pisma/",
    "korespondencja/",
    ".git/",
    "node_modules/",
    ".vscode/",
    ".idea/",
    "scripts/pre-commit-sanitizer.py",  # nie sprawdzaj samego hooka
]


# =============================================================================
# LOGIKA HOOKA
# =============================================================================


def get_staged_files() -> List[str]:
    """Zwraca listę plików staged do commitu (przekazanych przez git diff)."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [f.strip() for f in result.stdout.split("\n") if f.strip()]
        return files
    except subprocess.CalledProcessError:
        # Hook uruchamiany poza git — sprawdź wszystkie pliki md
        return get_all_md_files()


def get_all_md_files() -> List[str]:
    """Fallback — gdy hook uruchamiany poza git, skanuj wszystkie .md."""
    result = []
    for root, dirs, files in os.walk("."):
        # Skip excluded directories early
        dirs[:] = [
            d for d in dirs if not any(excl.rstrip("/") in d for excl in EXCLUDED_PATHS)
        ]
        for f in files:
            if f.endswith(".md") or f.endswith(".py") or f.endswith(".sh"):
                result.append(os.path.join(root, f))
    return result


def is_excluded(filepath: str) -> bool:
    """Sprawdza czy plik powinien być pominięty."""
    for excl in EXCLUDED_PATHS:
        if filepath.startswith(excl):
            return True
    return False


def check_file(filepath: str) -> List[Tuple[str, int, str, str]]:
    """
    Sprawdza pojedynczy plik. Zwraca listę naruszeń:
    (filepath, line_number, opis, severity)
    """
    violations = []

    try:
        if os.path.isdir(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (FileNotFoundError, UnicodeDecodeError):
        return []

    for line_num, line in enumerate(lines, start=1):
        # Sprawdź zakazane słowa
        for word in FORBIDDEN_WORDS:
            if word.lower() in line.lower():
                violations.append(
                    (
                        filepath,
                        line_num,
                        f"Zakazane słowo: '{word}'",
                        "block",
                    )
                )

        # Sprawdź regex
        for pattern, description, severity in REGEX_PATTERNS:
            if re.search(pattern, line):
                violations.append(
                    (filepath, line_num, f"Wzorzec: {description}", severity)
                )

    return violations


def format_violations(violations: List[Tuple[str, int, str, str]]) -> str:
    """Formatuje listę naruszeń do wyjścia."""
    blocking = [v for v in violations if v[3] == "block"]
    warnings = [v for v in violations if v[3] == "warn"]

    output = []

    if blocking:
        output.append("\n" + "=" * 70)
        output.append("❌ NARUSZENIA BLOKUJĄCE COMMIT")
        output.append("=" * 70)
        for filepath, line_num, description, _ in blocking:
            output.append(f"  {filepath}:{line_num}")
            output.append(f"    → {description}")

    if warnings:
        output.append("\n" + "=" * 70)
        output.append("⚠️  OSTRZEŻENIA (nie blokują, ale zweryfikuj)")
        output.append("=" * 70)
        for filepath, line_num, description, _ in warnings:
            output.append(f"  {filepath}:{line_num}")
            output.append(f"    → {description}")

    return "\n".join(output)


def main():
    print("🔍 Polish Commercial Legal — pre-commit sanitizer")
    print(f"   Sprawdzam pliki staged...")

    files = get_staged_files()

    if not files:
        print("   Brak plików staged. OK.")
        sys.exit(0)

    all_violations = []
    for filepath in files:
        if is_excluded(filepath):
            continue
        violations = check_file(filepath)
        all_violations.extend(violations)

    if not all_violations:
        print(f"   ✅ Sprawdzono {len(files)} plików, zero naruszeń.")
        sys.exit(0)

    print(format_violations(all_violations))

    blocking_count = sum(1 for v in all_violations if v[3] == "block")
    warning_count = sum(1 for v in all_violations if v[3] == "warn")

    print(
        f"\n📊 Podsumowanie: {blocking_count} naruszeń blokujących, "
        f"{warning_count} ostrzeżeń."
    )

    if blocking_count > 0:
        print("\n❌ Commit zablokowany.")
        print("   Aby kontynuować mimo wszystko (na własną odpowiedzialność):")
        print("       git commit --no-verify")
        print("   Lub: sanityzuj wymienione miejsca i ponów commit.\n")
        sys.exit(1)

    print("\n✅ Brak naruszeń blokujących — commit może iść dalej.")
    sys.exit(0)


if __name__ == "__main__":
    main()
