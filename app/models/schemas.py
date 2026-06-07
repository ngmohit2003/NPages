from pydantic import BaseModel
from typing import Optional


# tl-4
class AuthData(BaseModel):
    email:str
    password: str

class NoteData(BaseModel):
    title: str
    content: str



# tl-5
# class UpdateNoteData(BaseModel):
#     title: str
#     content: str


class UpdateNoteData(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None