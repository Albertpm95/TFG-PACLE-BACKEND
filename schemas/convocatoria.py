from pydantic import BaseModel
from sqlalchemy import DateTime

from constants import IDIOMAS_DISPONIBLES, TIPOS_ACTA


class ConvocatoriaNueva(BaseModel):
    comprension_auditiva_puntuacion_maxima_parte: int
    comprension_lectora_puntuacion_maxima_parte: int
    expresion_escrita_puntuacion_maxima_parte: int
    expresion_oral_puntuacion_maxima_parte: int
    id_convocatoria: str
    estado: bool
    fecha: DateTime | None = None
    id: str | None = None
    lenguaje: IDIOMAS_DISPONIBLES
    tipo: TIPOS_ACTA

    class Config:
        orm_mode = True
