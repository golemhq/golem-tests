from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify the user can add tags to a suite'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_no_envs')
    api.suite.create_access_random_suite('project_no_envs')


def test(data):
    actions.send_keys(suite_builder.tags_input, '001, 002')
    suite_builder.save_suite()
    actions.refresh_page()
    actions.assert_element_attribute(suite_builder.tags_input, 'value', '001, 002, ')
