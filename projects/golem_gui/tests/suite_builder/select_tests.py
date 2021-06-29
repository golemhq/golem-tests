from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify tests can be selected'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_builder')
    data.test = api.test.create_test(data.project)
    api.suite.create_access_suite(data.project)


def test(data):
    actions.wait(1)
    suite_builder.assert_test_not_selected(data.test)
    suite_builder.select_test(data.test)
    suite_builder.assert_test_counter(selected=1)
    suite_builder.save_suite()
    actions.refresh_page()
    suite_builder.assert_test_selected(data.test)
