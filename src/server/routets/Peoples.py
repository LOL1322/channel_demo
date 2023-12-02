from fastapi import APIRouter
from src.server.resolvers import People
from src.database.models import Peoples

rout = APIRouter(prefix='/peoples', tags=["Peoples"])


@rout.get(path='/get/{peoplesID}', response_model=dict)
def get_people(peoplesID: int) -> dict:
    return People.get(PeoplesID=peoplesID)


@rout.get(path='/get', response_model=dict)
def get_all_peoples() -> dict:
    return People.get_all()


@rout.post(path='/new', response_model=dict)
def new_people(data: Peoples) -> dict:
    return People.new(data=data)


@rout.put(path='/update/{peoplesID}', response_model=dict)
def update_people(data: Peoples, peoplesID: int) -> dict:
    return People.update(PeoplesID=peoplesID, new_data=data)


@rout.delete(path='/delete/{peoplesID}', response_model=dict)
def delete_people(peoplesID: int) -> dict:
    return People.delete(PeoplesID=peoplesID)
