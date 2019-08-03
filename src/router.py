from sanic import Blueprint
from config import CONFIG
from src.handler.login.loginHandler import LoginHandler

# 蓝图
bp = Blueprint('AgileD', url_prefix=CONFIG.URL_PREFIX)

# 添加路由
bp.add_route(uri="/v1/auth/login", handler=LoginHandler.as_view(), methods=["POST"])
