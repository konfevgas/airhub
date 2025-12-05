from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import list_airports

app = FastAPI(title="AirHub API")

# allow your Vite dev server
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (GET, POST, etc.)
    allow_headers=["*"],
)


app.include_router(list_airports.router)
