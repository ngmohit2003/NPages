from pydantic import BaseModel

# tl-4
class AuthData(BaseModel):
    email:str
    password: str

class NoteData(BaseModel):
    title: str
    content: str
