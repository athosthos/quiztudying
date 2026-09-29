from app.schemas.create_quiz import CreateQuizRequest
from app.schemas.quiz import QuizSchema
from app.services.openai_service import generate_quiz

def create_quiz(request: CreateQuizRequest) -> QuizSchema:
    quiz = generate_quiz(request)

    return quiz