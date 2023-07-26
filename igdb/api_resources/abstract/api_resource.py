import igdb

from igdb import http_methods
from igdb.api_requestor import APIRequestor
from igdb.igdb_object import IGDBObject
from igdb.util import convert_to_igdb_object

class APIResource(IGDBObject):
    @classmethod
    def retrieve(cls, pk, access_token=None, **params):
        requestor = APIRequestor(
            access_token
        )

        instance = cls(pk, access_token, **params)
        instance.refresh(requestor)
        return instance

    def refresh(self, requestor):
        response = requestor.request(http_methods.HTTP_METHOD_POST, self.class_url())
        igdb_object = convert_to_igdb_object(response, self.__class__)
        self.refresh_from(igdb_object)
        return self

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

    def request(self, method, url, params=None, headers=None):
        requestor = APIRequestor(
            self.access_token,
        )
        response = requestor.request(method, url, params)
        igdb_object = convert_to_igdb_object(response, self.__class__)
        return igdb_object