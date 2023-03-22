from pydantic import BaseModel
from schemas.correccion import Correccion

from constants import VALOR_PUNTUACION_MAX_DEFECTO


class Expresion(BaseModel):
    observaciones: str | None = None
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntosConseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacionMaxima: int = VALOR_PUNTUACION_MAX_DEFECTO
    correccion1: Correccion
    correccion2: Correccion

    class Config:
        orm_mode = True


class ExpresionDB(Expresion):
    idExpresion: int

    class Config:
        orm_mode = True
