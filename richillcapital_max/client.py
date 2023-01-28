

class MaxClient(object):
    """
    """
    
    REST_URL = "https://max-api.maicoin.com"
    WEBSOCKET_URL = "wss://max-stream.maicoin.com/ws"

    def __init__(self, api_key: str, secret_key: str) -> None:
        self._api_key: str = api_key
        self._secret_key: str = secret_key