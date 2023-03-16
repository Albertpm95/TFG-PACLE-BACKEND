from pydantic import BaseModel

from constants import VALOR_PUNTUACION_MAX_DEFECTO
from schemas.tarea import Tarea


class Comprension(BaseModel):
    observaciones: str | None = None
    tipo: str
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntosConseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacionMaxima: int = VALOR_PUNTUACION_MAX_DEFECTO
    tareas: list[Tarea]

    class Config:
        orm_mode = True


class ComprensionDB(Comprension):
    idComprension: int

    class Config:
        orm_mode = True
