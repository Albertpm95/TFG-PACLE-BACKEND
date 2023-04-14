from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

#from models.convocatoria import Convocatoria

class Nivel(SQLModel, table=True):
    __tablename__ = "niveles"
    
    idNivel: Optional[int] = Field(default=None, primary_key=True)
    nivel: str = Field(nullable=False, unique=True)

    #idConvocatoria: Optional[int] = Field(foreign_key="convocatorias.idConvocatoria")
    #convocatoria: Optional[list[Convocatoria]] = Relationship(back_populates="nivel")