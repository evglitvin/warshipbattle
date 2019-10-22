import React, { useState } from "react";
import { Menu, Container } from "semantic-ui-react";

const MainMenu = props => {
  const INITIAL_STATE = { activeItem: "game" };

  const [state, setState] = useState(INITIAL_STATE);

  const handleItemClick = (e, { name }) => setState({ activeItem: name });

  return (
    <Menu className="nrc">
      <Container>
        <Menu.Item
          name="game"
          active={state.activeItem === "game"}
          onClick={handleItemClick}
        />
        <Menu.Item
          name="stats"
          active={state.activeItem === "stats"}
          onClick={handleItemClick}
        />
        <Menu.Item
          name="friends"
          active={state.activeItem === "friends"}
          onClick={handleItemClick}
        />
        <Menu.Menu position="right">
          <Menu.Item
            name="logout"
            icon="logout"
            onClick={handleItemClick}
            color="red"
          ></Menu.Item>
        </Menu.Menu>
      </Container>
    </Menu>
  );
};

export default MainMenu;
