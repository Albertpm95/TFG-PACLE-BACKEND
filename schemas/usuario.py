from typing import Optional
from pydantic import BaseModel

from schemas.rol_usuario import Rol


class UsuarioBase(BaseModel):
    apellidos: str
    estado: bool
    id_usuario: int
    nombre: str
    rol: Rol
    username: str

    class Config:
        orm_mode = True


class UsuarioCreacion(UsuarioBase):
    plain_password: str

    class Config:
        orm_mode = True


class UsuarioLogin(UsuarioBase):
    hashed_password: str

    class Config:
        orm_mode = True


class UsuarioOptional(UsuarioBase):
    __annotations__ = {k: Optional[v] for k, v in UsuarioBase.__annotations__.items()}
