from fastapi import APIRouter, Header
from models.schemas import NoteData
from db.supabase_client import supabase


# tl-4
router = APIRouter()

@router.post("/notes")
def create_note(
    data: NoteData,
    authorization: str = Header(None)
):
    
    token = authorization.split(" ")[1]

    user = supabase.auth.get_user(token)

    res = supabase.table("notes").insert({
        "user_id": user.user.id,
        "title": data.title,
        "content": data.content
    }).execute()

    return res.data





@router.get("/notes")
def get_notes(
    authorization: str = Header(None)
):
    
    token = authorization.split(" ")[1]

    user = supabase.auth.get_user(token)

    res = supabase.table("notes") \
        .select("*") \
        .eq("user_id", user.user,id) \
        .execute()
    
    return res.data
