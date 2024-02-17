from typing import Union
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline

# model
model_path = "martin-ha/toxic-comment-model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
pipeline =  TextClassificationPipeline(model=model, tokenizer=tokenizer)



app = FastAPI()
# CORS MIDDLEWARE
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/clasification/{predicts}")
async def predict_items(predicts: str, query:str):
    item = {"message":"succesfull classification",
            "Status":200,
            "Query":query
            }
    if predicts:
        item.update({"result":pipeline(query)})
    return item