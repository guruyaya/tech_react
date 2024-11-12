from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Response
from lib.login_cookie import cookieChecker
from lib.startup import db_startup
from fastapi.security import OAuth2PasswordRequestForm

from app.todo.urls import router as todo_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = db_startup()

    # Load the ML model
    conn.cur.execute("""CREATE TABLE IF NOT EXISTS todo 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     name TEXT, description TEXT)""")
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

app.include_router(todo_router)

@app.get("/me")
def read_root(user: dict[str, bool]=Depends(cookieChecker.check_login_cookie)):   
    return user

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
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)