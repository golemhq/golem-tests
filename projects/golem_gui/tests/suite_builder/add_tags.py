
description = 'Verify the user can add tags to a suite'

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
    send_keys(suite_builder.tags_input, '001, 002')
    suite_builder.save_suite()
    refresh_page()
    assert_element_attribute(suite_builder.tags_input, 'value', '001, 002, ')
