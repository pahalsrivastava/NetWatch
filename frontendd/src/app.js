// frontend/src/App.js

import React, { useState } from 'react';

function App() {
  const [features, setFeatures] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ features: Object.values(features).map(Number) }),
    });
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        {/* Add input fields for each feature, assuming you have features 'f1', 'f2', ... */}
        <input type="text" name="f1" onChange={handleChange} placeholder="Feature 1" />
        <input type="text" name="f2" onChange={handleChange} placeholder="Feature 2" />
        {/* Add more input fields as needed */}
        <button type="submit">Predict</button>
      </form>
      {prediction !== null && <div>Prediction: {prediction}</div>}
    </div>
  );
}

export default App;
