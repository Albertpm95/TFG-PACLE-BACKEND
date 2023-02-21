from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fake_db import lista_acciones

from crud import crud

router = APIRouter()


@router.get("/usuario/actions")
async def get_lista_de_acciones():
    return lista_acciones


@router.get("/usuarios")
async def get_list_usuarios(db: Session = Depends(crud.get_db)):
    return crud.get_users(db)


@router.get("/usuario/{id_usuario}")
async def get_usuario_by_id(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud.get_user_id(db, id_usuario)


@router.get("/usuario/{username}")
async def get_usuario_by_username(username: str, db: Session = Depends(crud.get_db)):
    return crud.get_user_username(db, username)
