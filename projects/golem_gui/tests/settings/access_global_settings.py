from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import settings


description = 'Verify settings page contains global settings'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    common.navigate_menu('Global Settings')
    actions.assert_element_text(settings.title, 'Global Settings')
    actions.assert_element_displayed(settings.settings_editor)
