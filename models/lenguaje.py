from typing import Optional

from sqlmodel import  Field, SQLModel

class Lenguaje(SQLModel, table=True):
    __tablename__: str = "lenguajes"

    idLenguaje: Optional[int] = Field(default=None, primary_key=True)
    lenguaje: str = Field(nullable=False, unique=True)
