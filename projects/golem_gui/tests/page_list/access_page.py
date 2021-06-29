from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_builder
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can access a page by clicking on it in the page list.'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    data.page = api.page.create_page(data.project)
    common.navigate_menu('Pages')


def test_access_page_from_list(data):
    page_list.access_page(data.page)
    page_builder.is_displayed(data.page)
