import React, {useContext} from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Main from "./components/app/Main";



const App = props => {



    return (
        <BrowserRouter>

            <Main/>

        </BrowserRouter>
    );
};

export default App;
