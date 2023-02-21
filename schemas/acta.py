from datetime import datetime
from pydantic import BaseModel

from schemas.comprension import Comprension
from schemas.convocatoria import Convocatoria
from schemas.expresion import Expresion
from schemas.alumno import AlumnoActa


class Acta(BaseModel):
    alumno: AlumnoActa
    convocatoria: Convocatoria
    fecha: datetime
    id_acta: str
    expresiones: list[Expresion] = []
    comprensiones: list[Comprension] = []

    class Config:
        orm_mode = True
