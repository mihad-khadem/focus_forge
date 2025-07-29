from typing import Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase

class UserModel:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.get_collection("users")

    async def create_user(self, user_data: dict) -> dict:
        # Add timestamps
        now = datetime.utcnow()
        user_data.setdefault("created_at", now)
        user_data.setdefault("updated_at", now)

        result = await self.collection.insert_one(user_data)
        created_user = await self.collection.find_one({"_id": result.inserted_id})

        # Mongo returns ObjectId as _id; convert to str for Pydantic compatibility
        if created_user:
            created_user["_id"] = str(created_user["_id"])
        return created_user

    async def get_user_by_email(self, email: str) -> Optional[dict]:
        user = await self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
        return user

    async def get_user_by_id(self, user_id: str) -> Optional[dict]:
        from bson import ObjectId
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
        return user
    async def get_all_users(self) -> list[dict]:
        users = [] 
        cursor = self.collection.find()
        async for user in cursor:
            user["_id"] = str(user["_id"])
            users.append(user)
        return users
