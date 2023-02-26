from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import alumno as crud_alumno
from schemas.alumno import AlumnoActa, AlumnoBase

router = APIRouter()


@router.get("/alumnos/list", response_model=list[AlumnoActa])
async def recuperar_alumnos(db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumnos(db)


@router.post("/alumno/{nombre}")
async def recuperar_alumno_nombre():
    return


@router.post("/alumno/{id}")
async def recuperar_alumno_id():
    return
