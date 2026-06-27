"""Warstwa bazy danych ktzr-memory.

DATABASE_URL env var (domyślnie SQLite lokalnie):
  - sqlite+aiosqlite:///ktzr_memory.db    ← lokalne dev (default)
  - postgresql+asyncpg://user:pass@host/db ← Cloud SQL (produkcja)

Cloud Run zwykle podaje DATABASE_URL w formacie postgres:// lub postgresql://
— konwertujemy na asyncpg automatycznie.
"""
from __future__ import annotations

import os
from datetime import datetime

from sqlalchemy import DateTime, String, Text, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

_raw_url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///ktzr_memory.db").strip()

# Normalizuj postgres:// → postgresql+asyncpg://
if _raw_url.startswith("postgres://"):
    DATABASE_URL = _raw_url.replace("postgres://", "postgresql+asyncpg://", 1)
elif _raw_url.startswith("postgresql://") and "+asyncpg" not in _raw_url:
    DATABASE_URL = _raw_url.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    DATABASE_URL = _raw_url

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Memory(Base):
    __tablename__ = "memories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime | None] = mapped_column(
        DateTime, server_default=func.now(), nullable=True
    )
    category: Mapped[str] = mapped_column(String(100), index=True)
    case_ref: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    tags: Mapped[str | None] = mapped_column(Text, nullable=True)  # przecinkami


async def init_db() -> None:
    """Tworzy tabele jeśli nie istnieją (idempotentne)."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_memory(
    content: str,
    category: str,
    case_ref: str | None = None,
    tags: str | None = None,
) -> Memory:
    async with SessionLocal() as session:
        mem = Memory(content=content, category=category, case_ref=case_ref, tags=tags)
        session.add(mem)
        await session.commit()
        await session.refresh(mem)
        return mem


async def search_memories(
    query: str,
    category: str | None = None,
    case_ref: str | None = None,
    limit: int = 10,
) -> list[Memory]:
    """Wyszukiwanie AND: wszystkie słowa muszą wystąpić w content lub tags."""
    async with SessionLocal() as session:
        stmt = select(Memory)

        words = [w.strip() for w in query.split() if w.strip()]
        for word in words:
            escaped = word.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            pattern = f"%{escaped}%"
            stmt = stmt.where(
                or_(
                    Memory.content.ilike(pattern),
                    Memory.tags.ilike(pattern),
                )
            )

        if category:
            stmt = stmt.where(Memory.category == category)
        if case_ref:
            stmt = stmt.where(Memory.case_ref == case_ref)

        stmt = stmt.order_by(Memory.created_at.desc()).limit(limit)
        result = await session.execute(stmt)
        return list(result.scalars().all())


async def get_categories() -> list[tuple[str, int]]:
    """Zwraca pary (kategoria, liczba_wpisów) posortowane malejąco."""
    async with SessionLocal() as session:
        stmt = (
            select(Memory.category, func.count(Memory.id).label("cnt"))
            .group_by(Memory.category)
            .order_by(func.count(Memory.id).desc())
        )
        result = await session.execute(stmt)
        return [(row.category, row.cnt) for row in result]
