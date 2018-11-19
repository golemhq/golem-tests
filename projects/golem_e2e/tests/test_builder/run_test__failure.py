
description = 'Verify the user can run a test with a failure'

pages = ['common',
         'index',
         'project_tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_' + random('dddd'))
    project_tests.create_access_test(data.test_name)

def test(data):
    test_builder.add_action('fail', params=["'failure message'"])
    click(test_builder.run_button)
    test_builder.wait_for_test_to_run()
    test_builder.assert_result_log_line(0, 'Test execution started: {}'.format(data.test_name))
    test_builder.assert_result_log_line(1, 'INFO Browser: chrome')
    test_builder.assert_result_log_line(2, 'ERROR AssertionError: failure message')
    test_builder.assert_result_modal_result('failure')
    test_builder.assert_result_modal_errors(['AssertionError: failure message'])
    test_builder.assert_result_modal_steps(['Failure - AssertionError: failure message'])
