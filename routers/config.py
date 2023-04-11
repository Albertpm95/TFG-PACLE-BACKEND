from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import lenguaje as crud_idioma
from crud import nivel as crud_nivel
from crud import colectivoUV as crud_colectivoUV
from crud import genero as crud_genero
from crud import rol as crud_rol

from schemas.colectivoUV import ColectivoUV, ColectivoUVBase
from schemas.horario import Horario, HorarioBase
from schemas.lenguaje import Lenguaje, LenguajeBase
from schemas.nivel import Nivel, NivelBase
from schemas.genero import Genero, GeneroBase
from schemas.rol_usuario import Rol, RolBase

router = APIRouter(prefix="/config")

@router.get("/lenguaje/list", response_model=list[Lenguaje])
async def recuperar_lista_idiomas(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db)

@router.post("/lenguaje/create", response_model=Lenguaje)
async def create_lenguaje(lenguaje_nuevo: LenguajeBase, db: Session = Depends(crud.get_db)) -> Lenguaje:
    return crud_idioma.crear_lenguaje(db, lenguaje_nuevo.lenguaje)

@router.delete("/lenguaje/delete/{idLenguaje}", response_model=dict[str, str])
async def delete_lenguaje(
    idLenguaje: int, db: Session = Depends(crud.get_db)
) -> dict[str, str]:
    return crud_idioma.delete_idioma_id(db, idLenguaje)


@router.get("/horario/list", response_model=list[Horario])
async def recuperar_lista_horarios(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db)

@router.post("/horario/create", response_model=Horario)
async def create_horario(
    horario_nuevo: HorarioBase, db: Session = Depends(crud.get_db)
) -> Horario:
    return crud_horario.crear_horario(db, horario_nuevo.horario)

@router.delete("/horario/delete/{idHorario}", response_model=dict[str, str])
async def delete_horario(idHorario: int, db: Session = Depends(crud.get_db)):
    return crud_horario.delete_horario_id(db, idHorario)

@router.get("/nivel/list", response_model=list[Nivel])
async def recuperar_lista_niveles(db: Session = Depends(crud.get_db)):
    return crud_nivel.get_niveles(db)


@router.post("/nivel/create", response_model=Nivel)
async def create_nivel(nivel_nuevo: NivelBase, db: Session = Depends(crud.get_db)) -> Nivel:
    return crud_nivel.crear_nivel(db, nivel_nuevo.nivel)

@router.delete("/nivel/delete/{idNivel}", response_model=dict[str, str])
async def delete_nivel(idNivel: int, db: Session = Depends(crud.get_db)):
    return crud_nivel.delete_nivel_id(db, idNivel)

@router.get("/colectivoUV/list", response_model=list[ColectivoUV])
async def recuperar_lista_colectivosUV(
    db: Session = Depends(crud.get_db),
):
    return crud_colectivoUV.get_colectivosUV(db)

@router.post("/colectivoUV/create", response_model=ColectivoUV)
async def create_colectivo(colectivoUV_nuevo: ColectivoUVBase, db: Session = Depends(crud.get_db)) -> ColectivoUV:
    print(colectivoUV_nuevo)
    return crud_colectivoUV.crear_colectivoUV(db, colectivoUV_nuevo=colectivoUV_nuevo.colectivoUV)

@router.delete("/colectivoUV/delete/{idColectivoUV}", response_model=dict[str, str])
async def delete_colectivoUV(idColectivoUV: int, db: Session = Depends(crud.get_db)):
    return crud_colectivoUV.delete_colectivoUV_id(db, idColectivoUV)

@router.get("/genero/list", response_model=list[Genero])
async def recuperar_lista_generos(db: Session = Depends(crud.get_db)):
    return crud_genero.get_generos(db)


@router.post("/genero/create", response_model=Genero)
async def create_genero(
    genero_nuevo: GeneroBase, db: Session = Depends(crud.get_db)
) -> Genero:
    return crud_genero.crear_genero(db, genero_nuevo.genero)

@router.delete("/genero/delete/{idGenero}", response_model=dict[str, str])
async def delete_genero(idGenero: int, db: Session = Depends(crud.get_db)) -> dict[str, str]:
    return crud_genero.delete_genero_id(db, idGenero)

@router.get("/rol/list", response_model=list[Rol])
async def recuperar_lista_roles(db: Session = Depends(crud.get_db)):
    return crud_rol.get_roles(db)

@router.post("/rol/create", response_model=Rol)
async def create_rol(
    rol_nuevo: RolBase, db: Session = Depends(crud.get_db)
) -> Rol:
    return crud_rol.crear_rol(db, rol_nuevo.rol)