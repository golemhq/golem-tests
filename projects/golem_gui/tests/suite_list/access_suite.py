
description = 'Verify the user can access a suite by clicking on it in the suite list.'

pages = ['common',
         'index',
         'suite_list',
         'suite_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    suite_list.add_suite(data.suite_name)
    suite_list.access_suite(data.suite_name)
    assert_element_text(suite_builder.suite_name, data.suite_name)
