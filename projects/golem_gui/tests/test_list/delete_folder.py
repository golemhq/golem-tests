from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')
    data.folder = actions.random_str()
    test_list.add_folder(data.folder)


def test(data):
    test_list.delete_folder(data.folder)
    assert not test_list.folder_exists(data.folder)
    actions.refresh_page()
    assert not test_list.folder_exists(data.folder)
