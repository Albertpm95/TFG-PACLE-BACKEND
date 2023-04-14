from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

# from models.convocatoria import Convocatoria


class Horario(SQLModel, table=True):
    __tablename__: str = "horarios"

    idHorario: Optional[int] = Field(default=None, primary_key=True)
    horario: str = Field(nullable=False, unique=True)

    # idConvocatoria: Optional[int] = Field(foreign_key="convocatorias.idConvocatoria")
    # convocatoria: Optional[list[Convocatoria]] = Relationship(back_populates="horario")
