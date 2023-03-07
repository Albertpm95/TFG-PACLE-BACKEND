from pydantic import BaseModel

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class Comprension(BaseModel):
    id_acta: int
    tipo: str
    observaciones: str | None = None
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntos_conseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_maxima_parte: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_tarea_1: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_tarea_2: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_tarea_3: int = VALOR_PUNTUACION_MAX_DEFECTO

    class Config:
        orm_mode = True
