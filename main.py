from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from models import Alumno
from convocatorias import Convocatoria
from db import SessionLocal, engine


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/alumnos/", response_model=list[Alumno])
def get_alumnos(db: Session = Depends(get_db)):
    alumnos = crud.get_alumnos()
    return alumnos


@app.get("/convocatorias/", response_model=list[Convocatoria])
def get_alumnos(db: Session = Depends(get_db)):
    convocatorias = crud.get_convocatorias()
    return convocatorias
