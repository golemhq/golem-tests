
description = 'Verify that the user can add a directory in the pages section by appending \'\\\' at the end'

pages = ['login',
         'index',
         'project']


def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('directory_name', random('ccccc'))
    project.add_page_directory(data.directory_name)
    project.verify_page_directory_exists(data.directory_name)


def teardown(data):
    close()
