from golem import execution

from projects.golem_api.pages import auth


def url(endpoint, base_url=None):
    if base_url is None:
        base_url = execution.data.env.url
    return '{}api{}'.format(base_url, endpoint)


def headers(user=None):
    token = auth.get_token(user)
    return {'Content-Type': 'application/json', 'token': token}
