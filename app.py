from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from authx_extra.profiler import ProfilerMiddleware
import routes

app = FastAPI(
    title="YacineTV",
    description="This is an unofficial api wrapper for yacineapp.tv in python",
    version="1.0.0",
)

# هذا الجزء هو "التصريح" الذي يسمح لصفحتك بالاتصال بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
app.add_middleware(ProfilerMiddleware)

@app.get("/")
async def index():
    return {"message": "Hello World"}
