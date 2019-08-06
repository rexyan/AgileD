from src.handler.base.baseHandler import BaseHandler
from src.utils.ES import ES


class LouPanHandler(BaseHandler):
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
