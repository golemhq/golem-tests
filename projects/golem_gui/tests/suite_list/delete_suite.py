from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list


description = 'Verify the user can rename a suite from the suite list'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('suite', actions.random_str())
    api.suite.create_suite(data.project, data.suite)
    common.navigate_menu('Suites')


def test(data):
    suite_list.delete_suite(data.suite)
    assert not suite_list.suite_exists(data.suite)
    actions.refresh_page()
    assert not suite_list.suite_exists(data.suite)


def teardown(data):
    api.project.delete_project(data.project)
