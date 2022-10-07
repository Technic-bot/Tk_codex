import Form from "./components/Form";
import React, {useState, useEffect} from "react";

function App() {
  const [post,setPosts] = useState([]);
  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=10')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      setPosts(data);
    })
    .catch((err) => {
      console.log(err.message);
    })
  },[]);

  const postList = post.map((post) => (
    <div className="card" key={post.id}>
      <h2 className="post-title">{post.title}</h2>
      <p className="post-body">{post.body}</p>
      <div className="delete-btn">Delete</div>
    </div>
  ));

  return (
    <div className="App">
      <h1> Tk Codex </h1>
     <Form />
    </div>
    
  );
}

export default App;
