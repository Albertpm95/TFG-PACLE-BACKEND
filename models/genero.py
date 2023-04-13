from typing import Optional

from sqlmodel import Field, SQLModel

class Genero(SQLModel, table=True):
    __tablename__: str = "generos"

    idGenero: Optional[int] = Field(default=None, primary_key=True)
    genero: str = Field(nullable=False, unique=True)
