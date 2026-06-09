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

from fastapi import UploadFile, File
import uuid











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






# Create File-Upload Route for pdf/png/img...
@router.post("/notes/{note_id}/upload")
def upload_bucket_file(
    note_id: str,
    file: UploadFile = File(...),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    note = supabase.table("notes") \
        .select("*") \
        .eq("id", note_id) \
        .eq("user_id", user.user.id) \
        .execute()

    if not note.data:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    file_extension = file.filename.split(".")[-1]

    unique_filename = (
        f"{user.user.id}/"
        f"{uuid.uuid4()}.{file_extension}"
    )

    file_content = file.file.read()

    # supabase.storage \          #this section is not sending the content type.
    #     .from_("note-files") \
    #     .upload(
    #         unique_filename,
    #         file_content
    #     )

    supabase.storage \
    .from_("note-files") \
    .upload(
        unique_filename,
        file_content,
        file_options={
            "content-type": file.content_type
        }
    )

    file_url = supabase.storage \
        .from_("note-files") \
        .get_public_url(unique_filename)

    # res = supabase.table("note_files").insert({    #You do not store the storage path.
    #     "note_id": note_id,
    #     "file_name": file.filename,
    #     "file_url": file_url
    # }).execute()

    res = supabase.table("note_files").insert({
    "note_id": note_id,
    "file_name": file.filename,
    "file_url": file_url,
    "storage_path": unique_filename
    }).execute()

    return res.data




@router.get("/notes/{note_id}/files")
def get_bucket_files(
    note_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    user = supabase.auth.get_user(token)

    note = (
        supabase.table("notes")
        .select("*")
        .eq("id", note_id)
        .eq("user_id", user.user.id)
        .execute()
    )

    if not note.data:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    files = (
        supabase.table("note_files")
        .select("*")
        .eq("note_id", note_id)
        .order("created_at", desc=True)
        .execute()
    )

    return files.data






@router.delete("/files/{file_id}")
def delete_bucket_file(
    file_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    # Get JWT token
    token = credentials.credentials

    # Get current user
    user = supabase.auth.get_user(token)

    # Find file
    file_res = (
        supabase.table("note_files")
        .select("*")
        .eq("id", file_id)
        .execute()
    )

    if not file_res.data:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    file_data = file_res.data[0]

    print(file_data)   #trying debug bucket  delete issue
    print(file_data["storage_path"])

    # Find note linked to file
    note_res = (
        supabase.table("notes")
        .select("*")
        .eq("id", file_data["note_id"])
        .eq("user_id", user.user.id)
        .execute()
    )

    if not note_res.data:
        raise HTTPException(
            status_code=403,
            detail="You do not own this file"
        )

    # Delete from Storage
    # supabase.storage \
    #     .from_("note-files") \
    #     .remove([
    #         file_data["storage_path"]
    #     ])

    try:
        storage_result = (
            supabase.storage
            .from_("note-files")
            .remove([
                file_data["storage_path"]
            ])
        )

        print(storage_result)

    except Exception as e:
        print("STORAGE DELETE ERROR:", e)
        raise

  
    print("STORAGE DELETE RESULT:")  #trying debug bucket  delete issue
    print(storage_result)
    print(type(storage_result))

    # Delete DB record
    supabase.table("note_files") \
        .delete() \
        .eq("id", file_id) \
        .execute()

    return {
        "message": "File deleted successfully"
    }