from datetime import datetime

from pydantic import BaseModel

from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel
from schemas.parte import ParteBase, ParteBaseDB


class Convocatoria(BaseModel):
    estado: bool
    fecha: datetime | None = None
    horario: Horario
    lenguaje: Lenguaje
    nivel: Nivel
    specificIdentifier: int
    parteComprensionLectora: ParteBase | ParteBaseDB
    parteComprensionAuditiva: ParteBase | ParteBaseDB
    parteExpresionEscrita: ParteBase | ParteBaseDB
    parteExpresionOral: ParteBase | ParteBaseDB

    class Config:
        orm_mode = True


class ConvocatoriaDB(Convocatoria):
    idConvocatoria: int

    class Config:
        orm_mode = True
