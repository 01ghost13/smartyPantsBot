import os
import psycopg2 as pg


class Database:
    _database_url = os.environ['DATABASE_URL']

    def __init__(self):
        self._connection = pg.connect(self._database_url)

    def connect(self):
        return self._connection

    def prepare(self, query):
        return self._connection.prepare(query)

    def __del__(self):
        self.__close_connection__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__close_connection__()

    def __close_connection__(self):
        if self._connection is None:
            return
        self._connection.close()
        self._connection = None
