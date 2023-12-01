from fastapi import APIRouter
from src.server.resolvers import types_user
from src.database.models import TypesUsers

rout = APIRouter(prefix='/types', tags=["TypesUsers"])


@rout.get(path='/get/{typeID}', response_model=dict)
def get_type(typeID: int) -> dict:
    return types_user.get(typeID=typeID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return types_user.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: TypesUsers) -> dict:
    return types_user.new(data=data)


@rout.put(path='/update/{typeID}', response_model=dict)
def update_type(data: TypesUsers, typeID: int) -> dict:
    return types_user.update(typeID=typeID, new_data=data)


@rout.delete(path='/delete/{typeID}', response_model=dict)
def delete_type(typeID: int) -> dict:
    return types_user.delete(typeID=typeID)
