from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')


def test(data):
    folder = actions.random_str()
    test_list.add_folder(folder)
    test_list.navigate_to_folder(folder)
    test_one = actions.random_str()
    test_list.add_test_to_current_folder(test_one)
    test_two = 'foo.bar'
    test_list.add_test_to_current_folder(test_two)
    common.navigate_menu('Tests')
    test_list.assert_test_exists('{}.{}'.format(folder, test_one))
    test_list.assert_test_exists('{}.{}'.format(folder, test_two))
