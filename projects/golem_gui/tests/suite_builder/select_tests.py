from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify tests can be selected'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_builder')
    actions.store('test', actions.random_str())
    api.test.create_test('suite_builder', data.test)
    api.suite.create_access_random_suite('suite_builder')


def test(data):
    actions.wait(1)
    suite_builder.assert_test_not_selected(data.test)
    suite_builder.select_test(data.test)
    suite_builder.assert_test_counter(selected=1)
    suite_builder.save_suite()
    actions.refresh_page()
    suite_builder.assert_test_selected(data.test)
