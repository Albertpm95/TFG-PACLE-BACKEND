from datetime import datetime
from typing import Literal
from pydantic import BaseModel

from schemas.alumno import Alumno

IDIOMAS_DISPONIBLES = Literal['Español', 'English',
                              'Català', 'Français', 'Chainese', 'Deutsch']
TIPOS_ACTA = Literal['Ordinaria', 'Extraordinaria']


class ActaBase(BaseModel):
    id_acta: str | None = None
    lenguaje: IDIOMAS_DISPONIBLES
    tipo: TIPOS_ACTA
    fecha: datetime | None = None
    activa: bool


class Acta(ActaBase):
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True
