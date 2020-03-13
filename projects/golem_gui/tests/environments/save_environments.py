from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import environments


description = 'Verify project environments can be modified and saved'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_environments')


def test(data):
    code = '{\n"test": {"url": "foo"}\n}'
    common.navigate_menu('Environments')
    environments.set_value(code)
    actions.click(environments.save_button)
    common.assert_toast_message_is_displayed('Environments saved')
    actions.refresh_page()
    environments.assert_value(code)
