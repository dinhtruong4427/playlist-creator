from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import search, similar_songs

app = FastAPI(
    title="Playlist Builder API",
    version="0.1.0"
)

# CORS for frontend (Vite dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(
    similar_songs.router,
    prefix="/api/similar",
    tags=["similar-songs"]
)

@app.get("/")
def health_check():
    return {"status": "ok"}
