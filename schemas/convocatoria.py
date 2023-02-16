import numbers
from datetime import datetime
from typing import Literal

from pydantic import BaseModel
from constants import IDIOMAS_DISPONIBLES, TIPOS_ACTA, VALOR_PUNTUACION_MAX_DEFECTO

from schemas.alumno import Alumno
from schemas.comprension import Comprension
from schemas.expresion import Expresion
from schemas.tarea import Tarea






  
class ConvocatoriaNueva(BaseModel):
  estado: bool
  fecha: datetime | None = None
  id: str | None = None
  lenguaje: IDIOMAS_DISPONIBLES
  puntuacionMaximaParteComprensionAuditiva: int
  puntuacionMaximaParteComprensionLectora: int
  puntuacionMaximaParteExpresionEscrita: int
  puntuacionMaximaParteExpresionOral: int
  tipo: TIPOS_ACTA

class ConvocatoriaCorregida(ConvocatoriaNueva):
    participantes: list[Alumno] = []
    comprensionLectora: Comprension
    comprensionAuditiva: Comprension
    expresionEscrita: Expresion
    expresionOral: Expresion
    class Config:
        orm_mode = True
