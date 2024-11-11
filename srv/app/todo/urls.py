from fastapi import APIRouter

from lib.sqlite_connector import LiteCon
from app.todo.schemas import Todo, TodoInput, TodoItem, TodoItemInput, FullTodo, Message

router = APIRouter(prefix='/todo', tags=['todo'])

@router.get('/')
def list_todos() -> list[Todo]:
    conn = LiteCon.getInstance()
    conn.cur.execute('SELECT id, name, description FROM todo')
    return Todo.from_fetchall(conn)

@router.post('/')
def create_todo(todo: TodoInput) -> Todo:
    conn = LiteCon.getInstance()
    conn.cur.execute('INSERT INTO todo (name, description) VALUES (?, ?)', (todo.name, todo.description))
    conn.con.commit()
    return Todo(**todo.model_dump(), id=conn.cur.lastrowid)

@router.get('/{todo_id}')
def get_todo(todo_id: int) -> FullTodo:
    conn = LiteCon.getInstance()
    conn.cur.execute('SELECT id, name, description FROM todo WHERE id = ?', (todo_id,))
    todo = Todo.from_fetchall(conn)[0]
    conn.cur.execute('SELECT id, todo_id, name, description, status FROM todo_item WHERE todo_id = ?', (todo_id,))
    items = TodoItem.from_fetchall(conn)

    return FullTodo(id=todo.id, name=todo.name, description=todo.description, items=items)

@router.post('/{todo_id}')
def new_todo_item(todo_id: int, item: TodoItemInput) -> TodoItem:
    conn = LiteCon.getInstance()
    conn.cur.execute('INSERT INTO todo_item (todo_id, name, description) VALUES (?, ?, ?)', (todo_id, item.name, item.description))
    conn.con.commit()
    return TodoItem(**item.model_dump(), id=conn.cur.lastrowid, todo_id=todo_id)

@router.post('/{todo_id}/{item_id}')
def update_todo_item(todo_id: int, item_id: int, item: TodoItemInput) -> TodoItem:
    conn = LiteCon.getInstance()
    conn.cur.execute('UPDATE todo_item SET name = ?, description = ? WHERE id = ?', (item.name, item.description, item_id))
    conn.con.commit()
    return TodoItem(**item.model_dump(), id=item_id)

@router.post('/{todo_id}/{item_id}/status')
def update_todo_item_status(todo_id: int, item_id: int, status: int) -> Message:
    conn = LiteCon.getInstance()
    conn.cur.execute('UPDATE todo_item SET status = ? WHERE id = ?', (status, item_id))
    conn.con.commit()
    return Message(message='Updated', success=True)
