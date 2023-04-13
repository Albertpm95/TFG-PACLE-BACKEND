import datetime
from typing import Optional

from sqlmodel import Field, SQLModel
class Acta(SQLModel, table=True):
    __tablename__ = "actas"

    idActa: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime.datetime = Field(nullable=False)
    resultado: str = Field(nullable=False, default='No corregido')
    idConvocatoria: int = Field(nullable=False, foreign_key="convocatorias.idConvocatoria")
    idExpresionEscrita: int = Field(nullable=False, foreign_key="expresion.idExpresion")
    idExpresionOral: int = Field(nullable=False, foreign_key="expresion.idExpresion")
    idComprensionLectora: int = Field(nullable=False, foreign_key="comprension.idComprension")
    idComprensionAuditiva: int = Field(nullable=False, foreign_key="comprension.idComprension")