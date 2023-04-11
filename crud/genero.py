from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.genero import Genero

def crear_genero(db: Session, genero_nuevo: str) -> Genero:
    existe_genero: Genero = get_genero_nombre(db, genero_nuevo)
    if existe_genero:
        raise HTTPException(
            status_code=404, detail="Ya existe ese genero, no puede crearse otra vez."
        )
    db_genero = Genero(genero=genero_nuevo)
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero


def get_generos(db: Session) -> list[Genero]:
    return db.query(Genero).all()


def get_genero_id(db: Session, idGenero) -> Genero:
    return db.query(Genero).filter(Genero.idGenero==idGenero).first()


def get_genero_nombre(db: Session, genero: str) -> Genero:
    return db.query(Genero).filter(Genero.genero==genero).first()

def delete_genero_id(db: Session, idgenero: int) -> dict[str, str]:
    existe_genero: Genero | None = get_genero_id(db, idgenero)
    if not existe_genero:
        raise HTTPException(
            status_code=404, detail="No existe ese genero, no puede borrarse."
        )
    db.delete(existe_genero)
    db.commit()
    #return {"ok": True}
    return {'Borrado': 'Borrado el idioma ${genero.genero}'}