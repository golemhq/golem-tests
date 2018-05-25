
description = 'Verify the user can access a test by clicking on it in the test list.'

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
    store('description', 'description of the test')
    send_keys(test_builder.description, data.description)
    test_builder.save_test()
    refresh_page()
    test_builder.verify_description(data.description)
