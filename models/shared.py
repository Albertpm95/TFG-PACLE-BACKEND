
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from models.alumno import Alumno
from models.acta import Acta
from models.comprension import Comprension
from models.expresion import Expresion
from models.convocatoria import Convocatoria
from models.usuario import Usuario

class AlumnosActa(SQLModel, table=True):
    __tablename__ = "actas_alumnos"

    id: Optional[int] = Field(default=None, primary_key=True)
    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    idAlumno: int = Field(foreign_key="alumnos.idAlumno")


class AlumnosConvocatoria(SQLModel, table=True):
    __tablename__: str = "matriculados_convocatoria"

    id: Optional[int] = Field(default=None, primary_key=True)
    convocatoria: Convocatoria = Relationship(back_populates="alumno")
    idAlumno: int = Field(foreign_key="alumnos.idAlumno")
    alumno: Alumno = Relationship(back_populates="convocatoria")

class ActaCompresion(SQLModel, table=True):
    __tablename__ = "actas_compresion"

    id: Optional[int] = Field(default=None, primary_key=True)
    idComprension: int = Field(nullable=False, foreign_key="comprensiones.idComprension")
    comprension: Comprension = Relationship(back_populates="acta")
    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    acta: Acta = Relationship(back_populates="comprension")


class ActaExpresion(SQLModel, table=True):
    __tablename__ = "actas_expresion"

    id: Optional[int] = Field(default=None, primary_key=True)
    idExpresion: int = Field(nullable=False, foreign_key="expresiones.idExpresion")
    expresion: Expresion = Relationship(back_populates="acta")
    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    acta: Acta = Relationship(back_populates="expresion")