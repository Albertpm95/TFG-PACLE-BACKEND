from pydantic import BaseModel

from schemas.usuario import UsuarioDB
from schemas.tarea import Tarea, TareaDB


class Correccion(BaseModel):
    idCorreccion: int
    corrector: UsuarioDB
    tarea: list[TareaDB]
