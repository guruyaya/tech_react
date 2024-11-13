import { errorSignal } from "./signals/error"

export function Wait() { 
    return (
      <div>
        <h1>Wait</h1>
      </div>
    )
}

export function ErrorPage() { // Jsx function must start with a capital letter
    const error = errorSignal;

    return <main>
        <h1>There was an error</h1>
        <h2>{error.value}</h2>
    </main>
}