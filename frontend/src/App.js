import Form from "./components/Form";
import Page from "./components/Page";
import React, {useState} from "react";

function App() {
  const [pages,setPages] = useState([]);
  const [artQuery,setArtQuery] = useState('');
  const [charQuery,setCharQuery] = useState('');

  function addPages(pages) {
    setPages(pages);
  }

  async function fetchArt(queryStr) {
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
    addPages(jsonResp)
  }

  async function fetchText(queryStr) {
    const response = await fetch('/text', {
      method: 'POST',
      body: JSON.stringify({
        query: queryStr,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      }
    });
    const jsonResp = await response.json();
    addPages(jsonResp)
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

  const combinedQuery = charQuery + ' ' + artQuery; 

  return (
    <div className="App stack-large">
    <div class="topnav">
      <a href="./about">About</a>
    </div>
     <h1 className="label-wrapper"> Twokinds Codex </h1>
     <Form addPages={addPages} fetch={fetchArt} title={"Art search"}
         query={artQuery} setQuery={setArtQuery}/>
     <Form addPages={addPages} fetch={fetchText} title={"Textual search"} 
         query={charQuery} setQuery={setCharQuery}/>
     <p> {resultsSentence} </p>
    <ul>
      {pageList}
     </ul>
    </div>
    
  );
}

export default App;
