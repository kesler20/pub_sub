from fileinput import filename
from http.client import responses
from urllib import response
from boto3.dynamodb.conditions import Key
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import pandas as pd
from fastapi import Body, FastAPI, File, Body, UploadFile, Depends
import uuid
import json

####################################### INITIALISE APPLICATION AND CONFIGURE IT #######################################
app = FastAPI()

origins = [
    "."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

####################################### DEFINE CONTROLLER LOGIC AND ENDPOINTS #######################################


@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url='/docs')
    return response


@app.post('/mqtt/connection_status',)
async def handle_upload():
    # import mqtt
    return {"connection_status": 200}
