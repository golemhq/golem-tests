
description = 'Verify the user can duplicate a suite'

pages = ['common',
         'index',
         'suite_list',
         'suite_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')
    store('suite_name', 'suite_' + random('cccc'))
    store('new_suite_name', data.suite_name + '_new')
    suite_list.create_access_suite(data.suite_name)
    clear_element(suite_builder.processes_input)
    send_keys(suite_builder.processes_input, '3')
    suite_builder.save_suite()
    common.navigate_menu('Suites')


def test(data):
    suite_list.duplicate_suite(data.suite_name, data.new_suite_name)
    common.assert_toast_message_is_displayed('File was copied')
    assert suite_list.suite_exists(data.suite_name)
    assert suite_list.suite_exists(data.new_suite_name)
    refresh_page()
    assert suite_list.suite_exists(data.suite_name)
    assert suite_list.suite_exists(data.new_suite_name)
    suite_list.access_suite(data.new_suite_name)
    assert_element_value(suite_builder.processes_input, '3')
