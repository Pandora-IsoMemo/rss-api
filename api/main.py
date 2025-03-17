import datetime
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

client = None
db = None
collection = None


@app.on_event("startup")
def startup_db_client():
    global client, db, collection

    MONGO_USER = os.environ.get("DB_USER")
    MONGO_PASSWORD = os.environ.get("DB_PASSWORD")
    MONGO_HOST = os.environ.get("DB_HOST")
    MONGO_PORT = os.environ.get("DB_PORT")

    connection_string = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource=rss"
    client = MongoClient(connection_string)
    db = client["rss"]
    collection = db["articles"]


@app.on_event("shutdown")
def shutdown_db_client():
    if client:
        client.close()


@app.get("/articles/")
def get_articles(date: datetime.date):
    """
    Retrieve articles with 'ts_last_feed_updated' later than the provided date.

    Query Parameter:
    - date (YYYY-MM-DD): The starting date to filter articles.

    Returns:
    - A list of articles updated after the given date.
    """
    dt = datetime.datetime.combine(date, datetime.time.min)

    try:
        articles_cursor = collection.find({"ts_last_feed_updated": {"$gt": dt}})
        articles = []
        for article in articles_cursor:
            article["_id"] = str(article["_id"])
            articles.append(article)
        return articles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
