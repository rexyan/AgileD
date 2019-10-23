from loguru import logger as log
from elasticsearch import Elasticsearch

from config import CONFIG


class ESUtils:
    def __init__(self, index, es_config=CONFIG.ES_CONFIG):
        """
        初始化连接信息
        :param index:
        :param es_config:
        """
        self.index = index
        self.address = es_config.setdefault("address", "127.0.0.1")
        self.username = es_config.setdefault("username", "")
        self.password = es_config.setdefault("password", "")

    def __enter__(self):
        """
        创建连接实例
        :return:
        """
        self.es = Elasticsearch([self.address])
        return self

    def search(self, query_body):
        """
        普通查询
        :param query_body:
        :return:
        """
        result = self.es.search(index=self.index, body=query_body)
        log.info(f"es query body:{query_body}, query result:{result}")
        return result

    def get(self, doc_type, doc_id):
        """
        get
        :param doc_type:
        :param doc_id:
        :return:
        """
        result = self.es.get(index=self.index, doc_type=doc_type, id=doc_id)
        log.info(f"es get result:{result}")
        return result

    def scroll(self, body={}, scroll="5m"):
        """
        scroll 第一次查询，返回数据和 scroll id
        :param body:
        :param scroll:
        :return:
        """
        result = self.es.search(index=self.index, scroll=scroll, body=body)
        return result

    def next_scroll(self, scroll_id, scroll="5m"):
        """
        只需传入 scroll_id 即可进行后续的查询
        :param scroll_id:
        :param scroll:
        :return:
        """
        result = self.es.scroll(scroll_id=scroll_id, scroll=scroll)
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        pass


if __name__ == "__main__":
    with ESUtils(CONFIG.ES_INDEX_REAL_ESTATE) as es:
        search_result = es.scroll()
        sid = search_result.get("_scroll_id")
        print(sid)

        re1 = es.scroll_next(sid)
        print(re1)
