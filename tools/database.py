import os
import psycopg2 as pg


class Database:
    _database_url = os.environ['DATABASE_URL']
    _connection = pg.connect(_database_url)

    @staticmethod
    def connect():
        return Database._connection

    @staticmethod
    def prepare(query):
        return Database._connection.prepare(query)
