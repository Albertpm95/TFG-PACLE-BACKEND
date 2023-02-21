from datetime import datetime
from pydantic import BaseModel


class ConvocatoriaNueva(BaseModel):
    comprension_auditiva_puntuacion_maxima_parte: int
    comprension_lectora_puntuacion_maxima_parte: int
    expresion_escrita_puntuacion_maxima_parte: int
    expresion_oral_puntuacion_maxima_parte: int
    id_convocatoria: int
    estado: bool
    fecha: datetime | None = None
    lenguaje: str
    tipo: str
    horario: str

    class Config:
        orm_mode = True
