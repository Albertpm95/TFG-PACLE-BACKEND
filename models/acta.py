import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from models.alumno import Alumno

from models.convocatoria import Convocatoria
from models.parte import ParteCorregida


class Acta(SQLModel, table=True):
    __tablename__ = "actas"

    idActa: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime.datetime = Field(nullable=False)
    resultado: str = Field(nullable=False, default="No corregido")

    idConvocatoria: Optional[int] = Field(default=None, foreign_key="convocatorias.idConvocatoria")
    convocatoria: Convocatoria = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idConvocatoria==Convocatoria.idConvocatoria",
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

    idExpresionEscrita: Optional[int] = Field(default=None, foreign_key="partes_acta.idParteCorregida")
    expresionEscrita: ParteCorregida = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idExpresionEscrita==ParteCorregida.idParteCorregida",
            "lazy": "joined",
        }
    )

    idExpresionOral: Optional[int] = Field(default=None, foreign_key="partes_acta.idParteCorregida")
    expresionOral: ParteCorregida = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idExpresionOral==ParteCorregida.idParteCorregida",
            "lazy": "joined",
        }
    )

    idComprensionLectora: Optional[int] = Field(default=None, foreign_key="partes_acta.idParteCorregida")
    comprensionLectora: ParteCorregida = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idComprensionLectora==ParteCorregida.idParteCorregida",
            "lazy": "joined",
        }
    )

    idComprensionAuditiva: Optional[int] = Field(default=None, foreign_key="partes_acta.idParteCorregida")
    comprensionAuditiva: ParteCorregida = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Acta.idComprensionAuditiva==ParteCorregida.idParteCorregida",
            "lazy": "joined",
        }
    )
