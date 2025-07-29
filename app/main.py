from fastapi import FastAPI
from app.db.mongo import connect_to_mongo, close_mongo_connection
from app.api.auth import router as auth_router

app = FastAPI()


# Bootstrap
@app.on_event("startup")
async def startup():
    await connect_to_mongo()


# Teardown
@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()


# Routes
@app.get("/")
async def root():
    return {"message": "Hello, world!"}
# Auth/User Routes



app.include_router(auth_router)
