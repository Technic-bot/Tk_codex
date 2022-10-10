import Form from "./components/Form";
import Page from "./components/Page";
import React, {useState} from "react";

function App() {
  const [pages,setPages] = useState([]);

  function addPages(pages) {
    setPages(pages);
    console.log("Adding Pages");
    console.log(pages);
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
    <div className="App">
     <h1> Tk Codex </h1>
     <Form addPages={addPages} />
     <ul>
      {pageList}
     </ul>
    </div>
    
  );
}

export default App;
