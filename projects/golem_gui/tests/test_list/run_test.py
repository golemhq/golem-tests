from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list
from projects.golem_gui.pages import test_run_modal
from projects.golem_gui.pages import test_run_config_modal


description = 'Verify the user can run an empty test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('test', actions.random_str())
    api.test.create_test(data.project, data.test)
    common.navigate_menu('Tests')


def test(data):
    test_list.click_run_test_button(data.test)
    actions.wait_for_element_displayed(test_run_config_modal.config_modal)
    actions.click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result('success')


def teardown(data):
    api.project.delete_project(data.project)
