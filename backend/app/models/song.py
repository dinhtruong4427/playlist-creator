from pydantic import BaseModel

class Song(BaseModel):
    title: str
    artist: str
    image_url: str | None = None