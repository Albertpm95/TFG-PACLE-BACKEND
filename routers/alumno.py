from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import alumno as crud_alumno
from schemas.alumno import Alumno, AlumnoDB

router = APIRouter(prefix="/alumno")


@router.get("/list", response_model=list[AlumnoDB])
async def recuperar_alumnos(db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumnos(db)


@router.get("/list/{idConvocatoria}")
async def recuperar_alumnos_by_convocatoria(
    idConvocatoria: int, db: Session = Depends(crud.get_db)
):
    return crud_alumno.get_alumnos_by_convocatoria(idConvocatoria, db)


@router.get("/details/{nombre}", response_model=AlumnoDB)
async def recuperar_alumno_nombre(nombre: str, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_nombre(db=db, nombre=nombre)


@router.get("/details/{idAlumno}", response_model=AlumnoDB)
async def recuperar_alumno_id(idAlumno: int, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_id(idAlumno=idAlumno, db=db)


@router.get("/details/{dni}", response_model=AlumnoDB)
async def recuperar_alumno_dni(dni: str, db: Session = Depends(crud.get_db)):
    return crud_alumno.get_alumno_dni(dni=dni, db=db)


@router.get("/create", response_model=AlumnoDB)
async def create_alumno(alumno_nuevo: Alumno, db: Session = Depends(crud.get_db)):
    return crud_alumno.create_alumno(alumno=alumno_nuevo, db=db)


@router.get("/update", response_model=AlumnoDB)
async def update_alumno(alumno_nuevo: AlumnoDB, db: Session = Depends(crud.get_db)):
    return crud_alumno.update_alumno(alumno=alumno_nuevo, db=db)
