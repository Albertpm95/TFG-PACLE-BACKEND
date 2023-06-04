import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from models.horario import Horario
from models.lenguaje import Lenguaje
from models.nivel import Nivel
from models.parte import Parte

if TYPE_CHECKING:
    from models.shared import AlumnosConvocatoria


class Convocatoria(SQLModel, table=True):
    __tablename__ = "convocatorias"

    idConvocatoria: Optional[int] = Field(default=None, primary_key=True)

    specificIdentifier: str = Field(nullable=False, default="")
    fecha: datetime.datetime = Field(nullable=False)
    estado: bool = Field(nullable=False, default=False)

    idHorario: int = Field(nullable=False, foreign_key="horarios.idHorario")
    horario: Horario = Relationship()

    idLenguaje: int = Field(nullable=False, foreign_key="lenguajes.idLenguaje")
    lenguaje: Lenguaje = Relationship()

    idNivel: int = Field(nullable=False, foreign_key="niveles.idNivel")
    nivel: Nivel = Relationship()

    idParteComprensionLectora: int = Field(nullable=False, foreign_key=Parte.idParte)
    parteComprensionLectora: Parte = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Convocatoria.idParteComprensionLectora==Parte.idParte",
            "lazy": "joined",
        }
    )
    idParteComprensionAuditiva: int = Field(nullable=False, foreign_key=Parte.idParte)
    parteComprensionAuditiva: Parte = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Convocatoria.idParteComprensionAuditiva==Parte.idParte",
            "lazy": "joined",
        }
    )
    idParteExpresionEscrita: int = Field(nullable=False, foreign_key=Parte.idParte)
    parteExpresionEscrita: Parte = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Convocatoria.idParteExpresionEscrita==Parte.idParte",
            "lazy": "joined",
        }
    )
    idParteExpresionOral: int = Field(nullable=False, foreign_key=Parte.idParte)
    parteExpresionOral: Parte = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Convocatoria.idParteExpresionOral==Parte.idParte",
            "lazy": "joined",
        }
    )

    alumnos_matriculados: list["AlumnosConvocatoria"] = Relationship(back_populates="convocatoria")
