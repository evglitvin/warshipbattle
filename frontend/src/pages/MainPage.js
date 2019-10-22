import React from "react";
import { Grid, Header } from "semantic-ui-react";

import Field from "../components/Field";

const MainPage = props => {
  return (
    <Grid columns={2} relaxed="very" stackable>
      <Grid.Column>
        <Header as="h1" color="blue">
          Player 1
        </Header>
        <Field width={10} height={10} alien={0} />
      </Grid.Column>
      <Grid.Column>
        <Header as="h1" color="red">
          Player 2
        </Header>
        <Field width={10} height={10} alien={1} />
      </Grid.Column>
    </Grid>
  );
};

export default MainPage;
