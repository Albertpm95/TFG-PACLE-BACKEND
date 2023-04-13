from typing import Optional

from sqlmodel import  CheckConstraint, Field, SQLModel, UniqueConstraint

class comprension(SQLModel, table=True):
    __tablename__ = "comprensiones"

    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    idComprension: Optional[int] = Field(default=None, primary_key=True)
    idParte: int = Field(nullable=False, foreign_key="correcciones.idCorreccion")
    observaciones: str = Field(nullable=True, default='')
    porcentaje: int = Field(nullable=False, default=0)
    puntosConseguidos: int = Field(nullable=False, default=0)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    tipo: str = Field(CheckConstraint(("tipo IN ('auditiva', 'lectora')")), nullable=True )

    UniqueConstraint(idActa, tipo)