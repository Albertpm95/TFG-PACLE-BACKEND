from pydantic import BaseModel

from constants import ROLES


class UsuarioBase(BaseModel):
    id_usuario: int
    username: str
    nombre: str
    apellidos: str
    active: bool
    rol: ROLES

    class Config:
        orm_mode = True


class UsuarioLogin(UsuarioBase):
    hashed_password: str

    class Config:
        orm_mode = True
