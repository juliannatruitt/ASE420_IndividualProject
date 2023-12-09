# implements the singleton design pattern so that only one database can be created.
import sqlite3


class CreateConnection(object):

    __instance = None

    @staticmethod
    def get_instance():
        if CreateConnection.__instance is None:
            CreateConnection.__instance = CreateConnection()
        return CreateConnection.__instance

    def __init__(self):
        self._connect = sqlite3.connect("ver2_database.db")

    def get_connection(self):
        return self._connect

    def cursor(self):
        return self.get_connection().cursor()
