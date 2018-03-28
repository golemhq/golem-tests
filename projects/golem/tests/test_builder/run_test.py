
description = 'Verify the user can run a test'

pages = ['login',
         'index',
         'left_menu',
         'project_tests',
         'test_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.tests_menu)
    store('test_name', 'test_run_test_' + random('dddd'))
    project_tests.create_access_test(data.test_name)

def test(data):
    click(test_builder.run_button)
    test_builder.wait_for_test_to_run()
    test_builder.verify_empty_test_execution_modal_content(data.test_name)

def teardown(data):
    pass
