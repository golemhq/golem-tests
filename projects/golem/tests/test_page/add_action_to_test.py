
description = 'Verify that the user can access a test by clicking on it in the test list.'

pages = ['login',
         'index',
         'project',
         'test_page']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    project.create_access_test('testing_actions')
    test_page.add_action(data.action)
    click(test_page.save_button)
    refresh_page()
    test_page.verify_last_action(data.action)
    capture('the action was added to the test')


def teardown(data):
    close()
