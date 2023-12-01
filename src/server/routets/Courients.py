from fastapi import APIRouter
from src.server.resolvers import Countries
from src.database.models import Courients

rout = APIRouter(prefix='/courients', tags=["Courients"])


@rout.get(path='/get/{courientsID}', response_model=dict)
def get_type(courientsID: int) -> dict:
    return Countries.get(CourientsID=courientsID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return Countries.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: Courients) -> dict:
    return Countries.new(data=data)


@rout.put(path='/update/{courientsID}', response_model=dict)
def update_type(data: Courients, courientsID: int) -> dict:
    return Countries.update(CourientsID=courientsID, new_data=data)


@rout.delete(path='/delete/{courientsID}', response_model=dict)
def delete_type(courientsID: int) -> dict:
    return Countries.delete(CourientsID=courientsID)