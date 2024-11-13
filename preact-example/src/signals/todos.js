import { signal } from "@preact/signals";
import httpClient from '../lib/http_client';
import raiseError from './error';

const todosListSignal = signal(null);

export function getTodos() {
    httpClient.get("/todo/").then((response) => {
        todosListSignal.value = response.data
    }).catch((e) => {
        raiseError("Error Loading list", e)
    })
}

export function clearTodos () {
    todosListSignal.value = null
}
export default todosListSignal