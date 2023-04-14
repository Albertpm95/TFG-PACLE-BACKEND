from token import OP
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

#from models.usuario import Usuario

class Rol(SQLModel, table=True):
    __tablename__ = "roles"
    idRol: Optional[int] = Field(default=None, primary_key=True)
    rol: str = Field(nullable=False, unique=True)
    
    #idUsuario: Optional[int] = Field(foreign_key="usuarios.idUsuario")
    #usuario: Optional[list[Usuario]] = Relationship(back_populates="rol")