import React, { useState, useEffect } from 'react'
import "./Result.css"

function Result() {
    const [predictionValue, setPredictionValue] = useState({})
    let result = null;
    useEffect(()=>{
        fetch('/result')
        .then((res)=>res.json())
        .then((data)=>{
            setPredictionValue(data)
        })
    }, [])
    predictionValue.prediction === 0 ? result="Not Diabetic" : result = "Diabetic"
  return (
    <>
    <h1 id='prediction'>Prediction: {result}</h1>
    </>
  )
}

export default Result