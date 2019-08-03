from .config import Config


class DevConfig(Config):
    """
    开发环境配置
    """

    RUN_MODEL = {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True
    }
