"""ktzr-memory — serwer MCP pamięci kancelarii KTZR.

Narzędzia:
  remember()        — zapisz informację do pamięci
  recall()          — przeszukaj pamięć (full-text, filtry kategorii i sprawy)
  list_categories() — lista kategorii z liczbą wpisów

Transport:
  - Cloud Run (K_SERVICE lub PORT): streamable-http na 0.0.0.0:$PORT/mcp
  - lokalnie (brak PORT): stdio (Claude Desktop / Claude Code)

Backend DB (env DATABASE_URL):
  - sqlite+aiosqlite:///ktzr_memory.db   ← domyślnie (lokalnie)
  - postgresql+asyncpg://user:pass@/db?host=/cloudsql/... ← Cloud SQL
"""
from __future__ import annotations

import logging
import os
import sys
from contextlib import asynccontextmanager
from typing import AsyncIterator

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from ktzr_memory import db

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format="[ktzr-memory] %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(server: FastMCP) -> AsyncIterator[None]:
    await db.init_db()
    db_hint = db.DATABASE_URL.split("///")[-1][:60]
    logger.info("DB gotowe: %s", db_hint)
    yield


mcp = FastMCP("ktzr-memory", lifespan=lifespan)

VALID_CATEGORIES = {"klient", "negocjacje", "klauzule", "ryzyka", "precedensy", "misc"}
# Jeśli dodasz kategorię tutaj, zaktualizuj też docstringi remember() i recall() (parametr `category:`).


@mcp.tool()
async def remember(
    content: str,
    category: str,
    case_ref: str | None = None,
    tags: str | None = None,
) -> str:
    """Zapisuje informację do pamięci kancelarii KTZR.

    Używaj do zapamiętania: pozycji negocjacyjnych klienta, wyników analizy
    ryzyk, sprawdzonych klauzul, preferencji stron, precedensów ze spraw.

    Zasada: treść konkretna i samowyjaśnialna bez kontekstu — za rok ta notatka
    musi być zrozumiała bez dostępu do akt.
    Zły: "cap ok, Alfa zgodziła się"
    Dobry: "Alfa Solutions (NDA 2026) akceptuje cap odpowiedzialności = 3 miesiące
            wynagrodzenia netto; odrzuciła wariant 1 miesiąca jako 'zbyt niski'."

    Args:
        content:  Treść do zapamiętania (po polsku, konkretnie, min. 20 znaków).
        category: klient | negocjacje | klauzule | ryzyka | precedensy | misc
        case_ref: Referencja sprawy — np. "alfa-solutions/nda-2026",
                  "gamma-finance/body-leasing-q1-2026" (opcja).
        tags:     Tagi rozdzielone przecinkami — np. "NDA,IT,poufność,cap" (opcja).
    """
    content = content.strip()
    if len(content) < 10:
        return "❌ Treść za krótka — podaj konkretną informację (min. 10 znaków)."

    category = category.strip().lower()
    if category not in VALID_CATEGORIES:
        valid = " / ".join(sorted(VALID_CATEGORIES))
        return f'❌ Nieznana kategoria "{category}". Dostępne: {valid}'

    mem = await db.add_memory(
        content=content,
        category=category,
        case_ref=case_ref.strip() if case_ref else None,
        tags=tags.strip() if tags else None,
    )
    parts = [f"kategoria={mem.category}"]
    if mem.case_ref:
        parts.append(f"sprawa={mem.case_ref}")
    if mem.tags:
        parts.append(f"tagi={mem.tags}")
    return f"✅ Zapamiętano (id={mem.id}, {', '.join(parts)}):\n{mem.content}"


@mcp.tool()
async def recall(
    query: str,
    category: str | None = None,
    case_ref: str | None = None,
    limit: int = 10,
) -> str:
    """Przeszukuje pamięć kancelarii KTZR i zwraca pasujące wpisy.

    Wyszukiwanie AND: każde słowo z zapytania musi wystąpić w treści lub tagach.
    Wyniki posortowane od najnowszych. Używaj przed każdą sprawą żeby odtworzyć
    kontekst: pozycje negocjacyjne, preferencje klienta, zidentyfikowane ryzyka.

    Args:
        query:    Słowa kluczowe — np. "cap odpowiedzialności IT",
                  "Alfa Solutions pozycja", "klauzula anty-copyleft copyleft GPL"
        category: Ogranicz do kategorii (opcja):
                  klient | negocjacje | klauzule | ryzyka | precedensy | misc
        case_ref: Ogranicz do sprawy — np. "alfa-solutions/nda-2026" (opcja).
        limit:    Maks. liczba wyników (domyślnie 10, max 50).
    """
    query = query.strip()
    if not query:
        return "❌ Podaj zapytanie (słowa kluczowe)."

    if category:
        category = category.strip().lower()
        if category not in VALID_CATEGORIES:
            valid = " / ".join(sorted(VALID_CATEGORIES))
            return f'❌ Nieznana kategoria "{category}". Dostępne: {valid}'

    limit = min(max(1, limit), 50)
    results = await db.search_memories(
        query=query,
        category=category if category else None,
        case_ref=case_ref.strip() if case_ref else None,
        limit=limit,
    )

    if not results:
        filters = []
        if category:
            filters.append(f"kategoria={category}")
        if case_ref:
            filters.append(f"sprawa={case_ref}")
        suffix = f" ({', '.join(filters)})" if filters else ""
        return f'🔍 Brak wyników dla: "{query}"{suffix}'

    lines = [f'🔍 Znaleziono {len(results)} wpis(ów) dla: "{query}"\n']
    for m in results:
        date_str = m.created_at.strftime("%Y-%m-%d") if m.created_at else "?"
        meta_parts = [m.category]
        if m.case_ref:
            meta_parts.append(m.case_ref)
        tag_str = f"  [{m.tags}]" if m.tags else ""
        lines.append(f"─── [{' · '.join(meta_parts)}] {date_str}{tag_str}")
        lines.append(m.content)
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
async def list_categories() -> str:
    """Zwraca listę kategorii w pamięci kancelarii z liczbą wpisów.

    Wywołaj na początku sesji żeby zobaczyć co jest w pamięci zanim użyjesz recall().
    """
    cats = await db.get_categories()
    if not cats:
        return (
            "📂 Pamięć kancelarii jest pusta.\n"
            "Użyj remember() żeby zapisać pierwsze informacje."
        )

    lines = ["📂 Pamięć kancelarii KTZR — kategorie:\n"]
    for cat, count in cats:
        lines.append(f"  {cat:<15} {count} wpis(ów)")
    total = sum(c for _, c in cats)
    lines.append(f"\nŁącznie: {total} wpisów")
    return "\n".join(lines)


def main() -> None:
    if os.getenv("K_SERVICE") or os.getenv("PORT"):
        port_int = int(os.getenv("PORT", "8080"))
        logger.info("ktzr-memory start: streamable-http na 0.0.0.0:%s (/mcp)", port_int)

        mcp.settings.host = "0.0.0.0"
        mcp.settings.port = port_int
        mcp.settings.transport_security = TransportSecuritySettings(
            enable_dns_rebinding_protection=False
        )
        mcp.run(transport="streamable-http")
    else:
        logger.info("ktzr-memory start: stdio (lokalnie)")
        mcp.run()


if __name__ == "__main__":
    main()
