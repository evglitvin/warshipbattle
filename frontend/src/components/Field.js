import React from "react";
import FieldPart from "./FieldPart";

const Field = props => {
  const field = (w, h) => {
    let f = [];
    for (let counter = 1; counter <= w * h; counter++) {
      f.push(<FieldPart id={!props.alien ? counter : "X"} />);
    }
    return f;
  };

  return <div className="field">{field(props.width, props.height)}</div>;
};

export default Field;
