import React from 'react';
import {useState} from 'react';
import { useEffect } from 'react';
import './App.css';

function App() {
  const [name, setName] = useState("mario");

  const handleClick = () => {
    value = document.querySelector('.text-area').value;
    alert('You typed: ' + value);
  }

  return (
    <div className= "App">
      <h1>Pitch Query</h1>
      <h2> Search through the World Cup History</h2>
      <p> Welcome {name}!</p>
      <div className="chat-input">
        <form className="chat-input">
        <textarea className="text-area" placeholder="Type your query here..."></textarea>
        <button className="button" onClick={handleClick}>Send</button>
        </form>
      </div>

    </div>
  );
}

// function Greeting() {
//   const sayHi = (name, surname) => {
//     alert('Hello ' + name + ' ' + surname + '!')
//   }

//   return (
//     <div>
//       <button onClick={() => sayHi('John','Doe')} > Say Hi</button>
//     </div>
//   )
// }

export default App;
