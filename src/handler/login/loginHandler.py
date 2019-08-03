from src.handler.base.baseHandler import BaseHandler


class LoginHandler(BaseHandler):
    async def post(self, response):
        """
        登录
        :return:
        """
        return self.build_response("aaaa", "90000")

    async def get(self, response):
        """
        登录
        :return:
        """
        return self.build_response("welcome login AgileD!", "90000")
