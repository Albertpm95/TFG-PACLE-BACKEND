from typing import Union

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from models.user import Admin, Corrector, Gestor, User

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_db_users = [
    User(id=1, nombre='Bob', apellido='Swanson',
         usuario='bob_swanson', password=1234, rol='admin'),
    User(id=2, nombre='Rick', apellido='Sanchez',
         usuario='rick_sanchez', password=1234, rol='gestor'),
    User(id=3, nombre='Morty', apellido='Smith',
         usuario='morty_smith', password=1234, rol='corrector'),
]


@app.get("/users/")
async def get_users(token: str = Depends(oauth2_scheme)):
    return {"token": token}


def search_user(id: int):
    users = filter(lambda user: user.id == id, fake_db_users)
    print(id)
    try:
        return (users)[0]
    except:
        return {'error': 'No se ha encontrado al usuario.'}
