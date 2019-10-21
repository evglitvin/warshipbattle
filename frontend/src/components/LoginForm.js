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
        icon="user"
        name="username"
        iconPosition="left"
        type="text"
        onChange={inputChangeHandler}
      />
      <Form.Input
        placeholder="Password"
        icon="lock"
        name="password"
        iconPosition="left"
        type="password"
        onChange={inputChangeHandler}
      />
      <Form.Button type="submit" content="Login" primary fluid />
      <div></div>
    </Form>
  );
};

export default LoginForm;
