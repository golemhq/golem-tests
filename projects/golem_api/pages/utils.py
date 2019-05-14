from projects.golem_api.pages import auth


def common_headers(user=None):
    token = auth.get_token(user)
    return {'Content-Type': 'application/json', 'token': token}
