import requests

from golem import execution


tokens = {}

default_user = {
    'username': 'admin',
    'password': 'admin'
}

TOKEN_ENDPOINT = '/auth/token'


def get_token_request(username, password):
    url = '{}api{}'.format(execution.data.env.url, TOKEN_ENDPOINT)
    return requests.post(url, headers={'Content-Type': 'application/json'},
                         json={'username': username, 'password': password})


def get_token(user=None):
    global tokens
    if user:
        username = user['username']
        password = user['password']
    else:
        username = default_user['username']
        password = default_user['password']

    if username not in tokens:
        response = get_token_request(username, password)
        tokens[username] = response.json()
    return tokens[username]
