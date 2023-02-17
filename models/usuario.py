from sqlalchemy import Boolean, Column, String

from db.base_class import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    rol = Column(String)
    is_active = Column(Boolean, nullable=False)
