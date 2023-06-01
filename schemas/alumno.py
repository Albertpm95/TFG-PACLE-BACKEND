from datetime import date, datetime

from pydantic import BaseModel

from schemas.colectivoUV import ColectivoUV
from schemas.genero import Genero


class Alumno(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    email: str
    telefono: int
    fechaNacimiento: datetime
    pruebaAdaptada: bool
    genero: Genero
    colectivoUV: ColectivoUV

    class Config:
        orm_mode = True


class AlumnoDB(Alumno):
    idAlumno: int

    class Config:
        orm_mode = True
