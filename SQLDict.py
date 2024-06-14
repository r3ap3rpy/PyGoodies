from collections.abc import MutableMapping
from contextlib import suppress
from operator import itemgetter
import sqlite3

class SQLDict(MutableMapping):
    def __init__(self, dbname, items = [], **kwargs):
        self.dbname = dbname
        self.connection = sqlite3.connect(self.dbname)
        self.cursor = self.connection.cursor()

        with suppress(sqlite3.OperationalError):
            self.cursor.execute("CREATE TABLE Dict (key text, value text)")
            self.cursor.execute("CREATE UNIQUE INDEX Kndx ON Dict (key)")
        self.update(items, **kwargs)

    def __getitem__(self, key):
        try:
            key = [ _ for _ in self.cursor.execute(f"SELECT * FROM Dict WHERE key='{key}'")]
        except Exception as e:
            raise KeyError(key) from None

        if key:
            return key[0][1] # [(key, value)]
        else:
            raise KeyError(key) 

    def __setitem__(self, key, value):
        try:
            mkey = [ _ for _ in self.cursor.execute(f"SELECT * FROM Dict WHERE key='{key}'")]
        except:
            mkey = []

        if mkey:
            self.cursor.execute(f"UPDATE Dict SET value='{value}' WHERE key='{key}'")
        else:
            self.cursor.execute(f"INSERT INTO Dict VALUES('{key}','{value}')")

        self.connection.commit()

    def __len__(self):
        return len([_ for _ in self.cursor.execute("SELECT * FROM Dict")])

    def __iter__(self):
        return [ _ for _ in self.cursor.execute("SELECT * FROM Dict")]

    def __delitem__(self, key):
        self.cursor.execute(f"DELETE FROM Dict WHERE key='{key}'")
        self.connection.commit()

    def show_data(self):
        for row in self.cursor.execute("SELECT * FROM Dict"):
            print(row)
