import React, {useState} from "react";


function QueryButton(props){
  //const [query,setQuery] = useState('');
  function handleSubmit(e) {
    e.preventDefault();
    props.fetch(props.chars,props.text)
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit" className="btn btn__primary btn__lg">
        Dialogue Query
      </button>

    </form>
  )
}

export default QueryButton;
