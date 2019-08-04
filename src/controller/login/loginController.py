import time
from src.utils.jwtUtils import JwtUtils
from config import CONFIG


def check_user(username, password):
    """
    数据库校验用户信息
    :param username:
    :param password:
    :return:
    """
    # TODO [rex]
    if username and password:
        return {"username": username, "password": password, "permission": ["10001"]}


def gen_jwt_token(encode_data):
    return JwtUtils.encode(encode_data, CONFIG.SECRET_KEY, int(time.time() + 3600))
