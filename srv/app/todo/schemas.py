from __future__ import annotations

from typing_extensions import Self
from pydantic import BaseModel

from srv.lib.sqlite_connector import LiteCon

class TodoInput(BaseModel):
    name: str
    description: str

class Todo(TodoInput):
    id: int

    @staticmethod
    def from_db_row(tup:tuple):
        return Todo(id=tup[0], name=tup[1], description=tup[2])
        
    @staticmethod
    def from_fetchall(conn: LiteCon) -> list[Todo]: 
        return [Todo.from_db_row(t) for t in conn.cur.fetchall()]

class TodoItemInput(BaseModel):
    name: str
    description: str    

class TodoItem(TodoItemInput):
    todo_id: int
    id: int
    status: int = 0

    @staticmethod
    def from_db_row(tup:tuple):
        return TodoItem(id=tup[0], todo_id=tup[1], name=tup[2], description=tup[3], status=tup[4] or False)
        
    @staticmethod
    def from_fetchall(conn: LiteCon) -> list[Todo]: 
        return [TodoItem.from_db_row(t) for t in conn.cur.fetchall()]

class FullTodo(Todo):
    items: list[TodoItem]

class Message(BaseModel):
    message: str
    success: bool = True