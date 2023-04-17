from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class ColectivoUV(SQLModel, table=True):
    __tablename__: str = "colectivoUV"

    idColectivoUV: Optional[int] = Field(default=None, primary_key=True)
    colectivoUV: str = Field(nullable=False, unique=True)