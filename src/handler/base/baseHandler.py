import uuid

from functools import wraps
from sanic.response import json
from sanic import response
from sanic.views import HTTPMethodView


class BaseHandler(HTTPMethodView):
    @staticmethod
    def get_response_id():
        """
        生成 response_id
        :return:
        """
        return str(uuid.uuid1())

    def build_response(self, return_data, return_code, http_code=200):
        api_result = {"data": return_data, "code": return_code, "response_id": BaseHandler.get_response_id()}
        return response.json(api_result, status=http_code)

    @staticmethod
    def check_authorization_status(request):
        """
        校验用户是否登录
        :param request:
        :return:
        """
        # TODO[rex]
        return True

    @classmethod
    def authorized(*permission):
        """
        用户登录，权限校验装饰器
        :return:
        """

        def decorator(f):
            @wraps(f)
            async def decorated_function(request, *args, **kwargs):
                # run some method that checks the request
                # for the client's authorization status
                is_authorized = BaseHandler.check_authorization_status(request)
                if is_authorized:
                    # the user is authorized.
                    # run the handler method and return the response
                    response = await f(request, *args, **kwargs)
                    return response
                else:
                    # the user is not authorized.
                    return json({'status': 'not_authorized'}, 403)

            return decorated_function

        return decorator
