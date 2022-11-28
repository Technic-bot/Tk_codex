import React from "react";

export default function Page(props) {
  const keenspotUrl = `https://twokinds.keenspot.com/comic/${props.number}`
  return (
    <li key={props.page} className="todo stack-small">
      <div className="c-cb">
        <div className="todo-label" htmlFor="todo-0">
          {props.number}, {props.date},  
          <a href={keenspotUrl} target="_blank" rel="noopener noreferrer"> {props.title} </a>
        </div>
      </div>
    </li>
  );
}
