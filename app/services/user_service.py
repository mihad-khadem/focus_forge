from app.db.models.user import UserModel
from passlib.context import CryptContext
from typing import Optional
from app.schemas.user import UserCreate, UserPublic
# user service 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_model: UserModel):
        self.user_model = user_model

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    async def create_user(self, user_create: UserCreate) -> UserPublic:
        user_dict = user_create.dict(by_alias=True, exclude={"id"})
        user_dict["password"] = self.hash_password(user_create.password)
        created_user = await self.user_model.create_user(user_dict)
        return UserPublic(**created_user)

    async def get_user_by_email(self, email: str) -> Optional[UserPublic]:
        user = await self.user_model.get_user_by_email(email)
        if user:
            return UserPublic(**user)
        return None
    async def get_all_users(self) -> list[UserPublic]:
        users = await self.user_model.get_all_users()
        return [UserPublic(**user) for user in users]