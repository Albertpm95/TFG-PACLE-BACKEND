from db.database import SessionLocal


def fake_hash_password(password: str):  # TODO Delete
    return "fakehashed" + password


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
