from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')
    data.folder_one = 'foo'
    test_list.add_folder(data.folder_one)
    data.folder_two = 'bar'
    data.folder_three = actions.random_str()
    data.folder_two_full = '{}.{}'.format(data.folder_two, data.folder_three)
    test_list.add_folder(data.folder_two_full)
    actions.refresh_page()


def test(data):
    test_list.assert_breadcrumb(['tests'])
    test_list.navigate_to_folder(data.folder_one)
    test_list.assert_breadcrumb(['tests', 'foo'])
    test_list.navigate_to_breadcrumb('tests')
    test_list.assert_breadcrumb(['tests'])
    test_list.navigate_to_folder(data.folder_two_full)
    test_list.assert_breadcrumb(['tests', data.folder_two, data.folder_three])
