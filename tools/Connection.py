import os
import sqlite3


class Connection:
    _conn = sqlite3.connect(os.path.dirname(__file__) + '\\..\\database\\database.sqlite')

    @staticmethod
    def get():
        return Connection._conn
