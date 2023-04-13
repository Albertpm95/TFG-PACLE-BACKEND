from pydantic import BaseModel
from schemas.correccion import Correccion

class Expresion(BaseModel):
    observaciones: str | None = None
    porcentaje: int
    puntosConseguidos: int
    puntuacionMaxima: int
    tipo: str
    correccion1: Correccion
    correccion2: Correccion

    class Config:
        orm_mode = True


class ExpresionDB(Expresion):
    idExpresion: int

    class Config:
        orm_mode = True
