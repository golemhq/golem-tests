
description = 'Verify that the user cannot create a page with a name that contains spaces in the middle'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')

def test(data):
    index.create_access_project('test')
    project.add_page('test with spaces')
    project.verify_error_message('Only letters, numbers, \'-\' and \'_\' are allowed')


def teardown(data):
    close()
