import React from "react";
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import { Page } from "./pages/layout/Page.js";
import { Home } from "./pages/Home.js";
import { Kmom01 } from "./pages/Kmom01.js";

// export const App = () => <h1>test</h1>;
export const App = () => (
    <Router>
        <Page>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/kmom01" component={Kmom01} />
            </Switch>
        </Page>
    </Router>
);
