from pydantic import BaseModel
from schemas.tarea import Tarea, TareasExpresion

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class Expresion(BaseModel):
    observaciones: str | None = None
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntosConseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacionMaxima: int = VALOR_PUNTUACION_MAX_DEFECTO
    grupoTareas1: TareasExpresion
    grupoTareas2: TareasExpresion

    class Config:
        orm_mode = True


class ExpresionDB(Expresion):
    idExpresion: int

    class Config:
        orm_mode = True
