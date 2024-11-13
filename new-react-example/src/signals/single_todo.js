import { createSignal } from 'react-use-signals';
import httpClient from '../lib/http_client';
import raiseError from './error';

const todosSignal = createSignal(null);

export function getTodo(id) {
    httpClient.get(`/todo/${id}`).then((response) => {
        console.log(response.data.items instanceof Array, response.data.items )
        todosSignal.value = response.data
    }).catch((e) => {
        raiseError("Error Loading ", e)
    })
}

export function updateTodo(id, data) {
    httpClient.put(`/todo/${id}`, data).then((response) => {
        todosSignal.value = response.data
    }).catch((e) => {
        raiseError("Error Loading ", e)
    })
}

export function clearSingleTodo () {
    todosSignal.value = null
}

export function updateTodoItem(id, name) {
    const data = {name, description: '', status: 0}
    return httpClient.post(`/todo/${id}`, data).then(({data}) => {
        todosSignal.value.items = [...todosSignal.value.items, data]
    }).catch((e) => {
        raiseError("Error Loading ", e)
    })
}

export function updateTodoItemStatus(todo_id, item_id, status, index) {
    return httpClient.post(`/todo/${todo_id}/${item_id}/status?status=${status}`, {}).then(() => {
        todosSignal.value.items[index].status = status;
    }).catch((e) => {
        raiseError("Error Loading ", e)
    })
}

export default todosSignal