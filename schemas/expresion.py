from pydantic import BaseModel
from sqlalchemy import Integer
from schemas.tarea import Tarea

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class Expresion(BaseModel):
    id_acta: int
    tipo: str
    observaciones: str | None = None
    pocentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntos_conseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_maxima_parte: int = VALOR_PUNTUACION_MAX_DEFECTO
    tarea_1: Tarea
    tarea_2: Tarea

    class Config:
        orm_mode = True
