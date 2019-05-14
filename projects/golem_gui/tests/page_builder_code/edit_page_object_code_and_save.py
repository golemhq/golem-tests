
description = 'Verify the user can edit page code and save it'

tags = ['smoke']

pages = ['common',
         'index',
         'page_builder',
         'page_list',
         'page_builder_code']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')
    page_list.create_access_random_page()

def test(data):
    store('page_code', 'test = ("id", "test")')
    click(page_builder.code_button)
    page_builder_code.set_value(data.page_code)
    page_builder_code.save_page()
    click(page_builder_code.preview_button)
    click(page_builder.code_button)
    page_builder_code.assert_value(data.page_code)

def teardown(data):
    pass
