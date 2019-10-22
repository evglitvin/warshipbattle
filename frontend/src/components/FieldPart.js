import React, { useState, useEffect } from "react";

const FieldPart = props => {
  const MISSED = "missed";
  const INJURED = "injured";

  const INITIAL_STATE = {
    missed: 0,
    injured: 0,
    classes: "field-part bg-blue"
  };

  const isMissed = () => {
    return Math.random(1) < 0.5 ? 0 : 1;
  };

  const [state, setState] = useState(INITIAL_STATE);

  const getAttributes = event => {
    const x = event.target.getAttribute("x");
    const y = event.target.getAttribute("y");
    const isAlien = event.target.getAttribute("alien");
    const cls = event.target.getAttribute("class");
    return { x: x, y: y, isAlien: isAlien, cls: cls };
  };

  const fieldPartClickHandler = event => {
    const { cls } = getAttributes(event);
    const newCls = isMissed() ? INJURED : MISSED;
    console.log();
    event.target.setAttribute("class", cls + " " + newCls);
  };

  // const getProps = event => {
  //   const x = event.target.getAttribute("x");
  //   const y = event.target.getAttribute("y");
  //   const alien = event.target.getAttribute("alien");
  //   const cls = event.target.getAttribute("class");
  //   return { x: x, y: y, isAlien: alien, cls: cls };
  // };

  return <div {...props} onClick={fieldPartClickHandler}></div>;
};

export default FieldPart;
