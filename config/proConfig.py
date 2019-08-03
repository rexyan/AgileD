from .config import Config


class ProConfig(Config):
    """
    生产环境配置
    """

    RUN_MODEL = {
        "host": "0.0.0.0",
        "port": 9000,
        "debug": False
    }
