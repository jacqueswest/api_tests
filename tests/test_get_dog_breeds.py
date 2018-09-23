import pytest
from yaml import load
from pprint import pprint
from lib.helper import get_request


@pytest.fixture(scope="module")
def data_setup():
    global data

    with open(file="./test_data_lib/api_test_data.yaml") as f:
        data = load(f).get("dog_apis")


def test_get_all_breeds(data_setup):
    """ Return a list all dog breeds """

    results = get_request(url=data.get("all_breeds"))
    pprint(results)


def test_verify_retriever_breed(data_setup):
    """ Verify that the retriever breed is in the list """

    results = get_request(url=data.get("all_breeds"))
    breed = results.get("message").keys()
    assert "retriever" in breed


def test_get_retriever_sub_breeds(data_setup):
    """ Return a list all retriever sub-breeds """

    breed_url = data.get("sub_breed")
    results = get_request(url=breed_url.format(breed="retriever"))
    pprint(results)


def test_get_random_image_golden_retriever(data_setup):
    """ Return a random image link to a golden retriever image """

    random_image_url = data.get("sub_breed_random_image")
    results = get_request(url=random_image_url.format(breed="retriever", sub_breed="golden"))
    pprint(results)
