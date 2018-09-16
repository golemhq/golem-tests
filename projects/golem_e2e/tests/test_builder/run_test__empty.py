
description = 'Verify the user can run an empty test'

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
    click(test_builder.run_button)
    test_builder.wait_for_test_to_run()
    test_builder.assert_result_log_line(0, 'Test execution started: {}'.format(data.test_name))
    test_builder.assert_result_log_line(1, 'INFO Browser: chrome')
    test_builder.assert_result_log_line(2, 'INFO Test end: SUCCESS')
    test_builder.assert_result_modal_result('success')
    test_builder.assert_result_modal_errors([])
    test_builder.assert_result_modal_steps_is_empty()
