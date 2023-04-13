from typing import Optional

from sqlmodel import  Field, SQLModel

class Tarea(SQLModel, table=True):
    __tablename__ = "tareas"

    idTarea: Optional[int] = Field(default=None, primary_key=True)
    nombreTarea: str = Field(nullable=False)
    valor: int = Field(nullable=False, default=0)
