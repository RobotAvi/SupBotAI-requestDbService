from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Request(BaseModel):
    course: str
    name: str | None = None
    email: str | None = None
    phone: str | None = None

class RequestUpdate(BaseModel):
    course: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    
requests_db = {}
counter = 1

@app.post("/api/requests")
async def create_request(request: Request):
    global counter
    requests_db[counter] = request.dict()
    requests_db[counter]["id"] = counter
    counter += 1
    return requests_db[counter-1]

@app.get("/api/requests")
async def get_requests():
    return list(requests_db.values())

@app.get("/api/requests/{request_id}")
async def get_request(request_id: int):
    if request_id not in requests_db:
        raise HTTPException(404, detail="Заявка не найдена")
    return requests_db[request_id]

@app.put("/api/requests/{request_id}")
async def update_request(request_id: int, request: Request):
    if request_id not in requests_db:
        raise HTTPException(404, detail="Заявка не найдена")
    requests_db[request_id].update(request.dict(exclude_unset=True))
    return requests_db[request_id]

@app.delete("/api/requests/{request_id}")
async def delete_request(request_id: int):
    if request_id not in requests_db:
        raise HTTPException(404, detail="Заявка не найдена")
    del requests_db[request_id]
    return {"status": "Удалено"}

@app.patch("/api/requests/{request_id}")
async def patch_request(request_id: int, request: RequestUpdate):
    if request_id not in requests_db:
        raise HTTPException(404, detail="Заявка не найдена")
    stored_request = requests_db[request_id]
    update_data = request.dict(exclude_unset=True)
    stored_request.update(update_data)
    return stored_request