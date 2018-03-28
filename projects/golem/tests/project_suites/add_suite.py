
description = 'Verify the user can create a new suite from the project page'

pages = ['login',
         'index',
         'project_suites']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    project_suites.add_suite(data.suite_name)
    project_suites.verify_suite_exists(data.suite_name)


def teardown(data):
    close()
