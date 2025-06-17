from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import user, account, order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # o ["*"] para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(account.router)
app.include_router(order.router)
