from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can add an action to the teardown'

skip = True


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.add_action('click', where='teardown')
    test_builder.save_test()
    actions.refresh_page()
    test_builder.assert_last_action('click', where='teardown')
