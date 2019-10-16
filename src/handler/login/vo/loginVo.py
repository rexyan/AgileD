class LoginReqVo:
    """
    user login request vo
    """
    username = str
    password = str


class LoginRspVo:
    """
    user login response vo
    """
    data = {"token": str}
    code = str
    response_id = str

