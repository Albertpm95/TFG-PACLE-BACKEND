from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environment import SQLALCHEMY_DATABASE_URI

metadata = MetaData()

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"options": "-csearch_path=pacle_db"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=metadata)

from models import (
    alumno,
    usuario,
    comprension,
    tarea,
    expresion,
    convocatoria,
    acta,
)  # Order in wich the tables have to be created

Base.metadata.create_all(bind=engine)
