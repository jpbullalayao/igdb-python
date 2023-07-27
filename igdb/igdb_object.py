# import igdb

# from igdb.api_requestor import APIRequestor
# from igdb.util import convert_to_igdb_object

class IGDBObject(dict):
    def __init__(self, pk, access_token=None, **params):
        super(IGDBObject, self).__init__()

        object.__setattr__(self, "access_token", access_token)

        if pk:
            pk_field = self.get_pk_field()
            self[pk_field] = pk

    def __setattr__(self, k, v):
        self[k] = v
        return None

    def __getattr__(self, k):
        return self[k]

    @classmethod
    def get_pk_field(cls):
        return cls.FIELD_PK

    @classmethod
    def construct_from(cls, resp):
        instance = cls(resp.get(cls.get_pk_field()))
        instance.refresh_from(resp)
        return instance

    def refresh_from(self, values):
        for k, v in iter(values.items()):
            super(IGDBObject, self).__setitem__(k, v)

    # def request(self, method, url, access_token=None, params=None):
    #     requestor = APIRequestor(
    #         access_token or igdb.access_token
    #     )

    #     response = requestor.request(method, url, params)
    #     igdb_object = convert_to_igdb_object(response, self.__class__)
    #     return igdb_object
