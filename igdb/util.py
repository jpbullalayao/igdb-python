from igdb.igdb_response import IGDBResponse
from igdb.igdb_object import IGDBObject


def convert_to_igdb_object(resp, cls):
    if isinstance(resp, IGDBResponse):
        igdb_response = resp
        resp = igdb_response.data

    if isinstance(resp, list):
        return [
            convert_to_igdb_object(result, cls) for result in resp
        ]

    elif isinstance(resp, dict) and not isinstance(
        resp, IGDBObject
    ):
        return cls.construct_from(resp)

    else:
        return resp
