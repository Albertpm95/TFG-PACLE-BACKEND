from datetime import datetime
from pydantic import BaseModel

from schemas.comprension_auditiva import ComprensionAuditiva
from schemas.comprension_lectiva import ComprensionLectiva
from schemas.convocatoria import Convocatoria
from schemas.expresion_oral import ExpresionOral
from schemas.expresion_escrita import ExpresionEscrita
from schemas.alumno import AlumnoActa


class Acta(BaseModel):
    alumno: AlumnoActa
    convocatoria: Convocatoria
    fecha: datetime
    id_acta: int
    expresion_escrita: ExpresionEscrita
    expresion_oral: ExpresionOral
    comprension_auditiva: ComprensionAuditiva
    comprension_lectiva: ComprensionLectiva
    horario: str

    class Config:
        orm_mode = True
