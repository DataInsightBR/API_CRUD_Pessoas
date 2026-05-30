from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud, database, services

# 🚀 SINGLE APP (CORRETO)
#app = FastAPI(title="CRM SaaS API")

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

# 🌐 CORS (OBRIGATÓRIO PARA FRONTEND)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção: coloque domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🗄️ cria tabelas
models.Base.metadata.create_all(bind=database.engine)

# 🔌 DB dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 CREATE manual
@app.post("/people")
def create(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db, person)


# 🔹 AUTO CREATE (RandomUser BR)
@app.post("/people/random")
def create_random(db: Session = Depends(get_db)):
    data = services.fetch_random_user()
    person = schemas.PersonCreate(**data)
    return crud.create_person(db, person)


# 🔹 READ ALL
@app.get("/people")
def read_all(db: Session = Depends(get_db)):
    return crud.get_people(db)


# 🔹 READ ONE
@app.get("/people/{person_id}")
def read_one(person_id: int, db: Session = Depends(get_db)):
    return crud.get_person(db, person_id)


# 🔹 DELETE
@app.delete("/people/{person_id}")
def delete(person_id: int, db: Session = Depends(get_db)):
    return crud.delete_person(db, person_id)
