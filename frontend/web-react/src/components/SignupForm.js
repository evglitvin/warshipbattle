import React, { useState } from "react";
import { Form, Header } from "semantic-ui-react";

const SignupForm = props => {
  const INITIAL_STATE = {
    email: "",
    isSubmitting: false,
    errors: []
  };

  const [state, setState] = useState(INITIAL_STATE);

  const inputChangeHandler = event => {
    event.preventDefault();
    setState({ ...state, [event.target.name]: event.target.value });
  };

  const formSubmitHandler = event => {
    setState({ ...state, isSubmitting: true });
    console.log(state);
  };

  return (
    <React.Fragment>
      <Header as="h2" color="grey">
        Not yet joined?
      </Header>
      <Form onSubmit={formSubmitHandler}>
        <Form.Input
          name="email"
          placeholder="Email"
          icon="mail"
          iconPosition="left"
          onChange={inputChangeHandler}
        />
        <Form.Button content="Sign up" icon="signup" size="big" color="green" />
      </Form>
    </React.Fragment>
  );
};

export default SignupForm;
