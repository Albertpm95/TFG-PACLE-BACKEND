from datetime import datetime
from pydantic import BaseModel

from schemas.convocatoria import ConvocatoriaDB
from schemas.alumno import AlumnoDB
from schemas.parte import ParteCorregida


class ActaBase(BaseModel):
    alumno: AlumnoDB
    convocatoria: ConvocatoriaDB
    fecha: datetime
    resultado: str
    expresionOral: ParteCorregida
    expresionEscrita: ParteCorregida
    comprensionLectora: ParteCorregida
    comprensionAuditiva: ParteCorregida

    class Config:
        orm_mode = True


class ActaDB(ActaBase):
    idActa: int

    class Config:
        orm_mode = True
