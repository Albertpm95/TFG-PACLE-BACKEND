from sqlmodel import SQLModel, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URI: str | None = os.getenv("SQLALCHEMY_DATABASE_URI")

metadata = MetaData(schema="pacle_db")

#engine = create_engine(    SQLALCHEMY_DATABASE_URI, connect_args={"options": "-csearch_path=pacle_db"}, echo=True)
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: type = declarative_base()
SQLModel.metadata = Base.metadata

from models import (
    lenguaje,
    horario,
    colectivoUV,
    nivel,
    genero,
    alumno,
    rol_usuario,
    usuario,
    convocatoria,
    tarea,
    expresion,
    comprension,
    shared,
    acta,
)  # Order in wich the tables have to be created

SQLModel.metadata.create_all(engine)
