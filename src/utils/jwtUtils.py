import jwt


class JwtUtils(object):

    @staticmethod
    def encode(encode_data: dict, secret_key: str, expire_time: int, algorithm="HS256") -> str:
        """
        JWT encode
        :param encode_data:
        :param secret_key:
        :param expire_time:
        :param algorithm:
        :return:
        """
        # 设置过期时间
        encode_data.update({'exp': expire_time})
        encoded = jwt.encode(encode_data, secret_key, algorithm=algorithm)
        return str(encoded, encoding='ascii')

    @staticmethod
    def decode(encoded_str: str, secret_key: str, algorithm="HS256") -> dict:
        """
        JWT decode
        :param encoded_str:
        :param secret_key:
        :param algorithm:
        :return:
        """
        return jwt.decode(encoded_str, secret_key, algorithm=algorithm)
