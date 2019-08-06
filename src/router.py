from sanic import Blueprint
from config import CONFIG
from src.handler.login.loginHandler import LoginHandler
from src.handler.data.loupanHandler import LouPanHandler

# 蓝图
bp = Blueprint('AgileD', url_prefix=CONFIG.URL_PREFIX)

# 添加路由
bp.add_route(uri="/v1/auth/login", handler=LoginHandler.as_view(), methods=["POST"])  # 登录
bp.add_route(uri="/v1/data/loupan/term_city", handler=LouPanHandler.as_view(), methods=["GET"])  # 获取全国城市楼盘数据
