from fastapi import (APIRouter, File, UploadFile)
from fastapi.responses import JSONResponse
from ..settings import (BASE_DIR, os, uuid, OutPutData)

files = APIRouter()

@files.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(content={"message": "Invalid file type"}, status_code=400)
    file.filename = f"{uuid.uuid4().hex}_{file.filename.split('.')[0]}.{file.filename.split('.')[-1]}"
    data = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size,
        "extencion": file.filename.split(".")[-1]
    }
    with open(f"{BASE_DIR}/media/files/{file.filename}", "wb") as f:
        f.write(file.file.read())
    OutPutData(f"File Created into: {BASE_DIR}/media/files/{file.filename}\n Data: {data}")

    return JSONResponse(content=data)

@files.post("/upload-multiple/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    return JSONResponse(content={"filenames": [file.filename for file in files]})