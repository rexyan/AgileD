from sanic_openapi import doc
from loguru import logger as log

from src import CONFIG
from src.utils.esUtils import ESUtils
from src.handler.base.baseHandler import BaseHandler


class RealEstateHandler(BaseHandler):
    @doc.summary("获取全国城市楼盘分组")
    @doc.description('获取全国城市楼盘分组')
    @doc.consumes({'Authorization': str}, location='header', required=True)
    @BaseHandler.authorized(["10001, 10002"])
    async def get(self, response, **kwargs):
        """
        获取全国城市楼盘分组
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

        with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE) as es:
            search_result = es.search(query_body)
        filter_result = RealEstateHandler.filter_es_term_bucket_value("City", search_result)
        log.info(f"api filter result:{filter_result}")

        return self.build_response(filter_result)
