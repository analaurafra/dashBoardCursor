from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sqlalchemy as sa
import toml


@dataclass(frozen=True)
class PostgresConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    sslmode: str = "prefer"


def load_config(config_path: str | Path) -> PostgresConfig:
    path = Path(config_path)
    raw = toml.loads(path.read_text(encoding="utf-8"))
    pg = raw.get("postgres") or {}

    missing = [k for k in ("host", "port", "database", "user", "password") if k not in pg]
    if missing:
        raise ValueError(f"Config inválida. Campos ausentes em [postgres]: {', '.join(missing)}")

    return PostgresConfig(
        host=str(pg["host"]),
        port=int(pg["port"]),
        database=str(pg["database"]),
        user=str(pg["user"]),
        password=str(pg["password"]),
        sslmode=str(pg.get("sslmode", "prefer")),
    )


def make_engine(cfg: PostgresConfig) -> sa.Engine:
    url = sa.URL.create(
        drivername="postgresql+psycopg2",
        username=cfg.user,
        password=cfg.password,
        host=cfg.host,
        port=cfg.port,
        database=cfg.database,
        query={"sslmode": cfg.sslmode} if cfg.sslmode else None,
    )
    return sa.create_engine(url, pool_pre_ping=True)

