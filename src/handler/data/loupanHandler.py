from sanic_openapi import doc
from loguru import logger as log

from src import CONFIG
from src.utils.ESUtils import ESUtils
from src.handler.base.baseHandler import BaseHandler


class LouPanHandler(BaseHandler):
    @doc.summary("获取每个城市对应的楼盘数量")
    @doc.consumes({'Authorization': str}, location='header')
    @BaseHandler.authorized(["10001, 10002"])
    async def get(self, response, **kwargs):
        """
        获取每个城市对应的楼盘数量
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

        with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE, **CONFIG.ES_CONFIG) as es:
            search_result = es.search_data(query_body)
        filter_result = LouPanHandler.filter_es_term_bucket_value("City", search_result)
        log.info(f"api filter result:{filter_result}")

        return self.build_response(filter_result)
