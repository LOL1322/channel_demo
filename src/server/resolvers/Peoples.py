from src.database.models import Peoples
from src.database.db_manager import db_manager

def get(PeoplesID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Peoples WHERE ID = ?''', args=(PeoplesID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Peoples''', fetchall=True)

def new(data: Peoples) -> dict:
    return db_manager.execute(query='''INSERT INTO Peoples(ID, name) VALUES (?, ?)''', args=(data.ID, data.name))

def update(PeoplesID: int, new_data: Peoples) -> dict:
    return db_manager.execute(query='''UPDATE Peoples SET (ID, name) = (?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.name, PeoplesID))

def delete(PeoplesID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Peoples WHERE ID = ?''', args=(PeoplesID,))