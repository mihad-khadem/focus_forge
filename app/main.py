from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.scheduler import start_scheduler
from app.db.mongo import connect_to_mongo, close_mongo_connection

from app.api.auth import router as auth_router
from app.api.tasks import router as task_router
from app.api.habits import router as habit_router
from app.api.focus_sessions import router as focus_router
from app.api.wakastats import router as waka_router

app = FastAPI(
    title="FocusForge",
    description="Backend for tracking focus, tasks, habits and coding activity (via WakaTime).",
    version="1.0.0"
)

# Enable CORS (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(habit_router, prefix="/habits", tags=["Habits"])
app.include_router(focus_router, prefix="/focus_sessions", tags=["Focus Sessions"])
app.include_router(waka_router, prefix="/wakastats", tags=["WakaTime"])

# App startup
@app.on_event("startup")
async def on_startup():
    await connect_to_mongo()
    start_scheduler()

# App shutdown
@app.on_event("shutdown")
async def on_shutdown():
    await close_mongo_connection()
