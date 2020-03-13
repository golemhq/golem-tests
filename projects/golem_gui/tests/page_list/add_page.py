from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can create a new page from the project page'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Pages')


def test(data):
    # to root
    page_one = actions.random_str()
    page_list.add_page(page_one)
    page_list.assert_page_exists(page_one)
    # to folder
    page_two = 'folder1.' + actions.random_str()
    page_list.add_page(page_two)
    page_list.assert_page_exists(page_two)
    actions.refresh_page()
    page_list.assert_page_exists(page_one)
    page_list.assert_page_exists(page_two)


def teardown(data):
    api.project.delete_project(data.project)
