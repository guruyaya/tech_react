import {useRef} from 'react'
import { runLogIn } from './signals/user'

export default function LoginPage() {
    const formRefs = {
        username: useRef(null),
        password: useRef(null)
    }

    function logIn() {
        runLogIn(formRefs.username.current.value, formRefs.password.current.value)
    }
    
    return <>
    <h1>Lets login</h1>
    <main>
        <h2>Login form</h2>
        <form>
            <br />
            <div>
                <label htmlFor="username">Username</label>
                <input type="text" ref={formRefs.username} />
            </div>

            <div>
                <label htmlFor="password">Password</label>
                <input type="password" ref={formRefs.password} />
            </div>
            <button type="button" onClick={logIn}>Log In</button>
        </form>
    </main>
    </>
}