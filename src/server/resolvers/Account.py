from src.database.models import Accounts
from src.database.db_manager import db_manager

def get(AccountsID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Accounts WHERE ID = ?''', args=(AccountsID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Accounts''', fetchall=True)

def new(data: Accounts) -> dict:
    return db_manager.execute(query='''INSERT INTO Accounts(ID, userID, login, password) VALUES (?, ?, ?, ?)''', args=(data.ID, data.userID, data.login, data.password))

def update(AccountsID: int, new_data: Accounts) -> dict:
    return db_manager.execute(query='''UPDATE Accounts SET (ID, userID, login, password) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.userID, new_data.login, new_data.password, AccountsID))

def delete(AccountsID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Accounts WHERE ID = ?''', args=(AccountsID,))