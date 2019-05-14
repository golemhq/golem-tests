
description = 'Verify the user can run an empty test'

tags = ['smoke']

pages = ['common',
         'index',
         'test_builder',
         'test_run_modal',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_' + random('dddd'))
    test_list.create_access_test(data.test_name)

def test(data):
    click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result_log_line(0, 'Test execution started: {}'.format(data.test_name))
    test_run_modal.assert_result_log_line(1, 'INFO Browser: chrome')
    test_run_modal.assert_result_log_line(2, 'INFO Test Result: SUCCESS')
    test_run_modal.assert_result('success')
    test_run_modal.assert_result_errors([])
    test_run_modal.assert_result_steps_is_empty()
