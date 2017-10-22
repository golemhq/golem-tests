
description = 'Verify that the user can access a test by clicking on it in the test list.'

pages = ['login',
         'index',
         'project',
         'test_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('name', random('ccccccc'))
    project.create_access_test(data.name)
    send_keys(test_builder.description, data.description)
    wait(2)
    test_builder.save_test()
    refresh_page()
    test_builder.verify_description(data.description)


def teardown(data):
    close()
