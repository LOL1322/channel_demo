from src.database.models import FilmsCountrie
from src.database.db_manager import db_manager

def get(FilmsCountrieID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM FilmsCountries WHERE ID = ?''', args=(FilmsCountrieID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM FilmsCountries''', fetchall=True)

def new(data: FilmsCountrie) -> dict:
    return db_manager.execute(query='''INSERT INTO FilmsCountries(ID, countryID, filmID) VALUES (?, ?, ?)''', args=(data.ID, data.countryID, data.filmID ))

def update(FilmsCountrieID: int, new_data: FilmsCountrie) -> dict:
    return db_manager.execute(query='''UPDATE FilmsCountries SET (ID, countryID, filmID) = (?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.countryID, new_data.filmID, FilmsCountrieID))

def delete(FilmsCountrieID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM FilmsCountries WHERE ID = ?''', args=(FilmsCountrieID,))