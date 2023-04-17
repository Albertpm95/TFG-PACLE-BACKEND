
from typing import Optional
from pydantic import BaseModel

from schemas.correccion import Correccion
from schemas.tarea import Tarea

class ParteBase(BaseModel):
    tipo: str
    puntuacionMaxima: int
    tareas: list[Tarea]
    class Config:
        orm_mode = True

class ParteBaseDB(ParteBase):
    idParte: int
    class Config:
        orm_mode = True

class ParteCorregida(ParteBaseDB):
    correccion: Correccion
    correccion2: Optional[Correccion]
    observaciones: Optional[str]
    class Config:
        orm_mode = True

class ParteCorregidaDB(ParteCorregida):
    idParteCorregida: int
    class Config:
        orm_mode = True