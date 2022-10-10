import React, {useState} from "react";


function Form(props){
  async function fetchPost(queryStr) {
    const response = await fetch('/art', {
      method: 'POST',
      body: JSON.stringify({
        query: queryStr,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      }
    });
    const jsonResp = await response.json();
    props.addPages(jsonResp)
  }

  const [query,setQuery] = useState('');
  function handleSubmit(e) {
    e.preventDefault();
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
      <button type="submit" className="btn btn__primary btn__lg">
      Query
      </button>

    </form>
  )
}

export default Form;
