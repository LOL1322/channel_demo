import sqlite3
import os
import sys

sys.path.append('..\demo_app\src')

import settings


class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def connect_db(self) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        return connection, cursor 
    
    def check_base(self) -> bool:
        return not os.path.exists(self.db_path)
    
    def create_base(self, scripts: tuple[str, str]) -> dict:
        conn, cur = self.connect_db()
        if not self.check_base():
            try:
                [cur.executescript(open(script).read()) for script in scripts]
                conn.commit()
                conn.close()
                return {'code': 200, 'msg': 'Succesfully', 'result': True}
            except sqlite3.Error as err:
                conn.close()
                return {'code': 400, 'msg': str(err), 'result': False}
            
    def execute(self, query: str, args: tuple = (), fetchall: bool = False) -> dict:
        conn, cur = self.connect_db()
        try:
            res = cur.execute(query, args)
            if fetchall:
                res = res.fetchall()
            else:
                res = res.fetchone()
            conn.commit()
            conn.close()
            return {'code': 200, 'msg': 'Succesfully', 'result': res}
        except sqlite3.Error as err:
            conn.close()
            return {'code': 400, 'msg': str(err), 'result': None}

        
db_manager = DBManager(db_path=settings.DB_PATH)
