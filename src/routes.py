from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

from src.endpoints import HomePage
from src.ws import WSSF

routes = [
    Route('/', HomePage, methods=['GET']),
    WebSocketRoute('/ws', WSSF),
    WebSocketRoute('/ws_sf', WSSF),
    Mount('/static', StaticFiles(directory='static'), name='static')
]