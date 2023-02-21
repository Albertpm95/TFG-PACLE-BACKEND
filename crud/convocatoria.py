from fastapi import Query
from sqlalchemy.orm import Session

from models import idiomas as mod_idiomas
from models import tipos as mod_tipos
from models import horarios as mod_horarios
from models import convocatoria as mod_convocatoria


def get_convocatorias(db: Session):
    return db.query(mod_convocatoria.ConvocatoriaBase).all()


def get_convocatoria_id(id_convocatoria: str, db: Session):
    return db.query(mod_convocatoria.ConvocatoriaBase).filter(
        mod_convocatoria.ConvocatoriaBase.id_convocatoria == id_convocatoria
    )


def get_idiomas(db: Session):
    return db.query(mod_idiomas.Idiomas).all()


def add_idioma(lenguaje: str, db: Session):
    db_idioma = mod_idiomas.Idiomas(lenguaje=lenguaje)
    db.add(db_idioma)
    db.commit()
    db.refresh(db_idioma)
    return db_idioma


def get_tipos(db: Session):
    return db.query(mod_tipos.Tipos).all()


def add_tipo(db: Session, tipo: str):
    db_tipo = mod_tipos.Tipos(tipo=tipo)
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo


def get_horarios(db: Session):
    return db.query(mod_horarios.Horarios).all()


def add_horario(
    db: Session,
    horario: str = Query(regex="/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/"),
):
    db_horario = mod_horarios.Horarios(horario=horario)
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario
