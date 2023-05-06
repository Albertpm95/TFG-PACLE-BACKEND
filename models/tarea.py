from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from models.usuario import Usuario

if TYPE_CHECKING:
    from models.parte import Parte

class Tarea(SQLModel, table=True):
    __tablename__ = "tareas"
    
    idTarea: int = Field(primary_key=True)
    nombreTarea: str = Field(nullable=False)
    
    idParte: Optional[int] = Field(foreign_key="partes_convocatoria.idParte")
    parte: Optional["Parte"] = Relationship(back_populates="tareas",sa_relationship_kwargs={"primaryjoin": "Tarea.idParte==Parte.idParte","lazy": "joined",})

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