from datetime import datetime

from pydantic import BaseModel

from schemas.horario import Horario
from schemas.idiomas import Idioma


class Convocatoria(BaseModel):
    comprension_auditiva_puntuacion_maxima_parte: int
    comprension_lectora_puntuacion_maxima_parte: int
    estado: bool
    expresion_escrita_puntuacion_maxima_parte: int
    expresion_oral_puntuacion_maxima_parte: int
    fecha: datetime | None = None
    horario: Horario
    id_convocatoria: int
    lenguaje: Idioma

    class Config:
        orm_mode = True
