from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from typing import Optional, List , Dict
import requests
from fastapi.encoders import jsonable_encoder
import json
# import pandas as pd


app = FastAPI()

#hardcoded apiKey
apiKey = '644cd67ebf8d504be3973f6b815a4ac9'




callback_url="https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key=644cd67ebf8d504be3973f6b815a4ac9&file_type=json&series_id=GDP&value=7.00&date=2009-02-02"
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
def fredData(series_id: str):
    data =requests.get(callback_url).json()['observations'] 

    # return data
    # print(data)
    array1 = [] 
    array1=(data)


    array2 = [] 


    for x in array1:
        array1 = (x ['value'] , x['date'])
        print(array1)

        array2 = array1
    # for i in range(len(array1)):
    #     print (array1[i])
    
    return array2


# #gets specific values from callback_url
# @app.get("/series/specific")
# def getData():
#     Data_results = []

#     for Data in data:
#         series_id = data.get("series.id")
#         realtime_start= data.get('realtime_start')
#         realtime_end = data.get('realtime_end')
#         value= data.get('value')

#         DataFred_object = data( series_id, realtime_start,realtime_end,value)
#         Data_results.append(DataFred_object)

#     return Data_results
   