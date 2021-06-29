from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can create a new page from the test builder'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test(data):
    page_name = actions.random_str()
    test_builder.add_new_page(page_name)
    test_builder.assert_page_in_list(page_name)
