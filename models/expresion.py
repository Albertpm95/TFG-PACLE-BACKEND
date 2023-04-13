from typing import Optional

from sqlmodel import  CheckConstraint, Field, SQLModel, UniqueConstraint

class Expresion(SQLModel, table=True):
    __tablename__ = "expresiones"

    idActa: int = Field(nullable=False, foreign_key="colectivoUV.idColectivoUV")
    idExpresion: Optional[int] = Field(default=None, primary_key=True)
    idParte1: int = Field(nullable=False, foreign_key="correcciones.idCorreccion")
    idParte2: int = Field(nullable=False, foreign_key="correcciones.idCorreccion")
    observaciones: str = Field(nullable=True, default='')
    porcentaje: int = Field(nullable=False, default=0)
    puntosConseguidos: int = Field(nullable=False, default=0)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    tipo: str = Field(CheckConstraint(("tipo IN ('escrita', 'oral')")), nullable=True )

    UniqueConstraint(idActa, tipo)