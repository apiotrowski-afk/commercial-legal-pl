#!/usr/bin/env bash
# Polish Commercial Legal — pre-commit hook installer
#
# Ten skrypt instaluje pre-commit-sanitizer.py jako git hook.
#
# Użycie:
#     ./scripts/install-hooks.sh
#
# Wymagania:
#     - Python 3.7+
#     - git
#     - to repo musi być git-trackingowane

set -e

# Sprawdź czy jesteśmy w git repo
if [ ! -d ".git" ]; then
    echo "❌ Ten katalog nie jest git repo. Najpierw 'git init'."
    exit 1
fi

# Sprawdź czy Python 3 jest dostępny
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python 3 nie jest dostępny. Zainstaluj python3 i ponów."
    exit 1
fi

HOOK_PATH=".git/hooks/pre-commit"
SANITIZER_PATH="scripts/pre-commit-sanitizer.py"

if [ ! -f "$SANITIZER_PATH" ]; then
    echo "❌ Nie znaleziono $SANITIZER_PATH"
    echo "   Sprawdź, czy uruchamiasz skrypt z katalogu głównego repo."
    exit 1
fi

# Stwórz wrapper hook
cat > "$HOOK_PATH" << 'EOF'
#!/usr/bin/env bash
# Pre-commit hook Polish Commercial Legal
# Wywołuje sanitizer; blokuje commit w razie naruszeń.

REPO_ROOT="$(git rev-parse --show-toplevel)"
SANITIZER="$REPO_ROOT/scripts/pre-commit-sanitizer.py"

if [ ! -f "$SANITIZER" ]; then
    echo "⚠️  Sanitizer nie znaleziony: $SANITIZER"
    echo "   Commit kontynuowany bez sanitacji. Sprawdź instalację hooków."
    exit 0
fi

python3 "$SANITIZER"
EOF

chmod +x "$HOOK_PATH"
chmod +x "$SANITIZER_PATH"

echo "✅ Hook zainstalowany w $HOOK_PATH"
echo ""
echo "Test:"
echo "   python3 $SANITIZER_PATH"
echo ""
echo "Aktywacja przy commit — automatyczna od następnego commit."
echo ""
echo "Obejście (na własną odpowiedzialność):"
echo "   git commit --no-verify"
