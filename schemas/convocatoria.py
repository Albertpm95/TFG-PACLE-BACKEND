from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Date

from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel
from schemas.parte import ParteBase, ParteBaseDB


class ConvocatoriaBase(BaseModel):
    estado: bool
    fecha: datetime
    horario: Horario
    lenguaje: Lenguaje
    nivel: Nivel
    specificIdentifier: str
    parteComprensionLectora: ParteBase 
    parteComprensionAuditiva: ParteBase
    parteExpresionEscrita: ParteBase
    parteExpresionOral: ParteBase

    class Config:
        orm_mode = True

class ConvocatoriaNueva(ConvocatoriaBase):
    parteComprensionLectora: ParteBase 
    parteComprensionAuditiva: ParteBase
    parteExpresionEscrita: ParteBase
    parteExpresionOral: ParteBase

class ConvocatoriaDB(ConvocatoriaBase):
    idConvocatoria: int
    parteComprensionLectora: ParteBaseDB
    parteComprensionAuditiva: ParteBaseDB
    parteExpresionEscrita: ParteBaseDB
    parteExpresionOral: ParteBaseDB

    class Config:
        orm_mode = True
