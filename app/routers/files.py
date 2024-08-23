from fastapi import (APIRouter, File, UploadFile)
from fastapi.responses import JSONResponse
from ..settings import (BASE_DIR, os, uuid, OutPutData)
from ..models.files import Files, Session

files = APIRouter()

@files.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(content={"message": "Invalid file type"}, status_code=400)
    file.filename = f"{uuid.uuid4().hex}_{file.filename.split('.')[0]}.{file.filename.split('.')[-1]}"
    if not os.path.exists(f"{BASE_DIR}/media/files"):
        os.makedirs(f"{BASE_DIR}/media/files")
    
    with Session() as db:
        try:
            file_db = Files(
                filename=file.filename,
                content_type=file.content_type,
                size=file.size,
                extencion=file.filename.split(".")[-1],
                url=f"/media/files/{file.filename}"
            )
            db.add(file_db)
            db.commit()
        except Exception as e:
            db.rollback()
            return JSONResponse(content={"message": "Error uploading file"}, status_code=500)
    data = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size,
        "extencion": file.filename.split(".")[-1],
        "url":f"/media/files/{file.filename}"
    }
    with open(f"{BASE_DIR}/media/files/{file.filename}", "wb") as f:
        f.write(file.file.read())
    OutPutData(f"File Created into: {BASE_DIR}/media/files/{file.filename}\n Data: {data}")

    return JSONResponse(content=data)

@files.post("/upload-multiple/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    return JSONResponse(content={"filenames": [file.filename for file in files]})