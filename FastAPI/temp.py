from fastapi import FastAPI, WebSocket
import asyncio
import websockets
app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You said: {data}")


async def test():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
        await ws.send("Hello")
        print(await ws.recv())

asyncio.run(test())