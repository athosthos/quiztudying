from pydantic import BaseModel, Field

class CreateQuizRequest(BaseModel):
    title: str
    description: str
    language: str
    question_count: int = Field(
        ge=5,
        le=50
    )