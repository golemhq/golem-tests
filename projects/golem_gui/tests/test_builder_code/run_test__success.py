from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder_code
from projects.golem_gui.pages import test_run_modal


description = 'Verify the user can run an empty test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder_code')
    api.test.create_access_test_code(data.project)


def test(data):
    actions.click(test_builder_code.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result('success')
