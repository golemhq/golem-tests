from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    project = 'project'
    permission = 'admin'
    create_user.add_project_permission(project, permission)
    create_user.assert_project_permission_in_table(project, permission)
    create_user.remove_project_permission(project, permission)
    assert not create_user.project_permission_in_table(project, permission)
