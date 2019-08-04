import uuid

from functools import wraps
import json
from sanic import response
from sanic.views import HTTPMethodView


class BaseHandler(HTTPMethodView):
    @staticmethod
    async def dec_func(cls, func, request, *args, **kwargs):
        """
        执行被装饰函数
        :param cls:
        :param func:
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            response = await func(cls, request, *args, **kwargs)
            return response
        except Exception as e:
            return {'info': 'error'}

    def auth_params(*keys):
        """
        api请求参数验证
        :param keys: params
        :return:
        """

        def wrapper(func):
            @wraps(func)
            async def auth_param(cls, request=None, *args, **kwargs):
                request_params, params = {}, []

                # 根据不同请求进行参数 key 获取 'POST', 'PUT'
                if request.method in ['POST', 'PUT']:
                    try:
                        post_data = json.loads(str(request.body, encoding='utf-8'))
                    except Exception as e:
                        return BaseHandler.build_response(cls, {'info': 'error', 'desc': '解析参数错误！'}, "30001", 402)
                    else:
                        request_params.update(post_data)
                        params = [key for key, value in post_data.items() if value]

                # 根据不同请求进行参数 key 获取 'GET', 'DELETE'
                elif request.method in ['GET', 'DELETE']:
                    request_params.update(request.args)
                    params = [key for key, value in request.args.items() if value]
                else:
                    return BaseHandler.build_response(cls, {'info': 'error', 'desc': '不支持的 method！'}, "30001", 402)

                # 判断所传递参数中是否有期待参数
                if set(keys).issubset(set(params)):
                    kwargs['request_params'] = request_params
                    return await BaseHandler.dec_func(cls, func, request, *args, **kwargs)
                else:
                    return BaseHandler.build_response(cls, {'info': 'error', 'desc': f'参数不正确，缺少参数：{set(keys).difference(set(params))}'}, "30001", 402)
            return auth_param
        return wrapper

    @staticmethod
    def get_response_id():
        """
        生成 response_id
        :return:
        """
        return str(uuid.uuid1())

    def build_response(self, return_data, return_code="90000", http_code=200):
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
