import React from "react";
import "./Home.css";
import Form from "../Form/Form";
import { useState } from "react";

function Home() {
  const [showForm, setShowForm] = useState(false);
  const handleButtonClick = () => {
    setShowForm(!showForm);
  };

  return (
    <>
      {showForm ? (
        <Form />
      ) : (
        <div className="row d-flex flex-wrap-reverse justify-content-between">
          <div className="col" id="col1">
            <div className="box d-flex justify-content-center flex-column mx-5">
              <h1 id="infoHead">
                Take a test <br />
                Find out if you've got Diabetes!!
              </h1>
              <h5 className="mt-5">
                This test carries out your health factors and checks if you’re
                at risk
              </h5>
              <button
                id="btn"
                className="py-2 my-5"
                onClick={() => handleButtonClick()}
              >
                Take your test
              </button>
            </div>
          </div>
          <div className="col" id="col2">
            <div className="box d-flex flex-column justify-content-center align-items-center">
              <h1 id="question" className="px-4 py-2">
                Am I alright??
              </h1>
              <img src="./images/Polygon1.png" alt="Polygon" id="polygon" />
              <img id="guessImage" src="./images/guess.png" alt="" />
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default Home;
