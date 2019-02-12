
description = 'Verify that the user can access the "HTML", "JUnit" and JSON reports by url'


pages = ['common',
         'index',
         'utils',
         'suite_builder',
         'report_execution']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_reports')
    utils.create_access_simple_suite()


def test(data):
    suite_builder.run_suite()
    suite_builder.access_suite_execution_from_toast()
    report_execution.wait_until_execution_end()
    current_url = get_current_url()
    navigate(current_url + 'html/')
    assert_element_text_contains(report_execution.title, 'test reports - simple suite')
    navigate(current_url + 'html-no-images/')
    assert_element_text_contains(report_execution.title, 'test reports - simple suite')
    navigate(current_url + 'json/')
    assert '"totals_by_result"' in get_browser().page_source
    navigate(current_url + 'junit/')
    assert_url_contains('/junit')
