from sanic_openapi import doc
from src.handler.base.baseHandler import BaseHandler


class HealthHandler(BaseHandler):
    @doc.summary("健康检查")
    async def get(self, response):
        """
        登录
        :return:
        """
        return self.build_response("welcome login AgileD!", "90000")
