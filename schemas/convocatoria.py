from datetime import datetime

from pydantic import BaseModel

from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel


class Convocatoria(BaseModel):
    comprension_auditiva_puntuacion_maxima_parte: int
    comprension_lectora_puntuacion_maxima_parte: int
    estado: bool
    expresion_escrita_puntuacion_maxima_parte: int
    expresion_oral_puntuacion_maxima_parte: int
    fecha: datetime | None = None
    horario: Horario
    lenguaje: Lenguaje
    nivel: Nivel

    class Config:
        orm_mode = True


class ConvocatoriaDB(Convocatoria):
    id_convocatoria: int

    class Config:
        orm_mode = True
