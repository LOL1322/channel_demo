from src.database.models import Courients
from src.database.db_manager import db_manager

def get(CourientsID: int) -> dict:
    return db_manager.execute(query='''SELECT * FROM Courients WHERE ID = ?''', args=(CourientsID,))

def get_all() -> dict:
    return db_manager.execute(query='''SELECT * FROM Courients''', fetchall=True)

def new(data: Courients) -> dict:
    return db_manager.execute(query='''INSERT INTO Courients(ID, name) VALUES (?, ?)''', args=(data.ID, data.name))

def update(CourientsID: int, new_data: Courients) -> dict:
    return db_manager.execute(query='''UPDATE Courients SET (ID, name) = (?, ?) WHERE ID = ?''', args=(new_data.ID, new_data.name, CourientsID))

def delete(CourientsID: int) -> dict:
    return db_manager.execute(query='''DELETE FROM Countries WHERE ID = ?''', args=(CourientsID,))