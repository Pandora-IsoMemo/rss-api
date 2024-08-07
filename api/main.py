from datetime import datetime

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api.db_connect import MariaDBConnection

app = FastAPI()


class Item(BaseModel):
    title: str
    text: str
    timestamp_published: datetime


@app.get("/items/")
def read_items(start_date: datetime, end_date: datetime):
    # query = """
    # SELECT title, text, ts_item_published
    # FROM feed_text
    # WHERE timestamp_published BETWEEN %s AND %s
    # """

    # with MariaDBConnection() as conn:
    #     if not conn:
    #         raise HTTPException(
    #             status_code=500, detail="Datenbankverbindung fehlgeschlagen."
    #         )

    #     cursor = conn.cursor(dictionary=True)
    #     cursor.execute(query, (start_date, end_date))
    #     rows = cursor.fetchall()

    #     if not rows:
    #         raise HTTPException(
    #             status_code=404,
    #             detail="Keine Einträge für den angegebenen Zeitraum gefunden.",
    #         )

    #     items = [Item(**row) for row in rows]
    csv_file_path = "feed_text_202408061018.csv"
    df = pd.read_csv(csv_file_path)
    df = df[["title", "text", "ts_item_published"]]
    df["ts_item_published"] = pd.to_datetime(df["ts_item_published"])

    mask = (df["ts_item_published"] >= start_date) & (
        df["ts_item_published"] <= end_date
    )
    filtered_df = df.loc[mask]
    return filtered_df.to_json(orient="records")
