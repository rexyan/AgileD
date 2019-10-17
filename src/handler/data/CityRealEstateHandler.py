from sanic_openapi import doc
from loguru import logger as log

from src import CONFIG
from src.utils.ESUtils import ESUtils
from src.handler.base.baseHandler import BaseHandler


class CityRealEstateHandler(BaseHandler):
    @doc.summary("某个城市楼盘信息")
    @doc.description('某个具体某个城市楼盘详细信息')
    @doc.consumes({'Authorization': str}, location='header')
    @BaseHandler.authorized(["10001, 10002"])
    async def get(self, response, **kwargs):
        query_body = {
            "from": 0,
            "size": 0,
            "query": {
                "match_all": {}
            }
        }

        with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE, **CONFIG.ES_CONFIG) as es:
            search_result = es.search(query_body)

        log.info(f"api filter result:{search_result}")

        return self.build_response(search_result)
