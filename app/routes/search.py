from fastapi import APIRouter, Query

from app.services.search_service import (
    search_notes_service
)

router = APIRouter()


@router.get("/search")
def search_notes(
    q: str = Query(...)
):
    result = search_notes_service(q)

    return result.data