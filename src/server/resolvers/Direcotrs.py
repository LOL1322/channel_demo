from src.database.models import Directors
from src.database.db_manager import db_manager

def get(DirectorsID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Directors WHERE ID = ?''', args=(DirectorsID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Directors''', fetchall=True)

def new(data: Directors) -> dict:
    return db_manager.execute(query='''INSERT INTO Directors(ID, peopleID, filmID) VALUES (?, ?, ?)''', args=(data.ID, data.peopleID, data.filmID))

def update( DirectorsID: int, new_data:  Directors) -> dict:
    return db_manager.execute(query='''UPDATE  Directors SET (ID, peopleID, filmID) = (?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.peopleID, new_data.filmID, DirectorsID))

def delete(DirectorsID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Directors WHERE ID = ?''', args=(DirectorsID,)) 