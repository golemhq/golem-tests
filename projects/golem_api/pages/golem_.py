import requests

from golem import execution

from projects.golem_api.pages import utils


GOLEM_ACTIONS_ENDPOINT = 'api/golem/actions'
DEFAULT_BROWSER_ENDPOINT = 'api/golem/default-browser'


def golem_actions_url(base_url):
    return '{}{}'.format(base_url, GOLEM_ACTIONS_ENDPOINT)


def default_browser_url(base_url):
    return '{}{}'.format(base_url, DEFAULT_BROWSER_ENDPOINT)


def get_golem_actions(user=None):
    return requests.get(golem_actions_url(execution.data.env.url),
                        headers=utils.common_headers(user))


def get_default_browser(user=None):
    return requests.get(default_browser_url(execution.data.env.url),
                        headers=utils.common_headers(user))
