from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.tarea import Correccion, Tarea, TareaCorregida

class Parte(SQLModel, table=True):
    __tablename__ = "partes_convocatoria"
    
    idParte: Optional[int] = Field(default=None, primary_key=True)
    
    tipo: str = Field(nullable=False)
    puntuacionMaxima: int = Field(nullable=False, default=0)
    idTarea: int = Field(nullable=False, foreign_key=Tarea.idTarea)
    tareas: list[Tarea] = Relationship()
    
class ParteCorregida(SQLModel, table=True):
    __tablename__ = "partes_acta"
    
    idParte: int = Field(foreign_key=Parte.idParte)
    parte: Parte = Relationship()
    idParteCorregida: Optional[int] = Field(default=None, primary_key=True)
    observaciones: str = Field(nullable=True)
    idCorreccion: int = Field(nullable=False, foreign_key=Correccion.idCorreccion)
    correccion: Correccion = Relationship(
        sa_relationship_kwargs={    
            "primaryjoin": "ParteCorregida.idCorreccion==Correccion.idCorreccion",
            "lazy": "joined",
        }
    )
    idCorreccion2: Optional[int] = Field(nullable=False, foreign_key=Correccion.idCorreccion)
    correccion2: Optional[Correccion] = Relationship(
        sa_relationship_kwargs={    
            "primaryjoin": "ParteCorregida.idCorreccion2==Correccion.idCorreccion",
            "lazy": "joined",
        }
    )