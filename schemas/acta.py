from datetime import datetime
from pydantic import BaseModel


from schemas.comprension import ComprensionActa
from schemas.expresion import Expresion


class Acta(BaseModel):
    comprension_auditiva: ComprensionActa
    comprension_lectora: ComprensionActa
    expresion_escrita: Expresion
    expresion_oral: Expresion
    fecha: datetime
    id_acta: str
    id_alumno: str
    id_convocatoria: str

    class Config:
        orm_mode = True
