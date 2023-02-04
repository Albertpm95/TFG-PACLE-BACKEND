from fastapi import APIRouter, Body, Depends, HTTPException

from schemas import UsuarioLogin

router = APIRouter()


@router.post("/login")
async def login(usuario: UsuarioLogin):
    return {'message', 'Login de ' + usuario.username}
