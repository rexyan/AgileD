from sanic import Blueprint
from config import CONFIG
from src.handler.health.healthHandler import HealthHandler
from src.handler.login.loginHandler import LoginHandler
from src.handler.data.RealEstateHandler import RealEstateHandler
from src.handler.data.CityRealEstateHandler import CityRealEstateHandler

# 蓝图
bp = Blueprint('AgileD', url_prefix=CONFIG.URL_PREFIX)

# 添加路由
# 健康检查
bp.add_route(uri="/v1/auth/health", handler=HealthHandler.as_view(), methods=["GET"])
# 登录
bp.add_route(uri="/v1/auth/login", handler=LoginHandler.as_view(), methods=["POST"])
# 获取全国城市楼盘数据
bp.add_route(uri="/v1/data/real_estate/term_city", handler=RealEstateHandler.as_view(), methods=["GET"])
# 获取某个城市楼盘数据
bp.add_route(uri="/v1/data/real_estate/city/<name>", handler=CityRealEstateHandler.as_view(), methods=["GET"])
