from projects.golem_gui.pages import common
from projects.golem_gui.pages import page_list
from projects.golem_gui.pages import api


description = 'Verify the user can duplicate a page'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('page_list')
    data.page = api.page.create_page(data.project)
    common.navigate_menu('Pages')


def test_duplicate_page(data):
    new_name = data.page + 'copy'
    page_list.duplicate_page(data.page, new_name)
    assert page_list.page_exists(data.page)
    assert page_list.page_exists(new_name)
