import os
from typing import Annotated
from contextlib import asynccontextmanager

from lib.sqlite_connector import LiteCon
from fastapi import FastAPI, Depends, Response
from lib.login_cookie import cookieChecker
from fastapi.security import OAuth2PasswordRequestForm

@asynccontextmanager
async def lifespan(app: FastAPI):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isdir(f"{base_dir}/db"):
        os.mkdir(f"{base_dir}/db")
    
    # Load the ML model
    conn = LiteCon(f"{base_dir}/db/db.db")
    conn.cur.execute("""CREATE TABLE IF NOT EXISTS todo 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     name TEXT description TEXT)""")
    conn.cur.execute("""CREATE TABLE IF NOT EXISTS todo_item 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     todo_id INTEGER,
                     name TEXT, 
                     description TEXT,
                     status INTEGER,
                     FOREIGN KEY(todo_id) REFERENCES todo(id))""")
    
    conn.cur.execute("""CREATE INDEX IF NOT EXISTS todo_item_status_idx ON todo_item (status)""")

    conn.con.commit()
    
    yield
    conn.cur.close()
    conn.con.close()
    

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root(user: dict[str, bool]=Depends(cookieChecker.check_login_cookie)):   
    return {"Hello": "World"}

@app.post("/login")
def login(login: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response):
    if login.username == "not_secure" and login.password == "not_secure":
        cookieChecker.set_login_cookie(response=response)
        return {"message": "Login successful"}
    return {"message": "Login failed"}

@app.post("/logout")
def logout(response: Response, user: dict[str, bool]=Depends(cookieChecker.check_login_cookie)):
    cookieChecker.delete_cookie(response=response)
    return {"message": "Logout successful"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)