from typing import Optional

from sqlmodel import Field, SQLModel

class Horario(SQLModel, table=True):
    __tablename__: str = "horarios"

    idHorario: Optional[int] = Field(default=None, primary_key=True)
    horario: str = Field(nullable=False, unique=True)
