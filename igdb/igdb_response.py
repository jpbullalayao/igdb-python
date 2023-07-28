import json


class IGDBResponse(object):
    def __init__(self, body):
        self.data = json.loads(body)
