
description = 'Verify the user can create a new suite from the project page'

tags = ['smoke']

pages = ['index',
         'common',
         'suite_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    suite_list.add_suite(data.suite_name)
    suite_list.assert_suite_exists(data.suite_name)
