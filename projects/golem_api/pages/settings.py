import requests

from golem import execution

from projects.golem_api.pages import utils


SAVE_SETTINGS_ENDPOINT = 'api/settings/save'


def save_settings_url(base_url):
    return '{}{}'.format(base_url, SAVE_SETTINGS_ENDPOINT)


def save_settings(project_name, project_settings, global_settings, user=None):
    json_ = {
        'project': project_name,
        'projectSettings': project_settings,
        'globalSettings': global_settings
    }
    return requests.put(save_settings_url(execution.data.env.url),
                        headers=utils.common_headers(user), json=json_)
