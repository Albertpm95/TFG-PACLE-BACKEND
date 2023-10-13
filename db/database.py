import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import MetaData, SQLModel, create_engine

SQLALCHEMY_DATABASE_URI: str | None = os.environ.get("SQLALCHEMY_DATABASE_URI")

metadata = MetaData(schema="pacle_db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"options": "-csearch_path=pacle_db"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: type = declarative_base()
SQLModel.metadata = Base.metadata


SQLModel.metadata.create_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
