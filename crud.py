from sqlalchemy.orm import Session

import models
import schemas


def get_alumnos(db: Session):
    return db.query(models.Alumno).all()


def get_convocatorias(db: Session):
    return db.query(models.Convocatoria).all()
