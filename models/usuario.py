from typing import Optional

from sqlmodel import Field, SQLModel

class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    apellidos: str = Field(nullable=False) 
    estado: bool = Field(nullable=False, default=False)
    hashedPassword: str = Field(nullable=False)
    idUsuario: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(nullable=False)
    username: str = Field(nullable=False)
    idRol: int = Field(nullable=False, foreign_key="roles.idRol")