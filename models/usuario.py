from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.rol_usuario import Rol

# from models.shared import Correccion


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    idUsuario: Optional[int] = Field(default=None, primary_key=True)
    apellidos: str = Field(nullable=False)
    estado: bool = Field(nullable=False, default=False)
    hashedPassword: str = Field(nullable=False)
    nombre: str = Field(nullable=False)
    username: str = Field(nullable=False)

    idRol: int = Field(nullable=False, foreign_key="roles.idRol")
    rol: Rol = Relationship()

    # idCorreccion: Optional[int] = Field(foreign_key="correcciones.idCorreccion")
    # correccion: Optional[list[Correccion]] = Relationship(back_populates="usuario")
