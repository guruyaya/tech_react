import { forwardRef } from "react"

function TodoDescrption({todo}, ref) {
    
    return <div><textarea ref={ref} defaultValue={todo.description} /></div>
}

export default forwardRef(TodoDescrption)