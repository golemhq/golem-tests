
description = 'Verify the use can dismiss unsaved changes alert and stay on the page'

pages = ['common',
         'index',
         'project_tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    project_tests.create_access_random_test()

def test(data):
    test_builder.add_action('click')
    refresh_page()
    verify_alert_present()
    dismiss_alert()
    test_builder.verify_last_action('click')