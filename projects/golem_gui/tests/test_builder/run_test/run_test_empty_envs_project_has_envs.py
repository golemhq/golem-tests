from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_config_modal


description = 'The app will prompt the user to select one env when there is more than one'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    api.project.set_environments(data.project, '{"foo": {}, "bar": {}}')
    api.test.create_access_test(data.project)


def test(data):
    actions.click(test_builder.run_button)
    actions.wait_for_element_displayed(test_run_config_modal.config_modal)
    actions.assert_element_displayed(test_run_config_modal.config_modal)
    common.assert_info_bar_message('Select at least one environment')
