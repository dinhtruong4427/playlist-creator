# app/routes/similar_songs.py

from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

from app.services.similar_songs import find_similar_songs

router = APIRouter(prefix="", tags=["similar-songs"])

class SimilarSong(BaseModel):
    id: int
    title: str
    artist: str
    albumArtwork: str
    previewUrl: str


class SimilarSongsResponse(BaseModel):
    results: List[SimilarSong]


@router.get("/", response_model=SimilarSongsResponse)
async def similar_songs(
    song_id: int = Query(..., description="ID of the selected song"),
    top_n: int = Query(5, ge=1, le=20),
):
    """
    Find songs similar to the given song using audio embeddings.
    """
    results = find_similar_songs(
        song_id=song_id,
        top_n=top_n,
    )

    return {"results": results}
