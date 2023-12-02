from fastapi import APIRouter
from src.server.resolvers import FilmCountrie
from src.database.models import FilmsCountrie

rout = APIRouter(prefix='/filmsCountrie', tags=["FilmsCountrie"])


@rout.get(path='/get/{filmsCountrieID}', response_model=dict)
def get_filmsCountrie(filmsCountrieID: int) -> dict:
    return FilmCountrie.get(FilmsCountrieID=filmsCountrieID)


@rout.get(path='/get', response_model=dict)
def get_all_filmsCountries() -> dict:
    return FilmCountrie.get_all()


@rout.post(path='/new', response_model=dict)
def new_filmsCountrie(data: FilmsCountrie) -> dict:
    return FilmCountrie.new(data=data)


@rout.put(path='/update/{filmsCountrieID}', response_model=dict)
def update_filmsCountrie(data:FilmsCountrie, filmsCountrieID: int) -> dict:
    return FilmCountrie.update(FilmsCountrieID=filmsCountrieID, new_data=data)


@rout.delete(path='/delete/{filmsCountrieID}', response_model=dict)
def delete_filmsCountrie(filmsCountrieID: int) -> dict:
    return FilmCountrie.delete(FilmsCountrieID=filmsCountrieID)
