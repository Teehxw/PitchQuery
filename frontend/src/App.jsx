
/* Import Libraries */
import React from 'react';
import {useState} from 'react';

import './App.css';

/* Main App function */
function App() {

  // State Variables
  const [inputMess, setInputMess] = useState("") // inputMess is the current text in the input field, setInputMess is the function that is used to change i 
  const [loading, setLoading] = useState(false); // this is a boolean that is used to show the loading indicator when the user clicks the send button. Starts at False

  // Results
  const [results, setResults] = useState(null); // Before any quesiton is asked, results is null. After the backend replies, results will be an objects with rows and columns 

  // The function where everything happens when the user clicks the send button
  // Sends the question to the backend
  const handleClick = async () => {   // asyns is used when the function has to wait for a response in which for this case its waiting for a response from the backend 'await'
    setLoading(true);  // Show loading indicator

    // fetch the repsonse from the backend
   const response = await fetch('http://localhost:8000/query', { //sends a request to the FastAPI backend. await means to wait until the backend responds before moving on the next line of code
      method:"POST",    // Sending a question to the backend so "POST" is used
      headers: {"Content-Type": "application/json"},    // Tells the backend that the data is sent in JSON format
      body: JSON.stringify({ question: inputMess})    // The actual question being sent. JSON.stringify() converts the JavaScript object into a JSON string
                                                      // { question: "Who won in 2010?"} is the object being sent to the backend. The key is "question" and the value is the current text in the input field (inputMess)
    });

    // Save the response from the backend
    const data = await response.json();  // convert to JavaScript object

    // Save the results into react state
    setResults(data);
    setInputMess(""); // Clear the input field after sending
    setLoading(false);  // Hide loading indicator

  };

  return (
  <div className="App"> {/* Main container of the APP */}
    <div className="header">
      <div className="badge">⚽ FIFA World Cup · 1930–2022</div> {/* Creating a badge or icon for the top */}
      <h1>PitchQuery</h1>
      <p className="subtitle">Ask anything about World Cup history in plain English</p>

      {/* Example questions user can ask by clicking on them */}
      <div className="examples">
        {/* map loops through each question in the array and gives each a button */}
        {["Who scored the most goals ever?", "Which country has won the most?", "Top 5 goalscorers in 1998?"].map(q => (    
          <button key={q} className="example-pill" onClick={() => setInputMess(q)}>{q}</button>
        ))}
      <p className= "subtitle">Note: If an empty table is printed = no value </p>
      </div>
    </div>

    <div className="chat-input">

      {/* Input where the user enters the question */}
      <input className="input-field"
        type="text"
        placeholder="Ask a question about World Cup history..."
        value={inputMess}   /* the input value to the react state */
        onChange={(e) => setInputMess(e.target.value)} /* inputMess keeps updating everytime the user types something */

        onKeyDown={(e) => e.key === 'Enter' && handleClick()} /* is user presses enter then call the function handleClick() */
      />
      <button className="button" onClick={handleClick} disabled={loading}>  {/* button can't be pressed while loading */}
        {loading ? 'Thinking...' : 'Ask →'}   {/* if loading is true then show 'Thinking' otherwise 'Ask' */}
      </button>
    </div>

    {/* ---------------------  Display the results in a table if they exist ------------------------*/}
    {results?.rows && (    // 
      <table>   {/* creates the table */}
        <thead>   {/* this is the table headers */}
          <tr>  {/* loops through the column names from the backend and makes them the headers */}
            {results.columns.map((column) => (
              <th key={column}>{column}</th>
            ))}
          </tr>   {/* creates one table row */}
        </thead>
        {/* ----- Table body section ---- */}
        <tbody>
          {results.rows.map((row, rowIndex) => (  // Loop through each row of the result
            <tr key={rowIndex}>   {/* table row is created for each */}

              {/* Loop through each value inside that row */}
              {row.map((cell, cellIndex) => (
                <td key={cellIndex}>{cell}</td>   // Creates one table cell 
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    )}
  </div>
  );
}


// Run the function and dsiplay the page
export default App;
