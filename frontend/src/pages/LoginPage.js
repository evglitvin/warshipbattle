import React from "react";
import LoginForm from "../components/LoginForm";
import { Segment, Grid, Divider, Button } from "semantic-ui-react";

const LoginPage = props => {
  return (
    <Segment placeholder>
      <Grid columns={2} relaxed="very" stackable>
        <Grid.Column>
          <LoginForm />
          <a href="#">Forgot password?</a>
        </Grid.Column>
        <Grid.Column verticalAlign="middle">
          <Button content="Sign up" icon="signup" size="big" color="green" />
        </Grid.Column>
      </Grid>

      <Divider vertical>Or</Divider>
    </Segment>
  );
};

export default LoginPage;
