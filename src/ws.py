import typing

from icecream import ic
from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket



class WSSF(WebSocketEndpoint):
    encoding = 'json'

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
    async def on_disconnect(self, websocket: WebSocket) -> None:
        pass
    async def on_message(self, websocket: WebSocket) -> None:
        await websocket.send_json({'message': 'Connected'})
