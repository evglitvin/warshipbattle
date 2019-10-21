import React from "react";
import { Segment, Divider, Grid, Header } from "semantic-ui-react";

import Field from "../components/Field";

const MainPage = props => {
  return (
    <Grid columns={2} relaxed="very" stackable>
      <Grid.Column>
        <Header as="h1" color="blue">
          Player 1
        </Header>
        <Field width={10} height={10} />
      </Grid.Column>
      <Grid.Column>
        <Header as="h1" color="red">
          Player 2
        </Header>
        <Field width={10} height={10} alien />
      </Grid.Column>
    </Grid>
  );
};

export default MainPage;
