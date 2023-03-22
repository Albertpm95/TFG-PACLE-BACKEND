from pydantic import BaseModel

from schemas.usuario import UsuarioBase


class Tarea(BaseModel):
    valor: int
    nombre_tarea: str

    class Config:
        orm_mode = True


class TareaDB(Tarea):
    id_tarea: int

    class Config:
        orm_mode = True


class ListaTareas(BaseModel):
    corrector: UsuarioBase
    listaTareas: list[Tarea]

    class Config:
        orm_mode = True
