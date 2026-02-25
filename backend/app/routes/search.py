# app/routes/search.py
from fastapi import APIRouter, Query
from app.services.search import search_songs
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Define the API schema
class Song(BaseModel):
    id: int
    title: str
    artist: str
    previewUrl: str
    albumArtwork: Optional[str] = None

class SearchResponse(BaseModel):
    results: List[Song]

@router.get("/", response_model=SearchResponse)
async def search(q: str = Query(..., description="Search term for songs or artists")):
    """
    Search for songs by title or artist.
    """
    results = search_songs(q)
    return {"results": results}

