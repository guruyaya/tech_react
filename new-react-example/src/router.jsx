import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'

export default function App() { // This demonstrates the fact that the name of a default export can be anything, and imported as anything

  return (
      <Router>
        <h1>
          <Link to="/">TODO App</Link>
        </h1>
        <main>
        <Routes>
          <Route path="/" element={<h2>Home</h2>} />
          <Route path="/:todo_id" element={<h2>TODO</h2>} />
          <Route path="/:todo_id/:item_id" element={<h2>Item</h2>} />
        </Routes>
        </main>
      </Router>
  )
}
