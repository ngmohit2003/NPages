from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
# from db import supabase
from app.db.supabase_client import supabase

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.routes.auth import router as auth_router
from app.routes.notes import router as notes_router

from app.routes.search import router as search_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(notes_router)
app.include_router(search_router)

#  tl 1.
@app.get("/")
def root():
    return {"message": "API running"}

# @app.get("/test-db")

# def test_db():
#     res = supabase.table("notes").select("*").execute()
#     return res.data




# #  tl 2.
# class AuthData(BaseModel):
#     email:str
#     password:str

# @app.post("/signup")
# def signup(data: AuthData):
#     try:
#         res = supabase.auth.sign_up({
#             "email": data.email.strip(),   # sawagger inserts garbage in the json field while provinding the user credentials, strip()  cleans that garbage.
#             "password": data.password
#         })

#         return {
#             "message": "User Created",
#             "User": res.user
#         }
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))







# @app.post("/login")
# def login(data: AuthData):
#     try:
#         res = supabase.auth.sign_in_with_password({
#             "email": data.email.strip(),
#             "password": data.password
#         })

#         return {
#             "access_token": res.session.access_token,
#             "user": res.user
#         }
    
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=401, detail="Invalid Credentials")







# #  tl 3.
# class NoteData(BaseModel):
#     title: str
#     content: str

# security = HTTPBearer()


# @app.post("/notes")
# def create_note(
#     note: NoteData,
#     # authorization: str = Header(None)
#     credentials: HTTPAuthorizationCredentials = Depends(security)
# ):
#     try:
#         token = credentials.credentials

#         user = supabase.auth.get_user(jwt=token)


#         print(user) #debug method
#         print(type(user))
#         print(dir(user))

#         res = supabase.table("notes").insert({
#             "user_id": user.user.id,
#             "title": note.title,
#             "content": note.content
#         }).execute()

#         return res.data

#     except Exception as e:    #remember this debug method   helps a lot to understand whats going on and explain the error neatly....
#         print("ERROR:", e)
#         raise HTTPException(status_code=500, detail=str(e))

#     # if not authorization:
#     #     raise HTTPException(status_code=401, detail="Authorization header missing")

#     # token = authorization.split(" ")[1]

#     # return {"message": "Note Created"}

    
