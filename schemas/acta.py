from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from schemas.comprension_lectora import ComprensionLectora

from schemas.convocatoria import Convocatoria
from schemas.comprension_auditiva import ComprensionAuditiva
from schemas.comprension_auditiva import ComprensionAuditiva
from schemas.expresion_escrita import ExpresionEscrita
from schemas.expresion_oral import ExpresionOral
from schemas.alumno import Alumno


class ActaBase(BaseModel):
    alumno: Alumno
    convocatoria: Convocatoria
    fecha: datetime
    expresion_oral: ExpresionOral
    expresion_escrita: ExpresionOral
    comprension_lectora: ComprensionLectora
    comprension_auditiva: ComprensionAuditiva

    class Config:
        orm_mode = True


class ActaDB(ActaBase):
    id_acta: Optional[int]

    class Config:
        orm_mode = True
