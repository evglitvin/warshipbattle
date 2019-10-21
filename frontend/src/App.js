import React, { useState } from "react";
import "./App.css";

import { Header } from "semantic-ui-react";
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
      <div className="wrapper">
        <div className="wrap-login">
          <Header as="h1" color="blue">
            Warship Battle
          </Header>
          <div className="login">
            {!state.isAuthenticated ? <LoginPage /> : <MainPage />}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
