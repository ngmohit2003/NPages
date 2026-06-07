from fastapi import APIRouter, Header, Depends, HTTPException

from app.db.supabase_client import supabase

from .auth import oauth2_scheme

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.schemas import NoteData, UpdateNoteData


from app.services.notes_service import (
    create_note_service,
    get_notes_service,
    get_note_by_id_service,
    update_note_service,
    delete_note_service

)



security = HTTPBearer()

# tl-4
router = APIRouter()








# /////////////////////////////////////////////////////////////////////////////////////////
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

# /////////////////////////////////////////////////////////////////////////////////////////# /////////////////////////////////////////////////////////////////////////////////////////

















@router.post("/notes")
def create_note(
    data: NoteData,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    # res = supabase.table("notes").insert({
    #     "user_id": user.user.id,
    #     "title": data.title,
    #     "content": data.content
    # }).execute()

    res = create_note_service(
        user.user.id,
        data.title,
        data.content
    )

    return res.data






@router.get("/notes")
def get_notes(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    # res = (
    #     supabase.table("notes")
    #     .select("*")
    #     .eq("user_id", user.user.id)
    #     .execute()
    # )

    res = get_notes_service(
        user.user.id
    )

    return res.data








# tl-5
# getting single note
# if User A
#     ↓
# tries note_id from User B returns -> []
@router.get("/notes/{note_id}")
def get_single_note(
    note_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    user = supabase.auth.get_user(token)

    # res = (
    #     supabase.table("notes")
    #     .select("*")
    #     .eq("id", note_id)
    #     .eq("user_id", user.user.id)
    #     .execute()
    # )

    res = get_note_by_id_service(note_id)

    if not res.data:
        raise HTTPException(
            status_code=404,
            detail="Note Not Found"
        )
    
    note = res.data[0]

    if note["user_id"] != user.user.id:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    return note







# update endpoint
@router.put("/notes/{note_id}")
def update_note(
    note_id: str,
    data: UpdateNoteData,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    user = supabase.auth.get_user(token)

    existing = get_note_by_id_service(note_id)

    if not existing.data:
        raise HTTPException(
            status_code=404,
            detail="Note Not Found"
        )
    
    note = existing.data[0]

    if note["user_id"] != user.user.id:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )
    
    update_data = data.model_dump(exclude_unset=True)

    # res = (
    #     supabase.table("notes")
    #     .update({
    #         "title": data.title,
    #         "content": data.content
    #     })
    #     .eq("id", note_id)
    #     .eq("user_id", user.user.id)
    #     .execute()
    # )

    res = update_note_service(
        note_id,
        update_data
    )

    return res.data




# delete endpoint
@router.delete("/notes/{note_id}")
def delete_note(
    note_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    user = supabase.auth.get_user(token)


    existing = get_note_by_id_service(note_id)

    if not existing.data:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    note = existing.data[0]

    if note["user_id"] != user.user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )


    # res = (
    #     supabase.table("notes")
    #     .delete()
    #     .eq("id", note_id)
    #     .eq("user_id", user.user.id)
    #     .execute()
    # )

    res = delete_note_service(note_id)

    return {
        "message": "Note deleted successfully"
    }

    # return {
    #     "deleted": res.data
    # }