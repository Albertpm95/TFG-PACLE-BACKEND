from sqlalchemy import Column, Integer, String


from db.database import Base


class Tarea(Base):
    __tablename__ = "tarea"

    id_tarea = Column(Integer, nullable=False, primary_key=True)
    nombre_tarea = Column(String, nullable=False)
    valor = Column(Integer, nullable=False)
