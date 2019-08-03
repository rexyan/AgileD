import os


def load_config():
    """
    Load  config
    """

    mode = os.environ.get('MODE', 'DEV')
    try:
        if mode == 'PRO':
            from .proConfig import ProConfig
            return ProConfig
        elif mode == 'DEV':
            from .devConfig import DevConfig
            return DevConfig
        else:
            from .devConfig import DevConfig
            return DevConfig
    except ImportError:
        from .config import Config
        return Config


CONFIG = load_config()
