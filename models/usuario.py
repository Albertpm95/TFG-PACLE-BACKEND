from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from models.rol_usuario import Rol


class Usuario(Base):
    __tablename__ = "usuarios"

    apellidos = Column(String, nullable=False)
    estado = Column(Boolean, nullable=False)
    hashedPassword = Column(String(length=60), nullable=False)
    idUsuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    idRol = Column(Integer, ForeignKey("roles.idRol"))
    rol: Mapped[Rol] = relationship()
