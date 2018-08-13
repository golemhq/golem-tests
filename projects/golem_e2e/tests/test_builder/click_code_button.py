
description = 'Verify the test code page opens when clicking Code button'

pages = ['common',
         'index',
         'tests',
         'test_builder',
         'test_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    tests.create_access_random_test()

def test(data):
    click(test_builder.code_button)
    verify_element_present(test_builder_code.preview_button)
