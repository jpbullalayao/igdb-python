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
        print('values', values)
        for k, v in iter(values.items()):
            super(IGDBObject, self).__setitem__(k, v)
