from fastapi import APIRouter
from src.server.resolvers import user
from src.database.models import Users

rout = APIRouter(prefix='/users', tags=["Users"])


@rout.get(path='/get/{userID}', response_model=dict)
def get_type(userID: int) -> dict:
    return user.get(userID=userID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return user.get_all()


@rout.post(path='/new', response_model=dict)
def new_type(data: Users) -> dict:
    return user.new(data=data)


@rout.put(path='/update/{userID}', response_model=dict)
def update_type(data: Users, userID: int) -> dict:
    return user.update(userID=userID, new_data=data)


@rout.delete(path='/delete/{userID}', response_model=dict)
def delete_type(userID: int) -> dict:
    return user.delete(userID=userID)