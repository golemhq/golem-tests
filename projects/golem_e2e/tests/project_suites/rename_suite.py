
description = 'Verify the user can rename a suite'

pages = ['common',
         'index',
         'suites']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    store('new_suite_name', data.suite_name + '_rename')
    suites.add_suite(data.suite_name)
    suites.verify_suite_exists(data.suite_name)
    suites.rename_suite(data.suite_name, data.new_suite_name)
    suites.verify_suite_exists(data.new_suite_name)
