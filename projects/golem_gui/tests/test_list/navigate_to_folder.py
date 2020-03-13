from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.create_access_random_project()
    common.navigate_menu('Tests')
    actions.store('folder_one', 'foo')
    test_list.add_folder(data.folder_one)
    actions.store('folder_two', 'bar.baz')
    test_list.add_folder(data.folder_two)
    actions.refresh_page()


def test(data):
    test_list.assert_breadcrumb(['tests'])
    test_list.navigate_to_folder(data.folder_one)
    test_list.assert_breadcrumb(['tests', 'foo'])
    test_list.navigate_to_breadcrumb('tests')
    test_list.assert_breadcrumb(['tests'])
    test_list.navigate_to_folder(data.folder_two)
    test_list.assert_breadcrumb(['tests', 'bar', 'baz'])


def teardown(data):
    api.project.delete_project(data.project)
