
description = 'Verify the user can access a suite by clicking on it in the suite list.'

pages = ['login',
         'index',
         'project_suites',
         'suite_page']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('suite_name', 'suite_' + random('cccc'))
    project_suites.add_suite(data.suite_name)
    project_suites.access_suite(data.suite_name)
    verify_text_in_element(suite_page.suite_name, data.suite_name)


def teardown(data):
    close()
