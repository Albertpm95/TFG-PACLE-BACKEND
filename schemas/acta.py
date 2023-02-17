from datetime import datetime
from pydantic import BaseModel
from routers import convocatoria


from schemas.comprension import ComprensionActa
from schemas.convocatoria import ConvocatoriaNueva
from schemas.expresion import Expresion
from schemas.alumno import AlumnoActa


class Acta(BaseModel):
    comprension_auditiva: ComprensionActa
    comprension_lectora: ComprensionActa
    expresion_escrita: Expresion
    expresion_oral: Expresion
    fecha: datetime
    alumno: AlumnoActa
    convocatoria: ConvocatoriaNueva
    id_acta: str

    class Config:
        orm_mode = True
