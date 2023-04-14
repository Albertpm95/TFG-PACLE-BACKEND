from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.nivel import Nivel


def crear_nivel(db: Session, nivel_nuevo: str) -> Nivel:
    existe_nivel: Nivel | None = get_nivel_nombre(db, nivel_nuevo)
    print(nivel_nuevo)
    print(existe_nivel)
    if existe_nivel:
        raise HTTPException(
            status_code=404, detail="Ya existe ese nivel, no puede crearse otra vez."
        )

    db_nivel: Nivel = Nivel(nivel=nivel_nuevo)
    db.add(db_nivel)
    db.commit()
    db.refresh(db_nivel)
    return db_nivel


def get_niveles(db: Session) -> list[Nivel]:
    return db.query(Nivel).all()


def get_nivel_id(db: Session, idNivel: int) -> Nivel:
    return db.query(Nivel).filter(Nivel.idNivel == idNivel).first()


def get_nivel_nombre(db: Session, nivel: str) -> Nivel:
    return db.query(Nivel).filter(Nivel.nivel == nivel).first()


def delete_nivel_id(db: Session, idnivel: int):
    existe_nivel: Nivel | None = get_nivel_id(db, idnivel)
    if not existe_nivel:
        raise HTTPException(
            status_code=404, detail="No existe ese nivel, no puede borrarse."
        )
    db.delete(existe_nivel)
    db.commit()
    # return {"ok": True}
    return {"Borrado": "Borrado el nivel ${nivel.nivel}"}
