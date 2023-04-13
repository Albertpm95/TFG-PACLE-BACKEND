from typing import Optional

from sqlmodel import Field, SQLModel

class Rol(SQLModel, table=True):
    __tablename__ = "roles"
    idRol: Optional[int] = Field(default=None, primary_key=True)
    rol: str = Field(nullable=False, unique=True)
