import requests

from projects.golem_api.pages.utils import url, headers


GOLEM_ACTIONS_ENDPOINT = '/golem/actions'
DEFAULT_BROWSER_ENDPOINT = '/golem/default-browser'


def get_golem_actions(user=None):
    return requests.get(url(GOLEM_ACTIONS_ENDPOINT), headers=headers(user))


def get_default_browser(user=None):
    return requests.get(url(DEFAULT_BROWSER_ENDPOINT), headers=headers(user))
