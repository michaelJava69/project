# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from project.constants import BASE_URL


TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None


def get_uncompleted_todos():
    response = get_todos()
    if response is None:
        return []
    else:
        todos = response.json()
        return [todo for todo in todos if todo.get('completed') == False]

def get_headers():
    response = get_todos()
    if response is None:
        return None
    else:
        my_dic = dict(response.headers)
        print (" returning dict")
        return my_dic

