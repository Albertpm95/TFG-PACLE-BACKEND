from sqlalchemy import CheckConstraint, Column, String, Integer

from db.database import Base


class Rol(Base):
    __tablename__ = "roles"

    idRol = Column(Integer, primary_key=True)
    rol = Column(String, nullable=False, unique=True)