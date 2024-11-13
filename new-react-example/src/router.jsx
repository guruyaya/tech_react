import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'
import TodoHome from './app/home'
import Todo from './app/todo/index'

export default function App() { // This demonstrates the fact that the name of a default export can be anything, and imported as anything

  return (
      <Router>
        <h1>
          <Link to="/">TODO App</Link>
        </h1>
        <main>
        <Routes>
          <Route path="/" element={<TodoHome />} />
          <Route path="/:todo_id" element={<Todo />} />
          <Route path="/:todo_id/:item_id" element={<h2>Item</h2>} />
        </Routes>
        </main>
      </Router>
  )
}
