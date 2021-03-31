from fastapi import FastAPI
from routes import *

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Hello World'}