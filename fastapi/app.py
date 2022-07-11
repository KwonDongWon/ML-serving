import pickle

import numpy as np
import uvicorn
from fastapi import FastAPI
from typing import List

app = FastAPI()
model = pickle.load(open('../ml-model/model.pkl', 'rb'))


@app.post("/predict")
def home(values: List[float]):
    print(values)
    prediction = model.predict(np.array(values))
    print(prediction)
    return {"prediction": prediction}


if __name__ == "__main__":
    uvicorn.run("app:app")