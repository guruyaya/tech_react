import { useEffect } from "react"
import todosListSignal, {getTodos, clearTodos} from "../../signals/todos"
import { Link } from 'react-router-dom'

export function TodoList({todos}) {
    return <ul>
        {todos.map((todo) => <li key={todo.id}>
            <Link to={`/${todo.id}`}>{todo.name}</Link>
        </li>)}
    </ul>
}

export default function TodoHome() {
    useEffect(() => {
        getTodos()
        
        return clearTodos
    }, [])

    const todos = todosListSignal.useStateAdapter()
    return todos.value ? <TodoList todos={todos.value} /> : <h3>Wait...</h3>
}
