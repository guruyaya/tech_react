import { useEffect, useRef } from "react";
import TodoSignal, { clearSingleTodo, getTodo, updateTodo, updateTodoItem, updateTodoItemStatus } from "../../signals/single_todo";
import TodoDescription from "./todo_description";

export function Todo({todo, id}) {
    const formRef = {
        name: useRef(null),
        description: useRef(null),
    }
    const newItem = useRef(null)

    const saveDescrption = () => {
        updateTodo(id, {
            name: formRef.name.current.value,
            description: formRef.description.current.value
        })
    }
    
    function changeTodoItem (e) {
        if(e.key == "Enter") {
            updateTodoItem(id, newItem.current.value).then(() => {
                newItem.current.value = ''
            })
        }
    }
    
    function setStatus(item_id, status, index) {
        updateTodoItemStatus(id, item_id, status, index)
    }
    
    useEffect(() => {
        console.log(todo.items.map(a=> a))
    }, [todo])
    return <>
        <h2><input defaultValue={todo.name}  ref={formRef.name} /></h2>
        <div style={{padding: '30px'}}>
            <TodoDescription todo={todo} ref={formRef.description} />
            <input type="button" value="save" onClick={saveDescrption} />
        </div>
        <ul>
            {todo.items.map((item, index) => <li key={item.id}>
                <input type="checkbox" defaultChecked={item.status == 1} 
                    onChange={(e) => setStatus(item.id, e.target.checked ? 1: 0, index)}
                />
                <b>{item.name}</b>
            </li>)}
            <li><input type="text" ref={newItem} onKeyDown={changeTodoItem}/></li>
        </ul>
    </>
}
export default function TodoWrapper({todo_id}) {
    const todo = TodoSignal

    useEffect(() => {
        getTodo(todo_id)
        
        return clearSingleTodo
    }, [todo_id])

    return todo.value ? <Todo todo={todo.value} id={todo_id} /> : <h3>Wait...</h3>
}