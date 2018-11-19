
description = 'Verify the user can add an action to the setup'

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
    test_builder.add_action('click', where='setup')
    test_builder.add_action('send_keys', where='setup')
    test_builder.save_test()
    refresh_page()
    test_builder.assert_last_action('send_keys', where='setup')
