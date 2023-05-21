from pydantic import BaseModel

from schemas.tarea import TareaDB
from schemas.usuario import UsuarioDB


class Correccion(BaseModel):
    idCorreccion: int
    corrector: UsuarioDB
    tareas: list[TareaDB]
