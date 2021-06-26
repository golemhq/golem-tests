import requests

from projects.golem_api.pages.utils import url, headers


GET_USERS_ENDPOINT = '/users'
GET_USER_ENDPOINT = '/users/user'
NEW_USER_ENDPOINT = '/users/new'
EDIT_USER_ENDPOINT = '/users/edit'
DELETE_USER_ENDPOINT = '/users/delete'
RESET_USER_ENDPOINT = '/users/reset-password'
RESET_OWN_PASSWORD_ENDPOINT = '/user/reset-password'


def get_users(user=None):
    return requests.get(url(GET_USERS_ENDPOINT), headers=headers(user))


def get_user(username, user=None):
    return requests.get(url(GET_USER_ENDPOINT), headers=headers(user),
                        params={'username': username})


def create_new_user(username, password, email=None, is_superuser=False,
                    project_permissions=None, user=None):
    if project_permissions is None:
        project_permissions = {}
    json_ = {
        'username': username,
        'email': email,
        'password': password,
        'isSuperuser': is_superuser,
        'projectPermissions': project_permissions,
    }
    return requests.put(url(NEW_USER_ENDPOINT), headers=headers(user), json=json_)


def edit_user(username, new_username=None, new_email=False, new_is_superuser=None,
              new_project_permissions=None, user=None):
    json_ = {
        'oldUsername': username,
        'newUsername': new_username,
        'email': new_email,
        'isSuperuser': new_is_superuser,
        'projectPermissions': new_project_permissions,
    }
    return requests.post(url(EDIT_USER_ENDPOINT), headers=headers(user), json=json_)


def delete_user(username, user=None):
    return requests.delete(url(DELETE_USER_ENDPOINT), headers=headers(user),
                           json={'username': username})


def reset_password(username, new_password, user=None):
    return requests.post(url(RESET_USER_ENDPOINT), headers=headers(user),
                         json={'username': username, 'newPassword': new_password})
