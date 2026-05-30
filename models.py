from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)

    gender = Column(String)

    name = Column(JSON)
    location = Column(JSON)

    email = Column(String)
    dob = Column(JSON)
    registered = Column(JSON)

    phone = Column(String)
    cell = Column(String)

    id_info = Column(JSON)

    picture = Column(JSON)

    nat = Column(String)
