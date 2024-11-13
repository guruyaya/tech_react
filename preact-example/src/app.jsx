import './App.scss'
import Router from './router'
import { ErrorBoundary } from "react-error-boundary";
import { ErrorPage, Wait } from './components'
import userSignal, {checkLogin} from './signals/user';
import { useEffect } from 'react';
import { errorSignal } from './signals/error';
import Login from './login'
// The files created by vite have a first capital letter. This is not a good practice, as it may cause windows / linux differences. 
// Use only lowercase letters and numbers in file names other than those created by vite.

function App() {
  const user = userSignal
  const error = errorSignal

  useEffect(() => {
    checkLogin()
  }, [])

  useEffect(() => {
      console.error(error.value)
  }, [error.value])

  return (
    <ErrorBoundary FallbackComponent={ErrorPage}>{
      (error.value) ? <ErrorPage /> : 
        (user.value === null) ? <Wait /> : 
          (user.value.logged_in) ? <Router /> :
        <Login />
    }</ErrorBoundary>
  )
}


export default App
