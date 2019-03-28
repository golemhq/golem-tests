
description = 'Verify an alert is shown when exiting suite builder with unsaved changes'

pages = ['common',
         'index',
         'suite_list',
         'suite_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')
    suite_list.create_access_random_suite()


def test(data):
    clear_element(suite_builder.processes_input)
    send_keys(suite_builder.processes_input, 3)
    refresh_page()
    assert_alert_present()
    accept_alert()
    assert_element_value(suite_builder.processes_input, '1')
    clear_element(suite_builder.processes_input)
    send_keys(suite_builder.processes_input, 3)
    refresh_page()
    assert_alert_present()
    dismiss_alert()
    suite_builder.save_suite()
    common.navigate_menu('Suites')
    assert_title_contains(': Suites')
