import asyncio
import websockets
import config

async def send_websocket_request():
    uri = "ws://heroboxim.yingxiong.com:8190/ws-community-im-websocket"
    headers = {
        "appVersion": "3.3.0",
        "devCode": "26720144bb7c43264bd4dc542a7db9bad",
        "sourse": "android",
        "token": f"{config.token}",
        "User-Agent": "okhttp/3.10.0"
    }

    async with websockets.connect(uri, extra_headers=headers) as websocket:
        # Optionally, you can send a message or wait for a response
        # await websocket.send("Your message")
        response = await websocket.recv()
        print(response)
        # print("WebSocket connection established")

asyncio.run(send_websocket_request())