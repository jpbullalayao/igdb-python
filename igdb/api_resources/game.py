from igdb import api_endpoints
from igdb import http_methods

from igdb.api_resources.abstract.listable_api_resource import ListableAPIResource

class Game(ListableAPIResource):
    RESOURCE_NAME = "game"
    FIELD_PK = "id"

    @classmethod
    def base_url(cls, pk):
        base_url = cls.class_url()

        return f"{base_url}/{pk}"
