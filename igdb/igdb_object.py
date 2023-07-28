import json

class IGDBObject(dict):
    def __init__(self, pk, access_token=None, **params):
        super(IGDBObject, self).__init__()

        self.access_token = access_token

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

    def __repr__(self):
        ident_parts = [type(self).__name__]
        ident_parts.append("id=%s" % (self.get("id"),))

        unicode_repr = "<%s> JSON: %s" % (
            " ".join(ident_parts),
            str(self),
        )

        return unicode_repr

    def __str__(self):
        return json.dumps(
            self,
            sort_keys=True,
            indent=2,
        )
    
