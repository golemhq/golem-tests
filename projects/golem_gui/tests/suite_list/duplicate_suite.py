from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can duplicate a suite'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('suite', actions.random_str())
    api.suite.create_suite(data.project, data.suite)
    common.navigate_menu('Suites')


def test(data):
    suite_list.dismiss_no_tests_alert_if()
    new_name = data.suite + 'copy'
    suite_list.duplicate_suite(data.suite, new_name)
    suite_list.assert_suite_exists(data.suite)
    suite_list.assert_suite_exists(new_name)


def teardown(data):
    api.project.delete_project(data.project)
