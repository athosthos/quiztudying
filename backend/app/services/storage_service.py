from google.cloud import storage
from app.core.config import GCP_PROJECT_ID, GCS_BUCKET_NAME

client = storage.Client(
    project=GCP_PROJECT_ID
)

bucket = client.bucket(GCS_BUCKET_NAME)

def upload_file(
    file,
    file_name: str,
    content_type: str,
    quiz_id: int
) -> str:

    file_path = f"{quiz_id}/{file_name}"

    blob = bucket.blob(file_path)

    blob.upload_from_file(
        file,
        content_type=content_type,
        rewind=True
    )

    return f"gs://{GCS_BUCKET_NAME}/{file_path}"