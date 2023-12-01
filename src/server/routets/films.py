from fastapi import APIRouter
from src.server.resolvers import Film
from src.database.models import Films

rout = APIRouter(prefix='/films', tags=["Films"])


@rout.get(path='/get/{filmsID}', response_model=dict)
def get_type(filmsID: int) -> dict:
    return Film.get(FilmsID=filmsID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return Film.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: Films) -> dict:
    return Film.new(data=data)


@rout.put(path='/update/{filmsID}', response_model=dict)
def update_type(data: Films, filmsID: int) -> dict:
    return Film.update(FilmsID=filmsID, new_data=data)


@rout.delete(path='/delete/{filmsID}', response_model=dict)
def delete_type(filmsID: int) -> dict:
    return Film.delete(FilmsID=filmsID)
