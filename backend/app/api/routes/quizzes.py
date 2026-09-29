from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas.create_quiz import CreateQuizRequest
from app.services.quiz_service import create_quiz
from app.services.storage_service import upload_file

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"]
)

ALLOWED_FILE_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "image/jpeg",
    "image/png",
    "image/webp"
}

@router.post("")
def create_quiz_endpoint(request: CreateQuizRequest):
    return create_quiz(request)

@router.post("/{quiz_id}/files")
def upload_quiz_file(
    quiz_id: int,
    file: UploadFile = File(...)
):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    file_uri = upload_file(
        file=file.file,
        file_name=file.filename,
        content_type=file.content_type,
        quiz_id=quiz_id
    )

    return {
        "message": "File uploaded successfully",
        "file_name": file.filename,
        "content_type": file.content_type,
        "uri": file_uri
    }