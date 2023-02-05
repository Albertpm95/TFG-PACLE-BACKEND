from fastapi import APIRouter

from schemas.usuario import UsuarioLogin

router = APIRouter()


@router.post("/login")
async def login(usuario: UsuarioLogin):
    return {'message', 'Login de ' + usuario.username}
