from sqlalchemy.orm import sessionmaker
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import get_engine

engine = get_engine()
models.Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/alumnos/", response_model=list[schemas.Alumno])
def get_alumnos(db: Session = Depends(get_db)):
    alumnos = crud.get_alumnos(db=db)
    if not alumnos:
        return JSONResponse(content={"detail": "No se han encontrado alumnos."},
                            status_code=204)
    return alumnos


@app.get("/convocatorias/", response_model=list[schemas.Convocatoria])
def get_convocatorias(db: Session = Depends(get_db)):
    convocatorias = crud.get_convocatorias(db=db)
    if not convocatorias:
        return JSONResponse(content={"detail": "No se han encontrado alumnos."},
                            status_code=204)
    print('Convocatorias', convocatorias)
    return convocatorias


@app.post("/create/alumno", response_model=schemas.Alumno, status_code=201)
def new_alumno(alumno: schemas.Alumno, db: Session = Depends(get_db)):
    db_alumno = models.Alumno(name=alumno.name)
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno
