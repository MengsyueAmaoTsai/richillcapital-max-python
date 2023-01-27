
import sys 
import os
sys.path.append(os.getcwd())

def test_create_client():
    """
    """ 
    from richillcapital_max.client import MaxClient
    
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")
    assert (api_key)
    assert (secret_key)

    client = MaxClient(api_key, secret_key)
    assert isinstance(client, MaxClient)