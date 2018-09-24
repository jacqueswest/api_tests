import requests


def get_request(url):
    """ Creates a API request to the given url """
    
    return requests.get(url).json()
