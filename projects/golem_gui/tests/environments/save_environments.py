from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import environments
from projects.golem_gui.pages import api


description = 'Verify project environments can be modified and saved'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_environments')


def test_save_environments(data):
    code = '{\n"test": {"url": "foo"}\n}'
    common.navigate_menu('Environments')
    environments.set_value(code)
    actions.click(environments.save_button)
    common.assert_toast_message_is_displayed('Environments saved')
    actions.refresh_page()
    assert environments.get_value() == code
