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
    resultado: str = Field(nullable=False, default="No corregido")

    idConvocatoria: Optional[int] = Field(
        default=None, foreign_key="convocatorias.idConvocatoria"
    )
    convocatoria: Convocatoria = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idConvocatoria==Convocatoria.idConvocatoria",
            "lazy": "joined",
        }
    )

    idExpresionEscrita: Optional[int] = Field(
        default=None, foreign_key="expresiones.idExpresion"
    )
    expresionEscrita: Expresion = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idExpresionEscrita==Expresion.idExpresion",
            "lazy": "joined",
        }
    )

    idExpresionOral: Optional[int] = Field(
        default=None, foreign_key="expresiones.idExpresion"
    )
    expresionOral: Expresion = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idExpresionOral==Expresion.idExpresion",
            "lazy": "joined",
        }
    )

    idComprensionLectora: Optional[int] = Field(
        default=None, foreign_key="comprensiones.idComprension"
    )
    comprensionLectora: Comprension = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idComprensionLectora==Comprension.idComprension",
            "lazy": "joined",
        }
    )

    idComprensionAuditiva: Optional[int] = Field(
        default=None, foreign_key="comprensiones.idComprension"
    )
    comprensionAuditiva: Comprension = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idComprensionAuditiva==Comprension.idComprension",
            "lazy": "joined",
        }
    )

    idAlumno: Optional[int] = Field(default=None, foreign_key="alumnos.idAlumno")
    alumno: Alumno = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idAlumno==Alumno.idAlumno",
            "lazy": "joined",
        }
    )
