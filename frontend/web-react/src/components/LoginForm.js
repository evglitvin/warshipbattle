import React, { useState } from "react";
import { Form } from "semantic-ui-react";

const LoginForm = props => {
  const INITIAL_STATE = {
    username: "",
    password: "",
    isSubmitting: false,
    hasErrors: null
  };

  const [loginState, setLoginState] = useState(INITIAL_STATE);

  const submitFormHadler = event => {
    console.log({
      username: loginState.username,
      password: loginState.password
    });
  };

  const inputChangeHandler = event => {
    event.preventDefault();
    setLoginState({ ...loginState, [event.target.name]: event.target.value });
  };

  return (
    <Form onSubmit={submitFormHadler}>
      <Form.Input
        placeholder="Username"
        name="username"
        type="text"
        icon="user"
        iconPosition="left"
        onChange={inputChangeHandler}
      />
      <Form.Input
        placeholder="Password"
        name="password"
        icon="lock"
        type="password"
        iconPosition="left"
        onChange={inputChangeHandler}
      />
      <Form.Button content="Login" primary fluid />
      <div></div>
    </Form>
  );
};

export default LoginForm;
