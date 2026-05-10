# from fastapi import FastAPI     #imports the FastAPI class from the fastapi  library, need this to create web app instance

# app = FastAPI()     # creates an instance of fastapi app,  app is the main object that handles trouting, requests, responses etc,  very imp

# @app.get("/")       #  its a decorator, tells fastapi hwen somemone send a GET req to /, run the func below.,   /=root url (localhost-http//localhost:8000),  GET= HTTP method to fetch data
# def root():         #  defines the func that runs when / is accessed,  name doent matter can be anything
#     return {"message": "API running"}       # returns a py dictionary, fastapi auto converts it to JSON
# #WHAT HAPPENED--> 1. we run servers via uvicorn main:app --reload cmd,  2.someone hits GET,   3. fastapi routes it to root(),  4. function returns data,  5. fastapi sends it back as json

# @app.get("/test-db")
# def test_db():
#     res = supabase.table("notes").select("*").execute()
#     return res.data





from fastapi import FastAPI
from db import supabase

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}



@app.get("/test-db")

def test_db():
    res = supabase.table("notes").select("*").execute()
    return res.data

#  tz 1-


