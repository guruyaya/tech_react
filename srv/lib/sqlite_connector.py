import sqlite3

class LiteCon():
    @classmethod
    def getInstance(cls, filename=None):
        if not hasattr(cls, 'instance'):
            if filename is None:
                raise Exception('Filename is required')
            cls.instance = super().__new__(cls)
            cls.instance.__init__(filename)
        return cls.instance
    
    def __init__(self, filename):
        self.con = sqlite3.connect(filename, check_same_thread=False)
        self.cur = self.con.cursor()


