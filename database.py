from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


engine = create_engine("postgresql://postgres:1234@localhost:5432/pacle")


Base = declarative_base()
Base.metadata.schema = 'Pacle_db'

SessionLocal = sessionmaker(bind=engine)
