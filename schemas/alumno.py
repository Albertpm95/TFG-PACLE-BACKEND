from datetime import date, datetime
from pydantic import BaseModel

from schemas.colectivoUV import ColectivoUV
from schemas.genero import Genero


class Alumno(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    colectivoUV: ColectivoUV
    genero: Genero
    email: str
    telefono: int
    fechaNacimiento: date | datetime
    pruebaAdaptada: bool

    class Config:
        orm_mode = True


class AlumnoDB(Alumno):
    idAlumno: int

    class Config:
        orm_mode = True
