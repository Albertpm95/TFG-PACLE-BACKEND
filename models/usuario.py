from sqlalchemy import Boolean, Column, String

from db.base_class import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    rol = Column(String)
    is_active = Column(Boolean, nullable=False)
