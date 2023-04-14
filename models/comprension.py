from typing import Optional

from sqlmodel import  CheckConstraint, Field, Relationship, SQLModel, UniqueConstraint

#from models.acta import Acta
from models.correccion import Correccion

class Comprension(SQLModel, table=True):
    __tablename__ = "comprensiones"

    idComprension: Optional[int] = Field(default=None, primary_key=True)
    observaciones: str = Field(nullable=True, default='')
    porcentaje: int = Field(nullable=False, default=0)
    puntosConseguidos: int = Field(nullable=False, default=0)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    tipo: str = Field(CheckConstraint(("tipo IN ('auditiva', 'lectora')")), nullable=True )

    idCorreccion: int = Field(nullable=False, foreign_key="correcciones.idCorreccion")
    correccion: Correccion = Relationship(back_populates="comprension")

    #idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    #acta: Acta = Relationship(back_populates="comprension")

    #UniqueConstraint("idActa", "tipo")