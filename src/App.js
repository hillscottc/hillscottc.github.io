import React, { Component } from 'react';
import { Grid, Navbar, Jumbotron } from 'react-bootstrap';

class App extends Component {
  render() {
    return (
        <div>
          <Navbar inverse fixedTop>
            <Grid>
              <Navbar.Header>
                <Navbar.Brand>
                  <a href="/">React App</a>
                </Navbar.Brand>
                <Navbar.Toggle />
              </Navbar.Header>
            </Grid>
          </Navbar>
          <Jumbotron>
            <Grid>
              <h1>Scott C. Hill</h1>
              <p>software engineer, web developer</p>
              <p>
                [<a href="http://blog.scottchill.com">tech blog</a>,
                <a href="https://www.linkedin.com/in/scotthill2000">linkedin</a>]
              </p>

              <h2>Code Samples</h2>

              <section>
                <h3>Plants App</h3>
                <p> A react UI for 90,000 records of <a target="_blank" href="https://plants.usda.gov/dl_all.html">USDA plant data</a>. Implemented in two ways:
                </p>

                <p><span className="project">isomorphic React-Starter-Kit</span> boilerplate (<a href="https://github.com/hillscottc/plantapp-iso">github</a>
                  | <a href="https://plantapp-iso.herokuapp.com/">running</a>)
                </p>

                <p><span className="project">Create-React-App</span> boilerplate (<a href="https://github.com/hillscottc/plantapp">github</a>
                  | <a href="https://plantapp.herokuapp.com/">running</a>)
                </p>

              </section>

              <section>
                <h3>Trivia App</h3>

                <p>
                  A single-page web app as a UI for a collection of trivia questions. Uses <a href="https://nodejs.org/">Node</a>
                  and <a href="http://expressjs.com/">Express</a>
                  to serve an api for a PostgreSQL database of 180,000+ records.
                </p>
                <p>
                  This app has been re-implemented over time, using different technologies.
                </p>
                <br/>
                <p>
                  <span className="project">trivnode-react</span>...2016 with <a href="https://facebook.github.io/react/">React</a>.
                  (<a href="https://github.com/hillscottc/trivnode-react#readme">github</a>  | <a href="https://trivnode-react.herokuapp.com/">running</a>)
                </p>
                <p>
                  <span className="project">trivnode</span>...2014 with <a href="http://backbonejs.org/">Backbone.js</a> (<a href="https://github.com/hillscottc/trivnode#readme">github</a> | <a href="https://protected-lake-8296.herokuapp.com/">running</a>)
                </p>
                <p>
                  <span className="project">quest-django</span>...2013 with Python + <a href="https://www.djangoproject.com/">Django</a> (<a href="https://github.com/hillscottc/quest#readme">github</a> | <a href="https://quest-django.herokuapp.com/">running</a>)
                </p>
              </section>

              <section>
                <h3>Fortune Teller App</h3>

                <p><span className="project">nostra</span> (<a href="https://github.com/hillscottc/nostra#readme">github</a>
                  | <a href="https://badge.fury.io/js/nostra"><img src="https://badge.fury.io/js/nostra.svg" alt="npm version" height="18" /></a>)
                </p>
                <p>A <a href="https://nodejs.org/">Node</a> module for generating random-ish fortune text, hosted on the <a href="https://www.npmjs.com/">npm</a>
                  package registry.</p>

                <p><span className="project">nostranode-react</span>...simple UI in Node, express, and React
                  (<a href="https://github.com/hillscottc/nostranode-react#readme">github</a>)
                </p>

                <p>
                  <span className="project">nostranode</span>...simple UI with <a href="http://getbootstrap.com/">Bootstrap</a>
                  + <a href="https://jqueryui.com/">jQuery</a>
                  (<a href="https://github.com/hillscottc/nostranode#readme">github</a> | <a href="https://nostranode.herokuapp.com/">running</a>)
                </p>
              </section>


            </Grid>
          </Jumbotron>
        </div>
    );
  }
}

export default App;