import requests

from golem import execution


tokens = {}

default_user = {
    'username': 'admin',
    'password': 'admin'
}

TOKEN_ENDPOINT = 'api/auth/token'


def auth_token_url(base_url):
    return '{}{}'.format(base_url, TOKEN_ENDPOINT)


def get_token_request(username, password):
    return requests.post(auth_token_url(execution.data.env.url),
                         headers={'Content-Type': 'application/json'},
                         json={'username': username, 'password': password})


def get_token(user=None):
    global tokens
    if user:
        username = user.username
        password = user.password
    else:
        username = default_user['username']
        password = default_user['password']

    if username not in tokens:
        response = get_token_request(username, password)
        tokens[username] = response.json()
    return tokens[username]
