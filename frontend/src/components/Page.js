import React from "react";

export default function Page(props) {
  const keenspotUrl = `https://twokinds.keenspot.com/comic/${props.number}`
  return (
    <li>
      <div>
        <label>
          {props.number}, {props.date},  
          <a href={keenspotUrl}> {props.title} </a>
        </label>
      </div>
    </li>
  );
}
