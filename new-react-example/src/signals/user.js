import { createSignal } from 'react-use-signals';
import raiseError from './error';

import httpClient from '../lib/http_client';

const userSignal = createSignal(null);

export function checkLogin() {
    httpClient.get("/me").then(response => {
        userSignal.value = response.data
    }).catch(e => {
        if (e.response?.status == 401) {
            userSignal.value = {"logged_in": false, "username": null}
        }else{
            raiseError("Error Logging In", e)
        }
    })
}

export function runLogIn(username, password) {
    httpClient.post("/login", {username, password}, true).then(
        response => {
            userSignal.value = response.data
        }
    )
}
export default userSignal;

