import threading
from typing import List, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from get_result import get_result_movie, get_result_series
from push_result import push_result_movie, push_result_series
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def alive():
    return {'alive'}


@app.post("/pushResult/movie/")
async def upload_data(data: List[Dict]):
    threading.Thread(target=push_result_movie, args=(data,)).start()
    return {"success"}

@app.post("/pushResult/series/")
async def upload_data(data: List[Dict]):
    threading.Thread(target=push_result_series, args=(data,)).start()
    return {"success"}

@app.get("/getResult/series/")
async def upload_data(query: Dict):
    return get_result_series({"title": query["title"], "episode": query["episode"], "season": query["season"], "language": query["language"]})

@app.get("/getResult/movie/")
async def upload_data(query: Dict):
    return get_result_movie({"title": query["title"], "year": query["year"], "language": query["language"]})
