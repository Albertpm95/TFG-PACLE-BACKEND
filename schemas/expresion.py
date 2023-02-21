from pydantic import BaseModel
from schemas.tarea import Tarea


class Expresion(BaseModel):
    id_expresion: int
    observaciones: str | None = None
    pocentaje: int
    puntos_conseguidos: int
    puntuacion_maxima_parte: int
    tarea_1: Tarea
    tarea_2: Tarea

    class Config:
        orm_mode = True
