from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_list


description = 'Verify the user can access a test by clicking on it in the test list.'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_list')
    data.test = api.test.create_test(data.project)
    common.navigate_menu('Tests')


def test(data):
    test_list.access_test(data.test)
    actions.assert_element_text(test_builder.test_name, data.test)
