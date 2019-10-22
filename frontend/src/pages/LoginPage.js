import React, { useState } from "react";
import LoginForm from "../components/LoginForm";
import SignupForm from "../components/SignupForm";
import {
  Segment,
  Grid,
  Divider,
  Header,
  Icon,
  Message
} from "semantic-ui-react";

const LoginPage = props => {
  const INITIAL_STATE = {
    isSignupEmailSent: false
  };

  const [state, setState] = useState(INITIAL_STATE);

  return (
    <React.Fragment>
      <Header as="h1" textAlign="center" icon color="blue" className="w-header">
        <Icon name="th" />
        <Header.Content>WarshipBattle</Header.Content>
      </Header>
      <Segment placeholder>
        <Grid columns={2}>
          <Grid.Column>
            <LoginForm />
            <a href="http://localhost:3000/">Forgot password?</a>
          </Grid.Column>
          <Grid.Column verticalAlign="middle">
            {!state.isSignupEmailSent ? (
              <SignupForm />
            ) : (
              <Message
                className="message-compact"
                compact
                color="green"
                icon="check circle outline"
                header="Email has been sent to <mailbox>!"
                content="Please follow the link in email to finish registration."
              />
            )}
          </Grid.Column>
        </Grid>

        <Divider vertical>
          <Icon name="star" color="grey" />
        </Divider>
      </Segment>
    </React.Fragment>
  );
};

export default LoginPage;
