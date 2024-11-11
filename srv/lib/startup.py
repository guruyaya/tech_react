import os
from lib.sqlite_connector import LiteCon

def db_startup() -> LiteCon:    
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if not os.path.isdir(f"{base_dir}/db"):
        os.mkdir(f"{base_dir}/db")

    conn = LiteCon.getInstance(f"{base_dir}/db/db.db")
    return conn
