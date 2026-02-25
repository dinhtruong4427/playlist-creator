# app/routes/similar_songs.py

from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

from app.services.similar_songs import find_similar_songs

router = APIRouter(prefix="", tags=["similar-songs"])


# ---------- Response Models ----------

class SimilarSong(BaseModel):
    id: int
    title: str
    artist: str
    albumArtwork: str
    previewUrl: str


class SimilarSongsResponse(BaseModel):
    results: List[SimilarSong]


# ---------- Endpoint ----------

@router.get("/", response_model=SimilarSongsResponse)
async def similar_songs(
    song_url: str = Query(..., description="Preview URL of the selected song"),
    song_name: str = Query(..., description="Name of the selected song"),
    top_n: int = Query(5, ge=1, le=20),
):
    """
    Find songs similar to the given song using audio embeddings.
    """
    results = find_similar_songs(
        song_url=song_url,
        song_name=song_name,
        top_n=top_n,
    )

    return {"results": results}
