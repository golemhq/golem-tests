
description = 'Verify the user can access a test by clicking on it in the test list.'

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
    store('description', 'description of the test')
    send_keys(test_builder.description, data.description)
    test_builder.save_test()
    refresh_page()
    test_builder.assert_description(data.description)
