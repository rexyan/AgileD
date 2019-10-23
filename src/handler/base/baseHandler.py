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
            return await func(cls, request, *args, **kwargs)
        except Exception as e:
            return {'info': f'error: {e}'}

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
    def authorized(cls, *permission):
        """
        用户登录，权限校验装饰器
        :return:
        """

        def decorator(f):
            @wraps(f)
            async def decorated_function(request, *args, **kwargs):
                # 权限校验
                is_authorized = BaseHandler.check_authorization_status(request)

                if is_authorized:
                    # 若为 url 参数, 将参数更新至 kwargs 中。例如 http:xxx/xxx?name=zhangsan&age=20
                    kwargs.update(args[0].raw_args)
                    return await f(request, *args, **kwargs)
                else:
                    return response.json({'status': 'not_authorized'}, 403)

            return decorated_function

        return decorator

    @staticmethod
    def filter_es_term_bucket_value(term_name: str, es_term_result: dict) -> dict or list:
        """
        获取 es term 后 bucket 中的结果
        :param term_name:
        :param es_term_result:
        :return:
        """
        if es_term_result:
            return es_term_result.get("aggregations", {}).get(term_name, {}).get("buckets")
        else:
            return {}

    @staticmethod
    def filter_es_scroll_hits_value(scroll_hits_value: dict) -> (dict or list, str):
        """
        获取 es scroll 后 hits 中的结果
        :param scroll_hits_value:
        :return:
        """
        if scroll_hits_value:
            return scroll_hits_value.get("hits", {}).get("hits", {}), scroll_hits_value.get("_scroll_id")
        else:
            return {}, ""
