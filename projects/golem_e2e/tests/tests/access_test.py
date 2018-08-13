
description = 'Verify the user can access a test by clicking on it in the test list.'

pages = ['common',
         'index',
         'tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    tests.add_test(data.test_name)
    tests.access_test(data.test_name)
    verify_element_text(test_builder.test_name, data.test_name)
