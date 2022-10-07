import React, {useState} from "react";

async function fetchPost(query) {
  const response = await fetch('/art', {
    method: 'POST',
    body: JSON.stringify({
      body: query,
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    }
  });
  const jsonResp = await response.json();
  console.log(jsonResp);
}

function Form(props){
  const [query,setQuery] = useState('');
  function handleSubmit(e) {
    e.preventDefault();
    console.log(query);
    fetchPost(query)
    setQuery("");
  }
  function handleChange(e) {
    setQuery(e.target.value);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label> Insert your query </label>
      <input type="text"
        id="query-id"
        name="text"
        value={query}
        onChange = {handleChange}
      />
    </form>
  )
}

export default Form;
