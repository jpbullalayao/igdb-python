from igdb import http_methods
from igdb.api_requestor import APIRequestor

from igdb.api_resources.abstract.api_resource import APIResource
from igdb.util import convert_to_igdb_object

class ListableAPIResource(APIResource):

    @classmethod
    def list(cls, access_token=None, **params):
        requestor = APIRequestor(access_token)

        url = cls.class_url()
        response = requestor.request(http_methods.HTTP_METHOD_POST, url, params)
        igdb_object = convert_to_igdb_object(response, cls)
        return igdb_object
