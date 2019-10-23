from sanic_openapi import doc
from src.handler.base.baseHandler import BaseHandler
from src.controller.login.loginController import check_user, gen_jwt_token
from src.handler.login.vo.loginVo import LoginReqVo, LoginRspVo


class LoginHandler(BaseHandler):
    @doc.summary('用户登录')
    @doc.description('WJT 登录接口，此接口获取 token, 其余接口需要在请求头中传递此 token 值')
    @doc.consumes(LoginReqVo, location='body')
    @doc.produces(LoginRspVo)
    @BaseHandler.auth_params('username', "password")
    async def post(self, response, **kwargs):
        """
        用户登录
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
