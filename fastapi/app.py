import pickle

import numpy as np
import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()
model = pickle.load(open('../ml-model/model.pkl', 'rb'))


class Item(BaseModel):
    values: List[List[float]]


@app.post("/predict")
async def predict(item: Item):
    prediction = model.predict(np.array(item.values))
    return {"prediction": prediction.tolist()}


if __name__ == "__main__":
    uvicorn.run("app:app")