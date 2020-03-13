from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the use can dismiss unsaved changes alert and stay on the page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder.add_action('click')
    actions.refresh_page()
    actions.assert_alert_present()
    actions.dismiss_alert()
    test_builder.assert_last_action('click')
