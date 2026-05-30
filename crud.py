from sqlalchemy.orm import Session
from . import models, schemas

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_people(db: Session):
    return db.query(models.Person).all()


def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def delete_person(db: Session, person_id: int):
    person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if person:
        db.delete(person)
        db.commit()
    return person