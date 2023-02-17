from pydantic import BaseModel
from sqlalchemy import DateTime

from schemas.comprension import Comprension
from schemas.expresion import Expresion


class Acta(BaseModel):
    comprension_auditiva: Comprension
    comprension_lectora: Comprension
    expresion_escrita: Expresion
    expresion_oral: Expresion
    fecha: DateTime
    id_acta: str
    id_alumno: str
    id_convocatoria: str

    class Config:
        orm_mode = True
