
description = 'Verify the user can create a new suite from the project page'

pages = ['common',
         'index',
         'suites']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    suites.add_suite(data.suite_name)
    suites.verify_suite_exists(data.suite_name)
