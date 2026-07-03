import React from 'react';
import {useState} from 'react';

import './App.css';

function App() {
  const [inputMess, setInputMess] = useState("")

  const [messages, setMessages] = useState([]);

  const handleClick = () => {
    alert('You typed: ' + inputMess);
  }

  return (
    <div className= "App">
      <h1>Pitch Query</h1>
      <h2> Search through the World Cup History</h2>
      <div className="chat-input">
        <input
          type = "text"
          placeholder = "Type your query here..."
          value = {inputMess}
          onChange = {(e) => setInputMess(e.target.value)} />
        <button className="button" onClick={handleClick}>Send</button> 
      </div>

    </div>
  );
}

export default App;
