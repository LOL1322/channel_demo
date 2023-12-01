from src.database.models import Users
from src.database.db_manager import db_manager


def get(userID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Users WHERE ID = ?''', args=(userID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Users''', fetchall=True)

def new(data: Users) -> dict:
    return db_manager.execute(query='''INSERT INTO Users(ID, typeID, fio, phone) VALUES (?, ?, ?, ?)''', args=(data.ID, data.typeID, data.fio, data.phone))

def update(userID: int, new_data: Users) -> dict:
    return db_manager.execute(query='''UPDATE Users SET (ID, typeID, fio, phone) = (?, ?, ?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.typeID, new_data.fio, new_data.phone, userID))

def delete(userID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM TypesUsers WHERE ID = ?''', args=(userID,))