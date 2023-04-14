import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.acta import Acta
from models.horario import Horario
from models.lenguaje import Lenguaje
from models.nivel import Nivel


class Convocatoria(SQLModel, table=True):
    __tablename__ = "convocatorias"

    idConvocatoria: Optional[int] = Field(default=None, primary_key=True)
    maxComprensionLectora: int = Field(nullable=False, default=0)
    maxComprensionAuditiva: int = Field(nullable=False, default=0)
    maxExpresionEscrita: int = Field(nullable=False, default=0)
    maxExpresionOral: int = Field(nullable=False, default=0)
    specificIdentifier: str = Field(nullable=False, default="")
    fecha: datetime.datetime = Field(nullable=False)
    estado: bool = Field(nullable=False, default=False)

    idHorario: int = Field(nullable=False, foreign_key="horarios.idHorario")
    horario: Horario = Relationship()

    idLenguaje: int = Field(nullable=False, foreign_key="lenguajes.idLenguaje")
    lenguaje: Lenguaje = Relationship()

    idNivel: int = Field(nullable=False, foreign_key="niveles.idNivel")
    nivel: Nivel = Relationship()

    # idActa: Optional[int] = Field(foreign_key="actas.idActa")
    # actas: list[Acta] = Relationship(back_populates="convocatoria")
