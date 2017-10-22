
description = 'Verify that the user can create a new suite from the project page'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('suite_name', random('ccccc'))
    project.add_suite(data.suite_name)
    project.verify_suite_exists(data.suite_name)


def teardown(data):
    close()
