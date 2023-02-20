from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from db.database import engine
from routers import convocatoria, login, usuario, alumno, acta, admin

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(login.router)
app.include_router(usuario.router)
app.include_router(alumno.router)
app.include_router(convocatoria.router)
app.include_router(acta.router)
# app.include_router(admin.router)


origins = ["http://localhost:4200", "http://localhost:4200/", "http://localhost:4200/*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hay conexion con el servidor"}
