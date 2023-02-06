from fastapi import APIRouter

from schemas.usuario import UsuarioLogin
from constants import fake_usuarios_DB
router = APIRouter()


@router.post("/login")
async def login(usuario: UsuarioLogin):
    filter(lambda x: x.username == usuario.username, fake_usuarios_DB)
    return {"message": "No existe el usuario"}
