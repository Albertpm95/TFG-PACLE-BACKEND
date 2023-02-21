from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import alumno as crud_alumno

router = APIRouter()


@router.post("/alumno/{nombre}")
async def recuperar_alumno_nombre():
    return


@router.post("/alumno/{id}")
async def recuperar_alumno_id():
    return


@router.post("/alumnos")
async def recuperar_alumnos(db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumnos(db)
