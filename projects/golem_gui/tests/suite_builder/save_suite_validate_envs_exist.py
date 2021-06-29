from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify an error is displayed when an environment does not exist for project'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_builder')
    api.suite.create_access_suite(data.project)


def test(data):
    actions.send_keys(suite_builder.environments_input, 'not-existent')
    actions.wait(0.5)
    actions.click(suite_builder.save_button)
    common.assert_toast_message_is_displayed('Environment not-existent does not exist for project {}'.format(data.project))
    actions.refresh_page()
    actions.assert_alert_present()
    actions.accept_alert()
    actions.assert_element_value(suite_builder.environments_input, '')
