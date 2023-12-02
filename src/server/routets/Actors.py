from fastapi import APIRouter
from src.server.resolvers import Actor
from src.database.models import Actors

rout = APIRouter(prefix='/actors', tags=["Actors"])


@rout.get(path='/get/{actorsID}', response_model=dict)
def get_actor(actorsID: int) -> dict:
    return Actor.get(ActorsID=actorsID)


@rout.get(path='/get', response_model=dict)
def get_all_actors() -> dict:
    return Actor.get_all()


@rout.post(path='/new', response_model=dict)
def new_actor(data:Actors) -> dict:
    return Actor.new(data=data)


@rout.put(path='/update/{actorsID}', response_model=dict)
def update_actor(data: Actors, actorsID: int) -> dict:
    return Actor.update(ActorsID=actorsID, new_data=data)


@rout.delete(path='/delete/{actorsID}', response_model=dict)
def delete_actor(actorsID: int) -> dict:
    return Actor.delete(ActorsID=actorsID)