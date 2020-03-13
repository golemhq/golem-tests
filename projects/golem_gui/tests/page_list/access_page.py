from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can access a page by clicking on it in the page list.'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    actions.store('page', 'page')
    api.page.create_page(data.project, data.page)
    common.navigate_menu('Pages')


def test(data):
    page_list.access_page(data.page)
    actions.assert_element_text(page_builder.page_name, data.page)


def teardown(data):
    api.project.delete_project(data.project)
