import Form from "./components/Form";
import QueryButton from "./components/QueryButton";
import Page from "./components/Page";
import React, {useState} from "react";

function App() {
  const [pages,setPages] = useState([]);
  const [artQuery,setArtQuery] = useState('');
  const [textQuery,setTextQuery] = useState('');

  function addPages(pages) {
    setPages(pages);
  }

  async function fetchArt(queryStr) {
    try {
      const response = await fetch('/art', {
        method: 'POST',
        body: JSON.stringify({
          query: queryStr,
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      });

      if (response.ok) {
        const jsonResp = await response.json();
        addPages(jsonResp);
      } 

    } catch(err) {
      console.log(err);
    }
  }

  async function fetchText(queryStr) {
    try {
      const response = await fetch('/text', {
        method: 'POST',
        body: JSON.stringify({
          query: queryStr,
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      });

      if (response.ok) {
        const jsonResp = await response.json();
        addPages(jsonResp);
      }
    
    } catch(err) {
      console.log(err);
    }
  }

  async function fetchScript(charsQuery,textQuery) {
    try {
      const response = await fetch('/dialogue', {
        method: 'POST',
        body: JSON.stringify({
          characters: charsQuery,
          text: textQuery
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      });

      if (response.ok){
        const jsonResp = await response.json();
        addPages(jsonResp);
      }

    } catch(err) {
      console.log(err);
    }

  }

  const pageList = pages.map((page) => (
    <Page
      number={page.number}
      date={page.date}
      url={page.url} 
      title={page.title} 
    />
  ));

  let resultsSentence = "";
  if (pageList.length !== 0){
    resultsSentence = "Got " + pageList.length + " results from query";
  }

  return (
    <div className="App stack-large">
    <div class="topnav">
      <a href="./about">About</a>
    </div>
     <h1 className="label-wrapper"> Twokinds Codex </h1>
     <Form addPages={addPages} fetch={fetchArt} title={"Art search"}
         query={artQuery} setQuery={setArtQuery}/>
     <Form addPages={addPages} fetch={fetchText} title={"Textual search"} 
         query={textQuery} setQuery={setTextQuery}/>
     <QueryButton fetch={fetchScript} chars={artQuery} text={textQuery}/>
     <p> {resultsSentence} </p>
    <ul>
      {pageList}
     </ul>
    </div>
    
  );
}

export default App;
