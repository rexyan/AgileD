from sanic_openapi import doc
from loguru import logger as log

from src import CONFIG
from src.utils.esUtils import ESUtils
from src.handler.base.baseHandler import BaseHandler


class CityRealEstateHandler(BaseHandler):
    @doc.summary("获取某个城市楼盘数据")
    @doc.description('获取某个城市楼盘数据')
    @doc.consumes({"city_name": str})  # url 参数, 默认非必须
    @doc.consumes({"scroll_id": str})  # url 参数, 默认非必须
    @doc.consumes({'Authorization': str}, location='header', required=True)
    @BaseHandler.authorized(["10001, 10002"])
    async def get(self, response, **kwargs):
        """
        获取某个城市楼盘数据
        :param response:
        :param kwargs: city_name, 城市名称. scroll_id, scroll_id
        :return:
        """
        if kwargs.get("city_name"):
            # 第一次 scroll 查询
            query_body = {
                "query": {
                    "match": {
                        "spider_city": kwargs.get("city_name")
                    }
                }
            }
            with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE) as es:
                scroll_result = es.scroll(body=query_body)
        else:
            # 往后的 scroll 查询
            with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE) as es:
                scroll_result = es.next_scroll(scroll_id=kwargs.get("scroll_id"))

        log.info(f"api filter result:{scroll_result}")
        scroll_hits_value, scroll_id = CityRealEstateHandler.filter_es_scroll_hits_value(scroll_result)
        result = {"hits": scroll_hits_value, "scroll_id": scroll_id}
        return self.build_response(result)
