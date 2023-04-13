import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class Convocatoria(SQLModel, table=True):
    __tablename__ = "convocatorias"

    maxComprensionLectora: int = Field(nullable=False, default=0)
    maxComprensionAuditiva: int = Field(nullable=False, default=0)
    maxExpresionEscrita: int = Field(nullable=False, default=0)
    maxExpresionOral: int = Field(nullable=False, default=0)
    idConvocatoria: Optional[int] = Field(default=None, primary_key=True)
    specificIdentifier: str = Field(nullable=False, default='')
    idLenguaje: int = Field(nullable=False, foreign_key="lenguajes.idLenguaje")
    fecha: datetime.datetime = Field(nullable=False)
    idHorario: int = Field(nullable=False, foreign_key="horarios.idHorario")
    estado: bool = Field(nullable=False, default=False)
    idNivel: int = Field(nullable=False, foreign_key="niveles.idNivel")
