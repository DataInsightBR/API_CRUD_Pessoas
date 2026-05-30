from pydantic import BaseModel
from typing import Dict, Any

class PersonCreate(BaseModel):
    gender: str
    name: Dict[str, Any]
    location: Dict[str, Any]
    email: str
    dob: Dict[str, Any]
    registered: Dict[str, Any]
    phone: str
    cell: str
    id_info: Dict[str, Any]
    picture: Dict[str, Any]
    nat: str


class PersonResponse(PersonCreate):
    id: int

    class Config:
        orm_mode = True