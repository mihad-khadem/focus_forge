from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import UserCreate, UserPublic
from app.services.user_service import UserService
from app.db.mongo import get_db  # this should return your MongoDB client/db instance
from app.db.models.user import UserModel

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserPublic)
async def register(user_create: UserCreate, db=Depends(get_db)):
    user_model = UserModel(db)
    user_service = UserService(user_model)

    # Check if user already exists
    existing_user = await user_service.get_user_by_email(user_create.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Create new user
    new_user = await user_service.create_user(user_create)
    return new_user
# get all users
@router.get("/users", response_model=list[UserPublic])
async def get_all_users(db=Depends(get_db)):
    user_model = UserModel(db)
    user_service = UserService(user_model)
    users = await user_service.get_all_users()
    return users