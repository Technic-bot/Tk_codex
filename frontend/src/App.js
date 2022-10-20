import Form from "./components/Form";
import Page from "./components/Page";
import React, {useState} from "react";

function App() {
  const [pages,setPages] = useState([]);

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

  return (
    <div className="App stack-large">
    <div class="topnav">
      <a href="./about">About</a>
    </div>
     <h1 className="label-wrapper"> Tk Codex </h1>
     <Form addPages={addPages} fetch={fetchArt} title={"Art search"} />
     <Form addPages={addPages} fetch={fetchText} title={"Textual search"}/>
     <ul>
      {pageList}
     </ul>
    </div>
    
  );
}

export default App;
