
description = 'Verify the user can access a suite by clicking on it in the suite list.'

pages = ['common',
         'index',
         'suites',
         'suite_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    suites.add_suite(data.suite_name)
    suites.access_suite(data.suite_name)
    verify_element_text(suite_builder.suite_name, data.suite_name)
