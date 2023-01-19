from sqlalchemy.orm import sessionmaker
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import get_engine

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/alumnos/", response_model=list[schemas.Alumno])
def get_alumnos(db: Session = Depends(get_db)):
    alumnos = crud.get_alumnos(db=db)
    return alumnos


@app.get("/convocatorias/", response_model=list[schemas.Convocatoria])
def get_convocatorias(db: Session = Depends(get_db)):
    convocatorias = crud.get_convocatorias(db=db)
    return convocatorias
