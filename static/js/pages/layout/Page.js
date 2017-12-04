import React from "react";
import { Sidebar } from "./Sidebar.js";
import "./css/style.css";

export const PageLayout = ({ children }) => (
    <div className="app">
        <Sidebar />
        <main>
            <div className="container">{children}</div>
        </main>
    </div>
);
