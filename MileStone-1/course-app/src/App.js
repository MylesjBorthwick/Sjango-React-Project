import "bulma/css/bulma.css";
import React, { useState, useEffect } from "react";

import "./App.scss";

import Collapsible from "./Components/Collapsible";




const App =()=> {

  const [isClicked, setIsClicked] = useState(false); 

  const createNew = () => {
    
    setIsClicked(!isClicked);
    
    console.log('button pressed')
  };


  return (

    <div className="App">
      {isClicked}
      <section class="hero is-dark is-bold">
        <div class="hero-body">
          <div class="container">
            <h1 class="title is-1">Course Creation Form</h1>
            <h2 class="subtitle">Edit form by section or create new form</h2>

            
            <div className="container is full-width">
              <Collapsible isClicked={isClicked} />
            </div>

            <div className="container">
              <div className="column is-multiline is-centered">
                <div className="column is-fullhd"></div>

                <div class="container">
                  <h1 class="title is-1">Create New Course?</h1>
                  <div class="control">
                    <button
                      class="button is-primary is-large is-rounded is-halfwidth"
                      onClick={createNew}
                    >
                      Create
                    </button>
                  </div>

                
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
