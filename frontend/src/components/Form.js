import React, {useState} from "react";


function Form(props){
  //const [query,setQuery] = useState('');
  function handleSubmit(e) {
    e.preventDefault();
    props.fetch(props.query)
  }
  function handleChange(e) {
    props.setQuery(e.target.value);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="new-todo-input" className="label__lg"> 
        {props.title}
      </label>
      <input type="text"
        id="query-id"
        name="text"
        className="input input__lg"
        value={props.query}
        onChange = {handleChange}
        autoComplete="on"
      />
      <button type="submit" className="btn btn__primary btn__lg">
       Query
      </button>

    </form>
  )
}

export default Form;
