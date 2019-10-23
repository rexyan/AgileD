from sanic import Blueprint
from config import CONFIG
from src.handler.health.healthHandler import HealthHandler
from src.handler.login.loginHandler import LoginHandler
from src.handler.data.realEstateHandler import RealEstateHandler
from src.handler.data.cityRealEstateHandler import CityRealEstateHandler
from src.handler.data.realEstateTypeHandler import RealEstateTypeHandler
from src.handler.data.cityRealEstateTypeHandler import CityRealEstateTypeHandler

# 蓝图
bp = Blueprint('AgileD', url_prefix=CONFIG.URL_PREFIX)

# 添加路由
# 健康检查
bp.add_route(uri="/v1/auth/health", handler=HealthHandler.as_view(), methods=["GET"])
# 用户登录
bp.add_route(uri="/v1/auth/login", handler=LoginHandler.as_view(), methods=["POST"])
# 获取全国城市楼盘分组
bp.add_route(uri="/v1/data/re/term/city", handler=RealEstateHandler.as_view(), methods=["GET"])
# 获取某个城市楼盘数据
bp.add_route(uri="/v1/data/re/city", handler=CityRealEstateHandler.as_view(), methods=["GET"])
# 获取全国楼盘分组
bp.add_route(uri="/v1/data/re/term/type", handler=RealEstateTypeHandler.as_view(), methods=["GET"])
# 获取某个城市某种楼盘类型数据
bp.add_route(uri="/v1/data/re/city/type", handler=CityRealEstateTypeHandler.as_view(), methods=["GET"])

