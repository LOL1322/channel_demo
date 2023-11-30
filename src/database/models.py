from pydantic import BaseModel

class TypesUsers(BaseModel):
    ID: int
    type: str
    access_level: int

class Users(BaseModel):
    ID: int
    typeID: int
    fio: str
    phone: str

class Courients(BaseModel):
    ID: int
    name: str

class films(BaseModel):
    ID: int
    relyear: str
    runtime: str
    name: str

class FilmsCountrie(BaseModel):
    ID: int
    countryID: int
    filmID: int

class Accounts(BaseModel):
    ID: int
    userID:int

class Peoples(BaseModel):
    ID: int
    name: str

class Directors(BaseModel):
    ID: int
    peopleID: int
    filmID: int

class Actors(BaseModel):
    ID: int
    peopleID: int
    filmID: int


    

