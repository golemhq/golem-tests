from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_list
from projects.golem_gui.pages import suite_builder


description = 'Verify the user can access a suite by clicking on it in the suite list.'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('suite_list')
    data.suite = api.suite.create_suite(data.project)
    common.navigate_menu('Suites')


def test(data):
    suite_list.access_suite(data.suite)
    actions.assert_element_text(suite_builder.suite_name, data.suite)
