from fastapi import APIRouter
from src.server.resolvers import Account
from src.database.models import Accounts

rout = APIRouter(prefix='/accounts', tags=["Accounts"])


@rout.get(path='/get/{accountsID}', response_model=dict)
def get_type(accountID: int) -> dict:
    return Account.get(AccountsID=accountID)


@rout.get(path='/get', response_model=dict)
def get_all_types() -> dict:
    return Account.get_all()
    


@rout.post(path='/new', response_model=dict)
def new_type(data: Accounts) -> dict:
    return Account.new(data=data)


@rout.put(path='/update/{accountsID}', response_model=dict)
def update_type(data:Accounts, acountsID: int) -> dict:
    return Account.update(AccountsID=acountsID, new_data=data)


@rout.delete(path='/delete/{accountsID}', response_model=dict)
def delete_type(accountsID: int) -> dict:
    return Account.delete(AccountsID=accountsID)
