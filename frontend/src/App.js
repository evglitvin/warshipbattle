import React, { useState } from "react";
import "./App.css";

import { Header, Container } from "semantic-ui-react";
import MainPage from "./pages/MainPage";
import LoginPage from "./pages/LoginPage";

function App() {
  const INITIAL_STATE = {
    isAuthenticated: false,
    username: null,
    token: null
  };

  const [state, setState] = useState(INITIAL_STATE);

  return (
    <div className="App">
      <Container>
        <div className="login">
          {state.isAuthenticated ? <LoginPage /> : <MainPage />}
        </div>
      </Container>
    </div>
  );
}

export default App;
