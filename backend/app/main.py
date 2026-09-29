from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import APP_NAME, APP_VERSION, OPENAI_API_KEY
from app.api.routes.ai import router as ai_router
from app.api.routes.quizzes import router as quizzes_router

app = FastAPI(
    title=APP_NAME,
    description="Backend API for the Quiztudying platform",
    version=APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)
app.include_router(quizzes_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Quiztudying API"
    }

@app.get("/config-status")
def config_status():
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "environment": "development",
        "openai_configured": bool(OPENAI_API_KEY)
    }