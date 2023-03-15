from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from schemas.convocatoria import ConvocatoriaDB
from schemas.comprension_auditiva import ComprensionAuditiva
from schemas.comprension_lectora import ComprensionLectora
from schemas.expresion_escrita import ExpresionEscrita
from schemas.expresion_oral import ExpresionOral
from schemas.alumno import AlumnoDB


class ActaBase(BaseModel):
    alumno: AlumnoDB
    convocatoria: ConvocatoriaDB
    fecha: datetime
    expresion_oral: ExpresionOral
    expresionEscrita: ExpresionEscrita
    comprensionLectora: ComprensionLectora
    comprensionAuditiva: ComprensionAuditiva

    class Config:
        orm_mode = True


class ActaDB(ActaBase):
    idActa: Optional[int]

    class Config:
        orm_mode = True
