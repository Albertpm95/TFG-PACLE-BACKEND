from pydantic import BaseModel
from schemas.tarea import Tarea

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class ExpresionOral(BaseModel):
    observaciones: str | None = None
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntos_conseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_maxima_parte: int = VALOR_PUNTUACION_MAX_DEFECTO
    tarea_1: Tarea
    tarea_2: Tarea

    class Config:
        orm_mode = True
