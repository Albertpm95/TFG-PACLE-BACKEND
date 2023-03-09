from typing import Optional
from pydantic import BaseModel

from schemas.rol_usuario import Rol


class UsuarioBase(BaseModel):
    apellidos: str
    estado: bool
    id_usuario: int
    nombre: str
    username: str
    rol: Rol

    class Config:
        orm_mode = True


class UsuarioCreacion(Rol):
    plain_password: str


class UsuarioLogin(Rol):
    hashed_password: str


class UsuarioOptional(Rol):
    __annotations__ = {k: Optional[v] for k, v in UsuarioBase.__annotations__.items()}
