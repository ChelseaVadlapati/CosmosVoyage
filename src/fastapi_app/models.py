# ruff: noqa: UP007
# ruff: noqa: UP006
import os
import typing

from dotenv import load_dotenv
from sqlmodel import Field, Relationship, SQLModel, create_engine

load_dotenv()


def _require_env(name: str, allow_empty: bool = False) -> str:
    value = os.environ.get(name)
    if value is None or (value == "" and not allow_empty):
        raise RuntimeError(
            f"Missing required environment variable(s) for Postgres connection. Please set {name} (see .env.example)."
        )
    return value or ""


POSTGRES_USERNAME = _require_env("POSTGRES_USERNAME")
POSTGRES_PASSWORD = _require_env("POSTGRES_PASSWORD", allow_empty=True)
POSTGRES_HOST = _require_env("POSTGRES_HOST")
POSTGRES_DATABASE = _require_env("POSTGRES_DATABASE")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_SSL = os.environ.get("POSTGRES_SSL")

sql_url = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
if POSTGRES_SSL:
    sql_url = f"{sql_url}?sslmode={POSTGRES_SSL}"

engine = create_engine(sql_url)


def create_db_and_tables():
    return SQLModel.metadata.create_all(engine)


class CruiseDestinationLink(SQLModel, table=True):
    destination_id: int | None = Field(
        default=None,
        foreign_key="destination.id",
        primary_key=True,
    )
    cruise_id: int | None = Field(
        default=None,
        foreign_key="cruise.id",
        primary_key=True,
    )


class Destination(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    subtitle: str | None
    description: str | None
    cruises: typing.List["Cruise"] = Relationship(
        back_populates="destinations",
        link_model=CruiseDestinationLink,
    )

    def __str__(self):
        return f"{self.name}"


class Cruise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None
    subtitle: str | None
    destinations: typing.List["Destination"] = Relationship(
        back_populates="cruises",
        link_model=CruiseDestinationLink,
    )

    def __str__(self):
        return f"{self.name}"


class InfoRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    notes: str
    cruise_id: int = Field(default=None, foreign_key="cruise.id")
