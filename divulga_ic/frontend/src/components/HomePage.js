import React, { Component,useState } from "react";
  import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import Backdrop from "@material-ui/core/Backdrop";
import Header from "../components/Header";
//import CardIc from "../../components/CardIc";
//import DetailedCard from "../../components/DetailedCard";
//import mockData from "../../mock.data.json";

import { ExampleContainer, CardHolder } from "./styles";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {


    return (
      <Router>
        <Switch>
          <Route exact path="/">
          <div>roi</div>
          {/** 
          <ExampleContainer>
          <Header />
          <div>
            <CardHolder>
              {mockData.map((ic, index) => (
                <CardIc
                  data={ic}
                  key={`${ic._id}.${index}`}
                  showAllContent={false}
                  handleClick={() => handleOpenModal(ic)}
                />
              ))}
            </CardHolder>
            <Backdrop style={{ zIndex: 100 }} open={openModal} onClick={closeModal}>
              <DetailedCard data={icData} />
            </Backdrop>
          </div>
        </ExampleContainer>*/}

          </Route>
        </Switch>
      </Router>
    );
  }
}
