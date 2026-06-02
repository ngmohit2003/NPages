from fastapi import APIRouter, Header, Depends, HTTPException
from app.models.schemas import NoteData
from app.db.supabase_client import supabase

from .auth import oauth2_scheme

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

# tl-4
router = APIRouter()

# @router.post("/notes")
# def create_note(
#     data: NoteData,
#     authorization: str = Header(None)
# ):
    
#     token = authorization.split(" ")[1]

#     user = supabase.auth.get_user(token)

#     res = supabase.table("notes").insert({
#         "user_id": user.user.id,
#         "title": data.title,
#         "content": data.content
#     }).execute()

#     return res.data



@router.post("/notes")
def create_note(
    data: NoteData,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    res = supabase.table("notes").insert({
        "user_id": user.user.id,
        "title": data.title,
        "content": data.content
    }).execute()

    return res.data

























# @router.get("/notes")
# def get_notes(
#     # authorization: str = Header(None)
#     token: str = Depends(oauth2_scheme)
# ):
#     # if not authorization:
#     #     raise HTTPException(
#     #         status_code=401,
#     #         detail= "Authorization header Missing"
#     #     )
    
#     # token = authorization.split(" ")[1]

#     print(token)
    
#     user = supabase.auth.get_user(token)

#     res = supabase.table("notes") \
#         .select("*") \
#         .eq("user_id", user.user.id) \
#         .execute()
    
#     return res.data


# @router.get("/notes")
# def get_notes(
#     authorization: str = Header(None)
# ):
#     if not authorization:
#         raise HTTPException(
#             status_code=401,
#             detail="Authorization header missing"
#         )

#     token = authorization.split(" ")[1]
    
#     print("AUTH HEADER:", authorization)

#     user = supabase.auth.get_user(token)

#     res = supabase.table("notes") \
#         .select("*") \
#         .eq("user_id", user.user.id) \
#         .execute()

#     return res.data



@router.get("/notes")
def get_notes(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    res = (
        supabase.table("notes")
        .select("*")
        .eq("user_id", user.user.id)
        .execute()
    )

    return res.data