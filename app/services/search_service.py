from app.db.supabase_client import supabase


def search_notes_service(search_term: str):
    result = (
        supabase
        .rpc(
            "search_notes",
            {
                "search_term": search_term
            }
        )
        .execute()
    )

    return result