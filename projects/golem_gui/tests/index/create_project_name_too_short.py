from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify the application shows the correct error message when creating ' \
              'a project with the name too short (less than 3 chars long)'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    actions.click(index.create_project_button)
    project_name = actions.random('cc')
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    common.assert_error_message('Project name is too short')
