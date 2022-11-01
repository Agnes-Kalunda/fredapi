from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
# from typing import Optional, List , Dict
import requests
from fastapi.encoders import jsonable_encoder
# import pandas as pd


app = FastAPI()

#hardcoded apiKey
apiKey = '644cd67ebf8d504be3973f6b815a4ac9'




callback_url="https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key=644cd67ebf8d504be3973f6b815a4ac9&file_type=json&observation_start=2010-02-02&observation_end=2022-02-02&units=pc1"
# seriesID = "GDP"

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # can alter with time
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


class Data(BaseModel):
    start: int
    end: int
    seriesID: str
    units: str




#define endpoint
@app.get("/")
def home():
    return "Welcome Home"


@app.get("/series")
def fredData(series_ID: str,observation_start:str, observation_end:str):
    data =requests.get(callback_url).json()['observations']


    print(data)

   
    return data


#gets specific values from callback_url
@app.get("/series")
def getData():
    Data_results = []

    for Data in data:
        series_id = data.get("series.id")
        observation_start= data.get('observation_start')
        observation_end = data.get('observation_end')

        DataFred_object = data(series_id, observation_start,observation_end)
        Data_results.append(DataFred_object)

    return Data_results
   