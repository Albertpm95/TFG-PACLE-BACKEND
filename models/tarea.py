from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.shared import Correccion


class Tarea(SQLModel, table=True):
    __tablename__ = "tareas"

    idTarea: Optional[int] = Field(default=None, primary_key=True)
    nombreTarea: str = Field(nullable=False)
    valor: int = Field(nullable=False, default=0)

    # idCorreccion: int = Field(nullable=False, foreign_key="correcciones.idCorreccion")
    # correccion: Correccion = Relationship(back_populates="tareas")
