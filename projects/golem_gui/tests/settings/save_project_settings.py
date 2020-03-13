from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import settings
from projects.golem_gui.pages import index


description = 'Verify project settings can be modified and saved'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_project_settings')


def test(data):
    common.navigate_menu('Project Settings')
    settings.set_settings_value('{\n"search_timeout": 10\n}')
    actions.click(settings.save_button)
    common.assert_toast_message_is_displayed('Settings saved')
    actions.refresh_page()
    settings.assert_settings_value('{\n"search_timeout": 10\n}')
