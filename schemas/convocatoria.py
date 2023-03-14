from datetime import datetime

from pydantic import BaseModel

from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel


class Convocatoria(BaseModel):
    maximo_comprension_lectora: int
    maximo_comprension_auditiva: int
    estado: bool
    maximo_expresion_escrita: int
    maximo_expresion_oral: int
    fecha: datetime | None = None
    horario: Horario
    lenguaje: Lenguaje
    nivel: Nivel

    class Config:
        orm_mode = True


class ConvocatoriaDB(Convocatoria):
    id_convocatoria: int

    class Config:
        orm_mode = True
