from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from fake_db import fake_usuarios_DB
from crud import crud
from schemas.usuario import UsuarioLogin

router = APIRouter()


@router.post("/login")
async def login(usuario: UsuarioLogin, db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_username(db, usuario.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
