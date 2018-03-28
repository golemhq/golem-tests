
description = 'Verify the user can edit page code and save it'

pages = ['login',
         'index',
         'left_menu',
         'project_pages',
         'page_builder',
         'page_builder_code']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')
    click(left_menu.pages_menu)

def test(data):
    project_pages.create_access_page('test_view_code_' + random('ddd'))
    click(page_builder.code_button)
    store('test_code', 'test = ("id", "test")')
    page_builder_code.write_code(data.test_code)
    click(page_builder_code.save_button)
    click(page_builder_code.preview_button)
    click(page_builder.code_button)
    page_builder_code.verify_page_code(data.test_code)

def teardown(data):
    close()

