from pydantic import BaseModel

from constants import VALOR_PUNTUACION_MAX_DEFECTO
from schemas.correccion import Correccion


class Comprension(BaseModel):
    observaciones: str | None = None
    tipo: str
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntosConseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacionMaxima: int = VALOR_PUNTUACION_MAX_DEFECTO
    correccion: Correccion

    class Config:
        orm_mode = True


class ComprensionDB(Comprension):
    idComprension: int

    class Config:
        orm_mode = True
