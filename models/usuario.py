from sqlalchemy import Boolean, Column, String

from db.database import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    rol = Column(String)
    active = Column(Boolean, nullable=False)
