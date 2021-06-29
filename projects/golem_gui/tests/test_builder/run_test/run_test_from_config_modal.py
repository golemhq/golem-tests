from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_config_modal
from projects.golem_gui.pages import test_run_modal


description = 'Verify the user can run a test from the config modal'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_run')
    api.test.create_access_test(data.project)


def test(data):
    test_builder.open_run_configurations_modal()
    actions.click(test_run_config_modal.run_button)
    test_run_modal.assert_result('success')
