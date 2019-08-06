from elasticsearch import Elasticsearch


class ES:
    def __init__(self, index):
        self.index = index

    def __enter__(self, ip="127.0.0.1"):
        self.es = Elasticsearch([ip])
        return self

    def search_data(self, query_body):
        return self.es.search(index=self.index, body=query_body)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
