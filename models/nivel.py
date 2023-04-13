from typing import Optional

from sqlmodel import Field, SQLModel

class Nivel(SQLModel, table=True):
    idNivel: Optional[int] = Field(default=None, primary_key=True)
    nivel: str = Field(default=None, nullable=False, unique=True)
