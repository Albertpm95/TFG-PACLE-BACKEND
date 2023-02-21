from fastapi import Query
from sqlalchemy.orm import Session

from db.database import SessionLocal

from crud import crud

import models.idiomas
import models.tipos
import models.horarios
import models.convocatoria


def get_convocatorias(db: Session):
    return db.query(models.convocatoria.ConvocatoriaBase).all()


def get_convocatoria_id(id_convocatoria: str, db: Session):
    return db.query(models.convocatoria.ConvocatoriaBase).filter(
        models.convocatoria.ConvocatoriaBase.id_convocatoria == id_convocatoria
    )


def get_idiomas(db: Session):
    return db.query(models.idiomas.Idiomas).all()


def add_idioma(lenguaje: str, db: Session):
    db_idioma = models.idiomas.Idiomas(lenguaje=lenguaje)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


def get_tipos(db: Session):
    return db.query(models.tipos.Tipos).all()


def add_tipo(db: Session, tipo: str):
    db_tipo = models.tipos.Tipos(tipo=tipo)
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo


def get_horarios(db: Session):
    return db.query(models.horarios.Horarios).all()


def add_horario(
    db: Session,
    horario: str = Query(regex="/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/"),
):
    db_horario = models.horarios.Horarios(horario=horario)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario
