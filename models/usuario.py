from sqlalchemy import Boolean, Column, String, Integer

from db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    apellidos = Column(String, nullable=False)
    estado = Column(Boolean, nullable=False)
    hashed_password = Column(String, nullable=False)
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    rol = Column(String)
    username = Column(String, unique=True, nullable=False)
