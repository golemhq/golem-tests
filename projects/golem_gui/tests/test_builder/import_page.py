from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can import a page into the test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    actions.store('page_name', 'page_import_' + actions.random_str())
    api.page.create_page('test', data.page_name)
    api.test.create_access_random_test('test')


def test(data):
    test_builder.import_page(data.page_name)
    test_builder.assert_page_in_list(data.page_name)
