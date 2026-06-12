import React, { useState } from "react";

function App() {

  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  // Add Todo
  const addTodo = () => {
    if (input.trim() === "") return;
    setTodos([...todos, input]);
    setInput("");
  };

  // Delete Todo
  const deleteTodo = (indexToDelete) => {

    const updatedTodos = todos.filter(
      (todo, index) => index !== indexToDelete
    );

    setTodos(updatedTodos);

  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Todo List</h1>

      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={addTodo}>Add</button>

      <ul>

        {todos.map((todo, index) => (

          <li key={index}>

            {todo}

            <button
              onClick={() => deleteTodo(index)}
              style={{ marginLeft: "10px" }}
            >
              Delete
            </button>

          </li>

        ))}

      </ul>

    </div>
  );
}

export default App;
