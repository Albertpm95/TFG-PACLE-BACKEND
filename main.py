from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from constants import lista_acciones
app = FastAPI()

origins = ["http://localhost:4200",
           "http://localhost:4200/", "http://localhost:4200/*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@ app.get("/")
async def root():
    return {"message": "Hay conexion con el servidor"}


@app.get("/actions")
async def get_list_de_acciones():
    return lista_acciones
