from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import urls
from projects.golem_gui.pages import environments
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_config_modal


description = 'The app will prompt the user to select one env when there is more than one'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_two_envs')
    actions.navigate(urls.environments('project_two_envs'))
    environments.set_value('{"foo": {}, "bar": {}}')
    actions.click(environments.save_button)
    api.test.create_access_random_test('project_two_envs')


def test(data):
    actions.click(test_builder.run_button)
    actions.wait_for_element_displayed(test_run_config_modal.config_modal)
    actions.assert_element_displayed(test_run_config_modal.config_modal)
    common.assert_info_bar_message('Select at least one environment')
