from typing import Optional
from pydantic import BaseModel

from models.usuario import Usuario
from schemas.rol_usuario import Rol


class UsuarioBase(BaseModel):
    apellidos: str
    estado: bool
    nombre: str
    rol: Rol
    username: str

    class Config:
        orm_mode = True

class UsuarioLogin(UsuarioBase):
    hashed_password: str

    class Config:
        orm_mode = True


class UsuarioDB(UsuarioBase):
    idUsuario: int

    class Config:
        orm_mode = True