from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.DB_NAME]

async def close_mongo_connection():
    if client:
        client.close()
