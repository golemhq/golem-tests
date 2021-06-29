from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_list


description = 'Verify the user can rename a test from the test list'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    data.test_one = api.test.create_test(data.project)
    data.test_two = api.test.create_test(data.project)
    common.navigate_menu('Tests')


def test(data):
    test_list.rename_test(data.test_one, data.test_two)
    common.assert_error_message('A file with that name already exists')
