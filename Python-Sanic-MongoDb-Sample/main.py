from sanic import Sanic, Blueprint
from sanic.response import text

from sanic_limiter import Limiter, get_remote_address

from sanic import Sanic
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
from sanic_motor import BaseModel

app = Sanic(__name__)
limiter = Limiter(app, global_limits=['5 per minute'], key_func=get_remote_address)
bp = Blueprint('some_bp')
limiter.limit("5 per minute")(bp)


@bp.route("/")
@limiter.limit("5/minute")
async def root(request):
    return text("root")

app.blueprint(bp)

app.run(host="0.0.0.0", port=5000, debug=True)