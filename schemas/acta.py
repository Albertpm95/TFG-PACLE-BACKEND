import numbers
from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from schemas.alumno import Alumno

IDIOMAS_DISPONIBLES = Literal['Español', 'English',
                              'Català', 'Français', 'Chainese', 'Deutsch']
TIPOS_ACTA = Literal['Ordinaria', 'Extraordinaria']
HORARIOS = Literal['9:00']

class Comprension(BaseModel):
  observaciones: str
  porcentaje: int
  puntosConseguidos: int
  puntuacion_tarea1: int
  puntuacion_tarea2: int
  puntuacion_tarea3: int
  puntuacionMaximaParte: int
  
class Tarea(BaseModel):
  alcance: int
  coherencia: int
  correccion: int
  eficaciaC: int
  id_corrector: str | None = None
  nombre_corrector: str | None = None

class Expresion(BaseModel):
  observaciones: str | None = None
  pocentaje: int
  puntosConseguidos: int
  puntuacionMaximaParte: int
  tarea1: Tarea
  tarea2: Tarea
  
  
class ActaBase(BaseModel):
    estado: bool
    fecha: datetime | None = None
    id: str | None = None
    lenguaje: IDIOMAS_DISPONIBLES
    tipo: TIPOS_ACTA
    comprensionLectora: Comprension
    comprensionAuditiva: Comprension
    expresionEscrita: Expresion
    expresionOral: Expresion


class Acta(ActaBase):
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True
