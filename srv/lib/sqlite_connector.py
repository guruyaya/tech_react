import sqlite3

class LiteCon():
    def __new__(cls, filename=None):
        if not hasattr(cls, 'instance'):
            if filename is None:
                raise Exception('Filename is required')
            cls.instance = super().__new__(cls)
            cls.instance.__init__(filename)
        return cls.instance
    
    def __init__(self, filename):
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()


