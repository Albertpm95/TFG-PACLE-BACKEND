from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import alumno as crud_alumno
from crud import convocatoria as crud_convocatoria
from models.shared import AlumnosConvocatoria
from schemas.alumno import AlumnoDB as sch_alumnoDB
from schemas.convocatoria import ConvocatoriaDB as sch_convocatoriaDB


def get_matriculas(db: Session):
    return db.query(AlumnosConvocatoria).all()

def get_alumno_convocatoria(alumno: sch_alumnoDB, convocatoria: sch_convocatoriaDB, db: Session):
    return db.query(AlumnosConvocatoria).filter(AlumnosConvocatoria.alumno.idAlumno == alumno.idAlumno, AlumnosConvocatoria.convocatoria.idConvocatoria == convocatoria.idConvocatoria)

def matricular_alumno_convocatoria(alumno: sch_alumnoDB, convocatoria: sch_convocatoriaDB, db: Session):
    existe_alumno = crud_alumno.get_alumno_id()
    if not existe_alumno:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra el alumno seleccionada.",
        )
    existe_convocatoria = crud_convocatoria.get_convocatoria_id()
    if not existe_convocatoria:
        raise HTTPException(
            status_code=404,
            detail="No se encuentra la convocatoria seleccionada.",
        )
    existe_matricula = get_alumno_convocatoria(alumno, convocatoria, db)
    if existe_matricula:
        raise HTTPException(
            status_code=409,
            detail="Ese alumno ya esta matriculado en esa convocatoria.",
        )
    matricula = AlumnosConvocatoria(alumno=alumno, convocatoria=convocatoria)
    db.add(matricula)
    db.commit()
    db.refresh()
    return matricula
    
    