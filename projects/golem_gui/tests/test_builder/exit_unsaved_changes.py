
description = 'Verify an alert is displayed when the user leaves the test builder with unsaved changes'

pages = ['common',
         'index',
         'test_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    test_builder.add_action('click')
    refresh_page()
    assert_alert_present()
    accept_alert()
