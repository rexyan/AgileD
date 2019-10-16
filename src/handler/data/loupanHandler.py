from src.utils.ES import ES
from sanic_openapi import doc
from src.handler.base.baseHandler import BaseHandler


class LouPanHandler(BaseHandler):
    @doc.summary("获取每个城市对应的楼盘数量")
    @doc.consumes({'Authorization': str}, location='header')
    @BaseHandler.authorized(["10001, 10002"])
    async def get(self, response, **kwargs):
        """
        查询每个城市对应的楼盘数
        :param response:
        :param kwargs:
        :return:
        """
        query_body = {
            "size": 0,
            "aggs": {
                "City": {
                    "terms": {"field": "spider_city"}
                }
            }
        }

        with ES("lianjia_loupan") as es:
            search_result = es.search_data(query_body)

        return self.build_response(search_result)
