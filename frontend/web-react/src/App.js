import React, { useState } from "react";
import "./App.css";

import { Container } from "semantic-ui-react";
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
          {state.isAuthenticated ? (
            <LoginPage isAuth={state.isAuthenticated} />
          ) : (
            <MainPage />
          )}
        </div>
      </Container>
    </div>
  );
}

export default App;
