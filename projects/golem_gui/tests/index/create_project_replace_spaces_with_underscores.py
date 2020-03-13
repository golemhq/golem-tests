from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify that spaces are replaced with underscores when creating a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    project_name = actions.random_str(prefix='project_')
    actions.click(index.create_project_button)
    actions.wait_for_element_displayed(index.project_name_input)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    actions.wait_for_element_not_displayed(index.create_button)
    index.assert_project_exists(project_name.replace(' ', '_'))
