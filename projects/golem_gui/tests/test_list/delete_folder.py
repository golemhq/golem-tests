from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Tests')
    actions.store('folder', actions.random_str())
    test_list.add_folder(data.folder)


def test(data):
    test_list.delete_folder(data.folder)
    assert not test_list.folder_exists(data.folder)
    actions.refresh_page()
    assert not test_list.folder_exists(data.folder)


def teardown(data):
    api.project.delete_project(data.project)
