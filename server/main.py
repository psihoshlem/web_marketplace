from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, users


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)