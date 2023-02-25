from db.database import SessionLocal

import bcrypt
from environment import SECRET_KEY


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password, usuario_db_hashed_password):
    if get_password_hash(plain_password) == usuario_db_hashed_password:
        return True
    return False


def get_password_hash(plain_password):
    return plain_password
