from typing import Literal
from pydantic import BaseModel

from constants import ROLES


class UsuarioBase(BaseModel):
    username: str


class UsuarioLogin(UsuarioBase):
    password: str


class Usuario(UsuarioBase):
    id_usuario: int
    username: str
    nombre: str
    apellidos: str
    password: str
    active: bool
    rol: ROLES
