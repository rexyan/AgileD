from .config import Config


class ProConfig(Config):
    """
    生产环境配置
    """
    # 运行配置
    RUN_MODEL = {
        "host": "0.0.0.0",
        "port": 9000,
        "debug": False
    }

    # 安全 Key
    SECRET_KEY = "AgileD:Pro:4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg"

    # ES 配置
    ES_CONFIG = {
        "address": "192.168.16.161",
        "username": "",
        "password": ""
    }

    # ES 索引配置
    ES_INDEX_REAL_ESTATE = "lianjialoupan"
    ES_INDEX_SECOND_HAND_HOUSING = "lianjiaershoufang"

    # log 设置, 单个日志最大存储 5 MB，最长时间为1天
    LOG_RETENTION = "1 days"
    LOG_ROTATION = "5 MB"
