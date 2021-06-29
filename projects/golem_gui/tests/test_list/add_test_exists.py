from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user cannot create a new test if a test with the same name exists'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    common.navigate_menu('Tests')
    data.test_one = actions.random_str()
    test_list.add_test(data.test_one)


def test(data):
    test_list.add_test(data.test_one)
    common.assert_error_message('A test with that name already exists')
