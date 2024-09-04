from starlette.endpoints import HTTPEndpoint
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

class HomePage(HTTPEndpoint):
    async def get(self, request):
        return templates.TemplateResponse("sea_fight.html", {"request": request})