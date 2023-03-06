from datetime import datetime
from pydantic import BaseModel

from schemas.horario import Horario
from schemas.tipo import Tipo
from schemas.idiomas import Idioma


class Convocatoria(BaseModel):
    comprension_auditiva_puntuacion_maxima_parte: int
    comprension_lectora_puntuacion_maxima_parte: int
    expresion_escrita_puntuacion_maxima_parte: int
    expresion_oral_puntuacion_maxima_parte: int
    estado: bool
    fecha: datetime | None = None
    lenguaje: Idioma
    tipo: Tipo
    horario: Horario
    id_convocatoria: int

    class Config:
        orm_mode = True
