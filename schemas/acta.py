from datetime import datetime
from pydantic import BaseModel
from schemas.convocatoria import Convocatoria
from schemas.comprension import Comprension
from schemas.expresion import Expresion
from schemas.alumno import AlumnoActa


class Acta(BaseModel):
    alumno: AlumnoActa
    convocatoria: Convocatoria
    fecha: datetime
    id_acta: int
    # expresion_escrita: ExpresionEscrita
    # expresion_oral: ExpresionOral
    # comprension_auditiva: ComprensionAuditiva
    # comprension_lectiva: ComprensionLectiva
    expresion: Expresion
    comprension: Comprension
    horario: str

    class Config:
        orm_mode = True
