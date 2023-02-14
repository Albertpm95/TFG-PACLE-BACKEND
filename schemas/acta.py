from datetime import datetime
import numbers
from typing import Literal
from pydantic import BaseModel

from schemas.alumno import Alumno

IDIOMAS_DISPONIBLES = Literal['Español', 'English',
                              'Català', 'Français', 'Chainese', 'Deutsch']
TIPOS_ACTA = Literal['Ordinaria', 'Extraordinaria']
HORARIOS = Literal['9:00']

class ComprensionLectora(BaseModel):
  puntuacionMaximaParte: int
  puntuacion_tarea1: int
  puntuacion_tarea2: int
  puntuacion_tarea3: int
  puntosConseguidos: int
  observaciones: str
  porcentaje: int

class ActaBase(BaseModel):
    id: str | None = None
    lenguaje: IDIOMAS_DISPONIBLES
    tipo: TIPOS_ACTA
    fecha: datetime | None = None
    estado: bool


class Acta(ActaBase):
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True
