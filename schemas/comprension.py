from pydantic import BaseModel

from schemas.correccion import Correccion

class Comprension(BaseModel):
    observaciones: str | None = None
    tipo: str
    porcentaje: int
    puntosConseguidos: int
    puntuacionMaxima: int
    correccion: Correccion

    class Config:
        orm_mode = True


class ComprensionDB(Comprension):
    idComprension: int

    class Config:
        orm_mode = True
