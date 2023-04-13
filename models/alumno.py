import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class Alumno(SQLModel, table=True):
    __tablename__ = "alumnos"
    
    idAlumno: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(nullable=False)
    apellidos: str = Field(nullable=False)
    dni: str = Field(nullable=False, index=True, unique=True)
    idGenero: int = Field(nullable=False, foreign_key="generos.idGenero")
    idColectivoUV: int = Field(nullable=False, foreign_key="colectivoUV.idColectivoUV")
    email:  str = Field(nullable=False)
    telefono: str = Field(nullable=False)
    fechaNacimiento: datetime.datetime = Field(nullable=False)
    pruebaAdaptada: bool = Field(nullable=False, default=False)