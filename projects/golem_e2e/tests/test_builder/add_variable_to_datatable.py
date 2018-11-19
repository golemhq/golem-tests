
description = 'Verify the user can add a variable to the datatable'

pages = ['common',
         'index',
         'project_tests',
         'test_builder',
         'test_builder_common']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    project_tests.create_access_random_test()

def test(data):
    test_builder_common.add_variable_to_datatable('foo', ['bar'])
    test_builder.save_test()
    refresh_page()
    test_builder_common.assert_variable_in_datatable('foo')
