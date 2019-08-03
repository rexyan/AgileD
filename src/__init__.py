import uuid

from sanic import Sanic
from config import CONFIG
from src.router import bp

app = Sanic(__name__)


@app.middleware('request')
async def set_request_id(request):
    request.headers.update({'X-Request-ID': str(uuid.uuid4())})

app.blueprint(bp)
app.config.from_object(CONFIG)
