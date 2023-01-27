

class MaxClient(object):

    def __init__(self, api_key: str, secret_key: str) -> None:
        self._api_key: str = api_key
        self._secret_key: str = secret_key