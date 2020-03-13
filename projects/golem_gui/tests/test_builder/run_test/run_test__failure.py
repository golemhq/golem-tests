from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_run_modal


description = 'Verify the user can run a test with a failure'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder.add_action('fail', params=["'failure message'"])
    actions.click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result_log_line(0, 'Test execution started: {}'.format(data.test_name))
    test_run_modal.assert_result_log_line(1, 'INFO Browser: chrome')
    test_run_modal.assert_result_log_line(2, 'ERROR AssertionError: failure message')
    test_run_modal.assert_result('failure')
    test_run_modal.assert_result_errors(['AssertionError: failure message'])
    test_run_modal.assert_result_steps(['Failure - AssertionError: failure message'])
