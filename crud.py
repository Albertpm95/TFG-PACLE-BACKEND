from sqlalchemy.orm import Session

from alumnos import Alumno
from convocatorias import Convocatoria


def get_alumnos(db: Session):
    return db.query(Alumno).all()


def get_convocatorias(db: Session):
    return db.query(Convocatoria).all()
