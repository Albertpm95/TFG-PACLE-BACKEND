from typing import Optional

from sqlmodel import CheckConstraint, Field, Relationship, SQLModel

from models.correccion import Correccion


class Expresion(SQLModel, table=True):
    __tablename__ = "expresiones"

    idExpresion: Optional[int] = Field(default=None, primary_key=True)
    observaciones: str = Field(nullable=True, default="")
    porcentaje: int = Field(nullable=False, default=0)
    puntosConseguidos: int = Field(nullable=False, default=0)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    tipo: str = Field(CheckConstraint(("tipo IN ('escrita', 'oral')")))

    idCorreccion1: Optional[int] = Field(
        default=None, foreign_key="correcciones.idCorreccion"
    )
    correccion1: Correccion = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Expresion.idCorreccion1==Correccion.idCorreccion",
            "lazy": "joined",
        }
    )
    idCorreccion2: Optional[int] = Field(
        default=None, foreign_key="correcciones.idCorreccion"
    )
    correccion2: Correccion = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Expresion.idCorreccion2==Correccion.idCorreccion",
            "lazy": "joined",
        }
    )
