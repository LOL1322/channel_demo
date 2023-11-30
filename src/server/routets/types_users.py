from fastapi import APIRouter
from src.server import resolver
from src.database.models import TypesUsers

rout = APIRouter(prefix='/types', tags=["TypesUsers"])


@rout.get(path='/get/{typeID}', response_model=dict)
def get_type(typeID: int) -> dict:
    return resolver.get(typeID=typeID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return resolver.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: TypesUsers) -> dict:
    return resolver.new(data=data)


@rout.put(path='/update/{typeID}', response_model=dict)
def update_type(data: TypesUsers, typeID: int) -> dict:
    return resolver.update(typeID=typeID, new_data=data)


@rout.delete(path='/delete/{typeID}', response_model=dict)
def delete_type(typeID: int) -> dict:
    return resolver.delete(typeID=typeID)
