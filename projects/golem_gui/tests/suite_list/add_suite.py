from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can create a new suite the suite list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Suites')


def test(data):
    suite_list.dismiss_no_tests_alert_if()
    # to root
    actions.store('suite_one', actions.random_str())
    suite_list.add_suite(data.suite_one)
    suite_list.assert_suite_exists(data.suite_one)
    # to folder
    actions.store('suite_two', 'folder1.' + actions.random_str())
    suite_list.add_suite(data.suite_two)
    suite_list.assert_suite_exists(data.suite_two)
    actions.refresh_page()
    suite_list.assert_suite_exists(data.suite_one)
    suite_list.assert_suite_exists(data.suite_two)


def teardown(data):
    api.project.delete_project(data.project)
