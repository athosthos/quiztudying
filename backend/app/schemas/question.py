from pydantic import BaseModel, Field, model_validator
from app.schemas.alternative import AlternativeSchema

class QuestionSchema(BaseModel):
    order: int
    statement: str
    explanation: str
    alternatives: list[AlternativeSchema] = Field(
        min_length=4,
        max_length=4
    )

    @model_validator(mode="after")
    def validate_correct_answer(self):
        correct_answers = [
            alternative
            for alternative in self.alternatives
            if alternative.is_correct
        ]

        if len(correct_answers) != 1:
            raise ValueError(
                "Each question must have exactly one correct alternative."
            )

        return self