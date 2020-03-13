from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify the application shows the correct error message when creating a project without name'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    actions.click(index.create_project_button)
    actions.click(index.create_button)
    common.assert_error_message('Project name is too short')
