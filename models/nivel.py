from typing import Optional

from sqlmodel import Field, SQLModel

class Nivel(SQLModel, table=True):
    __tablename__ = "niveles"
    idNivel: Optional[int] = Field(default=None, primary_key=True)
    nivel: str = Field(nullable=False, unique=True)
