from openai import OpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from app.schemas.create_quiz import CreateQuizRequest
from app.schemas.quiz import QuizSchema

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def generate_quiz(request: CreateQuizRequest) -> QuizSchema:
    prompt = f"""
    Create a multiple-choice quiz using the following configuration:

    Title:
    {request.title}

    Description:
    {request.description}

    Language:
    {request.language}

    Number of questions:
    {request.question_count}

    Requirements:
    - Generate exactly {request.question_count} questions.
    - Each question must have exactly 4 alternatives.
    - Each question must have exactly one correct alternative.
    - Questions should cover different aspects of the subject.
    - Provide a short explanation for each question.
    - Keep the question statement and explanation as separate fields.
    - Write all quiz content in the specified language.
    """

    response = client.responses.parse(
        model=OPENAI_MODEL,
        input=prompt,
        text_format=QuizSchema
    )

    return response.output_parsed