import requests


def request(url):

    """
    Returns a dictionary of response code and content based on a url.

    :param url:
    :return:
    """

    response = {}

    try:
        r = requests.get(url)

        response = {
            'code': r.status_code,
            'content': r.content,
            'url': r.url
        }
    except ConnectionError:
        response = {
            'code': 503,
            'content': None,
            'url': url
        }

    return response
