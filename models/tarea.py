from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.usuario import Usuario

# from models.shared import Correccion


class Tarea(SQLModel, table=True):
    __tablename__ = "tareas"
    
    idTarea: int = Field(default=None, primary_key=True)
    nombreTarea: str = Field(nullable=False)

class TareaCorregida(SQLModel, table=True):
    __tablename__ = "tareas_corregidas"

    idTarea: int = Field(foreign_key=Tarea.idTarea)
    tarea: Tarea = Relationship()
    idTareaCorregida: Optional[int] = Field(default=None, primary_key=True)
    puntuacion: int = Field(nullable=False, default=0)
    
class Correccion(SQLModel, table=True):
    __tablename__ = "correccion"
    
    idCorreccion: int = Field(default=None, primary_key=True)
    idTareaCorregida: int = Field(foreign_key=TareaCorregida.idTareaCorregida)
    tareasCorregidas: list[TareaCorregida] = Relationship()
    idCorrector: int = Field(foreign_key=Usuario.idUsuario)
    corrector: Usuario = Relationship()