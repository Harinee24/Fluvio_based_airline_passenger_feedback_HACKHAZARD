from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
fastapi_app = FastAPI()

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_app.get("/")
async def root():
    return {"message": "✅ Socket.IO backend is running"}

# --- Log when consumer or frontend connects ---
@sio.event
async def connect(sid, environ):
    print(f"✅ Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"❌ Client disconnected: {sid}")

# --- Receive data from consumer ---
@sio.event
async def tweet(sid, data):
    print(f"📨 Tweet received from consumer.py: {data}")
    await sio.emit("tweet", data) 

app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)
