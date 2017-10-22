
description = 'Verify that the user can add an action to a test and save it successfully'

pages = ['login',
         'index',
         'project',
         'test_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    project.create_access_test('testing_actions')
    test_builder.add_action(data.action)
    click(test_builder.save_button)
    refresh_page()
    test_builder.verify_last_action(data.action)
