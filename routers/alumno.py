from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import alumno as crud_alumno
from schemas.alumno import AlumnoActa, AlumnoBase

router = APIRouter()


@router.get("/alumnos/list", response_model=list[AlumnoActa])
async def recuperar_alumnos(db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumnos(db)


@router.post("/alumnos/{nombre}")
async def recuperar_alumno_nombre(nombre: str, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_nombre(db=db, nombre=nombre)


@router.get("/alumnos/{id_alumno}", response_model=AlumnoActa)
async def recuperar_alumno_id(id_alumno: int, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_id(id_alumno=id_alumno, db=db)
