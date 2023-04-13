from fastapi import APIRouter
from routers import rol, genero, nivel, lenguaje, colectivoUV, horario

router = APIRouter(prefix="/config")

router.include_router(rol.router)
router.include_router(genero.router)
router.include_router(nivel.router)
router.include_router(lenguaje.router)
router.include_router(colectivoUV.router)
router.include_router(horario.router)