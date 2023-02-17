from pydantic import BaseModel
from schemas.tarea import Tarea


class Expresion(BaseModel):
    id_acta: str
    id_expresion: str
    observaciones: str | None = None
    pocentaje: int
    puntos_conseguidos: int
    puntuacion_maxima_parte: int
    tarea_1: Tarea
    tarea_2: Tarea
