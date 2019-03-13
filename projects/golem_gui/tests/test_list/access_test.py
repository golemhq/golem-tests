
description = 'Verify the user can access a test by clicking on it in the test list.'

pages = ['common',
         'index',
         'test_builder',
         'test_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')

def test(data):
    store('test_name', 'test_' + random('cccc'))
    test_list.add_test(data.test_name)
    test_list.access_test(data.test_name)
    assert_element_text(test_builder.test_name, data.test_name)
