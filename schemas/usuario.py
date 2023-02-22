from pydantic import BaseModel

from constants import ROLES


class UsuarioBase(BaseModel):
    apellidos: str
    estado: bool
    nombre: str
    rol: ROLES
    username: str

    class Config:
        orm_mode = True


class UsuarioLogin(UsuarioBase):
    hashed_password: str

    class Config:
        orm_mode = True
