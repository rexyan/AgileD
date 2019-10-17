from loguru import logger as log
from elasticsearch import Elasticsearch


class ESUtils:
    def __init__(self, index, **es_config):
        self.index = index
        self.address = es_config.setdefault("address", "127.0.0.1")
        self.username = es_config.setdefault("username", "")
        self.password = es_config.setdefault("password", "")

    def __enter__(self):
        self.es = Elasticsearch([self.address])
        return self

    def search(self, query_body):
        result = self.es.search(index=self.index, body=query_body)
        log.info(f"es query body:{query_body}, query result:{result}")
        return result

    def mget(self, query_body):
        result = self.es.mget(query_body, doc_type=None, index=self.index, params=None)
        log.info(f"es query body:{query_body}, query result:{result}")
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
