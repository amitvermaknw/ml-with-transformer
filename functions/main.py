# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`
#Run the firebase emulator and run below command 
# uvicorn main:app --host 127.0.0.1 --port 5001 --reload

import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI
from functions_framework import http
from pydantic import BaseModel
from typing import List, Optional
import os 
from dotenv import load_dotenv
from src.controller.translator import Translator
from src.controller.grammar import Grammar
from src.config.serviceacc import Serviceacc

#load_dotenv()

# cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS"))
service_acc = Serviceacc()
cred = credentials.Certificate(service_acc.get_service_acc())

firebase_admin.initialize_app(cred)

db= firestore.client()
app = FastAPI()


class HandleRequest(BaseModel):
    fromlang: Optional[str]=None
    tolang: Optional[str]=None
    content: str

@app.post("/translate")
def user_input(request: HandleRequest):
    translator = Translator()
    return translator.handle_request(request)


@app.post("/grammar")
def correct_grammer(request: HandleRequest):
    grammar = Grammar()
    return grammar.handle_request(request)


@app.post("/process", response_model=None)
def process_data(request: HandleRequest):
    return {"message": "Success" + request.input_data}

@http
def fastapi_fun(request):
    from mangum import Mangum
    handler = Mangum(app)
    return handler(request)



# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")s