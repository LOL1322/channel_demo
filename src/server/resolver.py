from src.database.models import TypesUsers
from src.database.db_manager import db_manager

def get(typeID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM TypesUsers WHERE ID = ?''', args=(typeID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM TypesUsers''', fetchall=True)

def new(data: TypesUsers) -> dict:
    return db_manager.execute(query='''INSERT INTO TypesUsers(type, access_level) VALUES (?, ?)''', args=(data.type, data.access_level))

def update(typeID: int, new_data: TypesUsers) -> dict:
    return db_manager.execute(query='''UPDATE TypesUsers SET (type, access_level) = (?, ?) WHERE ID = ?''', args=(new_data.type, new_data.access_level, typeID))

def delete(typeID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM TypesUsers WHERE ID = ?''', args=(typeID,))