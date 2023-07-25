import requests
import igdb

from igdb.igdb_response import IGDBResponse

class APIRequestor(object):
    def __init__(
        self,
        access_token=None,
        client_id=None,
        api_base=None,
    ):
        self.access_token = access_token or igdb.access_token
        self.api_base = api_base or igdb.api_base
        self.client_id = client_id or igdb.client_id

    def request(self, http_method, url, params=None):
        rbody = self.request_raw(http_method, url, params)
        resp = self.interpret_response(rbody)
        return resp

    def request_raw(self, http_method, url, params=None):
        if url.startswith("/"):
            url = url[1:]  # Removes slash

        abs_url = "{api_base}{url}".format(
            api_base=self.api_base,
            url=url
        )
        headers = self.request_headers()
        method_to_use = getattr(requests, http_method.lower())

        # TODO: Handle other status codes besides 200
        return method_to_use(abs_url, headers=headers, params=params)

    def request_headers(self):
        headers = {
            "Accept": "application/json",
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.access_token}",
        }
        return headers

    def interpret_response(self, rbody):
        resp = IGDBResponse(rbody.text)
        return resp
