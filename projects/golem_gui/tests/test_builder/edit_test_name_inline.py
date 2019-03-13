
description = 'Verify the user can edit the test name by clicking on the title'

pages = ['common',
         'index',
         'test_list',
         'page_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_builder')
    common.navigate_menu('Tests')
    store('test_name', 'test'+random('dddddd'))
    test_list.create_access_test(data.test_name)


def test(data):
    store('new_test_name', 'new_test_name'+random('ddddd'))
    click(test_builder.test_name)
    assert_element_displayed(test_builder.test_name_input)
    assert_element_value(test_builder.test_name_input, data.test_name)
    send_keys(test_builder.test_name_input, 'new')
    press_key(test_builder.test_name_input, 'TAB')
    common.assert_toast_message_is_displayed('File was renamed')
    wait_for_element_displayed(test_builder.test_name, 5)
    assert_element_text(test_builder.test_name, data.test_name + 'new')
    refresh_page()
    assert_element_text(test_builder.test_name, data.test_name + 'new')
