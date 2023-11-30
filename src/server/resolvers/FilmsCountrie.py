from src.database.models import FilmsCountrie
from src.database.db_manager import db_manager

def get(FilmsCountrieID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM FilmsCountrie WHERE ID = ?''', args=(FilmsCountrieID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM FilmsCountrie''', fetchall=True)

def new(data: FilmsCountrie) -> dict:
    return db_manager.execute(query='''INSERT INTO FilmsCountrie(ID, countryID, filmID) VALUES (?, ?, ?)''', args=(data.ID, data.countryID, data.filmID ))

def update(FilmsCountrieID: int, new_data: FilmsCountrie) -> dict:
    return db_manager.execute(query='''UPDATE FilmsCountrie SET (ID, countryID, filmID) = (?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.countryID, new_data.filmID, FilmsCountrieID))

def delete(FilmsCountrieID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM FilmsCountrie WHERE ID = ?''', args=(FilmsCountrieID))