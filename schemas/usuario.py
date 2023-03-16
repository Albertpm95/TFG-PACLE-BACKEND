from typing import Optional
from pydantic import BaseModel

from schemas.rol_usuario import Rol


class UsuarioBase(BaseModel):
    apellidos: str
    estado: bool
    idUsuario: int
    nombre: str
    username: str
    rol: Rol

    class Config:
        orm_mode = True


class UsuarioCreacion(UsuarioBase):
    plain_password: str


class UsuarioLogin(UsuarioBase):
    hashed_password: str


class UsuarioOptional(UsuarioBase):
    __annotations__ = {k: Optional[v] for k, v in UsuarioBase.__annotations__.items()}
