from fastapi import APIRouter
from app.models.schemas import AuthData
from app.db.supabase_client import supabase

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

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
