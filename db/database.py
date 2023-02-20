from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from environment import SQLALCHEMY_DATABASE_URI

metadata = MetaData()
engine = create_engine(
    # SQLALCHEMY_DATABASE_URI, connect_args={"options": "-csearch_path=Pacle_db"}
    SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
