from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()


class Convocatoria(BaseModel):
    id_convocatoria: int
    name: str


db = SessionLocal()


@app.get('/convocatorias', response_model=List[Convocatoria], status_code=200)
def get_all_convocatorias():
    convocatorias = db.query(models.Convocatoria).all()
    return convocatorias
