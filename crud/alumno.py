from fastapi import Query
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas import alumno as sch_alumno


def create_alumno(alumno: sch_alumno.AlumnoActa, db: Session):
    alumno_db = sch_alumno.AlumnoActa(**alumno.dict())
    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db
