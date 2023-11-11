from pydantic import BaseModel

class TypesUsers(BaseModel):
    type: str
    access_level: int

