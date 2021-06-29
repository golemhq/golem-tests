from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can create a new suite the suite list page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_list')
    common.navigate_menu('Suites')


def test(data):
    suite_list.dismiss_no_tests_alert_if()
    # to root
    suite_one = actions.random_str()
    suite_list.add_suite(suite_one)
    suite_list.assert_suite_exists(suite_one)
    # to folder
    suite_two = '{}.{}'.format(actions.random_str(), actions.random_str())
    suite_list.add_suite(suite_two)
    suite_list.assert_suite_exists(suite_two)
    actions.refresh_page()
    suite_list.assert_suite_exists(suite_one)
    suite_list.assert_suite_exists(suite_two)
