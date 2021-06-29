from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can import a page into the test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    data.page = api.page.create_page(data.project)
    api.test.create_access_test(data.project)


def test(data):
    test_builder.import_page(data.page)
    test_builder.assert_page_in_list(data.page)
