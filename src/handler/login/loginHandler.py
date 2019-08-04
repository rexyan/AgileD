from src.handler.base.baseHandler import BaseHandler
from src.controller.login.loginController import check_user, gen_jwt_token


class LoginHandler(BaseHandler):
    @BaseHandler.auth_params('username', "password")
    async def post(self, response, **kwargs):
        """
        登录
        :return:
        """
        # 获取用户名，密码
        request_params = kwargs.get("request_params", {})
        username, password = request_params.get("username"), request_params.get("password")

        # 校验用户信息
        user_info = check_user(username, password)
        jwt_token = gen_jwt_token(user_info)

        # 下发 jwt。后续要求请求头中含有 Authorization
        return self.build_response({"token": jwt_token})

    async def get(self, response):
        """
        登录
        :return:
        """
        return self.build_response("welcome login AgileD!", "90000")
