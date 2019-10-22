import React from "react";
import FieldPart from "./FieldPart";
import { makeUniqueId } from "../utils/utilities";

const Field = ({ width, height, alien }) => {
  const makeField = () => {
    let f = [];
    for (let x = 1; x <= width; x++) {
      for (let y = 1; y <= height; y++) {
        f.push(
          <FieldPart
            key={makeUniqueId(15)}
            x={x}
            y={y}
            alien={alien}
            className="field-part bg-blue"
          />
        );
      }
    }
    return f;
  };

  const field = makeField();

  return <div className="game-field">{field}</div>;
};

export default Field;
