from fastapi import APIRouter
from models.schemas import AuthData
from db.supabase_client import supabase

#tl-4
router = APIRouter()

@router.post("/signup")
def signup(data: AuthData):
    return supabase.auth.sign_up({
        "email": data.email,
        "password": data.password
    })



@router.post("/login")
def login(data: AuthData):
    res = supabase.auth.sign_in_with_password({
        "email": data.email,
        "password": data.password
    })

    return {
        "access_token": res.session.access_token
    }
