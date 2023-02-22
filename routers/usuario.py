from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

import csv
import codecs

from crud import crud
from crud import usuario as crud_usuario
from schemas.usuario import UsuarioLogin

router = APIRouter()
