from fastapi import APIRouter
from src.server.resolvers import Direcotrs
from src.database.models import Directors

rout = APIRouter(prefix='/directors', tags=["Directors"])


@rout.get(path='/get/{directorsID}', response_model=dict)
def get_director(directorsID: int) -> dict:
    return Direcotrs.get(DirectorsID=directorsID)


@rout.get(path='/get', response_model=dict)
def get_all_directors() -> dict:
    return Direcotrs.get_all()


@rout.post(path='/new', response_model=dict)
def new_director(data: Directors) -> dict:
    return Direcotrs.new(data=data)


@rout.put(path='/update/{directorsID}', response_model=dict)
def update_director(data: Directors, directorsID: int) -> dict:
    return Direcotrs.update(DirectorsID=directorsID, new_data=data)


@rout.delete(path='/delete/{directorsID}', response_model=dict)
def delete_director(directorsID: int) -> dict:
    return Direcotrs.delete(DirectorsID=directorsID)
