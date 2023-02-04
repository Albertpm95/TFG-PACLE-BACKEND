from datetime import datetime
from typing import Literal
from pydantic import BaseModel

from schemas.alumno import Alumno


class ActaBase(BaseModel):
    id_acta: str | None = None
    lenguage: str
    tipo: Literal['Ordinaria', 'Extraordinaria']
    fecha: datetime


class Acta(ActaBase):
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True
