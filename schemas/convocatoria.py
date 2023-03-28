from datetime import datetime

from pydantic import BaseModel

from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel


class Convocatoria(BaseModel):
    maxComprensionLectora: int
    maxComprensionAuditiva: int
    estado: bool
    maxExpresionEscrita: int
    maxExpresionOral: int
    fecha: datetime | None = None
    horario: Horario
    lenguaje: Lenguaje
    nivel: Nivel

    class Config:
        orm_mode = True


class ConvocatoriaDB(Convocatoria):
    idConvocatoria: int

    class Config:
        orm_mode = True
