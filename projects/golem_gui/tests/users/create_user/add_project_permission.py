from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    project = 'project1'
    permission = 'admin'
    create_user.select_project(project)
    create_user.select_permission(permission)
    actions.click(create_user.add_permission_button)
    create_user.assert_project_permission_in_table(project, permission)
