import os


class Config(object):
    """
    全局配置
    """
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    URL_PREFIX = "api"
