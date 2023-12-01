from src.database.models import Films
from src.database.db_manager import db_manager


def get(FilmsID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Films WHERE ID = ?''', args=(FilmsID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Films''', fetchall=True)

def new(data: Films) -> dict:
    return db_manager.execute(query='''INSERT INTO Films(ID, relyear, runtime, name) VALUES (?, ?, ?, ?)''', args=(data.ID, data.relyear, data.runtime, data.name))

def update(FilmsID: int, new_data: Films) -> dict:
    return db_manager.execute(query='''UPDATE Films SET (ID, relyear, runtime, name) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.relyear, new_data.runtime, new_data.name, FilmsID))

def delete(FilmsID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Films WHERE ID = ?''', args=(FilmsID,))