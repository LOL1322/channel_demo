from fastapi import APIRouter
from src.server.resolvers import FilmCountrie
from src.database.models import FilmsCountrie

rout = APIRouter(prefix='/filmsCountrie', tags=["FilmsCountrie"])


@rout.get(path='/get/{filmsCountrieID}', response_model=dict)
def get_type(filmsCountrieID: int) -> dict:
    return FilmCountrie.get(FilmsCountrieID=filmsCountrieID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return FilmCountrie.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: FilmsCountrie) -> dict:
    return FilmCountrie.new(data=data)


@rout.put(path='/update/{filmsCountrieID}', response_model=dict)
def update_type(data:FilmsCountrie, filmsCountrieID: int) -> dict:
    return FilmCountrie.update(FilmsCountrieID=filmsCountrieID, new_data=data)


@rout.delete(path='/delete/{filmsCountrieID}', response_model=dict)
def delete_type(filmsCountrieID: int) -> dict:
    return FilmCountrie.delete(FilmsCountrieID=filmsCountrieID)
