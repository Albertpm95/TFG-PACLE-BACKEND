from sqlmodel import SQLModel, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

SQLALCHEMY_DATABASE_URI: str | None = os.environ.get("SQLALCHEMY_DATABASE_URI")

metadata = MetaData(schema="pacle_db")

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"options": "-csearch_path=pacle_db"}, echo=True)
#engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

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

def create_db_and_tables():
        SQLModel.metadata.create_all(engine)

def create_roles():
    rol_1: rol_usuario.Rol(rol="Administrador")
    rol_2: rol_usuario.Rol(rol="Gestor")
    rol_3: rol_usuario.Rol(rol="Corrector")
    with SessionLocal(engine) as session:
        session.add(rol_1)
        session.add(rol_2)
        session.add(rol_3)
        session.commit()
    print(rol_1)        
    print(rol_2)
    print(rol_3)
        
if __name__ == "__main__":    
    create_db_and_tables()
    create_roles()