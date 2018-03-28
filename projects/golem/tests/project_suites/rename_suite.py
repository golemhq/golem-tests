
description = 'Verify the user can rename a suite'

pages = ['login',
         'index',
         'project_suites']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test_rename')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    store('new_suite_name', data.suite_name + '_rename')
    project_suites.add_suite(data.suite_name)
    project_suites.verify_suite_exists(data.suite_name)
    project_suites.rename_suite(data.suite_name, data.new_suite_name)
    project_suites.verify_suite_exists(data.new_suite_name)


def teardown(data):
    close()
