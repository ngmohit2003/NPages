from app.db.supabase_client import supabase





# code post MVP or Barebone commit
def create_note_service(
        user_id: str,
        title: str,
        content: str
):
    return (
        supabase
        .table("notes")
        .insert({
            "user_id": user_id,
            "title": title,
            "content": content
        })
        .execute()
    )


def get_notes_service(
        user_id: str
):
    return (
        supabase
        .table("notes")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )



def get_note_by_id_service(
        note_id: str
):
    return (
        supabase
        .table("notes")
        .select("*")
        .eq("id", note_id)
        .execute()
    )





def update_note_service(
        note_id: str,
        data: dict
):
    return (
        supabase
        .table("notes")
        .update(data)
        .eq("id", note_id)
        .execute()
    )





def delete_note_service(
        note_id: str
):
    return (
        supabase
        .table("notes")
        .delete()
        .eq("id", note_id)
        .execute()
    )