import json
from typing import List
from fastapi import APIRouter, HTTPException
from redis_dict import RedisDict
from models.products import X, Source
from dependencies import distribute_products


router = APIRouter()
db = RedisDict(host="127.0.0.1", port=6379)


@router.post("/x/")
async def add_x_value(x: X):
    db[x.key] = x.val
    return {"message": "X created successfully"}


@router.get("/x/{key}")
async def read_x_value(key: str):
    val = db.get(key)
    if val is None:
        raise HTTPException(status_code=404, detail="X not found")
    return {"key": key, "val": val}


@router.post("/source/")
async def create_source(sources: List[Source]):
    for source in sources:
        source_json = source.model_dump_json()
        source_dict = json.loads(source_json)
        db[source.name] = source_dict
    return {"message": "Source created successfully"}


@router.post("/storage/")
async def create_storage():
    storages = distribute_products(db)
    for storage in storages:
        storage_json = storage.model_dump_json()
        storage_dict = json.loads(storage_json)
        db[storage.name] = storage_dict
    return {"message": "Storage created successfully"}


@router.get("/database/")
async def read_database():
    return db
