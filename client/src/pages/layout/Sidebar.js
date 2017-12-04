import React from "react";

import { Link, NavLink } from "react-router-dom";

export const Sidebar = () => (
    <div className="menu-logo">
        <h1 className="big-logo">
            <Link to="/">matmod</Link>
        </h1>
        <h5 className="sub-logo">
            Anders Nygren, litemerafrukt. Webprogrammering 120p på BTH, andra året.
        </h5>

        <div className="side-panel">
            <header>
                <div className="">
                    <nav className="header-nav">
                        <NavLink exact to="/" activeClassName="nav-selected">
                            Hem
                        </NavLink>
                        <NavLink to="/kmom01" activeClassName="nav-selected">
                            Kmom01
                        </NavLink>
                    </nav>
                </div>
            </header>
            <div className="contact">
                <h2>Kontakt</h2>

                <p>Bor och verkar i Skåne.</p>
                <p>
                    <a href="mailto:litemerafrukt@gmail.com">litemerafrukt@gmail.com</a>
                </p>
                <p>
                    <a href="https://www.linkedin.com/in/anders-nygren-7a6aa113a/">LinkedIn</a>
                </p>
                <p>
                    <a href="https://twitter.com/litemerafrukt">Twitter</a>
                </p>
                <p>litemerafrukt på irc.bsnet.se</p>
                <p>
                    Träffas även på <a href="https://dbwebb.se/forum/">dbwebbs-forum</a>.
                </p>
            </div>
        </div>
    </div>
);
