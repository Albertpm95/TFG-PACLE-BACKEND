from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from schemas.convocatoria import ConvocatoriaDB
from schemas.comprension import ComprensionDB
from schemas.expresion import ExpresionDB
from schemas.alumno import AlumnoDB


class ActaBase(BaseModel):
    alumno: AlumnoDB
    convocatoria: ConvocatoriaDB
    fecha: datetime
    expresion_oral: ExpresionDB
    expresionEscrita: ExpresionDB
    comprensionLectora: ComprensionDB
    comprensionAuditiva: ComprensionDB

    class Config:
        orm_mode = True


class ActaDB(ActaBase):
    idActa: Optional[int]

    class Config:
        orm_mode = True
