from pydantic import BaseModel
from schemas.usuario import UsuarioBase


class Tarea(BaseModel):
    alcance: int
    coherencia: int
    correccion: int
    eficaciaC: int
    corrector: UsuarioBase
