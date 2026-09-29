from fastapi import APIRouter
from app.schemas.create_quiz import CreateQuizRequest
from app.services.openai_service import generate_quiz


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/generate-quiz")
def generate_quiz_endpoint(request: CreateQuizRequest):
    quiz = generate_quiz(request)

    return quiz.model_dump()