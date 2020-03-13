from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import common


description = 'Verify the application shows the correct error message when the user' \
              'tries to create a project with non unique name'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)


def test(data):
    actions.click(index.create_project_button)
    project_name = actions.random_str(prefix='project_')
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    actions.click(index.create_project_button)
    actions.send_keys(index.project_name_input, project_name)
    actions.click(index.create_button)
    common.assert_error_message('A project with that name already exists')
