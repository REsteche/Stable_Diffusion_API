from fastapi import FastAPI
from app.route import health, image_association, metrics, logs
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(image_association.router)
app.include_router(metrics.router)
app.include_router(logs.router)