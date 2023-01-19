from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'postgres'
passwd = '1234'
port = '5432'
host = 'localhost'
db = 'pacle'
DATABASE_URL = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"


def get_engine():
    return create_engine(DATABASE_URL)
