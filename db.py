#  thsi is where the app really connects to supabase to do work
import os       # imports py builtin  os module, use this to read env vars
from supabase import create_client      # imports create_client from supabase py SDK,   t his func builds a client  obj to talk to ur database/api
from dotenv import load_dotenv      # imports load_dotenv from same package, lets pyton read vars from .env file

load_dotenv()       # this loads the .env vars into the environment,  w/o this line .env file is nothing,   and with os.getenv we can access them
#  tl 1.
supabase = create_client(       #  creates a supabase client instance  and stores in supabase so u can reuse it everywhere
    os.getenv("SUPABASE_URL"),  # fetches ut project url from env
    os.getenv("SUPABASE_KEY")   # fetches the api key
)
