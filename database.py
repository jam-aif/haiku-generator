import os
from supabase import create_client, Client
from datetime import datetime
from typing import List, Dict

def get_supabase_client() -> Client:
    """Initialize Supabase client"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")

    return create_client(url, key)

def create_haikus_table():
    """Create the haikus table if it doesn't exist"""
    supabase = get_supabase_client()

    # This will be run manually via Supabase dashboard
    # SQL:
    # CREATE TABLE haikus (
    #     id SERIAL PRIMARY KEY,
    #     theme VARCHAR(255) NOT NULL,
    #     season VARCHAR(50) NOT NULL,
    #     mood VARCHAR(50) NOT NULL,
    #     keywords TEXT,
    #     haiku_text TEXT NOT NULL,
    #     created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    # );
    pass

def save_haiku(theme: str, season: str, mood: str, keywords: str, haiku_text: str) -> int:
    """Save a generated haiku to the database"""
    supabase = get_supabase_client()

    data = {
        "theme": theme,
        "season": season,
        "mood": mood,
        "keywords": keywords if keywords else None,
        "haiku_text": haiku_text,
        "created_at": datetime.now().isoformat()
    }

    try:
        result = supabase.table("haikus").insert(data).execute()
        return result.data[0]["id"]
    except Exception as e:
        print(f"Error saving haiku: {e}")
        raise

def get_all_haikus() -> List[Dict]:
    """Retrieve all haikus from the database"""
    supabase = get_supabase_client()

    try:
        result = supabase.table("haikus").select("*").order("created_at", desc=True).execute()
        return result.data
    except Exception as e:
        print(f"Error retrieving haikus: {e}")
        raise