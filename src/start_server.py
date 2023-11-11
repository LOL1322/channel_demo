from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import sys 

sys.path.append('C:/channel_demo')

from src.server.router import rout
import uvicorn
import settings


app = FastAPI(title='Films API', version='0.1 Alpha')

app.include_router(router=rout)


@app.router.get(path='/')
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)