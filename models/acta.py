import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from models.alumno import Alumno

from models.convocatoria import Convocatoria
from models.expresion import Expresion
from models.comprension import Comprension

class Acta(SQLModel, table=True):
    __tablename__ = "actas"

    idActa: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime.datetime = Field(nullable=False)
    resultado: str = Field(nullable=False, default='No corregido')

    idConvocatoria: int = Field(nullable=False, foreign_key="convocatorias.idConvocatoria")
    convocatoria: Convocatoria = Relationship(back_populates="actas")

    idExpresionEscrita: int = Field(nullable=False, foreign_key="expresiones.idExpresion")
    expresionEscrita: Expresion = Relationship(back_populates="acta")

    idExpresionOral: int = Field(nullable=False, foreign_key="expresiones.idExpresion")
    expresionOral: Expresion = Relationship(back_populates="acta")

    idComprensionLectora: int = Field(nullable=False, foreign_key="comprensiones.idComprension")
    comprensionLectora: Comprension = Relationship(back_populates="acta")

    idComprensionAuditiva: int = Field(nullable=False, foreign_key="comprensiones.idComprension")
    comprensionAuditiva: Comprension = Relationship(back_populates="acta")
    
    idAlumno: int = Field(foreign_key=Alumno.idAlumno)
    alumno: Alumno = Relationship(back_populates="acta")