from typing import Optional

from sqlmodel import CheckConstraint, Field, Relationship, SQLModel, UniqueConstraint

from models.correccion import Correccion


class Comprension(SQLModel, table=True):
    __tablename__ = "comprensiones"

    idComprension: Optional[int] = Field(default=None, primary_key=True)
    observaciones: str = Field(nullable=True, default="")
    porcentaje: int = Field(nullable=False, default=0)
    puntosConseguidos: int = Field(nullable=False, default=0)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    tipo: str = Field(
        CheckConstraint(("tipo IN ('auditiva', 'lectora')")), nullable=True
    )

    idCorreccion: Optional[int] = Field(
        default=None, foreign_key="correcciones.idCorreccion"
    )
    correccion: Correccion = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Comprension.idCorreccion==Correccion.idCorreccion",
            "lazy": "joined",
        }
    )
