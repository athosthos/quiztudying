from pydantic import BaseModel, Field
from app.schemas.question import QuestionSchema

class QuizSchema(BaseModel):
    title: str
    description: str
    questions: list[QuestionSchema] = Field(
        min_length=5,
        max_length=50
    )