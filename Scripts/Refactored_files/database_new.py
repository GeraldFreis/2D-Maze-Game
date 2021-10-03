import sqlite3 as sq
from new_tkinter_input import level, name

"""Creating Globals"""

db_level = level
db_name = name

class Database():  # creating the database
    def __init__(self):
        self.db = sq.connect("player_database.db")
        self.cursor = self.db.cursor()
        # self.db.execute("create table names(name, level)")  #commented out because the database has been created
    
    def adding_data_for_new_player(self, name, level):  # adding information for new players
        sq_insert = """INSERT INTO names (name, level) VALUES (?, ?);"""
        data = name, level
        self.db.execute(sq_insert, data)
        self.db.commit()
        print("Hi {} your level of: {} will now be played".format(name, level))
    
    def retrieve_data_for_returned_player(self, name):  # retrieving information for existing players
        names = list(self.cursor.execute("""SELECT * FROM names {}""".format(name)))
        names.sort(reverse=True)
        refined_list = names[0]
        latest_level = refined_list[1]
        print("Your latest level played is {}".format(str(latest_level)))
        return latest_level


db = Database()
db.adding_data_for_new_player(db_name, db_level)
db.retrieve_data_for_returned_player(db_name)
