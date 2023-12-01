from src.database.models import Actors
from src.database.db_manager import db_manager

def get(ActorsID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Actors WHERE ID = ?''', args=(ActorsID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Actors''', fetchall=True)

def new(data: Actors) -> dict:
    return db_manager.execute(query='''INSERT INTO Actors(ID, peopleID, filmID) VALUES (?, ?, ? )''', args=(data.ID, data.peopleID,  data.filmID ))

def update(ActorsID: int, new_data: Actors) -> dict:
    return db_manager.execute(query='''UPDATE Actors SET (ID, peopleID, filmID) = (?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.peopleID, new_data.filmID, ActorsID ))

def delete(ActorsID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Actors WHERE ID = ?''', args=(ActorsID,))