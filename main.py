from tkinter.tix import Form
from fastapi import FastAPI, File, UploadFile,  Depends
from fastapi.security.api_key import  APIKey
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import auth
import json
from test import uncommanwords
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from joinfile import  pathfile


app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/joinfiles")
async def upload( text: str = Form()):
 
    res = pathfile(text)    
    
   
    return  res
@app.post("/upload")
def upload(file: UploadFile = File(...),file1: UploadFile = File(...)):
     try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
     finally:
        file.file.close() 
     try:
        contents1 = file1.file.read()
        with open(file1.filename, 'wb') as f:
            f.write(contents1)
     finally:
        file1.file.close()

     res = uncommanwords(file.filename,file1.filename)    
    
   
     return  res





if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)



