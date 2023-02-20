from pydantic import BaseModel

from constants import ROLES


class UsuarioBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UsuarioLogin(BaseModel):
    password: str

    class Config:
        orm_mode = True


class UsuarioFront(UsuarioBase):
    id_usuario: int
    nombre: str
    apellidos: str
    active: bool
    rol: ROLES

    class Config:
        orm_mode = True
