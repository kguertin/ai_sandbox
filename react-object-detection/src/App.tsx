import React, { useEffect, useState } from "react";
import * as mobilenetModel from "@tensorflow-models/mobilenet";
import "@tensorflow/tfjs";
import "./App.css";

function App() {
  const [mobilenet, setMobilenet] = useState<any>();
  const [modelLoaded, setModelLoaded] = useState<boolean>(false);

  const loadMobilenet = async () => {
    try {
      const model = await mobilenetModel.load();
      setMobilenet(model);
      setModelLoaded(true);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    loadMobilenet();
  }, []);

  return (
    <div className="container">
      <p id="status">{`${modelLoaded ? "Model Loaded" : "Loading Model"}`}</p>
      <div className="formContainer">
        <input type="file" accept="image/*" className="uploadInput" />
      </div>
    </div>
  );
}

export default App;
