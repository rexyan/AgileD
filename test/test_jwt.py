import time

import pytest
from src.utils.jwtUtils import JwtUtils
from config import CONFIG


@pytest.mark.smoke
@pytest.mark.jwt
def test_jwt_encode():
    encode_data = {
        "user_name": "san.zhang",
        "permission": ["10001", "10002"],
        "admin": False
    }
    secret_key = CONFIG.SECRET_KEY
    expire_time = int(time.time()) + 3600
    assert JwtUtils.encode(encode_data, secret_key, expire_time) is not None


@pytest.mark.smoke
@pytest.mark.jwt
def test_jwt_decode():
    secret_key = CONFIG.SECRET_KEY
    encoded_str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJzYW4uemhhbmciLCJwZXJtaXNzaW9uIjpbIjEwM" \
                  "DAxIiwiMTAwMDIiXSwiYWRtaW4iOmZhbHNlLCJleHAiOjE1NjQ4OTEwMDZ9.CGuhP7AO9qbCG-aNK7ClDvFLFpZAqbenGXKa" \
                  "nAjMHeA"
    assert JwtUtils.decode(encoded_str, secret_key) is not None
