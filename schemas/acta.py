from datetime import datetime
from pydantic import BaseModel
from schemas.convocatoria import Convocatoria
from schemas.comprension import Comprension
from schemas.expresion import Expresion
from schemas.alumno import AlumnoActa


class Acta(BaseModel):
    id_acta: int
    alumno: AlumnoActa
    convocatoria: Convocatoria
    fecha: datetime
    expresion: Expresion
    comprension: Comprension
    horario: str

    class Config:
        orm_mode = True
