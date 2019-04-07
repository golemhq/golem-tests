
description = 'Verify an error is displayed when an environment does not exist for project'

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
    send_keys(suite_builder.environments_input, 'not-existent')
    wait(0.5)
    click(suite_builder.save_button)
    common.assert_toast_message_is_displayed('Environment not-existent does not exist for project test')
    refresh_page()
    assert_alert_present()
    accept_alert()
    assert_element_value(suite_builder.environments_input, '')
