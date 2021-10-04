from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify an alert is displayed when the user leaves the test builder with unsaved changes'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.add_step_to_test('test', 'click')
    actions.refresh_page()
    actions.assert_alert_present()
    actions.accept_alert()
