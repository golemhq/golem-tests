
description = 'Verify the user can add an action to a test and save it successfully'

pages = ['common',
         'index',
         'tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    tests.create_access_random_test()

def test(data):
    test_builder.add_action(data.action)
    test_builder.save_test()
    refresh_page()
    test_builder.verify_last_action(data.action)
