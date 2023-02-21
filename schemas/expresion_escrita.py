from pydantic import BaseModel
from schemas.tarea import Tarea

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class ExpresionEscrita(BaseModel):
    id_expresion_escrita: int
    id_acta: int
    observaciones: str | None = None
    pocentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntos_conseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_maxima_parte: int = VALOR_PUNTUACION_MAX_DEFECTO
    tarea_1: Tarea
    tarea_2: Tarea

    class Config:
        orm_mode = True
