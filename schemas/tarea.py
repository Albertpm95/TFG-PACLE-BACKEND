from pydantic import BaseModel
from schemas.usuario import Usuario


class Tarea(BaseModel):
    alcance: int
    coherencia: int
    correccion: int
    eficaciaC: int
    corrector: Usuario
