import igdb

from igdb import http_methods
from igdb.api_requestor import APIRequestor
from igdb.igdb_object import IGDBObject
from igdb.util import convert_to_igdb_object

class APIResource(IGDBObject):
    @classmethod
    def retrieve(cls, pk, access_token=None, **params):
        instance = cls(pk, access_token, **params)
        retrieve_query = instance.generate_retrieve_query(pk)
        return instance.request_and_refresh(http_methods.HTTP_METHOD_POST, retrieve_query, params)

    def request_and_refresh(self, method, query=None, params=None):
        return self.request(method, self.class_url(), query, params)

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform "
                "actions on its subclasses (e.g. Game)"
            )
        return "{resource_name}s".format(
            resource_name=cls.RESOURCE_NAME
        )

    @classmethod
    def static_request(cls, method, url, access_token=None, params=None, headers=None):
        requestor = APIRequestor(
            access_token or igdb.access_token
        )
        response = requestor.request(method, url, params)
        igdb_object = convert_to_igdb_object(response, cls)
        return igdb_object

    def request(self, method, url, query=None, params=None, headers=None):
        requestor = APIRequestor(
            self.access_token,
        )
        params_query = requestor.generate_query(params)
        response = requestor.request(method, url, f"{query}{params_query}")
        igdb_object = convert_to_igdb_object(response, self.__class__)
        return igdb_object

    def generate_retrieve_query(self, pk):
        if isinstance(pk, list):
            pk = tuple(pk)

        # TODO: How to handle '<' and '>'?
        return f"where id = {pk};"
