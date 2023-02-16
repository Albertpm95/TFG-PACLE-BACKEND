from pydantic import BaseModel

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class Comprension(BaseModel):
  observaciones: str = ''
  porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
  puntosConseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
  puntuacion_tarea1: int = VALOR_PUNTUACION_MAX_DEFECTO
  puntuacion_tarea2: int = VALOR_PUNTUACION_MAX_DEFECTO
  puntuacion_tarea3: int = VALOR_PUNTUACION_MAX_DEFECTO
  puntuacionMaximaParte: int = VALOR_PUNTUACION_MAX_DEFECTO