import React from "react";
import "./Form.css";
import { useState, useEffect } from "react";

function Form() {
  const [submit, setSubmit] = useState(false);
  const [column, setColumn] = useState({});
  const [formValues, setFormValues] = useState({})

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("/submit_form", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formValues),
      });

      if (response.ok) {
        console.log("Form submitted successfully");
      } else {
        console.error("Form submission failed");
      }
    } catch (error) {
      console.error("Error during form submission:", error);
    }
    setSubmit(!submit);
    console.log("Form values: ", formValues);
  };

  const handleChange = (e, column)=>{
    const { value } = e.target;
    setFormValues(prevValues => ({
      ...prevValues,
      [column]: isNaN(value) ? value : +value,
    }));
  }

  useEffect(() => {
    fetch("/members")
      .then((res) => res.json())
      .then((data) => {
        setColumn(data);
      });
  }, []);

  return (
    <>
      <div className="form mx-5 mt-3">
        <form action="" method="get" onSubmit={handleSubmit}>
          <fieldset>
            <legend className="text-center" id="head">
              Diabetes Prediction
            </legend>
            {typeof column.members == "undefined" ? (
              <div className="loading text-center mb-3">
                <img src="./images/loader.gif" alt="Loading..." />
              </div>
            ) : (
              column.members.map((column, i) => (
                <div key={i} className="form-floating mb-3">
                  <input
                    type="number"
                    name={column}
                    className="form-control bg-light text-dark"
                    placeholder=""
                    onChange={(e)=>handleChange(e, column)}
                    required
                  />
                  <label htmlFor={column} className="text-dark">
                    {column}
                  </label>
                </div>
              ))
            )}
            <input
              type="submit"
              onClick={handleSubmit}
              value="Check for Diabetes"
              className="mb-3 button"
            />
          </fieldset>
        </form>
      </div>
    </>
  );
}

export default Form;
