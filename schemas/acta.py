from datetime import datetime
from typing import Literal
from pydantic import BaseModel

from schemas.alumno import Alumno


class ActaBase(BaseModel):
    id_acta: str | None = None
    lenguage: Literal['Español', 'English', 'Català', 'Français', 'Chainese', 'Deutsch']
    tipo: Literal['Ordinaria', 'Extraordinaria']
    fecha: datetime | None = None
    activa: bool


class Acta(ActaBase):
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True
