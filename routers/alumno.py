from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import alumno as crud_alumno
from schemas.alumno import Alumno, AlumnoDB

router = APIRouter()


@router.get("/alumno/list", response_model=list[AlumnoDB])
async def recuperar_alumnos(db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumnos(db)


@router.get("/alumno/update/{nombre}", response_model=AlumnoDB)
async def recuperar_alumno_nombre(nombre: str, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_nombre(db=db, nombre=nombre)


@router.get("/alumno/update/{id_alumno}", response_model=AlumnoDB)
async def recuperar_alumno_id(id_alumno: int, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_id(id_alumno=id_alumno, db=db)


@router.get("/alumno/update/{dni}", response_model=AlumnoDB)
async def recuperar_alumno_dni(dni: str, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_dni(dni=dni, db=db)


@router.get("/alumno/create", response_model=AlumnoDB)
async def create_alumno(alumno_nuevo: Alumno, db: Session = Depends(crud.get_db)):
    return crud_alumno.create_alumno(alumno=alumno_nuevo, db=db)


@router.get("/alumno/update", response_model=AlumnoDB)
async def create_update(alumno_nuevo: AlumnoDB, db: Session = Depends(crud.get_db)):
    return crud_alumno.update_alumno(alumno=alumno_nuevo, db=db)
