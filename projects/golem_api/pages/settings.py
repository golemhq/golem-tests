import requests

from projects.golem_api.pages.utils import url, headers


SAVE_GLOBAL_SETTINGS_ENDPOINT = '/settings/global/save'
SAVE_PROJECT_SETTINGS_ENDPOINT = '/settings/project/save'
GET_GLOBAL_SETTINGS_ENDPOINT = '/settings/global'
GET_PROJECT_SETTINGS_ENDPOINT = '/settings/project'


def save_global_settings(settings, user=None):
    return requests.put(url(SAVE_GLOBAL_SETTINGS_ENDPOINT), headers=headers(user),
                        json={'settings': settings})


def save_project_settings(project_name, settings, user=None):
    json_ = {
        'project': project_name,
        'settings': settings,
    }
    return requests.put(url(SAVE_PROJECT_SETTINGS_ENDPOINT), headers=headers(user), json=json_)


def get_global_settings(user=None):
    return requests.get(url(GET_GLOBAL_SETTINGS_ENDPOINT), headers=headers(user))


def get_project_settings(project_name, user=None):
    return requests.get(url(GET_PROJECT_SETTINGS_ENDPOINT), headers=headers(user),
                        params={'project': project_name})
