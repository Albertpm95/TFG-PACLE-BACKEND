from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from models.tarea import Tarea
from models.usuario import Usuario


class Correccion(SQLModel, table=True):
    __tablename__ = "correcciones"

    idCorreccion: Optional[int] = Field(default=None, primary_key=True)
    idUsuario: int = Field(nullable=False, foreign_key="usuarios.idUsuario")
    usuario: Usuario = Relationship()
    idTarea: int = Field(nullable=False, foreign_key="tareas.idTarea")
    tareas: list[Tarea] = Relationship()
