import sqlite3 as sq
import pandas as pd
from new_tkinter_input import name, level

db_name = name
db_level = level


class Database:
    def __init__(self):
        self.db = sq.connect('database.db')
        # self.db.execute("create table names(name, level)")  #commented out because the database has been created
        self.db.cursor()
        self.cur = self.db.cursor()

    """
    Checking if name exists and if not adding the name into the table
    """

    def retrieve(self, name, level):
        self.cur.execute("""SELECT * FROM names""")
        name_ = self.cur.fetchone()
        if name in name_:
            print(self.db)
            print('Your name: {} is already in the database with level {} in it'.format(name, str(level)))
            return level + 1
        else:
            sq_insert = """INSERT INTO names (name, level) VALUES (?, ?);"""
            data = name, level
            self.db.execute(sq_insert, data)
            self.db.commit()
            self.db.close()
            lev = str(level)
            print('Adding {} and your level {} to the database'.format(name, lev))
        return name, level
    
    def retrieve_iterate(self, name, level):
        query = """SELECT Gerald FROM names"""
        dataframe = pd.read_sql_table(self.db, query)
        print(dataframe)


db = Database()
db.retrieve(db_name, db_level)
db.retrieve_iterate
