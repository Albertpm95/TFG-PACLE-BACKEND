from sqlalchemy import Column, String, Integer
from db.database import Base


class Rol(Base):
    __tablename__ = "rol"

    id_rol = Column(Integer, primary_key=True)
    rol = Column(String, nullable=False)
