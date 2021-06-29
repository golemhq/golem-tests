from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import settings
from projects.golem_gui.pages import api


description = 'Verify settings page contains settings for project and global'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('settings')


def test(data):
    common.navigate_menu('Project Settings')
    actions.assert_element_text(settings.title, 'Settings - Settings')
    actions.assert_element_displayed(settings.settings_editor)
