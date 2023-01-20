from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class AlumnoBase(BaseModel):
    nombre: str
    apellidos: str


class Alumno(AlumnoBase):
    id: str
    examinado_convocatoria: str

    class Config:
        orm_mode = True


class ActaBase(BaseModel):
    lenguage: str
    tipo: Literal['Ordinaria', 'Extraordinaria']
    fecha: datetime


class Acta(ActaBase):
    id_acta: str | None = None
    participantes: list[Alumno] = []

    class Config:
        orm_mode = True


class UsuarioBase(BaseModel):
    nombre: str
    apellidos: str


class UsuarioCreate(UsuarioBase):
    password: str


class Usuario(UsuarioBase):
    id: int
    is_active: bool
    rol: Literal['Admin', 'Gestor', 'Corrector']
