from sqlalchemy import Boolean, Column, ForeignKey, String, Integer

from db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    apellidos = Column(String, nullable=False)
    estado = Column(Boolean, nullable=False)
    hashed_password = Column(String(length=60), nullable=False)
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    id_rol = Column(Integer, ForeignKey("rol.id_rol"), nullable=False)
    username = Column(String, unique=True, nullable=False)
