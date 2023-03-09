from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from schemas.convocatoria import Convocatoria
from schemas.comprension import Comprension
from schemas.expresion import Expresion
from schemas.alumno import Alumno


class ActaBase(BaseModel):
    alumno: Alumno
    convocatoria: Convocatoria
    fecha: datetime
    expresion: Expresion
    comprension: Comprension

    class Config:
        orm_mode = True


class ActaDB(ActaBase):
    id_acta: Optional[int]

    class Config:
        orm_mode = True
