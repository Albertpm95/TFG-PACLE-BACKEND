from typing import Optional
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


class UsuarioOptional(UsuarioBase):
    __annotations__ = {k: Optional[v] for k, v in UsuarioBase.__annotations__.items()}
