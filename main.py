from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb://localhost:27017/")

@app.get("/")
def read_root():
    return {"Hello": "World"}
# Database name
db = conn["school"]
   
# Collection name
col = db["students"]
 
# if we don't want to print id then pass _id:0
for x in col.find({}, {"_id":1, "name": 1, "age": 1, "gpa":1 }):
    print(x)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
