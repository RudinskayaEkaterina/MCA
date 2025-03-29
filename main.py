from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List, Optional
import uvicorn


class Contact(BaseModel):
    id: int
    username: str
    given_name: str
    family_name: str
    full_name: str
    phone: List[str]
    email: List[str]
    birthdate: str

class Group(BaseModel):
    id: int
    title: str
    description: str
    contacts: List[int]

class ContactHandler:
    router = APIRouter(prefix="/api/v1/contact", tags=["contacts"])
    @staticmethod
    @router.get("")
    @router.post("")
    @router.put("")
    @router.delete("")
    async def handle_contact(contact: Optional[Contact] = None):
        return Contact(
            id=0,
            username="",
            given_name="",
            family_name="",
            full_name="",
            phone=[],
            email=[],
            birthdate=""
        )

class GroupHandler:
    router = APIRouter(prefix="/api/v1/group", tags=["groups"])
    @staticmethod
    @router.get("")
    @router.post("")
    @router.put("")
    @router.delete("")
    async def handle_group(group: Optional[Group] = None):
        return Group(
            id=0,
            title="",
            description="",
            contacts=[]
        )

def create_app():
    app = FastAPI(title="Contacts API", version="1.0")
    app.include_router(ContactHandler.router)
    app.include_router(GroupHandler.router)
    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=6080)