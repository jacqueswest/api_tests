import requests


def get_request(url):
    """ Creates an API request to the given url """
    
    return requests.get(url).json()
