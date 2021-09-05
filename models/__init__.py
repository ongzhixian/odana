import sqlite3


class Ada():
    
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        pass
        
    def aa(self):
        c = self.conn.cursor()

        # Create table
        c.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        self.conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.conn.close()