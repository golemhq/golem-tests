

description = 'Run a suite'

pages = ['common',
         'index',
         'project_tests',
         'suites',
         'suite_builder',
         'report_execution']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('run_suite')
    common.navigate_menu('Tests')
    tests.create_access_test('empty_test_one')
    common.navigate_menu('Tests')
    tests.create_access_test('empty_test_two')
    common.navigate_menu('Suites')
    store('suite_name', random('suite' + random('dddd')))
    suites.create_access_suite(data.suite_name)

def test(data):
    suite_builder.select_test('empty_test_one')
    suite_builder.select_test('empty_test_two')
    suite_builder.save_suite()
    click(suite_builder.run_suite_button)
    suite_builder.verify_suite_was_run(data.suite_name)
    suite_builder.access_suite_execution_from_toast()
    report_execution.verify_amount_of_tests(2)