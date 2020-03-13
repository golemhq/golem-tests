from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('suite', actions.random_str())
    api.suite.create_suite(data.project, data.suite)
    common.navigate_menu('Suites')


def test(data):
    new_name = data.suite + '_rename'
    suite_list.rename_suite(data.suite, new_name)
    assert not suite_list.suite_exists(data.suite)
    suite_list.assert_suite_exists(new_name)
    actions.refresh_page()
    suite_list.assert_suite_exists(new_name)


def teardown(data):
    api.project.delete_project(data.project)
