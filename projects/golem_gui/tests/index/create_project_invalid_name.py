from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify a project cannot be created with invalid characters'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    project_name = 'project_test_$'
    actions.click(index.create_project_button)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    common.assert_error_message('Only letters, numbers and underscores are allowed')
