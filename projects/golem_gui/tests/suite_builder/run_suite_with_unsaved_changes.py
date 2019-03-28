

description = 'The suite is saved when running with unsaved changes'

pages = ['common',
         'index',
         'test_list',
         'suite_list',
         'suite_builder',
         'report_execution']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('run_suite')
    common.navigate_menu('Tests')
    test_list.create_access_test('empty_test_one')
    common.navigate_menu('Suites')
    store('suite_name', random('suite' + random('dddd')))
    suite_list.create_access_suite(data.suite_name)

def test(data):
    suite_builder.select_test('empty_test_one')
    click(suite_builder.run_suite_button)
    suite_builder.assert_suite_was_run(data.suite_name)
    suite_builder.access_suite_execution_from_toast()
    report_execution.assert_amount_of_tests(1)