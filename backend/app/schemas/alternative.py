from pydantic import BaseModel

class AlternativeSchema(BaseModel):
    text: str
    is_correct: bool