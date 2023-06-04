import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from models.colectivoUV import ColectivoUV
from models.genero import Genero

if TYPE_CHECKING:
    from models.shared import AlumnosConvocatoria


class Alumno(SQLModel, table=True):
    __tablename__ = "alumnos"

    idAlumno: Optional[int] = Field(default=None, primary_key=True)
    
    nombre: str = Field(nullable=False)
    apellidos: str = Field(nullable=False)
    dni: str = Field(nullable=False, index=True, unique=True)
    email: str = Field(nullable=False)
    telefono: str = Field(nullable=False)
    fechaNacimiento: datetime.datetime = Field(nullable=False)
    pruebaAdaptada: bool = Field(default=False)

    idGenero: int = Field(nullable=False, foreign_key="generos.idGenero")
    genero: Genero = Relationship()

    idColectivoUV: int = Field(nullable=False, foreign_key="colectivoUV.idColectivoUV")
    colectivoUV: ColectivoUV = Relationship()

    convocatorias_matriculadas: list["AlumnosConvocatoria"] = Relationship(back_populates="alumno")